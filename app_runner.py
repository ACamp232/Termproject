"""application that calculates the amount of months needed for the user to buy a certain product
"""
from flask import Flask, render_template, request
from fin_calc import mon_savings, surplus_calc 



app = Flask(__name__)

@app.route('/surp/', methods=["GET", "POST"])
def calc_surplus():
    if request.method == "POST":
        mon_exp = request.form["exp"]
        mon_inc = request.form["inc"]
        calc_result = surplus_calc(mon_exp,mon_inc)
        return render_template('output_pg.html', exp=mon_exp, inc=mon_inc, surp=calc_result)
    return render_template('beg_pg.html')

@app.route('/purchase-calc/', methods=["GET","POST"])
def purchase_calc():
    if request.method =="POST":
        item = request.form["product_name"]
        price = request.form["product_price"]
        surplus = request.form["surp"]
        calc_result_2 = mon_savings(item,price)
        return render_template("result_pg.html", product_name = item, product_price=price, mon_calc=calc_result_2)
    return render_template("output_pg.html")

if __name__=='__main__':
    app.run(debug =True)
