import bottle

@bottle.route('/')
def home_page():
    fruit = [ 'apple', 'orange', 'kiwi', 'apple']
    return bottle.template('hello_world', { 'username' : 'Nicolas', 'things' : fruit })
    
@bottle.route('/favorite_fruit', method='POST')
def favorite_fruit():
    fruit = bottle.request.forms.get("fruit")
    if (fruit == None or fruit == ""):
        fruit = 'no available fruit'
        
    # return bottle.template('favorite', { 'username' : 'Nicolas', 'fruit' : fruit })
    bottle.response.set_cookie('fruit', fruit)
    bottle.redirect('/show_fruit')    

@bottle.route('/testpage')
def test_page():
    return '<h1>This is the test page</h1>'

@bottle.route('/show_fruit')
def show_fruit():
    fruit = bottle.request.get_cookie('fruit')
    
    return bottle.template('favorite' , { 'username' : 'Nicolas', 'fruit' : fruit })
        
bottle.debug(True)
bottle.run(host='localhost', port=3000)


    
