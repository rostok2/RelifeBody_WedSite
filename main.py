from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start() -> 'html':

    return render_template('page1.html')

if __name__ == '__main__':
    app.run(debug=True)