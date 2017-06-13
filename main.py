from flask import Flask, render_template, request
from flask_mail import Mail, Message
import random
import os
import pprint

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'troll.talk.sms'
app.config['MAIL_PASSWORD'] = 'superbaby'

mail = Mail(app)

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
INSULTS_PATH = '/static/talk.txt'

CARRIERS = {
    'Verizon':'@vzwpix.com',
    'AT&T':'@mms.att.net',
    'Sprint':'@pm.sprint.com',
    'T-Mobile':'@tmomail.net'
    }

@app.route('/', methods=['POST'])
def parse_request():
    phone_num = request.form['phone_num']
    carrier = request.form['carrier']
    phone_num = phone_num.replace('-', '')
    if (phone_num.isdigit() and len(phone_num) == 10):
        msg = 'Thanks for using Troll Talk!'
        insult = get_random_insult(insults)
        htmlInsult = 'Insult sent: ' + insult
        send_insult(phone_num, carrier, insult)
        return render_template('index.html', carriers=CARRIERS.keys(), message=msg, insult=htmlInsult)
    else:
        error_msg = "Please input a valid phone number"
        return render_template('index.html', carriers=CARRIERS.keys(), message=error_msg, insult=error_msg)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', carriers=CARRIERS.keys())

@app.route('/sms_test')
def index():
    msg = Message('Troll Talk SMS', sender=("Troll Talk", "troll.talk.sms@gmail.com"), recipients=['2484082851@vtext.com'])
    msg.body = "I need an apology letter. Can I borrow your birth certificate?"
    mail.send(msg)
    return 'Message Sent!'

def get_insult_list():
    with open(DIR_PATH+INSULTS_PATH) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def get_random_insult(insults):
    return insults[random.randint(0, len(insults)-1)]

def get_carrier_domain(carrier):
    return(CARRIERS[carrier])

def send_insult(number, carrier, insult):
    msg = Message('Troll Talk SMS', sender=("Troll Talk", "troll.talk.sms@gmail.com"), recipients=[number + get_carrier_domain(carrier)])
    msg.body = insult
    file_name = "image" + str(random.randint(0, 5)) + ".png"
    with app.open_resource(file_name) as fp:
        msg.attach(file_name, "image/png", fp.read())
    mail.send(msg)
    return 'Message Sent!'

insults = get_insult_list()

if __name__ == '__main__':
    app.run(debug=True)
