from flask import Flask, render_template
import random
import time
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query')
def query():
    #simulate a query and return some json data
    #time.sleep(random.random() * 10) # sleep 1-10 seconds
    from bokeh.sampledata.iris import flowers # pandas dataframe of iris sample (150 rows x 4 columns)
    # Add our own 'color' column on the server side because it's easier than doing it in javascript
    colors = dict(zip(flowers.species.unique(), ['blue', 'green', 'red']))
    flowers['color'] = flowers.apply(lambda rec: colors[rec.species], axis=1)
    return flowers.to_json(orient='records') # return JSON in the form of a list of dictionaries

@app.route('/example1')
def example1():
    return render_template('example1.html')

@app.route('/example2')
def example2():
    return render_template('example2.html')

@app.route('/<path>')
def catch_all(path):
    # This is a way to set dynamic rules, more info: http://flask.pocoo.org/docs/0.12/quickstart/#routing
    # instead of manually adding /example3 -> render_template('example3.html'), etc, etc
    html_file = '%s.html' % path # i.e. a request to /example5 would look for 'example5.html'
    return render_template(html_file)

if __name__ == '__main__':
    app.run(debug=True)