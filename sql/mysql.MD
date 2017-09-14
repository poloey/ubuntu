### To log in 
~~~   
mysql -u root -p
~~~   

### to show databases
~~~   
SHOW DATABASES;
~~~   

### To select a database
~~~   
USE databaseName;
~~~   

### To show tables;
~~~   
SHOW TABLES;
~~~   

### To show details of a specific table
~~~   
DESCRIBE tableName;
~~~   

### to create a database
~~~   
CREATE DATABASE databaseName
~~~   

###to delete a database 
~~~   
DROP DATABASE databaseName
~~~   

### to create a table under a database
~~~   
CREATE TABLE tableName(
 id INT(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
 name VARCHAR(30) NOT NULL,
 email VARCHAR(30) NOT NULL,
 contact INT(11),
 time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
~~~   

### to delete a table
~~~   
DROP TABLE tableName;
~~~   

### add primary key to existing table
~~~   
ALTER TABLE tableName
ADD PRIMARY KEY (columnName);
~~~   

### remove primary key from a table;
~~~   
ALTER TABLE tableName
DROP PRIMARY KEY;
~~~   

### How to delete a column in existing table
~~~   
ALTER TABLE tableName
DROP COLUMN
columnName;
~~~   

### How to add a new column in existing table;
~~~   
ALTER TABLE tableName
ADD COLUMN
columnName;
~~~   

### How to add a new column with current timestamp;
~~~   
ALTER TABLE tableName
ADD COLUMN
time TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
~~~   

### How to change datatype of column in mysql
~~~   
ALTER TABLE tableName
MODIFY (COLUMN = optional)
columnName VARCHAR(30);
~~~   

### alter a column to be auto increment;
~~~   
ALTER TABLE tableName 
MODIFY COLUMN (column keyword is optional) 
columnName INT AUTO_INCREMENT;
~~~   

### Insertion in a table
~~~   
INSERT INTO 
tableName (column1, column2, column3) 
VALUES ('value_1', 'value_2', 'value_3');
~~~   

### to show all row in table;
~~~   
SELECT * FROM tableName;
~~~   

### to update a row in table;
~~~   
UPDATE tableName 
SET country = 'india', name = 'Vasanth', email = 'vasanth@gmail.com'
WHERE id = 2; 
~~~   

### to delete a row in a table
~~~   
DELETE FROM tableName WHERE id = 3;
~~~   

### how to move a column OR sort column
~~~   
ALTER TABLE tableName 
MODIFY COLUMN (column keyword is optional)
id INT(11) AFTER another_column_name;
~~~   

~~~   
ALTER TABLE tableName
MODIFY COLUMN (column keyword is optional)
id INT(11) FIRST;
~~~   

