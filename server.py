from flask import Flask, render_template, redirect, request, session
import datetime
import random
app = Flask(__name__)
app.secret_key = 'abcdefghijklmnopqrstuvwxyz'

@app.route('/')
def index():
  if 'gold' in session:
    session['gold'] = session['gold']
  else:
    session['gold'] = 0
  if 'append' not in session:
    session['append'] = []

  session['farm'] = random.randrange(10,20)
  session['cave'] = random.randrange(5,10)
  session['house'] = random.randrange(2,5)
  session['casino'] = random.randrange(-50,50)
  return render_template('index.html')

@app.route('/process_gold', methods=['POST'])
def gold():
  if request.form['location'] == 'farm':
    session['gold'] += session['farm']
    session['append'].insert(0, "Gained " + str(session['farm']) + " from the farm. " + str(datetime.datetime.now()))
  if request.form['location'] == 'cave':
    session['gold'] += session['cave']
    session['append'].insert(0, "Gained " + str(session['cave']) + " from the cave. " + str(datetime.datetime.now()))
  if request.form['location'] == 'house':
    session['gold'] += session['house']
    session['append'].insert(0, "Gained " + str(session['house']) + " from the house " + str(datetime.datetime.now()))
  if request.form['location'] == 'casino':
    session['gold'] += session['casino']
    session['append'].insert(0, str(session['casino']) + " from the casino " + str(datetime.datetime.now()))
  return redirect('/')

@app.route('/reset')
def reset():
  session.clear()
  return redirect('/')

app.run(debug=True)