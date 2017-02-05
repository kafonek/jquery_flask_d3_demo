from flask import Flask, render_template
import random
import time
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/query')
def query():
    #simulate a query and return some json data
    #time.sleep(random.random() * 10) # sleep 1-10 seconds
    from bokeh.sampledata.iris import flowers # pandas dataframe of iris 
    colors = dict(zip(flowers.species.unique(), ['blue', 'green', 'red']))
    flowers['color'] = flowers.apply(lambda rec: colors[rec.species], axis=1)
    data = flowers.to_dict('records') # convert from dataframe to list of dicts
    return json.dumps(data)

@app.route('/example1')
def example1():
    return render_template('example1.html')

@app.route('/example2')
def example2():
    return render_template('example2.html')

@app.route('/<path>')
def catch_all(path):
    # This catches anything that doesn't have an explicit match
    # so using this instead of continuing with the /example3 -> render_template('example3.html') etc etc.
    html_file = '%s.html' % path # i.e. a request to /example5 would look for 'example5.html'
    return render_template(html_file)

if __name__ == '__main__':
    app.run(debug=True)