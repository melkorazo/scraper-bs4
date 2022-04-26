# Web Scraper

_Se utiliza BeautifulSOUP4, lxml y Requests en Python para obtener datos de la Web: http://books.toscrape.com/index.html._

## Requisitos previos

1. Python 3
2. virtualenv (pip install virtualenv)

## Instrucciones de uso

### 1. Crear ambiente virtual de Python

Usando virtualenv creamos un ambiente virtual llamado ".ENV", en el directorio del proyecto, utilizando los comandos:
```
virtualenv .ENV
```

Activar ambiente virtual con:

#### Windows:
```
.ENV\Scripts\activate.ps1
```

#### Linux:
```
source .ENV/bin/activate
```

### 2. Instalar paquetes requeridos

Una vez activado el ambiente virtual, instalamos los paquetes necesarios para utilizar ejecutar el programa.

```
pip install -r requirements.txt
```

### 3. Ejecutamos programa

```
python src/start.py
```



---
Por [Fabián Aravena](mailto://fabian@aravena.dev)
