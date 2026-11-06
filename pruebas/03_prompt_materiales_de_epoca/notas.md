# 03 prompt materiales de epoca

- **Datos enviados al modelo:** Solo imagen, sin datos del monumento
- **Codigo:** Solo enviaba el prompt y la imagen, no saba ningún contexto más, ni decía donde estaba ni que tipo de monumento era
- **Parametros:** Modelo gemini-3.1-flash-image (Nano Banana 2)
- **Imagen de entrada:** castillo_dorset_1.jpg, castillo_dunottar_2.jpg, puma_pumku.jpg, teatro_romano_merida_1.jpg, templo_de_saturno_1.jpg, templo_de_saturno_2.jpg
- **Imagen de salida:** monumento_reconstruido_castillo_dorset.png, monumento_reconstruido_dunottar_2.png, monumento_reconstruido_puma_pumku.png, monumento_reconstruido_teatro_merida2.png, monumento_reconstruido_templo_saturno_1_1.png, monumento_reconstruido_templo_saturno_2_1.png

## Prompt usado (en inglés para mayor eficacia)
Transform the provided monument image into a complete, pristine, fully restored architectural masterpiece. 
Fill in all broken, missing, or destroyed sections, arches, walls, roofs, and upper levels. 
Do not leave any ruins, decay, or damaged elements. 
Rebuild the missing structures using original, period-appropriate authentic architectural materials matching the existing 
heritage building (such as fully restored masonry, stone, slate, or original cladding). 
Maintain historical accuracy, crisp photorealistic details, complete architectural symmetry, and bright natural daylight.


## Conclusiones
**monumento_reconstruido_castillo_dorset.png**:es un monumento con difícil deducibilidad ya que está muy derruido y no cuenta con simetría. Se ha reconstruido de forma más o menos realista pero solo las partes que estaban menos derruidas, no ha montado un castillo entero. Los materiales si que son adecuados a la época. 

**monumento_reconstruido_dunottar_2.png**: al igual en el castillo de dorset, tiene poca deducibilidad debido a la cantidad alta de ruinas y paredes derruidas. Los materiales si que estan adaptados a la época pero no ha sido cpaz de reconstruir el castillo en su totalidad. Solo se ha centrado en reconstruir las partes que estaban menos derruidas, pero no ha sido capaz de inventar mucho. 

**monumento_reconstruido_puma_pumku.png**: ha reconstruido el monumento, el cual tenía también poca deducibilidad pero sí simetría. Lo que ha hecho ha sido cambiar la vista de la foto, no lo ha dejado como en la original. 

**monumento_reconstruido_teatro_merida2.png**: este prompt ha mejorado la réplica del teatro de mérida respecto al anterior. La simetría que presenta ha sido clave para la reconstrucción pero los materiales usados ahora si que son los adecuados. 

**monumento_reconstruido_templo_saturno_1_1.png**: al ser la perspectiva de la foto no muy buena, no ha sido capaz de dar una réplica buena, hay zonas en las que se encuentran todavia zonas derruidas. 

**monumento_reconstruido_templo_saturno_2_1.png**: en este caso, al tener la imagen otra perspectiva que la anterior, ha dado una mejor réplica. El modelo tenía que inventar algunas, ya que es un templo con partes diferenciadas y no tanto que ver entre sí, y con bastantes zonas derruidas. 

