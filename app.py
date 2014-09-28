import os, cStringIO, mandrill, base64, time
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def send_email(subject, fields, file_to_attach=None):
    if file_to_attach:
        attachment = {
            'content': base64.b64encode(file_to_attach.read()),
            'name': file_to_attach.filename,
            'type': file_to_attach.content_type
        }

    text = ''
    for k in fields:
        text += "%s: %s\n" % (k, fields[k])

    message = {
        'from_email': 'no-reply@pairstaffing.com',
        'from_name': 'Pair Staffing',
        'headers': { 'Reply-To': 'no-reply@pairstaffing.com' },
        'html': text,
        'important': True,
        'subject': subject,
        'text': text,
        'to': [{
            'email': 'info@pairstaffing.com',
            'name': 'Evan Myers',
            'type': 'to'
        }]
    }
    if file_to_attach:
        message['attachments'] = [attachment]

    mandrill.Mandrill().messages.send(message=message, async=False)



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/candidate", methods=['POST'])
def candidate():
    send_email('Candidate Resume', request.form, request.files['file'])
    return redirect(url_for('index'))

@app.route("/employer")
def employer():
    send_email('Job Details', request.form, request.files['file'])
    return redirect(url_for('index'))

@app.route("/other")
def other():
    send_email('Comment/Question', request.form)
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
