import requests, sys, json, os, subprocess, pexpect
from graphviz import render

for arg in sys.argv: 
    1
    print(arg)

def read_json(file):
    with open(file) as f:
        data = json.load(f)
    return data

#Récupération des infos
info = read_json(arg)

#Clone du dépôt distant
subprocess.run(["git", "clone", info['url']])

#Récupération des informations
id = info['id']
file = info['file']
path = os.getcwd()+"/"+id+"/"

#Exécution du fichier
render('dot', 'json', path+file)

#Ajout du résultat pour l'envoyer au dépot distant
subprocess.Popen(['git', 'add', '.'], cwd=path)

#Commit du résultat à envoyer
subprocess.Popen(['git', 'commit' ,'-m', 'Push du résultat après traitement'], cwd=path)

#Push du projet, rentrée auto du username et du password
child = pexpect.spawn('git push', cwd=path)
child.expect([pexpect.TIMEOUT, "Username for 'https://github.com':"])
child.sendline("Projet704\n".encode())
child.expect([pexpect.TIMEOUT, "Password for 'https://Projet704@github.com':"])
child.sendline("MaxenceThomas51\n".encode())
child.read()
