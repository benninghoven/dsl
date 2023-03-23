PATH=$PATH:/opt/homebrew/bin
PATH=$PATH:/Users/devin/Library/Python/3.9/bin
export EDITOR=nvim

alias cl="clear"
alias src="source ~/.zshrc;echo zshrc sourced 🦑"
alias ll="ls -la --color"
alias ls="ls --color"
alias genkey="ssh-keygen -t rsa -b 4096"
alias vz="vim ~/.zshrc"
alias vr="vim ~/.config/nvim/init.vim"
alias tkill="tmux kill-server"
alias vim="nvim"
alias v="nvim"
alias myip="ipconfig getifaddr en0"
alias cleand="bash ~/Sandbox/dsl/docker/scripts/cleanup.sh"
alias t="tmux"


PROMPT="%~"$'\n'

source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh
source $(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

cat ~/Sandbox/dsl/dotfiles/fish.txt

