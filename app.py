from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('CV1.html')

@app.route('/assignment8')
def ass8():
    return render_template('assignment8.html', firstName='Noa', lastName='Matityahu',
                           hobbies=('Baking', 'Sleep', 'Pilates'))


if __name__ == '__main__':
    app.run(debug=True)