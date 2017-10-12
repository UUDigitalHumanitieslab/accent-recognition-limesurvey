scp ./*{.js,.css} im-static:
scp ./img/*.jpg im-static:
ssh -t im-static "sudo mv ./*{.js,.css} /hum/web/dhstatic.hum.uu.nl/htdocs/name-face && sudo chown -R www-data:www-data /hum/web/dhstatic.hum.uu.nl/htdocs/name-face &&
sudo mv ./*.jpg /hum/web/dhstatic.hum.uu.nl/htdocs/name-face/img && sudo chown -R www-data:www-data /hum/web/dhstatic.hum.uu.nl/htdocs/name-face/img"
