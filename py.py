from PIL import Image
import os

def resize_image(input_path, output_path, sizes):
    """
    Redimensiona la imagen a diferentes tamaños y guarda los archivos.
    
    :param input_path: Ruta de la imagen original.
    :param output_path: Ruta de la carpeta donde se guardarán las imágenes redimensionadas.
    :param sizes: Lista de tamaños (ancho, alto) a redimensionar.
    """
    if not os.path.isfile(input_path):
        print(f"Error: El archivo '{input_path}' no existe.")
        return

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    with Image.open(input_path) as img:
        for size in sizes:
            img_resized = img.resize(size, Image.LANCZOS)
            img_resized.save(f"{output_path}/favicon-{size[0]}x{size[1]}.png")
            print(f"Imagen guardada: favicon-{size[0]}x{size[1]}.png")

def convert_to_ico(input_path, output_path):
    """
    Convierte la imagen a formato .ico.
    
    :param input_path: Ruta de la imagen original.
    :param output_path: Ruta de la carpeta donde se guardará el favicon.ico.
    """
    if not os.path.isfile(input_path):
        print(f"Error: El archivo '{input_path}' no existe.")
        return

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    with Image.open(input_path) as img:
        img.save(f"{output_path}/favicon.ico", format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
        print("Imagen guardada: favicon.ico")

# Ruta de la imagen original
input_image_path = "img/icon/favicon.ico"

# Ruta de la carpeta donde se guardarán las imágenes redimensionadas
output_image_path = "img/icon"

# Tamaños a los que quieres redimensionar la imagen
image_sizes = [(32, 32), (16, 16), (192, 192), (512, 512), (180, 180)]

# Redimensionar la imagen a diferentes tamaños
resize_image(input_image_path, output_image_path, image_sizes)

# Convertir la imagen a favicon.ico
convert_to_ico(input_image_path, output_image_path)
