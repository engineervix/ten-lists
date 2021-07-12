#!/usr/bin/env bash

# requires the dialog package (https://hightek.org/projects/dialog)
#   on Ubuntu: sudo apt install dialog
#   on a Mac: brew install dialog 
#   on Windows via cygwin: apt-cyg install dialog

# Usage: . set_env.sh

HEIGHT=25
WIDTH=80
CHOICE_HEIGHT=10
BACKTITLE="Setup Flask Configuration"
TITLE="Choose the Environment"
MENU="Choose one of the following environment options:"

OPTIONS=(1 "default"
         2 "development"
         3 "staging"
         4 "production")

CHOICE=$(dialog --clear \
                --backtitle "$BACKTITLE" \
                --title "$TITLE" \
                --menu "$MENU" \
                $HEIGHT $WIDTH $CHOICE_HEIGHT \
                "${OPTIONS[@]}" \
                2>&1 >/dev/tty)

clear
case $CHOICE in
        1)
            export FLASK_CONFIGURATION="default" && export FLASK_ENV=production
            ;;
        2)
            export FLASK_CONFIGURATION="development" && export FLASK_ENV=development
            ;;
        3)
            export FLASK_CONFIGURATION="staging" && export FLASK_ENV=production
            ;;
        4)
            export FLASK_CONFIGURATION="production" && export FLASK_ENV=production
            ;;
esac
