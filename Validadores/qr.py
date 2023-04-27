import pdf417gen
from PIL import Image

# texto que se va a codificar en el QR
texto = "Hola, este es un ejemplo de código QR en formato PDF417 generado con Python"

# generar el código QR
codigo = pdf417gen.encode(texto, columns=5, security_level=3)

# convertir el código a imagen
image = pdf417gen.render_image(codigo, scale=3, padding=15)

# guardar el código QR en un archivo
image.save("codigo.png")
