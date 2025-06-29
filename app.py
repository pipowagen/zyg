from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/roster')
def roster():
    # Sample member data
    sample_members = [
        {"name": "Mightymike", "class": "Warrior", "level": 60, "status": "Online"},
        {"name": "Healzforu", "class": "Priest", "level": 60, "status": "Offline"},
        {"name": "Sneakysneak", "class": "Rogue", "level": 58, "status": "Online"},
        {"name": "Frostyfingers", "class": "Mage", "level": 60, "status": "Away"},
        {"name": "Druidude", "class": "Druid", "level": 55, "status": "Offline"},
    ]
    return render_template('roster.html', members=sample_members)

@app.route('/recruitment')
def recruitment():
    return render_template('recruitment.html')

if __name__ == '__main__':
    app.run(debug=True)
