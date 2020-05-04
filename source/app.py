from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/trigger', methods=['POST'])
def trigger():
    message = request.form.get('message')
    print(f'Received message "{message}"')
    return '', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
