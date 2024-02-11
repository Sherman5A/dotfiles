
HISTSIZE=1000
SAVEHIST=10000
HISTFILE=~/.zsh_history
setopt INC_APPEND_HISTORY_TIME

bindkey -e
# colours
PS1="%F{#FF5570}%n%f%F{#7bed61}@%f%F{#53d8fc}%m%f %F{#ff9e9e}%B%~%b%f %F{#7bed61}❭❭%f "
#2e8FF0
# ❭
autoload -Uz compinit
zstyle ':completion:*' completer _complete _approximate _extensions
zstyle ':completion:*' menu select
zstyle ':completion:*' expand prefix suffix
zstyle ':completion:*:descriptions' format '%F{cyan}%d%f' 
compinit

# Alias
alias please-go-to-sleep='sudo shutdown -H 0'
alias ls='ls --color=auto'
alias ponnng='ping www.archlinux.org'
alias please-battery='cat /sys/class/power_supply/BAT0/capacity'
alias pavucontrol='(pavucontrol &) && sleep 0.2 && leftwm-command "TileToFloating"'
alias hx="helix"
alias dot-config="/usr/bin/git --git-dir=$HOME/.config-git/ --work-tree=$HOME"
#
# Path
path+=('/home/jake/.config' '/home/jake/.deno/bin')
export PATH
