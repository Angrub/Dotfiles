if status is-interactive
    # Commands to run in interactive sessions can go here
alias ls='exa --group-directories-first'
alias ll="ls -la"
alias tree='exa -T'
alias cat='ccat'
alias stop-containers='docker stop $(docker ps -q)'
    # ssh-agent
fish_ssh_agent
end
