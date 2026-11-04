import os
import pathlib
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

# 1. Cargar la clave desde el archivo .env
load_dotenv()
api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("No se encontró API_KEY en el archivo .env")

client = genai.Client(api_key=api_key)

# 2. Cargar la imagen del monumento con Pillow
ruta_imagen = "puma_pumku.jpg"

if not pathlib.Path(ruta_imagen).exists():
    raise FileNotFoundError(f"No se encontró el archivo '{ruta_imagen}'. Asegúrate de que esté en la carpeta del proyecto.")

imagen_entrada = Image.open(ruta_imagen)

# 3. Prompt para la reconstrucción
prompt_reconstruccion = (
    "Transform the provided monument image into a complete, pristine, fully restored architectural masterpiece. "
    "Fill in all broken, missing, or destroyed sections, arches, walls, roofs, and upper levels. "
    "Do not leave any ruins, decay, or damaged elements. Rebuild the missing structures using original, period-appropriate "
    "authentic architectural materials matching the existing heritage building (such as fully restored masonry, stone, slate, or original cladding). "
    "Maintain historical accuracy, crisp photorealistic details, complete architectural symmetry, and bright natural daylight."
)


print("Enviando imagen a gemini-3.1-flash-image...")

# 4. Llamada al modelo gemini-3.1-flash-image pasando la imagen y el prompt
response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=[imagen_entrada, prompt_reconstruccion]
)

# 5. Extraer y guardar la imagen o texto devuelto
imagen_guardada = False

if hasattr(response, "candidates") and response.candidates:
    for candidate in response.candidates:
        if hasattr(candidate, "content") and candidate.content.parts:
            for part in candidate.content.parts:
                # Si la parte contiene datos de imagen devueltos
                if hasattr(part, "inline_data") and part.inline_data:
                    with open("monumento_reconstruido.png", "wb") as f:
                        f.write(part.inline_data.data)
                    print("¡ÉXITO! Imagen guardada como 'monumento_reconstruido.png'")
                    imagen_guardada = True
                    break

if not imagen_guardada:
    # Si devuelve la respuesta en texto explicativo/descripción
    print("\nRespuesta textual del modelo:")
    print(response.text)