# Práctica 8 — Serialización

Este repositorio contiene el desarrollo de la **Práctica 8** de la asignatura **Aplicaciones para Comunicaciones en Red (6CV2)**, impartida en la **Escuela Superior de Cómputo (ESCOM)** del **Instituto Politécnico Nacional (IPN)**.  
La práctica aborda el concepto de **serialización de datos** aplicado al envío de archivos PDF entre cliente y servidor mediante el lenguaje **Python**.

---

## Objetivo
Enviar el contenido de un documento **PDF** desde un cliente hacia un servidor utilizando un proceso de **serialización y deserialización**, donde el cliente convierte el archivo en una secuencia de bytes para su transmisión, y el servidor lo recibe, procesa y reconstruye en un nuevo documento PDF:contentReference[oaicite:0]{index=0}.

---

## Explicación
La práctica tiene como propósito comprender el funcionamiento de la **serialización**, que consiste en transformar estructuras de datos u objetos en un formato que pueda ser almacenado o transmitido a través de una red.  
Del mismo modo, se aplica la **deserialización** para reconstruir el objeto original a partir de la información recibida.

Para lograrlo, se utilizó el **microframework Flask** como servidor HTTP y las bibliotecas **pickle** y **requests** de Python:  
- El **cliente** serializa el contenido del archivo PDF utilizando `pickle` y lo envía al servidor mediante una solicitud **POST**.  
- El **servidor** recibe los datos serializados, los deserializa y crea un nuevo archivo PDF con el contenido original.  

El proceso fue verificado utilizando **Wireshark**, observando la transmisión de datos serializados y la respuesta correcta del servidor ante la recepción del archivo.

Este ejercicio permite visualizar cómo la serialización es una técnica clave en el **intercambio de datos estructurados**, la **comunicación entre procesos** y el **almacenamiento eficiente** en redes distribuidas o aplicaciones cliente-servidor:contentReference[oaicite:1]{index=1}.
