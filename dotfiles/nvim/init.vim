:set number
:set tabstop=4 softtabstop=4
:set shiftwidth=4
:set expandtab
:set smartindent
:set ai
:set nohlsearch
:set hidden
:set noerrorbells
:set nowrap
:set noswapfile
:set nobackup
:set incsearch
:set termguicolors
:set backspace=indent,eol,start
:set belloff=all
:set ic

:set clipboard+=unnamedplus

:syntax on

au BufReadPost * if line("'\"") > 0 && line ("'\"") <= line("$") | exe "normal! g'\"" | endif

call plug#begin()

Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'Mofiqul/dracula.nvim'
Plug 'leafgarland/typescript-vim'
Plug 'peitalin/vim-jsx-typescript'
Plug 'styled-components/vim-styled-components', { 'branch': 'main' }
Plug 'jparise/vim-graphql'
Plug 'wakatime/vim-wakatime'

call plug#end()

color dracula


highlight Normal guibg=none
highlight NonText guibg=none

:set colorcolumn=72

inoremap <silent><expr> <tab> pumvisible() ? coc#_select_confirm() : "\<C-g>u\<TAB>"
