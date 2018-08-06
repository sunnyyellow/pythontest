#Micro gevent chatroom

from gevent import monkey; monkey.patch_all()
from flask import Flask, render_template, request, json

from gevent import queue
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
app.debug = True

class Room(object):
    def __init__(self, name):
        self.name = name
        self.users = set()
        self.messages = []

    def backlog(self, size = 25):
        index = size if size < len(self.messages) else len(self.messages)
        return self.messages[-index:]
    
    def subscribe(self, user):
        self.users.add(user)
    
    def send_msg(self, message):
        for user in self.users:
            print user
            user.queue.put_nowait(message)
        self.messages.append(message)

class User(object):
    def __init__(self, uid):
        self.uid = uid
        self.queue = queue.Queue()

rooms = {
    'python': Room('python'),
    'flask': Room('flask')
}

users = {}

@app.route('/')
def choose_name():
    return render_template('choose.html')

@app.route('/<uid>')
def main(uid):
    return render_template('main.html', uid = uid, rooms = rooms.keys())

@app.route('/<room>/<uid>')
def join(room, uid):
    user = users.get(uid, None)

    if user is None:
        users[uid] = user = User(uid)

    active_room = rooms[room]
    active_room.subscribe(user)
    print 'subscribe', active_room, user

    messages = active_room.backlog()

    return render_template('room.html', room=room, uid=uid, messages=messages)

@app.route('/put/<room>/<uid>', methods=["POST"])
def put(room, uid):
    room = rooms[room]

    message = request.form['message']
    room.send_msg(':'.join([uid, message]))

    return ''

@app.route('/poll/<uid>', methods=["POST"])
def poll(uid):
    try:
        msg = users[uid].queue.get(timeout=10)
    except Exception,e:
        print 'poll error: %s' % e
        msg = []
    return json.dumps(msg)

if __name__ == "__main__":
    http = WSGIServer(('', 5000), app)
    http.serve_forever()

