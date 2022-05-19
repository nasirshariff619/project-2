from flask import Flask, Response
import random

app = Flask(__name__)

@app.route('/get/country', methods = ['GET'])
def get_country():
    country = ['England', 'France', 'Germany']
    x = random.randint(0,2)
    return Response(country[x], mimetype = 'text/plain')  
if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')