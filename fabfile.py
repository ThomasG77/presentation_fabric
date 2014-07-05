#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import *

# Utilisateur pour la connexion distante
env.user = 'utilisateurapplication'
    
# Urls des serveurs de déploiement
    
env.hosts = ['server1.exemple.com', 'server2.exemple.com']
		
def deploy():
    run('uname -a')
