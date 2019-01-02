# Development Environment setup after Installing Ubuntu

~~~
sudo apt upgrade
sudo apt update
~~~

## Installing vim
~~~
sudo apt install vim
~~~

## Installing curl
~~~
sudo apt install curl
~~~

## Installing git
~~~
sudo apt install git
git config --global core.editor "vim"
~~~

## deleting lock file 
~~~
sudo rm /var/lib/apt/lists/lock
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock
~~~




## for storing  git credentials
~~~
sudo apt-get install libgnome-keyring-dev
sudo make --directory=/usr/share/doc/git/contrib/credential/gnome-keyring
git config --global credential.helper /usr/share/doc/git/contrib/credential/gnome-keyring/git-credential-gnome-keyring
~~~
we can logout from `password and keys > login >  network password`

### for finger print in ubuntu
~~~
sudo add-apt-repository ppa:fingerprint/fingerprint-gui
sudo apt update
sudo apt install libbsapi policykit-1-fingerprint-gui fingerprint-gui
~~~

## installing sublime 


~~~
apt-get install libgtk2.0-0
~~~


* Installing sublime from official website
* installing package controll
* clone my 2 repo

## for fixing sound in x250
I temporarily solved that problem on my x250.     
for fixing sound in news devices       
https://wiki.ubuntu.com/Audio/UpgradingAlsa/DKMS     

* Switch to terminal mode via `Ctrl+Alt+F1` and log in.
* Stop the display manager LightDM with: `sudo service lightdm stop`
* Reload ALSA with: `sudo alsa reload`
* Then restart LightDM with: `sudo service lightdm start`


## for further shell customization 
~~~
https://github.com/alebcay/awesome-shell
~~~

## ZSH
Installing zsh in ubuntu
~~~
sudo apt install zsh
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

All alias can be found do_setting repo of mac

### how to install power line font for agnoster theme
first create a .fonts folder in home directory
~~~
mkdir ~/.fonts
~~~

install powerline font
~~~
wget https://github.com/powerline/powerline/raw/develop/font/PowerlineSymbols.otf
wget https://github.com/powerline/powerline/raw/develop/font/10-powerline-symbols.conf
mv PowerlineSymbols.otf ~/.fonts/
mkdir -p ~/.config/fontconfig/conf.d 
~~~

clean fonts cache
~~~
fc-cache -vf ~/.fonts/
~~~

Move config file
~~~
mv 10-powerline-symbols.conf ~/.config/fontconfig/conf.d/
~~~

## How to install theme with profile  in linux terminal

for visual tweeking terminal using lot of theme. Here I have to link how to use sever color scheme and background (terminal theme)   
[https://github.com/Mayccoll/Gogh]( https://github.com/Mayccoll/Gogh )


## Vim key bindings in Wordprocessing software
libre office
============
https://github.com/seanyeh/vibreoffice/
just download plugin form state above git repo and open with libre office.


## Installing xampp in Ubuntu
first download net-tools for netstat command. since xampp need netstat command
~~~
sudo apt install net-tools
~~~
download xampp.run file official directory   
~~~
sudo chmod +x <xamppfile.run>
sudo ./<xamppfile.run>
~~~
xampp doesn't comes with desktop entry. So what we can do ? We can add a alias following
~~~
alias xampp="sudo /opt/lampp/manager-linux-x64.run"
~~~

## fixing mysql permission 
~~~
sudo chmod 755 /opt/lampp/phpmyadmin/config.inc.php
~~~



To give permission to temp file
~~~
sudo chmod -R o+w /opt/lampp/
~~~
To give permission htdocs recursively
~~~
sudo chmod 777 -R /opt/lampp/htdocs
~~~
for further reading regarding xampp https://azuraakbar.wordpress.com/2012/05/30/52/    
How to start xampp control panel in ubuntu
~~~
sudo gedit /usr/share/applications/xampp-control-panel.desktop
~~~
paste the following code if you have 64bit pc
~~~
[Desktop Entry]
Encoding=UTF-8
Name=XAMPP Control Panel
Comment=Start and Stop XAMPP
Exec=gksudo /opt/lampp/manager-linux-x64.run
Icon=/opt/lampp/htdocs/favicon.ico
Categories=Application
Type=Application
Terminal=false
~~~
state above stuff getting from following link https://askubuntu.com/questions/890818/ubuntu-16-04-how-to-start-xampp-control-panel



## Add php mysql to path
export PATH=/opt/lampp/bin:$PATH


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
//or
export PATH=$HOME/.config/composer/vendor/bin/:$PATH

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

## Handy terminal application ranger and tree for fun
~~~
sudo apt-get install tree
sudo apt-get install ranger
~~~

### Handy copy paste in terminal using xclip (only 16kb)
~~~
sudo apt-get install xclip
~~~
You can then pipe the output into xclip to be copied into the clipboard:

~~~
cat file | xclip
~~~
To paste the text you just copied, you shall use:

~~~
xclip -o
~~~
To simplify life, you can set up an alias in your .bashrc / .zshrc file as I did:

~~~
alias c="xclip"
alias v="xclip -o"
~~~

To see how useful this is, imagine I want to open my current path in a new terminal window (there may be other ways of doing it like Ctrl+T on some systems, but this is just for illustration purposes):    
Terminal 1:
~~~
pwd | c
~~~

Terminal 2:
~~~
cd `v`
~~~
getting tutorial from [stack overlow](https://stackoverflow.com/questions/5130968/how-can-i-copy-the-output-of-a-command-directly-into-my-clipboard)    visit [main repo](https://github.com/astrand/xclip)

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


## Mounting
### exfat mounting in ubunutu
We can mounted exFat formatted External hard drive using `fuse`. We have to install following package
~~~
sudo apt-get install exfat-utils exfat-fuse
~~~

### NTFS mounting in case dual boot
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

  I have having permission issue in ntfs file. I have solving this issue by installing `NTFS Configuration Tool` from software center. If you have `gprted` installed you have to uninstall it.

#  Installing jekyll

~~~
sudo apt install ruby ruby-dev
sudo gem install jekyll bundle
~~~



# Installing avro in ubuntu
go to this following link [https://bn.maateen.me/install-avro-keyboard-in-ubuntu/](https://bn.maateen.me/install-avro-keyboard-in-ubuntu/)

### installing  Java in ubuntu
first download java file from oracle website. http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html     
To download manually on your machine follow instruction from https://www.digitalocean.com/community/tutorials/how-to-manually-install-oracle-java-on-a-debian-or-ubuntu-vps


## Setting default os in dual boot 

~~~bash
sudo vi /etc/default/grub
~~~

from grub change following

~~~bash
GRUB_DEFAULT=0
#GRUB_HIDDEN_TIMEOUT=0
GRUB_HIDDEN_TIMEOUT_QUIET=true
GRUB_TIMEOUT=2
GRUB_DISTRIBUTOR=`lsb_release -i -s 2> /dev/null || echo Debian`
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
GRUB_CMDLINE_LINUX=""
~~~

Here change `GRUB_DEFAULT` value. In my case its 0 means `ubuntu` and `4` means windows. take a look grub menu when your pc is booting. you can update `GRUB_TIMEOUT` value lesser for quick booting. save the grub file do following command
~~~bash
sudo update-grub
~~~

















