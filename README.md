#Virtrael API

Virtrael.api es una api RESTFUL realizada en Python+Django+Tastypie para el proyecto [Virtrael] (http://asistic.ugr.es/virtra-el/)

##1. Comenzando: Apache, Python y MySQL

En primer lugar, debemos configurar nuestra máquina para poder dar soporte a Virtrael.api

Necesitaremos: GIT, Apache2, Python, MySQL y Django. Para más detalles, puedes consultar el siguiente tutorial

https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu

####Respecto a MySQL para Python:####
http://codeinthehole.com/writing/how-to-set-up-mysql-for-python-on-ubuntu/

####Django:####
http://blog.xenodesystems.com/2012/10/montar-entorno-de-desarrollo-python.html

####Resumiendo:####
```
sudo su
apt-get install git
apt-get install apache2
apt-get install python
apt-get install mysql-server libapache2-mod-auth-mysql php5-mysql
apt-get install python-django
```

###Clonar el proyecto Virtrael.api###
Una vez tengamos el entorno, clonamos nuestro proyecto en `/var/www/` (carpeta por defecto en UBUNTU para servir aplicaciones web)

```
git clone https://github.com/SalMax/virtrael.api.git
```

##2. Configurando Apache
La configuración de los [Virtural Hosts de Apache](http://httpd.apache.org/docs/2.2/vhosts/), en UBUNTU, se hace añadiendo configuraciones en `/etc/apache2/sites-available`. En nuestro caso vamos a crear una para el proyecto Virtrael.api

Archivo virtrael.conf
```
<VirtualHost *:80>
        ServerName localhost

        # Habilitamos CORS (para poder hacer llamadas desde otros dominios)
        SetEnvIfNoCase ORIGIN (.*) ORIGIN=$1
        Header always set Access-Control-Allow-Methods "POST, GET, PUT, DELETE"
        Header always set Access-Control-Allow-Origin "%{ORIGIN}e"
        Header always set Access-Control-Allow-Credentials "true"
        Header always set Access-Control-Allow-Headers "X-CSRFToken,Content-Type"

        # Configuracion del archivo wsgi
        WSGIScriptAlias / /var/www/virtrael.api/apache/django.wsgi
        <Directory "/var/www/virtrael.api/virtrael">
                <Files django.wsgi>
                        Require all granted
                </Files>
        </Directory>

        # Configuracion del directorio de contenido estatico
        Alias /site_media/static/ /var/www/virtrael.api/virtrael/site_media/static/
        <Directory "/var/www/virtrael.api/virtrael/site_media/static/">
                Options Indexes FollowSymLinks
                AllowOverride None
                Require all granted
        </Directory>
</VirtualHost>
```

A continuacion, debemos comprobar que apache esté escuchando el puerto 80 (o el que elijas). Para ello comproblamos, en el archivo `/etc/apache2/ports.conf`, que tengas la siguietne línea (si no está, la añades)
```
Listen 80
````

Finalmente, activas el sitio en Apache y reinicias el servicio: 

(desde la carpeta /etc/apache2/sites-available/)
```
a2ensite virtrael.conf
/etc/init.d/apache2 restart
```

##3. Dependencias Python de Virtrael.api ##

Antes de comenzar, necesitaremos instalar algunas apps de Django. El método más cómod es usando [pip](https://pip.pypa.io/en/latest/).


```
pip install admin-bootstrap
```
Look bootstrap para la administracion de Django. No es estrictamente necesario, pero hace la admin de Django bastante más atractiva.
<br>
```
pip install django-tastypie
pip instarll simplejson
```
[Tastypie](https://django-tastypie.readthedocs.org/en/latest/) es la base para crear los servicios web que necesitamos. [Simplejson](https://pypi.python.org/pypi/simplejson) es un sencillo encoder/decoder json para Python.
<br>
```
pip install south
```
[South](https://south.readthedocs.org/en/latest/) es una utilidad para migraciones y alteraciones de la base de datos en Django muy buena. Tampoco estrictamente necesario, pero es muy conveniente tener esta aplicación cuando se trabaja con bases de datos en Django.

##4. Pasos para inicializar Virtrael.api##

1. Crear en MySQL una base de datos para virtrael y añadirle el script `virtrael.sql`, situado en la carpeta `scripts` de virtrael.api
2. Configurar el fichero `vitrael/settings.py` para conectar con la base de datos virtrael (líneas 31 y 32)
3. Desde la raíz del proyecto, ejecutar `python mange.py syncdb` para crear crear las tablas de Django y `python manage.py migrate` para las tablas de tastypie.
4. En la raíz del proyecto, crear la carpeta `log` *con permisos de escritura* (muy importante, o tendrás un error cuando trates de lanzar el proyecto), para que el Virtrael.api pueda volcar ahí los logs.
5. Juntar los archivos estáticos (principalmente, los de la app admin-bootstrap), en una sola carpeta que sea accesible para Django. Para ello tenemos el comando `python manage.py collectstatic`

Con estos pasos básicos, ya deberías tener la aplicación funcionando.

##5. Funcionamiento Básico de la aplicación##

Para los ejemplos sobre uso de Virtrael.api, tengo el proyecto ya desplegado en Microsoft Azure, concretamente en www.virtrael.cloudapp.net

Para administrar la base de datos:
```
http://virtrael.cloudapp.net/admin
```
Ahí tienes una administración generada por Django para poder trabajar cómodamente con la base de datos de Virtrael.

Para usar la api:

```
http://virtrael.cloudapp.net/api/virtrael/<nombre_del_recurso>/?format=json
````

Esa consulta genérica nos devuelve toda la información disponible sobra el recurso consultado.
###Recursos disponibles###
* `user_profile` ejemplo: http://virtrael.cloudapp.net/api/virtrael/user_profile/?format=json
* `user_avatar` 
* `carer_patient`
* `thearpist_patient`
* `exercise_error`
* `exercise_level`
* `exercise_result`
* `medal`
* `partial_result`
* `session_log`






