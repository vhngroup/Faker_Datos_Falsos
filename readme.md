# Creación de datos falsos con Faker
![Ejemplo](https://github.com/vhngroup/Faker_Datos_Falsos/blob/main/static/image.png)

Gracias a esta libreria podemos crear dataset de datos falsos para hacer pruebas en nuestros desarrollos.
Faker es muy personalizable permitiendo hasta la generación de los datos por region. Desde nombre y apellidos a numeros de tarjeta de credito y pasaporte.
Con una documentación muy completa de cada una de sus caracteristicas permite escalar tu proyecto hasta donde requieras datos.
Repo: https://faker.readthedocs.io/en/master/index.html

* ## Caracteristicas:
Para esta Demo hemos usado Streamlit, el cual nos permite tener una interfas e interacción web, openpyxl para escribir en archivos xlsx, pandas para la creación del dataframe generado por Faker para almacenar el dataset en excel.


* ## Instrucciones:
* Se recomienda el uso de virtualenv
* Ejecutar el comando: pip install -r requirements.txt para instal las dependencias.
* Ejecutar el script con ```streamlit run main.py``` y selecionar las categorias de datos a generar.