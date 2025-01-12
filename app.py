from talon import quotations
from talon.signature.bruteforce import extract_signature

from flask import Flask, Response, request

quotations.register_xpath_extensions()

app = Flask(__name__)


@app.route('/reply/extract_from_html', methods=['POST'])
def extract_from_html():
    html = request.get_data(as_text=True)
    msg = quotations.extract_from_html(html)
    text, signature = extract_signature(msg)
    return text

@app.route('/reply/extract_from_plain', methods=['POST'])
def extract_from_plain():
    data = request.get_data(as_text=True)
    msg = quotations.extract_from_plain(data)

    text, signature = extract_signature(msg)

    return text

@app.route('/health')
def health():
    return Response('OK', status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
