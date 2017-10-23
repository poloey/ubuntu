# Things I need to do after installing windows

Install sublime text, vs code, git bash, xampp.      
After installing xampp add php and mysql path to environment path. php can be found `xampp > php` and mysql can be found `xampp > mysql > bin`.   

Now install chocolaty package manager. Afer installing chocolaty I can easily install `vlc`, `python`, `cmder`, `wget` and many others. 

for styling git bash and adding alias I will use `bash_it` library from github. Once I install `bash_it` I will make `.bash_aliash` file inside `~` and added source to `.bashrc` file. `source ~/.bash_alias`. 

For working with vim I will install `vundle` from github. Once `vundle` install in my pc I will keep `plugins.vim` file inside `~/.vim` directory and keep `.vimrc` file inside `~` folder.

### Problem with mysql in gitbash
I didn't get mysql in gitbash terminal. So I have to use winpty before mysql command
~~~
winpty mysql -uroot -p
~~~

