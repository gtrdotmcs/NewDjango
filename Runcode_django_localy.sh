#!/bin/env bash
{
    read -p "This script run the code with command python manage.py runserver. do You like to y/n " -n 1 -r
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        echo "Running the code......"
        source venv/bin/activate
        python manage.py runserver
    else
        printf "\n *****************It is fine dude****************** \n"    
    fi
}
