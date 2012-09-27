from flask import *
from flask_flatpages import FlatPages 
from flask_frozen import Freezer
import yaml
import markdown
import sys

#app config
DEBUG = True
SECRET_KEY = 'development key'
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.html'
FREEZER_DESTINATION = 'data-services'
FREEZER_RELATIVE_URLS = True
FREEZER_DEFAULT_MIMETYPE = 'text/html'
FREEZER_BASE_URL = 'http://doemo.lib.berkeley.edu/data-services/'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

@app.route('/')
def index():
	'''homepage, returns template with pages object for listing'''
	return render_template('index.html', pages=pages)

@app.route('/<path:path>.html')
def page(path):
	'''individual pages, gets pages based on request path. returns object for page requested'''
	page = pages.get_or_404(path)
	return render_template('page.html', page=page)

"""@app.route('/tag/<string:tag>/')
def tag(tag):
	'''returns pages and meta data tags that are in yaml metadata in markdown file headers'''
	tagged = [p for p in pages if tag in p.meta.get('tags', [])]
	return render_template('tag.html', pages=tagged, tag=tag)"""

if __name__ == '__main__':
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		freezer.freeze()
	else:
		app.run()
