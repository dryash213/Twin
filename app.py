from types import MethodType
from flask import Flask
from flask import Flask, request, jsonify, render_template

import Direc.Course
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/course',methods=['POST'])
def course():
    int_features = [str(x) for x in request.form.values()]
    lst = []
    # print(Direc.Course.course(int_features[0]))
    for i in Direc.Course.course(int_features[0]):
        if(i!=""):
            lst.append(i)
    return render_template("ret.html",Name = int_features[0], len = len(lst), lst = lst)
 
 
@app.route('/stats')
def stats():
    return render_template("indexplot.html")
 

if __name__ == '__main__':
   app.run(debug=True)
