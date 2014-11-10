import bottle

@bottle.route('/')
def home_page():
    return 'Hello world'
    
@bottle.route('/testpage')
def test_page():
    return '<h1>This is the test page</h1>'
    
bottle.debug(True)
bottle.run(host='localhost', port=3000)
