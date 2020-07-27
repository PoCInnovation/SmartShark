from flask import Flask, render_template, request, Response, jsonify
from threading import Thread
from datetime import datetime
import json, time, SmartShark.SmSh

app = Flask(__name__)

SS = SmartShark.SmSh.SmSh()

FlaskSave = {"MAX_INFECTED": 10,
             "ANTI_BRUIT": 0}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/',methods = ['POST'])
def process():
    cmd = request.form['cmd']

    cmd = request.form['cmd']
    print(cmd)
    cmd = cmd.split(" ")
    if len(cmd) == 0:
        return render_template('home.html')
    if cmd[0] == "time":
        if len(cmd) != 2:
            return render_template('home.html')
        if int(cmd[1]) > 0:
            SS.IA["TIME"] = int(cmd[1])
    if cmd[0] == "save":
        if len(cmd) != 2:
            return render_template('home.html')
        if bool(cmd[1]) == True or bool(cmd[1]) == False:
            SS.Status['SAVING'] = bool(cmd[1])
    if cmd[0] == "detect":
        if len(cmd) != 2:
            return render_template('home.html')
        if int(cmd[1]) > 0:
            FlaskSave["MAX_INFECTED"] = int(cmd[1])
    if cmd[0] == "start":
        SS.Status["GO"] = True
    if cmd[0] == "stop":
        SS.Status["GO"] = False
    if cmd[0] == "ddos":
        SS.Status["DDOS"] = True
        SS.Status["MITM"] = False
    if cmd[0] == "ddos&mitm":
        SS.Status["DDOS"] = True
        SS.Status["MITM"] = True
    if cmd[0] == "mitm":
        SS.Status["DDOS"] = False
        SS.Status["MITM"] = True
    return render_template('home.html')

@app.route('/chart-data')
def chart_data():
    def generate_new_data():
        json_data = {}
        while True:
            if SS.Status['NEW']:
                json_data = json.dumps({
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'value': [SS.IA["NUMBER_BAD_PACKETS"], SS.IA["NUMBER_PACKETS"], FlaskSave["MAX_INFECTED"], FlaskSave["ANTI_BRUIT"], SS.IA["SPY"]]
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