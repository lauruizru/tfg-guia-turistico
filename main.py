#Reconstrucción de monumentos con IA generativa
#
# Idea general: se envía al modelo de imagen de Google (Nano Banana 2) una foto
# de un monumento en ruinas junto con un prompt de texto, y el modelo devuelve
# una imagen de cómo pudo verse el monumento cuando estaba completo.


import base64
import mimetypes
import os
import pathlib
from dotenv import load_dotenv # carga las variables del archivo .env
from google import genai  # SDK oficial de Google para la API de Gemini

# Configuración y autenticación 
# La clave de la API se guarda en un archivo .env 
# para que nadie pueda acceder a ella.
load_dotenv()
api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("No se encontró API_KEY en el archivo .env")

# Cliente que se usa para hacer todas las llamadas a la API
client = genai.Client(api_key=api_key)


# Construcción del prompt
def construir_prompt(nombre=None, ubicacion=None, epoca=None, notas=None):
    """Prompt genérico; los datos opcionales mejoran la precisión."""
    if nombre:
        entrada = f"This photo shows {nombre}"
        if ubicacion:
            entrada += f" ({ubicacion})"
        entrada += "."
    else:
        # Si no se conoce, se le pide que lo identifique él, y que no se
        # invente un monumento famoso parecido si no está seguro
        entrada = (
            "This photo shows a historical monument or heritage building. "
            "First identify which monument it is from its architecture and surroundings; "
            "if you cannot identify it with confidence, infer its culture and period "
            "from the visible construction techniques instead of guessing a famous lookalike."
        )

    if epoca:
        entrada += f" It dates from {epoca}."

    # Cuerpo del prompt (igual para todos los monumentos). Es bastante extenso, 
    # cuanta más informacionn demos más realista será el resultado
    prompt = (
        f"{entrada} "
        "Create a photorealistic image showing how this monument most likely looked "
        "when it was newly built and complete, as an archaeological and historical reconstruction. "
        "Use the surviving parts visible in the photo as the ground truth: keep their exact position, "
        "proportions, materials and construction style, and extend them to restore the missing walls, "
        "roofs, arches, columns, upper levels and decoration. "
        "Choose the materials, colors, ornamentation and architectural style that are documented "
        "for this specific monument, culture and period; do not apply the style of another "
        "civilization or a generic 'ancient' look. "
        "Where the historical evidence is uncertain, prefer a sober, plausible solution over invention. "
        "Keep the same camera angle, framing, landscape and sky conditions as the original photo, "
        "with natural daylight. Do not add modern elements, people or text."
    )

     # Las notas permiten añadir detalles específicos de un monumento concreto
    # (por ejemplo, qué elemento reconstruir si salen varios en la foto)(es totalmente opcional)
    if notas:
        prompt += f" Additional details: {notas}"
    return prompt


# Llamada a la API y guardado del resultado
def reconstruir(ruta, nombre=None, ubicacion=None, epoca=None, notas=None,
                salida="monumento_reconstruido.jpg"):
    # Comprueba que la imagen de entrada existe antes de llamar a la API
    ruta = pathlib.Path(ruta)
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró '{ruta}'")

    mime = mimetypes.guess_type(ruta)[0] or "image/jpeg"
    # La API recibe la petición en JSON, que no admite datos binarios, así que
    # la imagen se convierte a texto en base64
    img_b64 = base64.b64encode(ruta.read_bytes()).decode("utf-8")

    interaction = client.interactions.create(
        # Modelo de generación y edición de imágenes (Nano Banana 2)
        model="gemini-3.1-flash-image",
        # Entrada: el prompt de texto y la imagen del monumento
        input=[
            {"type": "text", "text": construir_prompt(nombre, ubicacion, epoca, notas)},
            {"type": "image", "data": img_b64, "mime_type": mime},
        ],
         # Permite al modelo buscar en Google para apoyarse en información real del monumento
        tools=[{"type": "google_search"}],
        # Formato de la salida: imagen JPEG con resolución 2K.
        response_format={"type": "image", "mime_type": "image/jpeg", "image_size": "2K"},
        generation_config={"thinking_level": "high"},
    )

    # La respuesta se compone de distitos "pasos"
    guardada = False
    for step in interaction.steps:
        if step.type == "model_output":
            for bloque in step.content:
                if bloque.type == "text":
                     # Texto del modelo (como explicaciones o avisos)
                    print(bloque.text)
                elif bloque.type == "image":
                    # La imagen llega codificada en base64: se decodifica 
                    # y se guarda como archivo. 
                    with open(salida, "wb") as f:
                        f.write(base64.b64decode(bloque.data))
                    guardada = True
    # Si el modelo no devolvió ninguna imagen
    if not guardada:
        print("El modelo no devolvió imagen.")
    return guardada


# Casos de prueba ( hay que ejecutarlo de uno en uno!)
#reconstruir("imagenes_entrada/puma_pumku.jpg", nombre="Puma Punku, Tiwanaku", ubicacion="Bolivia")

reconstruir("imagenes_entrada/castillo_dorset_1.jpg", nombre="Corfe Castle", ubicacion="Dorset, England")

#reconstruir("imagenes_entrada/castillo_dunottar_2.jpg", nombre="Dunnottar Castle", ubicacion="Aberdeenshire, Scotland")

#reconstruir("imagenes_entrada/templo_de_saturno_1.jpg", nombre="the Temple of Saturn", ubicacion="Roman Forum, Rome, Italy",
            #notas=(
               # "Reconstruct only the Temple of Saturn, the group of columns in the center, in its late antique "
                #"rebuilt phase (4th century AD), the phase the surviving columns belong to. "
                #"Keep the surviving columns in their exact position and build the temple around them. "
                #"The temple is prostyle hexastyle: six columns across the front and a deep porch with a second row "
                #"of columns behind them, and plain cella walls with no colonnade along the sides. "
                #"The order is Ionic, with volute capitals, on smooth unfluted monolithic granite shafts. "
                #"The temple stands on a very tall podium with a wide frontal staircase facing the forum. "
                #"Keep the warm sunset lighting and sky of the original photo. "
                #"Leave the domed building on the left unchanged."
            #))

# reconstruir("castillo.jpg")  # sin datos: el modelo intenta identificarlo