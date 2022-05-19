from flask import Flask, request, Response

app = Flask(__name__)
@app.route('/post/task', methods=['POST', 'GET'])
def post_task():
    country_food = request.data.decode('utf 8') 
    to_do = country_food.split()
    if to_do[0] == 'England' and to_do[1] == 'Sausage-roll':
        task = 'Go to London and buy a sausage-roll from greggs'
    elif to_do[0] == 'England' and to_do[1] == 'Croissant':
        task = 'Eat a croissant on the London Eye'
    elif to_do[0] == 'England' and to_do[1] == 'Schnitzel':
        task = 'Google where to buy schnitzel in England because I have no clue or try again'
    elif to_do[0] == 'France' and to_do[1] == 'Sausage-roll':
        task = 'Sausage-rolls are banned from France. Try again.'
    elif to_do[0] == 'France' and to_do[1] == 'Croissant':
        task = 'Eat a croissant at the top of the Eiffel Tower'
    elif to_do[0] == 'France' and to_do[1] == 'Schnitzel':
        task = 'Google where to buy schnitzel in France because I have no clue or try again'
    elif to_do[0] == 'Germany' and to_do[1] == 'Sausage-roll':
        task = 'Watch Bayern Munich play while eating sausage roll'
    elif to_do[0] == 'Germany' and to_do[1] == 'Croissant':
        task = 'Eat croissant at Nuremberg Clock Tower'
    elif to_do[0] == 'Germany' and to_do[1] == 'Schnitzel':
        task = 'Eat Schnitzel at an Oktoberfest event'
    return Response(task, mimetype = 'text/plain')


if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')

