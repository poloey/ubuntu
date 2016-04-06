" following code for escaping using jj
ino jj <esc>
"following code for cindent which is kind of cindent
"set cindent
"set number is used for gutter numbering
set number

"calling pathogen auto bundle loader
execute pathogen#infect()

"following code for no swapfile by vim
set noswapfile

"colorscheme molokai >> this things coming from plugin setting
colorscheme base
"
"following codes for indentation
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4
set smartindent
set autoindent

"for file type detection and indentation according file
filetype plugin indent on
"for the cursor change following code will be implemented 
if has("autocmd")
    au VimEnter,InsertLeave * silent execute '!echo -ne "\e[2 q"' | redraw!
    au InsertEnter,InsertChange *
        \ if v:insertmode == 'i' | 
        \   silent execute '!echo -ne "\e[6 q"' | redraw! |
        \ elseif v:insertmode == 'r' |
        \   silent execute '!echo -ne "\e[4 q"' | redraw! |
        \ endif
    au VimLeave * silent execute '!echo -ne "\e[ q"' | redraw!
endif
