#Introducción
El proyecto consiste en la implementación de un servidor web (TWS) que permite procesar peticiones con la versión de protocolo HTTP/1.1. El servidor se desarrolló utilizando la API Berkeley Sockets y es capaz de analizar (parsing) tres tipos de métodos a nivel de HTTPRequest: GET, HEAD y POST, de acuerdo con la especificación del estándar de HTTP/1.1 RFC 2616. El servidor también es capaz de manejar errores de manera robusta, con códigos de respuesta 200, 400 y 404.

#Desarrollo
El servidor TWS implementa el concepto de "logger", lo que permite visualizar por la terminal todas las peticiones entrantes a nivel de HTTP, así como la respuesta que se envía a cada cliente. El servidor es capaz de procesar peticiones de manera concurrente, utilizando una aproximación Thread Based para el manejo de la concurrencia, lo que permite manejar múltiples peticiones de forma eficiente.

Para probar el funcionamiento del servidor, se desplegó en la infraestructura de AWS. Se realizaron pruebas utilizando diferentes recursos web, como páginas con hipertextos e imágenes, así como archivos de gran tamaño (1MB). Se utilizaron herramientas como telnet, scripts en Python, Postman y Wireshark, así como navegadores web reales para realizar pruebas exhaustivas del servidor.

#Conclusiones
El proyecto ha logrado implementar con éxito un servidor web (TWS) que cumple con los requerimientos establecidos en el alcance del proyecto. El servidor es capaz de procesar peticiones HTTP/1.1, manejar errores de manera robusta, implementar el concepto de "logger" y procesar peticiones de manera concurrente utilizando hilos. El despliegue en la infraestructura de AWS ha sido exitoso y se han realizado pruebas exhaustivas utilizando diferentes recursos web.

#Referencias
Linux Manual Page: socket()
Beej's Guide to Network Programming
Ejemplo Client/Server en C
Especificación del estándar de HTTP/1.1 RFC 2616 (https://datatracker.ietf.org/doc/rfc2616/)
