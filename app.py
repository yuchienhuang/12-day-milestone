from flask import Flask, render_template, request, redirect, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField
from day10 import *
import os
import base64
import io


class ReusableForm(Form):
    name = TextField('Ticker symbol:', validators=[validators.DataRequired()])
   
    #month = IntegerField("Month")
    month = SelectField('Select Month', choices = [(1, 'Jan'), 
      (2, 'Feb'),(3,'Mar'),(4,'Apr'),(5,'May'),(6,'Jun'),(7,'Jul'),(8,'Aug'),(9,'Sep'),(10,'Oct'),(11,'Nov'),(12,'Dec')])


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
  if os.path.exists('public/plot.png'):
    os.remove('public/plot.png')
  form = ReusableForm(request.form)
  print(form.errors)
  if request.method == 'POST':
      name=request.form['name']
      month=request.form['month']
      #print(name, month, type(month))
      
      img = io.BytesIO()
      fig = df_one_month_closing_price(2017,int(month),name)
      #fig.savefig(os.path.join(app.root_path, 'public/plot'))
      fig.savefig(img, format='png')
      img.seek(0)
      plot_url = base64.b64encode(img.getvalue()).decode()
      
      #return '<img src="data:image/png;base64,{}">'.format(plot_url)

      
      return render_template('graph.html',plot_url=plot_url)
      
      
      
      # script, div = df_one_month_closing_price_v2(2017,12,'FB')
      
      # return render_template('/graph2.html', script= script, div= div)
      
      
      
# Save the comment here.
      
  
      

  
  return render_template('about.html',form =form)



if __name__ == '__main__':
  app.run(port=3000)
  
