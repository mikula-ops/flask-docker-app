from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Rute
@app.route('/')
def home():
    return render_template('index.html')  # učitava front-end

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    message = data.get('message', '')
    response = f"Server je primio: {message}"
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
