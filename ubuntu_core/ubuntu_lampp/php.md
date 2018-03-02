# Installing php

~~~bash
sudo apt install php7.1 libapache2-mod-php7.1 php7.1-mysql php-common php7.1-cli php7.1-common php7.1-json php7.1-opcache php7.1-readline  
~~~

# some other extension if we work with pgsql, sqlite, cakephp, laravel

~~~bash
sudo apt install php7.1-curl php7.1-xml php7.1-mbstring php7.1-sqlite3 php7.1-xmlrpc php7.1-pgsql php7.1-bcmath php7.1-mcrypt php7.1-gd libapache2-mod-php7.1 libphp7.1-embed
~~~


# installing phpmyadmin

~~~bash
sudo apt install phpmyadmin
~~~

# creating symbolic link for phpmyadmin

~~~bash
ln -s /usr/share/phpmyadmin /var/www/html 
~~~

# ini file for enabaling mbstring     

~~~bash
/etc/php/7.1/apache2/phpini 
~~~


#  no password allow for phpmyadmin   

~~~bash
sudo vi /etc/phpmyadmin/config.inc.php
~~~

There are two instances of this line in the configuration file… be SURE to uncomment both of them!

~~~php
// $cfg['Servers'][$i]['AllowNoPassword'] = TRUE;
~~~

## login to phpmyadmin    

* user is `root`
* password is empty







