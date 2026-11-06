# 02 prompt marmol mediterraneo

- **Datos enviados al modelo:** Solo imagen, sin datos del monumento
- **Codigo:** Solo enviaba el prompt y la imagen, no saba ningún contexto más, ni decía donde estaba ni que tipo de monumento era
- **Parametros:** Modelo gemini-3.1-flash-image (Nano Banana 2)
- **Imagen de entrada:** coliseo1.jpg, castillo_dunottar_2.jpg, templo_luxor_1.jpg, partenon1.jpg, teatro_romano_merida_1.jpg
- **Imagen de salida:** monumento_reconstruido_coliseo2.png, monumento_reconstruido_castillo_dunottar_1.png, monumento_reconstruido_luxor.png, monumento_reconstruido_partenon.png, monumento_reconstruido_teatro_romano_merida_1.png

## Prompt usado (en inglés para mayor eficacia)

Transform the provided monument image into a complete, pristine, fully restored architectural masterpiece. 
Fill in all broken, missing, or destroyed sections, arches, walls, and upper levels. 
Do not leave any ruins or damaged stone. Replace decayed materials with polished white marble, golden accents, and fully intact classical columns. 
Vibrant Mediterranean daylight, 8k resolution, photorealistic historical restoration.

## Conclusiones

**monumento_reconstruido_coliseo2.png**: con este prompt ya es capaz de reconstruirlo en su totalidad. Lo reconstruye con un material parecido al mármol, y pone alrededor a personas ambientadas de la época.
**monumento_reconstruido_castillo_dunottar_1.png**: este castillo tiene un deterioro moderado pero es difícil deducir su estructura. Como se ha especificado un material que no es el adecuado para este tipo de castillo, no da una réplica muy bien adaptada a la realidad.
**monumento_reconstruido_luxor.png**: tiene un deterioro medio y una deducibilidad media/alta. Los materiales no son los más adecuados para este tipo de monumento.
**monumento_reconstruido_partenon.png**: es capaz de reconstruirlo en su totalidad. Tiene un deterioro medio/alto pero gran deducibilidad debido a la simetría. Los materiales sí que se adaptan mejor a la época en este caso.
**monumento_reconstruido_teatro_romano_merida_1.png**: gran deducibilidad y simetría pero materiales no muy bien adaptados. Sí que es capaz de reconstruirlo en su totalidad y de forma eficaz.


