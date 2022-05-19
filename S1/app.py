from flask import Flask, render_template
import requests

app = Flask(__name__)
@app.route('/country/food', methods = ['GET', 'POST'])
def get_task():
    country = requests.get('service2:5001/get/country').text #local host can be container name
    food = requests.get('service3:5002/get/food').text
    country_food = country + " " + food 
    task = requests.post('service4:5003/post/task', data=country_food).text
    
    return render_template('home.html', title = 'Country Food', country = country, food = food, task = task)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
