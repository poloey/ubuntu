# Development Environment setup after Installing Ubuntu

## Installing vim
~~~
sudo apt-get installing vim
~~~

## ZSH
Installing zsh in ubuntu
~~~
sudo apt-get install zsh
~~~

after installing zsh now I have to configure by downloading ad installing oh-my-zsh configuration through curl or wget
~~~
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
~~~

To make zsh as my default bash (require restart machine in order to take effect)
~~~
chsh -s /bin/zsh
~~~


If you open ~/.zshrc file you will find default theme is
~~~
ZSH_THEME="robbyrussell"
~~~
I personally love agnoster so in my ~/.zshrc file I changed to ZSH_THEME="agnoster"

To make a alias in .zshrc file 
~~~
alias zshconfig="vi ~/.zshrc" 
alias zshconfig_alias="vi ~/.zsh_alias" 
~~~

I can make a file with load of alias and load to .zshrc by following
~~~
source ~/.zsh_alias 
~~~

#### to install font and solarized theme      
zsh icon require power line font. I fork a repo from another author. 

[https://gist.github.com/renshuki/3cf3de6e7f00fa7e744a](https://gist.github.com/renshuki/3cf3de6e7f00fa7e744a)

mine

[https://gist.github.com/polodev/444028fb558bed0fbe6131bf288230f0]( https://gist.github.com/polodev/444028fb558bed0fbe6131bf288230f0)

for visual tweeking terminal using lot of theme. Here I have to link how to use sever color scheme and background (terminal theme)   
[https://github.com/Mayccoll/Gogh]( https://github.com/Mayccoll/Gogh )


## Vim key bindings in Wordprocessing software
libre office
============
https://github.com/seanyeh/vibreoffice/
just download plugin form state above git repo and open with libre office.


## Installing xampp in Ubuntu
download xampp.run file official directory   
~~~
sudo chmod +x <xamppfile.run>
sudo ./<xamppfile.run>
~~~


## Add php mysql to path
making a symbolik link for php and mysql
~~~
sudo ln -s /opt/lampp/bin/php /usr/bin/php
sudo ln -s /opt/lampp/bin/mysql /usr/bin/mysql
~~~


## Installing composer
first install some php extension for php. Those extension is essential for installing laravel
~~~
apt install php-mcrypt php-gd php-mbstring
~~~
if php in your path download from following [composer official site](https://getcomposer.org/download/). After downloading composer.phar file move composer.phar file to /usr/bin/composer folder
~~~
sudo mv composer.phar /usr/bin/composer
~~~
adding composer bin folder to the path for composer global package (.zshrc)
~~~
$HOME/.config/composer/vendor/bin/:
~~~
For tinkering laravel project i need readline.  
By using rlwrap prefix command i can cycle through previous command in laravel tinker
~~~
sudo apt-get install rlwrap
rlwrap php artisan rlwrap
~~~


## Installing nodejs in ubuntu  (currently i am using nvm apporach)
You have to install nvm after fully installing zsh shell. since it will add path to .zshrc file 
https://github.com/nodesource/distributions   

## Install nodejs with nvm (https://github.com/creationix/nvm)
~~~
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.4/install.sh | bash
~~~

~~~
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm
~~~

~~~
nvm install 8
nvm use 8
~~~

## Wifi driver for ubuntu
~~~
sudo apt-get install bcmwl-kernel-source
~~~

## Installing ranger and tree for fun
~~~
sudo apt-get install tree
sudo apt-get install ranger
~~~

### Minimize single window application on click
~~~
sudo apt-get install unity-tweak-tool
~~~
### If you need pair dependency you can run following command (It required when I installed vscode)
~~~
sudo apt --fix-broken install
~~~

### To minimize single window app click
functionality will be available `Unity Tweak Tool > Launcher > Minimize single window application on click`

### To keep terminal new tab in same director I have put following code last line of `.zshrc` file.
~~~
. /etc/profile.d/vte.sh
// in my case 
. /etc/profile.d/vte-2.91.sh
~~~

### To manage teminal credential
~~~
sudo apt install keepassx
~~~

### If I ever face grub rescue mode in dual boot ubuntu and windows. you will write inside `grub rescue >` console 
To know all available partitions in grub rescue menu
~~~bash
ls  
~~~
output might look like following    
~~~
(hd0) (hd0,msdos5) (hd0,msdos3) (hd0,msdos2) (hd0,msdos1) (hd1) (hd1,msdos1)
~~~

You can check appropriate ubuntu partition by checking them
~~~
ls (hd0,msdos5) //never put any space after `,`
~~~
Once you sure about right partitions you will do following. Let, in our case right partition is `(hd0,msdos3)`     
~~~
set prefix="(hd0,msdos3)/boot/grub"
set root="(hd0,msdos3)"
insmod normal
normal
~~~
Once you boot into ubuntu run following 2 command as well:
~~~
sudo update-grub
sudo grub-install /dev/sda
~~~


### How to mounting windows partitions in ubuntu in case of dual boot
first know the uuid of your windows partitions
~~~
sudo blkid
~~~
once you know the windows partition uuid open fstab file in sublime or any other editor. In my case I am opening fstab using vim
~~~
sudo vi /etc/fstab
~~~
added following line in fstab file
~~~
UUID=<UUID>    /your_desired_filename   ntfs   defaults,errors=remount-ro 0       1
~~~
`<UUID>` will be replaced by your own UUID which you have get by `sudo blkid` command. Save fstab and restart



















