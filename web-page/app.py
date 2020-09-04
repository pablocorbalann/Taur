# This file is the main file for our web page, it's coded in python and
# manages the routes and python-side information of the site

# imports
from flask import Flask, render_template, url_for
# create the "app" object
app = Flask(__name__)

# home page
@app.route('/')
def home():
	"""
	This function is the function that renders and return
	the home page of the web so it can be used in the browser. 
	The index.html (loaded by this function) is an HTML5 template 
	located in templates/ that extends from the layout.html template
	"""

	# create a "features_of_taur" diccionary to display as an HTML 5
	# element in the page
	features_of_taur = [
		{
			'title':'Commands',
			'text':'Taur is a new bot and every week we add 3 new commands to Taur',
		},
		{
			'title':'Open source',
			'text':'Taur is a new bot and every week we add 3 new commands to Taur',
		},
		{
			'title':'Commands',
			'text':'Taur is a new bot and every week we add 3 new commands to Taur',
		}
	]
	return render_template('index.html', cards=features_of_taur)


if __name__ == '__main__':
	app.run(debug=True)			