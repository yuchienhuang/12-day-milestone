from flask import Flask, render_template, request, redirect, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from day10 import *
import os


class ReusableForm(Form):
    name = TextField('Ticker symbol:', validators=[validators.DataRequired()])
    month = TextField('month:', validators=[validators.DataRequired()])


app = Flask(__name__, static_folder='public', template_folder='templates')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/graph', methods=['GET','POST'])
def graph():
    return render_template('graph.html')


@app.route('/about', methods=['GET','POST'])
def about():
  form = ReusableForm(request.form)
  print(form.errors)
  if request.method == 'POST':
      name=request.form['name']
      month=int(request.form['month'])
      print(name)
      fig = df_one_month_closing_price(2017,12,'FB')
      fig.savefig(os.path.join(app.root_path, 'public/plot'))
      return render_template('graph.html', name = 'new_plot', url ='/public/plot.png')
# Save the comment here.
      flash('Hello ' + name)
  else:
      flash('All the form fields are required. ')
      

  
  return render_template('about.html',form =form)



if __name__ == '__main__':
  app.run(port=3000)
  
