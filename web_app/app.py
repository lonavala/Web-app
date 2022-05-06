from flask import Flask,render_template,request         # we have installed flask lib-- from that we are Flask

app = Flask(__name__)           #Flask cha Object --> web all the function

#local machinec --> 127.0.0.1 ---> localhost

@app.route('/add')         # app -->Flask cha oBject -> route -->
def addition():                 #http://localhost:5000/addition --> browser vr enter
    data = request.args
    print(data)
    n1 = int(data.get('num1'))
    n2 = int(data.get('num2'))
    result = n1 + n2
    #return "Addition method in invoked.."
    return render_template('index.html',output = result)

@app.route('/calculator')       #http://localhost:5000/calculator
def welcome_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) #when u make change inside code --> automatically server restart

