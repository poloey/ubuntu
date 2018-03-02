### How to install mysql in ubuntu

~~~bash
sudo apt install mariadb-server mariadb-client
~~~

#### security script for mysql 

~~~bash
sudo mysql_secure_installation
~~~




### To enable MariaDB to automatically start at boot time, run

~~~bash
sudo systemctl enable mariadb
~~~

### If it’s not running, start it with this command:

~~~bash
sudo systemctl start mariadb
~~~

### to know status about mariadb

~~~bash
systemctl status mariadb
~~~

### removing sudo from mariadb 

~~~bash
sudo mysql -uroot -p
~~~
#### mysql 

~~~sql
use mysql
select user, plugin from user;
update user set plugin='' where user='root'
select user, plugin from user;
~~~


#### If earlier one not working for we can drop earlier user and create a new user and give privileges to that user 

~~~bash
sudo mysql -u root
~~~

sql part 

~~~sql
SELECT User,Host FROM mysql.user;
 DROP USER 'root'@'localhost'
CREATE USER 'root'@'localhost' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;

 FLUSH PRIVILEGES;

~~~



