@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie(): # setter
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)

    return resp


@app.route('/getcookie')
def getcookie(): # getter
   name = request.cookies.get('userID')
   return '<h1>welcome ' + name + '</h1>'

