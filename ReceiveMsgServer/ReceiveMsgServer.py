import os
from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
# from flask_ngrok import run_with_ngrok


app = Flask(__name__)
# run_with_ngrok(app)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():

    body = request.values.get('Body', None)

    resp = MessagingResponse()
    yes = "yes"
    no = "no"

    if yes in body.lower():
        resp.message("The bills will be paid within 1-2 business days.")
        __write_file(yes)

    if no in body.lower():
        resp.message(
            "The bill will not be paid. You will get a reminder the next day until paid.")
        __write_file(no)

    return Response(str(resp), mimetype="application/xml")


@app.route("/", methods=['GET'])
def main():
    print("hello world")
    return str("hello world")


@app.route("/getResp", methods=['GET'])
def get_resp():
    print("Getting response")
    f = open("./resp.txt", "r")
    resp = str(f.read())
    print(resp)
    return Response(resp, mimetype="text/plain")


def __write_file(resp):
    f = open("resp.txt", "w")
    f.write(resp)
    f.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
