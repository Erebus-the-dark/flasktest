from flask import Flask,request,make_response,render_template


app=Flask(__name__,template_folder='templates' )


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)



'''
@app.route('/greet/<name>')
def greet(name):
    return f"hello {name}"

@app.route('/hello')
def hello():
    response=make_response('Hello world\n')
    response.status_code=202
    response.headers['content-type']='application/octet-stream'
    return response
    
@app.route('/add/<int:number1>/<int:number2>')
def add(number1,number2):
    return f'{number1}+{number2}={number1+number2}'

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
     greeting=request.args['greeting']
     name=request.args.get('name')
     return f'{greeting},{name}'
    else:
        return 'some para are missing'

'''
