from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')

@app.route('/temp', methods=["GET", "POST"])
def temp():
    return render_template("temp_hum.html")


if __name__ == "__main__":
    app.run(debug=True)