from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/auth/<username>', methods = ['POST'])
def auth(username, password):

    if (username == "buloy") and (password == "dagan"):
        status = "ok"
    return jsonify(status = status)

    else if (username == "kalay") and (password == "magad"):
        status = "ko"
    return jsonify(status=status)

@app.route('/load/<username>', methods = ['GET'])
def load(username):
    if username == "buloy":
        subjects = [{
                    "subject": "CSC 101",
                    "time": "07:30-09:00",
                    "day": "MTH"
                   },
                   {
                    "subject": "FIL 1",
                    "time": "07:30-09:00",
                    "day": "TF"
                    },
                    {
                    "subject": "MATH 51",
                    "time": "04:30-06:00",
                    "day": "MTTHF"
                    }]
    return jsonify(subjects = subjects)
    else if username == "kalay":
        subjects1 = [{
                    "subject": "CSC 101",
                    "time": "07:30-09:00",
                    "day": "MTH"
                    }
                    ]
        return jsonify(subjects=subjects1)

if __name__ == '__main__':
    app.run(debug = True)