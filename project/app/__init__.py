from flask import Flask, render_template, request, Response
from threading import Thread
from datetime import datetime
import json, time, SmartShark.SmSh


app = Flask(__name__)

SS = SmartShark.SmSh.SmSh()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start')
def start():
    SS.Status["GO"] = True
    return render_template('home.html')

@app.route('/stop')
def stop():
    SS.Status["GO"] = False
    return render_template('home.html')

@app.route('/chart-data')
def chart_data():
    def generate_new_data():
        json_data = {}
        while True:
            if SS.Status['NEW']:
                print(f'bad packets -> {SS.IA["NUMBER_BAD_PACKETS"]} / {SS.IA["NUMBER_PACKETS"]}')
                json_data = json.dumps({
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'value': [SS.IA["NUMBER_BAD_PACKETS"], SS.IA["NUMBER_PACKETS"]]
                    })
                SS.Status['NEW'] = False
                yield f'data:{json_data}\n\n'
    t2 = Thread(target = generate_new_data)
    t2.daemon = True
    t2.start()
    return Response(generate_new_data(), mimetype='text/event-stream')

if __name__ == '__main__':
    t1 = Thread(target=SS.StartSmSh)
    t1.daemon = True
    t1.start()
    app.run(debug=True, threaded=True, host='0.0.0.0')