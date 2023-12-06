import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

##############################################

# Request:
# GET /hello?name=David

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"

# To make a request, run:
# curl "http://localhost:5001/hello?name=David"

############################################

# Request:
# POST /goodbye
#   With body parameter: name=Alice

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

# exercise: building a route

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']

    return f"Thanks {name}, you sent this message: {message}"

# challenge

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']

    return f"I am waving at {name}"

# exercise 1

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    for i in text:
        if i in vowels:
            vowel_count += 1
        
    return f"There are {vowel_count} vowels in \"{text}\""

# exercise 2

@app.route('/sort_names', methods=['POST'])
def sort_names():
    names = request.form['names']
    names_list = names.split(',')
    names_list.sort()
    return ','.join(names_list)


# challenge

@app.route('/names', methods=['GET'])
def names():
    add = request.args['add']
    names_list = ['Julia','Alice','Karim']
    names_list.append(add)
    return names_list




# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)




# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

