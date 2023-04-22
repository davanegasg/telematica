
# Introducción
El proyecto consiste en la implementación de un servidor web (TWS) que permite procesar peticiones con la versión de protocolo HTTP/1.1. El servidor se desarrolló utilizando la API Berkeley Sockets y es capaz de analizar tres tipos de métodos a nivel de HTTPRequest: GET, HEAD y POST, de acuerdo con la especificación del estándar de HTTP/1.1 RFC 2616. El servidor también es capaz de manejar errores, con códigos de respuesta 200, 400 y 404.

# Desarrollo
El servidor TWS implementa el concepto de "logger", lo que permite visualizar por la terminal todas las peticiones entrantes a nivel de HTTP, así como la respuesta que se envía a cada cliente. El servidor es capaz de procesar peticiones de manera constante, utilizando una aproximación Thread Based para el manejo de esto mismo, lo que permite manejar múltiples peticiones de forma eficiente.

El servidor es compatible con tres tipos de métodos a nivel de HTTPRequest: GET, HEAD y POST. El método GET permite obtener recursos del servidor, el método HEAD permite obtener solo los encabezados de respuesta sin el cuerpo del recurso que fue solicitado, y el método POST permite enviar datos al servidor para su procesamiento.

Para probar el funcionamiento del servidor, se desplegó en los servicios web de Amazon (AWS). Se realizaron pruebas utilizando diferentes recursos web, como páginas con hipertextos e imágenes, así como archivos de gran tamaño que en este caso son de 1MB. Se utilizaron herramientas como telnet, scripts en Python, Postman y Wireshark, así como navegadores web reales para realizar pruebas del servidor.

Paso a paso para conetar al AWS:
1. Haces Login en AWS academy
2. entras en cursos y luego en modulos
3. entras en laboratorio de aprendizaje
4. Presionas StarLab y luego cuando la luz al lado de aws cambie a verde lo presionas
5. Entras en EC2
6. Entras en instances y creas una instancia
7. cuando hayas creado la instancias la eliges y presionas connect
8. Eliges la opcion "EC2 Instance Connect" y presionas connect
9. Cuando estes dentro de la terminal escribes "cd (nombre de la carpeta)"
10. cuando estes dentro de la carpeta escribes "python 3 server.py" para correr el server.
11. Verificas que funcione y ya estaria listo

Cómo hacer un GET, HEAD y POST request

Para el método GET, simplemente debemos ingresar el Request GET y la URL a la cuál le queremos hacer el GET

Ejemplo

'''
GET http://3.87.227.208:8080/caso1/template1
'''


# Conclusiones
Hemos logrado implementar con éxito un servidor web (TWS) que cumple con los requerimientos establecidos en el alcance del proyecto. El servidor es capaz de procesar peticiones HTTP/1.1, tener en cuenta el manejo de errores, implementar el concepto de "logger" y procesar peticiones de manera constante. El despliegue en la infraestructura de AWS ha sido exitoso y se han realizado pruebas utilizando diferentes recursos web.

# Referencias
<ul>
<li>https://man7.org/linux/man-pages/man7/socket.7.html</li>
<li>https://www.geeksforgeeks.org/tcp-server-client-implementation-in-c/</li>
<li>https://datatracker.ietf.org/doc/rfc2616/</li>
<li>https://www.postman.com</li>
<li>https://aws.amazon.com/es/training/awsacademy/</li>
</ul>
