import json
import random
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def basee():
    return render_template('base.html')


@app.route('/member')
def member():
    with open('templates/crew.json', encoding='utf-8') as f:
        crew = json.load(f)
    random_member = random.choice(crew)
    return render_template('member.html', member=random_member)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
