import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('./Fondos/ClasCabeza.png')

# Obtener las dimensiones de la imagen
alto, ancho, _ = imagen.shape

# Crear una columna extra de color negro
columna_negra = np.zeros((alto, 350, 3), dtype=np.uint8)

# Concatenar la columna extra a la imagen
imagen_con_columna = np.concatenate((columna_negra,imagen ), axis=1)

# Mostrar la imagen resultante
cv2.imshow("Imagen con columna extra", imagen_con_columna)
cv2.waitKey(0)
cv2.destroyAllWindows()