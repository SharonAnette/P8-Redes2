from flask import Flask, request
import pickle
import json

app = Flask(_name_)

@app.route('/prueba_serializacion', methods=['POST'])
def upload():
    try:
        # Verificar si el archivo 'file' está presente en la solicitud
        if 'file' not in request.files:
            return 'No se ha enviado ningún archivo', 400

        # Obtener el archivo serializado
        serialized_data = request.files['file'].read()
        print(f"Tamaño de los datos serializados: {len(serialized_data)} bytes")

        # Deserializar el contenido
        try:
            pdf_data = pickle.loads(serialized_data)
        except Exception as e:
            print(f"Error al deserializar el archivo: {e}")
            return 'Error al deserializar el archivo', 400

        # Guardar el archivo PDF deserializado
        with open('archivo.pdf', 'wb') as f:
            f.write(pdf_data)

        print("Archivo PDF guardado como 'archivo.pdf'")

        # Imprimir los headers
        print("Headers: ", request.headers)

        # Crear un diccionario con la información relevante del request
        request_info = {
            'headers': dict(request.headers),
            'form': request.form.to_dict(),
            'files': {file_name: file.filename for file_name, file in request.files.items()}
        }

        # Imprimir el mensaje en formato JSON
        print("Request Info (JSON):", json.dumps(request_info, indent=4))

        return 'Archivo serializado recibido y guardado', 200

    except Exception as e:
        print(f"Error general: {e}")
        return 'Error en el servidor', 500

if _name_ == '_main_':
    app.run(port=8080)
