Paquetes UBUNTU

GIT

Apache2, Python y MySQL

https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu

apt-get install apache2
apt-get install python
apt-get install mysql-server libapache2-mod-auth-mysql php5-mysql

MySQL para Python

http://codeinthehole.com/writing/how-to-set-up-mysql-for-python-on-ubuntu/

Django
http://blog.xenodesystems.com/2012/10/montar-entorno-de-desarrollo-python.html


Configuracion Virtual Hosts de Apache (/etc/apache2/sites-available)

Archivo virtrael.conf

<VirtualHost *:8080>
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

Configuracion de los puertos de Apache para habilitar el puerto 8080 (/etc/apache2/ports.conf)

Añadir la línea

Listen 8080

Activar el sitio en apache: (desde la carpeta /etc/apache2/sites-available/)

a2ensite virtrael.conf

Finalmente, reiniciamos Apache

/etc/init.d/apache2 restart





