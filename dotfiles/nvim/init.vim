" Disable compatibility mode (not needed with Neovim)
set nocompatible

set nowrap

" Temporarily turn off filetype detection and plugin loading
filetype off

" Add vim-airline plugin directory to the runtimepath
set rtp+=~/.config/nvim/plugged/vim-airline

" Begin managing plugins with Vim-Plug
call plug#begin('~/.config/nvim/plugged')

" Add plugins to be installed
Plug 'vim-airline/vim-airline' "this plugin provides a customizable and informative statusline
Plug 'tpope/vim-fugitive' "This plugin provides integration with Git
Plug 'scrooloose/nerdtree' "file explorer for Neovim
Plug 'jiangmiao/auto-pairs' " automatically inserts matching pairs of brackets, braces, and quotes as you type
Plug 'tpope/vim-surround' "easily surround text with various types of characters
Plug 'tpope/vim-repeat' "extends the functionality of the . command,
Plug 'tpope/vim-commentary' "This plugin provides a variety of commands for commenting and uncommenting
Plug 'tpope/vim-sleuth' "automatically detects and sets the indentation settings for each file based on its contents
Plug 'tpope/vim-endwise' "This plugin automatically inserts matching end keywords for various programming languages 
Plug 'itchyny/lightline.vim' "This is an alternative statusline plugin
Plug 'preservim/nerdcommenter' "variety of commands for commenting and uncommenting code
Plug 'morhetz/gruvbox'
Plug 'joshdick/onedark.vim'
Plug 'Mofiqul/dracula.nvim'
Plug 'EdenEast/nightfox.nvim'

Plug 'wakatime/vim-wakatime'

Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'fannheyward/coc-pyright'
"Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}




" End plugin management with Vim-Plug
call plug#end()


" Turn filetype detection and plugin loading back on, and enable syntax highlighting
filetype plugin indent on
syntax enable

colorscheme carbonfox


" Enable line numbering and relative line numbering
set number
set relativenumber

" Enable auto-indentation and smart indentation
set autoindent
set smartindent

" Set indentation settings for tabs and spaces
set tabstop=4
set shiftwidth=4
set expandtab

" Enable incremental search and highlight search results
set incsearch
set hlsearch

" Use the system clipboard by default
set clipboard=unnamedplus

" Configure various settings related to editing files
set hidden
set backspace=indent,eol,start
set laststatus=2

" Enable mouse support in Neovim
set mouse=a

" Set the time (in milliseconds) that Neovim waits before updating the display during certain operations
set updatetime=300

au BufReadPost * if line("'\"") > 0 && line ("'\"") <= line("$") | exe "normal! g'\"" | endif

:set colorcolumn=120

:tnoremap <Esc> <C-\><C-n>

:inoremap <silent><expr> <TAB>
      \ coc#pum#visible() ? coc#pum#next(1) :
      \ CheckBackspace() ? "\<Tab>" :
      \ coc#refresh()
