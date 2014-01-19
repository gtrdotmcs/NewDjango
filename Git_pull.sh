#!/bin/env bash
{
    read -p "This script pull all chanages to dir  all local chnages will be undone do You like to y/n " -n 1 -r
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        git stash save --keep-index
        git pull origin master
    else
        printf "\n *****************It is fine dude****************** \n"    
    fi
}
