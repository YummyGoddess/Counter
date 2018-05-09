from flask imposrt Flask, render_template, request, redirect, seesion
app =Flask(__name__)

app.secret_key = '1fish2fishredfishbluefish'
app.count =
@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html')


@app.route('/clear', methods=['POST'])
def ():
    return render_template

app.run(debug=True)
