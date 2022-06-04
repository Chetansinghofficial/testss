from flask import Flask,render_template,redirect
from flask_cors import CORS
import requests
import rsa
import base64
import random as rand
privateKey = rsa.PrivateKey(7802045239286059309623703691501237961139444555844104666518165169699850024458605155586399760382407954406856876123886253609328200094685343197254896025360323, 65537, 2087505733721120130525529765330640823482615320913779625667882665527669409642089164327221668075901927809635418275903143700450513687324779115409451446763873, 4514858500735242502807823479020932919839796515251106454801106968306136743401783891, 1728081896257767558199720568342951196658967378853532520948341464886675153)
safelinks =['https://ez4short.com/api?api=171fc1cd1ffb9e7dfdcdb58150ed1c321d305378&url=','https://droplink.co/api?api=361aea60139704c76f713d28bfb546e47f1074a0&url=','https://link1s.com/api?api=960a9ec21ba4bf936c392ca3ba1d9181a6dcd772&url=','https://try2link.com/api?api=c41296ea4688072c7eb758ee65621c096670e2f5&url=']

app = Flask(__name__)
CORS(app, expose_headers=["Content-Disposition"])

@app.route("/")  
def home():
	return render_template('403.html')


@app.route("/stream/<idx>/<idn>") #naruto-episode-1 #TwBqzFeK2KWz9EzdAgg3Imf3x2rz++b5fct0doQsguUQrAWBGeig7P6eA4bV0hdvaA5vfeM3N2Ag9+Q+MtvmFw==
def download(idx,idn):

    idx = idx.replace('+c++','/')
    idx = idx.replace('++c+','\\')
    id = rsa.decrypt(base64.b64decode('MSNOp5lWcWwPNPqmzod+GNTxugO19lWow5heAiqiyx33wTGfhwT4QT/3QoVMYr9MVWhEtg7CHsW4ZZnfyBeyng=='), privateKey).decode()


    reqUrl = "https://tesxtssm.toonsmafia.com/api/v1/AnimeEpisodeHandler/"+id

    headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
}

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
    response = response.json()
    # xx = response['anime'][0]['servers'][0]['name']
    # yy1 = response['anime'][0]['servers'][0]['iframe']
    # yy = yy1.replace('https://','')
    # return render_template('stream.html',fname = xx, ifurl = 'https://'+yy)
    ur = response['anime'][0]['servers'][int(idn)]['iframe']
    yy = ur.replace('https://','')
    x = rand.randint(1,4)
    sf = requests.request("GET", safelinks[x-1]+'https://'+yy)
    sf=sf.json()
    return redirect(sf['shortenedUrl'],code=302)


@app.route('/down/<idx>')
def down(idx):
    idx = idx.replace('+c++','/')
    idx = idx.replace('++c+','\\')
    id = rsa.decrypt(base64.b64decode('MSNOp5lWcWwPNPqmzod+GNTxugO19lWow5heAiqiyx33wTGfhwT4QT/3QoVMYr9MVWhEtg7CHsW4ZZnfyBeyng=='), privateKey).decode()


    reqUrl = "https://tesxtssm.toonsmafia.com/api/v1/AnimeEpisodeHandler/"+id

    headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
}

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
    response = response.json()
    # xx = response['anime'][0]['servers'][0]['name']
    # yy1 = response['anime'][0]['servers'][0]['iframe']
    # yy = yy1.replace('https://','')
    # return render_template('stream.html',fname = xx, ifurl = 'https://'+yy)
    ur = response['anime'][0]['servers'][0]['iframe']
    yy = ur.replace('https://','')
    yy = yy.replace('streaming.php','download')
    x = rand.randint(1,4)
    sf = requests.request("GET", safelinks[x-1]+'https://'+yy)
    sf=sf.json()
    return redirect(sf['shortenedUrl'],code=302)
    
if __name__ == "__main__":
    app.run()