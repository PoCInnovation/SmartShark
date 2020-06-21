import json
import random
import time
from threading import Thread
from datetime import datetime

from flask import Flask, Response, render_template
import app.static.SmartShark.SmSh


application = Flask(__name__)
random.seed()

SS = app.static.SmartShark.SmSh.SmSh()

@application.route('/')
def index():
    return render_template('index.html')


@application.route('/chart-data')
def chart_data():
    def generate_new_data():
        json_data = {}
        while True:
            if SS.Status['NEW']:
                print(SS.IA["NUMBER_BAD_PACKETS"])
                json_data = json.dumps({
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'value': SS.IA["NUMBER_BAD_PACKETS"]})
                SS.Status['NEW'] = False
                yield f'data:{json_data}\n\n'
    t1 = Thread(target = SS.StartSmSh)
    t2 = Thread(target = generate_new_data)
    t1.daemon = True
    t2.daemon = True
    t1.start()
    t2.start()
    return Response(generate_new_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    application.run(debug=True, threaded=True)
