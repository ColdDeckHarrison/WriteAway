from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def run_app():
    return render_template("index.html")
    # return render_template("Landing.html")

@app.route('/home')
def run_stuff():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

