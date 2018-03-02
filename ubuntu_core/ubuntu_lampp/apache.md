### installing apache

~~~bash
sudo apt install -y apache2 apache2-utils
~~~

### Check Apache version:

~~~bash
apache2 -v
~~~

### to know current status

~~~bash
systemctl status apache2
~~~

### to start  apache2 service 

~~~bash
sudo systemctl start apache2
~~~

### enable Apache to automatically start at boot time.

~~~bash
sudo systemctl enable apache2
~~~

### Now we need to set www-data (Apache user) as the owner of document root. By default it’s owned by the root user.

~~~bash
sudo chown www-data:www-data /var/www/html/ -R
sudo chown -R polo:root /var/www/html/
~~~

### give read permission to /var/www/html folder recursively

~~~bash
sudo chmod 755 -R /var/www/html  
~~~


