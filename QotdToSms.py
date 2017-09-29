#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Encode fortune and pass it to free-mobile API
# Gaël Aveline - 2015
# https://github.com/vinylourson
# depends on python 3.4.2 or higher
# also needs fortunes program (and its local variants if needed)

from urllib.parse import quote
from urllib.request import urlopen
import subprocess
import ssl

# replace identifiant and mdp values
# with your own credentials
identifiant = str('xxxx')
mdp = str('xxxx')
apifree = 'https://smsapi.free-mobile.fr/sendmsg?user=' + identifiant + '&pass=' + mdp + '&msg=' + str(quote(subprocess.check_output(["/usr/bin/fortune", "-n120", "-s", "fr"])))

# If Python 3.4.4, uncomment the line below
# urlopen(apifree, context=ssl._create_unverified_context())
# If Python 3.4.2, comment the line above and use the line below instead  
urlopen(apifree)
