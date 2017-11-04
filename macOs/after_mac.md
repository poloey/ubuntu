# after mac

### to open sublime through terminal (making symbolic link)
~~~
ln -sv "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl
~~~

### downloading mysql and php using home brew
first tap php using `brew tap homebrew/homebrew-php`. Then you can search php using `brew search`. `brew search php` or `brew search mysql`       
some essential command for installing and configuring php and mysql
~~~
brew info mysql
brew install mysql
brew tap homebrew/services
brew services start mysql
brew services list
~~~

### downloading composer 
download composer through php command which shown in composer website      
getting started > globally > `mv composer.phar /usr/local/bin/composer`     
added `/Users/polodev/.composer/vendor/bin` to path for composer global package


### sublime key repeat and other apps key repeat on holding key
~~~
defaults write com.sublimetext.3 ApplePressAndHoldEnabled -bool false
defaults write -g ApplePressAndHoldEnabled -bool false
~~~

