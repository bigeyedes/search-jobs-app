# imports
from flask import Flask, render_template, request
from wtforms import Form, TextField, validators, StringField, SubmitField
from models import *

# zmienna aplikacji
app = Flask(__name__)

# home
class SearchForm(Form):
	# stwórz pola
	tech = TextField('Technologia:',  validators=[validators.required()])
	place = TextField('Lokalizacja:')

	@app.route('/')
	def index():
		form = SearchForm(request.form)
		return render_template('index.html', form=form)

#results
@app.route('/results', methods=('GET', 'POST'))
def search_resluts():

	if request.method == 'POST':
		description = request.form['tech']
		location = request.form['place']
		response(description, location)

	with open('jobs.json', encoding="utf-8") as jobs_file:
		jobs = json.load(jobs_file)

	return render_template('results.html', jobs = jobs, tech = description , loc = location)

# debug
if __name__=='__main__':
	app.run(debug=True)