POST /sort-names

route: curl -X POST -d "names=Joe,Alice,Zoe,Julia,Kieran" http://localhost:5001/sort-names

names: string

"""
When: I make a POST request to /sort-names
And: I send "Joe,Alice,Zoe,Julia,Kieran" as the body parameter text
Then: I should get a 200 response with Alice, Joe, Julia, Kieran, Zoe in the message
"""

def test_sort-names(web_client):
    response = web_client.post('/sort-names', data={'names': 'Joe, Alice, Zoe, Julia, Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Joe, Julia, Kieran, Zoe'

<!--           -->
# challenge

GET /names

route: GET /names?add=Eddie

add: string

# This route should return a list of pre-defined names, plus the name given.
# Expected response (2OO OK):
Julia, Alice, Karim, Eddie

"""
When: I make a GET request to /names
And: I send "Eddie" as the parameter add
Then: I should get a 200 response with Julia, Alice, Karim, Eddie in the message
"""

def test_add_names(web_client):
    response = web_client.get('/names', data={'add': 'Eddie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'