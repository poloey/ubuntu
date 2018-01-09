# software
~~~
sudo apt install vim git zsh net-tools rlwrap tree ranger xclip unity-tweak-tool exfat-utils exfat-fuse ruby ruby-dev chromium-browser
~~~


# sublime

~~~
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-get install apt-transport-https
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install sublime-text
~~~

# zsh path and alias and nvm (first have to download nvm)
~~~
export PATH=/opt/lampp/bin:$PATH
export PATH=$HOME/.config/composer/vendor/bin/:$PATH
alias zshconfig="vi ~/.zshrc" 
alias zshconfig_alias="vi ~/.zsh_alias" 
source ~/.zsh_alias
alias xampp="sudo /opt/lampp/manager-linux-x64.run"
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
~~~


# giving permission

~~~
sudo chmod -R o+w /opt/lampp/
sudo chmod 777 -R /opt/lampp/htdocs
sudo chmod 755 /opt/lampp/phpmyadmin/config.inc.php
~~~




