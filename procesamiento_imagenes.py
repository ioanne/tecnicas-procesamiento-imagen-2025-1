import cv2
import matplotlib.pyplot as plt


url_imagen_original = 'naranja_2.jpg'

imagen_original = cv2.imread(url_imagen_original)

# cv2 no trabaja con RGB, sino con BGR

# RGB to BGR
imagen_bgr = cv2.cvtColor(imagen_original, cv2.COLOR_RGB2BGR)

plt.imshow(imagen_bgr)
plt.axis('off')
plt.title("Imagen Original")
plt.savefig('images/naranja_2_bgr.jpg')
plt.close()


# pasarla a escala de grises
imagen_gris = cv2.imread(url_imagen_original, cv2.IMREAD_GRAYSCALE)

plt.imshow(imagen_gris, cmap='gray')
plt.axis('off')
plt.title("Imagen escala de grises")
plt.savefig('images/naranja_escala_gris.jpg')
plt.close()


def reducir_tonos_grises(imagen, niveles):
    """Reduce los tonos de gris de una imagen a un número específico de niveles."""
    factor = 256 // niveles
    return (imagen//factor) * factor


def reducir_tonos_grises_imagen(imagen, niveles):
    nueva_imagen = reducir_tonos_grises(imagen, niveles)
    plt.imshow(nueva_imagen, cmap='gray')
    plt.axis('off')
    plt.title(f"Imagen en escala {niveles} de grises")
    plt.savefig(f'images/naranja_escala_gris-{niveles}.jpg')
    plt.close()


reducir_tonos_grises_imagen(imagen_gris, 2)
reducir_tonos_grises_imagen(imagen_gris, 4)
reducir_tonos_grises_imagen(imagen_gris, 8)
reducir_tonos_grises_imagen(imagen_gris, 16)
reducir_tonos_grises_imagen(imagen_gris, 32)
reducir_tonos_grises_imagen(imagen_gris, 64)
reducir_tonos_grises_imagen(imagen_gris, 128)
reducir_tonos_grises_imagen(imagen_gris, 256)


# Detectar bordes aplicando Canny
imagen_bordes = cv2.Canny(imagen_gris, 50, 250)


plt.imshow(imagen_bordes, cmap='gray')
plt.axis('off')
plt.title("Imagen bordes")
plt.savefig('images/imagen_bordes.jpg')
plt.close()