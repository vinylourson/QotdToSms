#!/bin/bash
# Quote of The Day (à lancer avec un cron par ex)
# permettant d'envoyer un sms contenant une QoTD.
# Fonctionne avec l'option "notif par sms" de chez Free Mobile
# dépendances : curl, fortunes, fortunes-fr
# user et pass sont à récupérer sur l'interface abonné http://mobile.free.fr
# dans l'option "Notification par sms"

# on limite la fortune à 120 caractère pour pouvoir tenir dans un sms
fortunefr=`fortune -n120 -s fr`
# on encode la fortune au format URL 
textpercent=`curl -s -o /dev/null -w %{url_effective} --get --data-urlencode "$fortunefr" ""`
# variables à remplir avec les identifiants récupérés sur http://mobile.free.fr
user=
pass=

curl -k "https://smsapi.free-mobile.fr/sendmsg?user=$user&pass=$pass&msg=$textpercent"
