from flask import Flask, Response
import random

app = Flask(__name__)

@app.route('/get/food', methods = ['GET'])
def get_food():
    food = ['Sausage-roll', 'Croissant', 'Schnitzel']
    #food = ['Sausage-roll', 'Croissant']
    x = random.randint(0,2)
    return Response(food[x], mimetype = 'text/plain')  
if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')