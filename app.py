import socket
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def render():

    return render_template(
        'index.html',
        hostname=socket.gethostname(),
        ip=socket.gethostbyname(socket.gethostname()))

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
