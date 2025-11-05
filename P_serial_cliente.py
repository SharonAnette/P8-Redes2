import pickle
import requests

# Nombre del archivo PDF que se va a enviar
archivo_pdf = 'documento.pdf'

try:
    # Leer el archivo PDF
    with open(archivo_pdf, 'rb') as f:
        pdf_data = f.read()
        print(f"Tamaño del archivo PDF leído: {len(pdf_data)} bytes")

    # Serializar el contenido del PDF
    try:
        serialized_data = pickle.dumps(pdf_data)
        print(f"Tamaño de los datos serializados: {len(serialized_data)} bytes")
    except pickle.PicklingError as e:
        print(f"Error al serializar el archivo PDF: {e}")
        exit(1)

    # Enviar el contenido serializado al servidor
    try:
        response = requests.post(
            'http://localhost:8080/prueba_serializacion',
            files={'file': (archivo_pdf, serialized_data)}
        )

        # Imprimir la respuesta del servidor
        print("Respuesta del servidor:", response.status_code)
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error al enviar la solicitud al servidor: {e}")

except FileNotFoundError:
    print(f"Error: El archivo '{archivo_pdf}' no se encontró. Asegúrate de que el archivo está en la misma carpeta que este script.")
except Exception as e:
    print(f"Error inesperado: {e}")

