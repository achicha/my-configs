# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

alias l='ls -aCF'
alias ll='ls -lah'
alias h='history 50'
alias grep='grep --color=auto'
alias dir='dir --color=auto'

alias cdd='cd /usr2/scripts/Green/download-external-data'
alias ae='deactivate &> /dev/null; source ./venv/bin/activate'
alias de='deactivate'

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=
export EDITOR=nano

# User specific aliases and functions
PS1='\[\033[01;32m\]\u@\H\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
