# 04 prompt generico con datos

- **Datos enviados al modelo:** Nombre y ubicacion del monumento
- **Codigo:** Segundo codigo (interactions), imagen + datos del monumento
- **Parametros:** Modelo gemini-3.1-flash-image (Nano Banana 2); API interactions; thinking_level=high; google_search; image_size=2K; mime_type=image/jpeg
- **Imagen de entrada:**
        **puma_pumku.jpg**: Puma Punku, Tiwanaku (Bolivia)
        **castillo_dorset_1.jpg**: Corfe Castle (Dorset, Inglaterra)
        **castillo_dunottar_2.jpg**: Castillo de Dunnottar (Aberdeenshire, Escocia)
        **templo_de_saturno_1.jpg**: Templo de Saturno (Foro Romano, Roma, Italia)
        **templo_de_saturno_2.jpg**: Templo de Saturno (Foro Romano, Roma, Italia)

## Prompt usado (en inglés para mayor eficacia)

This photo shows {nombre_monumento}, {lugar}. 
Create a photorealistic image showing how this monument most likely looked when it was newly built and complete, as an archaeological and historical reconstruction.
Use the surviving parts visible in the photo as the ground truth: keep their exact position, proportions, materials and construction style, 
and extend them to restore the missing walls, roofs, arches, columns, upper levels and decoration. 
Choose the materials, colors, ornamentation and architectural style that are documented for this specific monument, culture and period; do not apply the style of another civilization or a generic 'ancient' look. Where the historical evidence is uncertain, prefer a sober, plausible solution over invention. 
Keep the same camera angle, framing, landscape and sky conditions as the original photo, with natural daylight. 
Do not add modern elements, people or text.

## Conclusiones

GENERALES: cuanta más información tiene el modelo (lugar, época, datos adicionales) más eficaz es la recosntrucción. El caso en el que mejor se aprecia es en la reconstruccion del castillo de Dorset. 

**monumento_reconstruido_puma_pumku.png**:
- **Imagen de entrada:** puma_pumku.jpg
- **Nombre del monumento:** Puma Punku, Tiwanaku
- **Ubicación:** Bolivia
- **Conclusiones:** la réplica ha mejorado bastante con este prompt, es más fiel a la realidad y no se ha cambiado el frame respecto a la imagen original. 

**monumento_reconstruido_castillo_dorset.png**:
- **Imagen de entrada:** castillo_dorset_1.jpg
- **Nombre del monumento:** Corfe Castle
- **Ubicación:** Dorset, England
- **Conclusiones:** la reconstrucción ha tenido una mejora exponencial. Ahora podemos ver perfectamnete el castillo y no quedan partes derruidas. Se han añadido murallas, paredes, un puente etc. Ahora si lo vemos lo podemos identificar como un castillo inglés de la época. 

**monumento_reconstruido_dunottar_2.png**:
- **Imagen de entrada:** castillo_dunottar_2.jpg
- **Nombre del monumento:** Dunnottar Castle
- **Ubicación:** Aberdeenshire, Scotland
- **Conclusiones:** se ha reconstruido una parte del castillo escocés, pero la parte delantera que parece una muralla no consigue reconstruirla, deduzco que es por el ángulo de la foto. Aún así ha mejorado respecto al prompt anterior. 

**monumento_reconstruido_templo_saturno_2_1.png** y **monumento_reconstruido_templo_saturno_1_1.png**
- **Imagen de entrada:** templo_de_saturno_2.jpg
- **Nombre del monumento:** the Temple of Saturn
- **Ubicación:** Roman Forum, Rome, Italy
- **Notas añadidas al prompt:** Reconstruct only the Temple of Saturn, the group of columns in the center. Keep the warm sunset lighting and sky of the original photo. Leave the domed building on the left unchanged.
- **Conclusiones:** En este caso, además del prompt se han añadido unas notas adicionales debido a la complejidad del templo, ya que hay varias partes y solo queremos reconstruir una. Se ha reconstruido mejor que en los casos anteriores, pero no está del todo afinado. Es mejor el caso primero debido al ángulo de la foto. 

**monumento_reconstruido_templo_saturno_1_2.png** 
- **Imagen de entrada:** templo_de_saturno_2.jpg
- **Nombre del monumento:** the Temple of Saturn
- **Ubicación:** Roman Forum, Rome, Italy
- **Notas añadidas al prompt:** "Reconstruct only the Temple of Saturn, the group of columns in the center, in its late antique "
    "rebuilt phase (4th century AD), the phase the surviving columns belong to. "
    "Keep the surviving columns in their exact position and build the temple around them. "
    "The temple is prostyle hexastyle: six columns across the front and a deep porch with a second row "
    "of columns behind them, and plain cella walls with no colonnade along the sides. "
    "The order is Ionic, with volute capitals, on smooth unfluted monolithic granite shafts. "
    "The temple stands on a very tall podium with a wide frontal staircase facing the forum. "
    "Keep the warm sunset lighting and sky of the original photo. "
    "Leave the domed building on the left unchanged."
- **Conclusiones:** En este caso,al igual que en el anterior, además del prompt se han añadido unas notas adicionales debido a la complejidad del templo. como son bastante más específicas, se ha reconstruido mucho mejor. Era un caso complicado debido a que estaba bastante derruido y tenía varias partes. Presenta simetría pero solo en algunas partes, entonces es difícil deducir ciertas cosas. De todas las réplicas que ha dado de este templo a lo largo de los diferentes prompts, esta es la más adecuada. 

