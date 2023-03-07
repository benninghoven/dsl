PATH=$PATH:/opt/homebrew/bin
# CUSTOMIZE THIS AS YOU PLEASE
#= Visual
#clear
#neofetch
#= Utility
alias cl="clear"
#alias rf="clear;neofetch"
alias src="source ~/.zshrc;echo zshrc sourced 🦑"
alias ll="ls -la --color"
alias ls="ls --color"
alias genkey="ssh-keygen -t rsa -b 4096"
alias vz="vim ~/.zshrc"
alias vr="vim ~/.config/nvim/init.vim"
#alias tmux="TERM=screen-256color tmux" # fixes tmux sessions not having color
#alias tmux="TERM=screen-256color-bce tmux" # fixes tmux sessions not having color
alias tkill="tmux kill-server"
alias vim="nvim"

PROMPT="%~"$'\n'

source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh
source $(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
