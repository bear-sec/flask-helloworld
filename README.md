# flask-helloworld
flask hello world web shell app and client

# requirements

1. flask
2. requests

# usage

app.py is a simple web-shell on flask that accepts commands via http get requests.
run the server by first exporting FLASK_APP env var to be the path to app.py, and run using 
`python -m flask run --host=0.0.0.0`
this tells the host to listen on all public IPs.

run the client code and set `server` and `port` vars to the ip,and port to connect to and input os commands.
*remember:* if you run flask on a windows machine, commands such as `dir` wont run properly since its not a process, but just a cmd thing.
to run internal cmd commands, run cmd /c `command`
