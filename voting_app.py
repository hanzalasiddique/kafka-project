from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize the votes dictionary with four color options and set their initial counts to 0
votes = {
    "Red": 0,
    "Blue": 0,
    "Green": 0,
    "Yellow": 0
}

@app.route('/')
def index():
    return render_template('index.html', votes=votes)

@app.route('/vote', methods=['POST'])
def vote():
    option = request.form['option']
    if option in votes:
        votes[option] += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
