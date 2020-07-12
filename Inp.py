from flask import Flask,render_template,request, send_file, Response
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from io import BytesIO


app=Flask("ash")

@app.route('/')
def index():
    return render_template("Boot.html")


@app.route('/final',methods=['POST'])
def show():

    ttl=request.form['Title']
    
    xlbl=request.form['Horizontal Axis']
    
    ylbl=request.form['Vertical Axis']
    
    choice = request.form['choice']
    
    listx = list(map(float,request.form['Horizontal Axis Data'].split(',')))
    
    listy = list(map(float,request.form['Vertical Axis Data'].split(',')))
    
    plt.figure()
    if choice == 'Lineplot':
        test = sorted(zip(listx,listy),key=lambda x: x[0])
        listx = [i[0] for i in test]
        listy = [i[1] for i in test]
        plt.plot(listx,listy,marker='*')
        plt.xlabel(xlbl,fontsize=18)
        plt.ylabel(ylbl,fontsize=11)
        narray = np.array(listx)
        plt.text(2,0.65,np.mean(narray))
        plt.title(ttl,fontsize=20)
        
    if choice == 'BarGraph':
        plt.bar(listx,listy, align='center', alpha=0.5)
        test = sorted(zip(listx,listy),key=lambda x: x[0])
        listx = [i[0] for i in test]
        listy = [i[1] for i in test]
        plt.bar(listx,listy)
        plt.xlabel(xlbl,fontsize=18)
        plt.ylabel(ylbl,fontsize=18)
        narray = np.array(listx)
        plt.text(2,0.65,np.mean(narray))
        plt.title(ttl,fontsize=20)
        
    if choice == 'Scatter':
        test = sorted(zip(listx,listy),key=lambda x: x[0])
        listx = [i[0] for i in test]
        listy = [i[1] for i in test]
        plt.scatter(listx,listy)
        plt.xlabel(xlbl,fontsize=18)
        plt.ylabel(ylbl,fontsize=18)
        narray = np.array(listx)
        plt.text(2,0.65,np.mean(narray))
        plt.title(ttl,fontsize=20)
        
    if choice == 'Histogram':
       test = sorted(zip(listx,listy),key=lambda x: x[0])
       listx = [i[0] for i in test]
       listy = [i[1] for i in test]
       plt.hist(listx,listy)
       plt.xlabel(xlbl,fontsize=18)
       plt.ylabel(ylbl,fontsize=18)
       narray = np.array(listx)
       plt.text(2,0.65,np.mean(narray))
       plt.title(ttl,fontsize=20)
       
    pfile = BytesIO()
    plt.savefig(pfile)
    pfile.seek(0)
    resp = Response(pfile.getvalue())
    resp.headers['content-type'] = 'image/png'
    return resp

app.run(host='0.0.0.0',port=2000)
