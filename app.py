#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_bootstrap import WebCDN
from flask_nav import Nav
from flask_nav.elements import Navbar, View
import csv

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.extensions['bootstrap']['cdns']['bootstrap'] = WebCDN('//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.1/')
nav = Nav()
nav.init_app(app)



@nav.navigation()
def mynavbar():
    return Navbar(
        'Might & Magic: Elemental Gardians',
        View('Home', 'index'),
        View('Search', 'search'),
        View('About', 'about'),
    )

@app.route('/')

@app.route('/index')
def index():
    monsters=[]
    with open('mameg.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        next(spamreader, None)
        for row in spamreader:
            liste=[row[0],row[1], int(row[3]), row[15], 'Description: Il est beau, il est fort, il est swag']
            monsters.append(liste)
    return render_template('index.html', title='All monsters',monsters=monsters)

@app.route('/search')
def search():
    return render_template('index.html', title='Hello World?')

@app.route('/detail/<id>')
def detail(id):
    with open('mameg.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        labeltmp =next(spamreader, None)
        labelStat = []
        zone=[]
        for i in range(4,12):
            labelStat.append(labeltmp[i])
        for i in range(16, 22):
            zone.append(labeltmp[i])
        for row in spamreader:
            if row[0] == id:
                monster = row
                stats = []
                note = []
                for i in range(4, 12):
                    if row[i] == '':
                        stats.append(0)
                    else:
                        stats.append(int(row[i]))
                for i in range(16,22):
                    note.append(row[i])
                    awake=[row[-2], row[-1]]
                return render_template('detail.html', title=monster[1], monster=monster, star=int(monster[3]), labels=labelStat, datas=stats, zone=zone, note=note, awake= awake)
@app.route('/about')
def about():
    return render_template('index.html', title='Tu as pas un PO ?')
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)

