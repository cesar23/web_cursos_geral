#!/usr/bin/env bash
function upgit() {
	git pull
    git add -A
    git commit -m "cmder se actualizo :${DATE_HOUR_GIT}"
    git push -u origin master
}

function gitup() {
    git pull
	  git add -A
    git commit -m "cmder se actualizo :${DATE_HOUR_GIT}"
    git push -u origin master
}

function gitup2() {
    git pull
	  git add -A
    git commit -m "cmder se actualizo :${DATE_HOUR_GIT}"
    git push
}


python listar_img_webp.py


clear
gitup

echo ""
echo "  ██████  ██   ██                ██████ ███████ ███████  █████  ██████  "
echo " ██    ██ ██  ██                ██      ██      ██      ██   ██ ██   ██ "
echo " ██    ██ █████       █████     ██      █████   ███████ ███████ ██████  "
echo " ██    ██ ██  ██                ██      ██           ██ ██   ██ ██   ██ "
echo "  ██████  ██   ██                ██████ ███████ ███████ ██   ██ ██   ██ "
echo ""
echo ""
sleep 4