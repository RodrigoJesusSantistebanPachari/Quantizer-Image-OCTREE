from PIL import Image
from color import Color
from octree_quantizer import OctreeQuantizer


if __name__ == '__main__':
    imagen = Image.open('ImagenEntrada/Entrada.png')

    pixeles = imagen.load()

    width, height = imagen.size

    octree = OctreeQuantizer()


    #Los píxeles de la imagen de entrada se añaden al octree
    for i in range(height):
        for j in range(width):
            octree.add_color(Color(*pixeles[j, i]))


    #Del octree se obtiene la paleta
    paleta = octree.make_palette(4096)

    #La imagen de la paleta estará en 64x64
    imagen_paleta = Image.new('RGB', (64, 64))
    pixeles_paleta = imagen_paleta.load()
    for i, color in enumerate(paleta):
        pixeles_paleta[int(i % 64), int(i / 64)] = (int(color.rojo), int(color.verde), int(color.azul))
    imagen_paleta.save('PaletaGenerada/Paleta.png') #Directorio de salida de la paleta


    #Imagen de salida
    imagen_salida = Image.new('RGB', (width, height)) #Será de los mismo píxeles de la entrada
    pixeles_salida = imagen_salida.load()
    for i in range(height):
        for j in range(width):
            index = octree.get_palette_index(Color(*pixeles[j, i]))
            color = paleta[index]   #Se usa la paleta
            pixeles_salida[j, i] = (int(color.rojo), int(color.verde), int(color.azul))
    imagen_salida.save('ImagenFinal/Salida.png')