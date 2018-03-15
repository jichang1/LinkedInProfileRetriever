from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
from os import path
import requests
import json

app = Flask(__name__)

@app.route('/')
def Index():
       return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year
       )
   
@app.route('/oauth/callback')
def Auth_upload():
    authcode = request.args.get('code', '')
    token = GetToken(authcode)
    profile = GetMe(token)
    return render_template(
        'profile.html',
        token=token,
        profile=profile
        )

def GetToken(authcode):
    client_id = '$client_id$'
    client_secret = '$client_secret$'
    redirect_uri = 'https://localhost:5000/oauth/callback'

    url = "https://www.linkedin.com/oauth/v2/accessToken"
    
    row_data = { 'grant_type': 'authorization_code', 'code': authcode, 'redirect_uri': redirect_uri, 'client_id': client_id, 'client_secret': client_secret }
    response = requests.post(url, data= row_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})

    if response.status_code == 200 and 'access_token' in response.json():
       return response.json()['access_token']
    else:
       return ''

def GetMe(token):
    url = 'https://api.linkedin.com/v2/me'
    response = requests.get(url, headers={'Connection': 'keep-alive', 'X-RestLi-Protocol-Version': '2.0.0', 'Authorization': 'Bearer %s' % token })
    return json.dumps(response.json(), sort_keys=True, indent=4)


rootdir = path.dirname(__file__)
key_path = path.join(rootdir, 'ssl', 'server.key')
crt_path = path.join(rootdir, 'ssl', 'server.crt')
ssl_context = (crt_path, key_path)

if __name__ == '__main__':
  app.run('127.0.0.1', 5000, ssl_context=ssl_context)
