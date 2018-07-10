# install php 

~~~
sudo apt install php7.2 libapache2-mod-php7.2 php7.2-mysql php-common php7.2-cli php7.2-common php7.2-json php7.2-opcache php7.2-readline  
~~~

# installing phpmyadmin

~~~bash
sudo apt install phpmyadmin
~~~

# creating symbolic link for phpmyadmin

~~~bash
ln -s /usr/share/phpmyadmin /var/www/html 
~~~

# ini file for enabaling mbstring and showing display errors 

~~~bash
/etc/php/7.1/apache2/phpini 
~~~

~~~bash
display_errors = on
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







