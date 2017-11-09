# Basic Linux command

### For authorization
~~~
sudo chmod 777 -R htdocs
~~~

### delete non empty folder
~~~
sudo rm -rf folderName
~~~

### delete empty folder
~~~
rmdir folderName
~~~

### to edit something which in root folder
~~~
sudo nautilus 
~~~

### to copy all from a exiting folder to another folder
~~~
cp -a . <folderName>
~~~

### to get the location of file path of the command. like node, gulp, bower
~~~
which <command>
~~~

### to exit terminal from terminal
~~~
exit
~~~

### to make a simple python server
~~~
python -m SimpleHTTPServer
~~~

### to install debian software
~~~
sudo dpkg -i <file>
~~~


### to make mulitple folder at a time
~~~
mkdir -p one/two/three/four_folder
~~~

### to delete a program with association 
~~~
sudo apt-get remove --purge wine*
~~~

### to maximize and minimize screen
~~~
alt + spce =>then=> x
~~~

### to close screen
~~~
alt + spce =>then=> c
~~~

### grub menu for changing boot menu
~~~
$ sudo vi /etc/default/grub
now set the default bootloader in my case windows was in number 5. so index will be 4
$ sudo update-grub
~~~

### grub menu for changing boot menu through terminal command
~~~
sudo grub-set-default 3 
~~~

### to know the size of the folder (disk uses - summary human-readable)
~~~
du -sh
~~~

###  to know the size of the individual file inside folder
~~~
du -sh *
~~~

### double command in single line
~~~
mkdir foo && cd $_
mkdir foo && mv <file> $_
~~~


### for owner ship <chown to your apache account>
~~~
sudo chown www-data:www-data -R <you_publishing_directory  || wordpess || megento>
~~~

### to uninstall a .deb package
~~~
sudo dpkg --remove <packageName>
~~~

### to write same content in multiple file
~~~
echo 'hello' | tee -a file1 file2
~~~
in my case it was like that
~~~
echo 'hello world'  | tee -a *.html
~~~

### to zip a file
~~~
zip -r php.zip php
~~~
