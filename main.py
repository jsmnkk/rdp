from flask import Flask
import os, _thread

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"




def start():
    port = int(os.environ.get('PORT', 8080))
    cmd = "sudo apt-get install docker-ce docker-ce-cli containerd.io"
    if (os.system(cmd)):
        cmd = "sudo systemctl enable docker.service"
        if (os.system(cmd)):
            cmd = f"docker run -d -p {port}:{port} u1ih/ubuntu-novnc"
            os.system(cmd)
            
if __name__ == '__main__':
    _thread.start_new_thread(start, ())
    app.run(host='0.0.0.0', port=5000,debug=False)
