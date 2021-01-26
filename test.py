import requests, sys, json, os, subprocess

for arg in sys.argv: 
    1
    print(arg)

def read_json(file):
    with open(file) as f:
        data = json.load(f)
    return data



test = read_json(arg)
print(test['url'])
subprocess.run(["git", "clone",test['url']])

id = test['id']
print(id)
print(os.getcwd())
path  = os.getcwd()+"/"+id+"/"
print(path)
list = os.listdir(path)
len(list)
i = 0
while list[i] != test['file']:
	i+=1
print(list)
fichier = list[i]
print(fichier)
path2 = path+fichier
exec("path2")
subprocess.run(["python3", path2])
test['etat'] = 'done'
print(test)

