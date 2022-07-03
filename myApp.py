from os import name
from flask import Flask, redirect, url_for, render_template, request, session
import mysql.connector
from datetime import datetime

#from mysql.connector import errorcode

app = Flask(__name__)
app.secret_key = "qwertuiop"
# app.permanent_session_lifetime = timedelta(minutes=1)

idgot = ""

mydb = mysql.connector.connect(
    host="localhost",
    user="megaUser",
    passwd="root",
    database="BoutiqueManagementSystem"
)


@app.route('/login', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # session.permanent = True
        user = request.form['nm']
        pwd = request.form['pass']

        errorcode = ""

        loginpart = mydb.cursor()
        loginpart.execute(
            "SELECT empid FROM employeeLogin a, employeeDetails b WHERE a.empUsername = %s AND empPassword = %s AND a.empUsername = b.empUsername", (user, pwd))
        loginresult = loginpart.fetchall()
        if loginresult:
            session["user"] = loginresult[0][0]
            return redirect(url_for("user"))
        else:
            errorcode = "Invalid Username or Password"
            return render_template('login.html', errorcode=errorcode)

    else:
        return render_template('login.html')


@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']

        mainpagepart = mydb.cursor()
        mainpagepart.execute(
            "SELECT * FROM employeeDetails WHERE empId = %s", (user,))
        mainpageresult = mainpagepart.fetchall()

        mainpagepartphno = mydb.cursor()
        mainpagepartphno.execute(
            "SELECT empPhone FROM employeePhone WHERE empId = %s", (user,))
        mainpageresultphno = mainpagepartphno.fetchall()

        return render_template('mainpage.html', empid=mainpageresult[0][0], empname=mainpageresult[0][1], empusername=mainpageresult[0][2],  emprolerank=mainpageresult[0][3], empphno=mainpageresultphno, sizeofphno=len(mainpageresultphno))
    else:
        return redirect(url_for('login'))


@app.route('/customers')
def customers():
    if 'user' in session:
        nameIdMail = mydb.cursor()
        nameIdMail.execute(
            "SELECT custid, custname, email, houseno, street, pincode FROM customers")
        NIEresult = nameIdMail.fetchall()

        phoneNo = mydb.cursor()
        phoneNo.execute("SELECT * FROM custPhone")
        pnoresult = phoneNo.fetchall()

        list1 = []
        unique_list = []

        for x in pnoresult:
            list1.append(x[0])

        for x in list1:
            if x not in unique_list:
                unique_list.append(x)

        aaa = (pnoresult.__len__())
        bbb = (unique_list.__len__())

        return render_template('customers.html', finalresult=NIEresult, sizeofresult=NIEresult.__len__(), phone=pnoresult, phoneSize=aaa, uniqueSize=bbb, unique=unique_list)
    else:
        return redirect(url_for('user'))


@app.route('/products')
def products():
    if 'user' in session:

        productm1 = mydb.cursor()
        productm1.execute("SELECT * FROM productsmain1")
        productm1result = productm1.fetchall()

        productm2 = mydb.cursor()
        productm2.execute("SELECT * FROM productsmain2")
        productm2result = productm2.fetchall()

        products1 = mydb.cursor()
        products1.execute(
            "select distinct(dresssize), prodid from productssecondary order by prodid;")
        products1result = products1.fetchall()

        products2 = mydb.cursor()
        products2.execute(
            "select distinct(dresscolor), prodid from productssecondary order by prodid;")
        products2result = products2.fetchall()

        maxprod = mydb.cursor()
        maxprod.execute("select max(prodid) from productssecondary;")
        maxprodres = maxprod.fetchall()

        lststock = []
        prodqty = mydb.cursor()
        for u in range(1, maxprodres[0][0]+1):
            prodqty.execute(
                "select distinct sum(qtyinstock) from productssecondary where prodid = %s;", (u,))
            prodqtyres = prodqty.fetchall()
            lststock.append(prodqtyres[0][0])

        prodlinks = ["https://images.unsplash.com/photo-1588140686379-1b76a52103dc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80",
                     "https://thumbs.dreamstime.com/b/collection-beautiful-dresses-sarees-salwar-kameez-indian-192505245.jpg",
                     "https://5.imimg.com/data5/TestImages/FR/DR/QJ/SELLER-27618037/churidar-materials-1000x1000.jpeg",
                     "https://images.unsplash.com/photo-1534217466718-ef4950786e24?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
                     "https://images.unsplash.com/photo-1506072590044-75de1b7b7806?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"]

        return render_template('products.html', link=prodlinks, pm1size=productm1result.__len__(), pm1r=productm1result, pm2size=productm2result.__len__(), pm2r=productm2result, ps1size=products1result.__len__(), ps1r=products1result, ps2size=products2result.__len__(), ps2r=products2result, lststock=lststock)
    else:
        return redirect(url_for('user'))


@app.route('/custAdd', methods=['POST', 'GET'])
def custAdd():
    if 'user' in session:

        if request.method == 'POST':
            Name = request.form['custname']
            Email = request.form['custemail']
            HouseNo = request.form['addr1']
            Street = request.form['addr2']
            Pincode = request.form['addr3']
            p = request.form['phno']
            phoneNo = []
            phoneNo = p.split(',')

            mymaxid = mydb.cursor()
            mymaxid.execute("SELECT MAX(custid) FROM customers")
            maxidtest = mymaxid.fetchall()

            maxid = maxidtest[0][0]+1

            addanewcust = mydb.cursor()
            addanewcust.execute("INSERT INTO customers (custid, custname, email, houseno, street, pincode) VALUES (%s, %s, %s, %s, %s, %s)", (
                maxid, Name, Email, HouseNo, Street, Pincode))
            mydb.commit()
            #lastid = addanewcust.lastrowid
            addnewcustphone = mydb.cursor()
            for x in phoneNo:
                addnewcustphone.execute(
                    "INSERT INTO custPhone (custid, custPhone) VALUES (%s, %s)", (maxid, x))
                mydb.commit()

            return redirect(url_for('customers'))

        else:
            return render_template('custAdd.html')


@app.route('/custDel', methods=['POST', 'GET'])
def custDel():
    if 'user' in session:

        if request.method == 'POST':
            delId = request.form['custid']

            delcust = mydb.cursor()
            delcust.execute(
                "DELETE FROM customers, custPhone USING customers INNER JOIN custPhone ON customers.custid = custPhone.custid  WHERE customers.custid= %s", (delId,))
            mydb.commit()

            return redirect(url_for('customers'))

        else:
            return render_template('custdel.html')


@app.route('/custMod', methods=['POST', 'GET'])
def custMod():
    if 'user' in session:

        if request.method == 'POST':
            modId = request.form['custid']

            modName = request.form['custname']
            modEmail = request.form['custemail']
            modHouseNo = request.form['addr1']
            modStreet = request.form['addr2']
            modPincode = request.form['addr3']

            modOldPhone = request.form['oldphno']
            modNewPhone = request.form['newphno']

            if modOldPhone != "" and modNewPhone != "" and modName == "" and modEmail == "" and modHouseNo == "" and modStreet == "" and modPincode == "":
                modcust = mydb.cursor()
                modcust.execute(
                    "UPDATE custPhone SET custPhone = %s WHERE custid = %s AND custPhone = %s", (modNewPhone, modId, modOldPhone))
                mydb.commit()
            elif modOldPhone == "" and modNewPhone == "" and modName != "" and modEmail != "" and modHouseNo != "" and modStreet != "" and modPincode != "":
                modcust = mydb.cursor()
                modcust.execute("UPDATE customers SET custname = %s, email = %s, houseno = %s, street = %s, pincode = %s WHERE custid = %s", (
                    modName, modEmail, modHouseNo, modStreet, modPincode, modId))
                mydb.commit()
            elif modOldPhone != "" and modNewPhone != "" and modName != "" and modEmail != "" and modHouseNo != "" and modStreet != "" and modPincode != "":
                modcust = mydb.cursor()
                modcust.execute("UPDATE customers SET custname = %s, email = %s, houseno = %s, street = %s, pincode = %s WHERE custid = %s", (
                    modName, modEmail, modHouseNo, modStreet, modPincode, modId))
                modcust.execute(
                    "UPDATE custPhone SET custPhone = %s WHERE custid = %s AND custPhone = %s", (modNewPhone, modId, modOldPhone))
                mydb.commit()

            return redirect(url_for('customers'))

        else:
            return render_template('custmod.html')


@ app.route('/invoice', methods=['POST', 'GET'])
def billget():
    if 'user' in session:

        if request.method == 'POST':
            getbillid = request.form['billid']

            billidres1 = mydb.cursor()
            billidres1.execute(
                "SELECT * FROM bill_1 WHERE billid = %s", (getbillid,))
            bill1res = billidres1.fetchall()

            billidres2 = mydb.cursor()
            billidres2.execute(
                "SELECT * FROM bill_2 WHERE billid = %s", (getbillid,))
            bill2res = billidres2.fetchall()

            billcustdet = mydb.cursor()
            billcustdet.execute(
                "select * from customers where custid in (select custid from bill_1 where billid = %s)", (getbillid,))
            billcustdetres = billcustdet.fetchall()

            billcustphno = mydb.cursor()
            billcustphno.execute(
                "select * from custPhone where custid in (select custid from bill_1 where billid = %s)", (getbillid,))
            billcustphnores = billcustphno.fetchall()

            billprod1 = mydb.cursor()
            billprod1.execute(
                "select amount from productsmain2 where prodtype in (select prodtype from productsmain1 where prodid in (select prodid from bill_1 where billid = %s));", (getbillid,))
            billprod1res = billprod1.fetchall()

            billprod2 = mydb.cursor()
            billprod2.execute(
                "select prodname from productsmain1 where prodid in (select prodid from bill_1 where billid = %s);", (getbillid,))
            billprod2res = billprod2.fetchall()

            flag = 0
            lol = 0
            for xbillprod1 in billprod1res:
                flag = flag + xbillprod1[0]*bill1res[lol][2]
                lol = lol + 1

            return render_template('invoice.html', b1r=bill1res, b2r=bill2res, cdet=billcustdetres, cphno=billcustphnores, bprod1=billprod1res, bprod1size=len(billprod1res), bprod2=billprod2res, flag=flag)

        else:
            return render_template('billget.html')


@app.route('/returnorder', methods=['POST', 'GET'])
def returnorder():
    if 'user' in session:

        if request.method == 'POST':

            returnorderid = request.form['billidProcessed']
            splitted = returnorderid.split(",")

            if splitted.__len__() == 1:
                modretordr = mydb.cursor()
                modretordr.execute(
                    "delete from returnorder where returnid = %s", (returnorderid,))
                mydb.commit()
            else:

                now = datetime.now().strftime("%d-%m-%Y : %H:%M")
                addtoreturnorder = mydb.cursor()
                addtoreturnorder.execute("insert into returnorder (returnid, billid, custid, prodid, retDateTime) values (%s, %s, %s, %s, %s)", (
                    splitted[0], splitted[1], splitted[2], splitted[3], now))
                mydb.commit()

            returnorder = mydb.cursor()
            returnorder.execute("select * from returnorder;")
            returnorderidres = returnorder.fetchall()

            custname = mydb.cursor()
            custname.execute(
                "select custname from customers where custid in (select custid from returnorder);")
            custnameres = custname.fetchall()

            prodname = mydb.cursor()
            prodname.execute(
                "select prodname from productsmain1 where prodid in (select prodid from returnorder);")
            prodnameres = prodname.fetchall()

            return render_template('returnorder.html', roir=returnorderidres, roirsize=returnorderidres.__len__(), cn=custnameres, pn=prodnameres)
        else:

            returnorder = mydb.cursor()
            returnorder.execute("select * from returnorder;")
            returnorderidres = returnorder.fetchall()

            custname = mydb.cursor()
            custname.execute(
                "select custname from customers where custid in (select custid from returnorder);")
            custnameres = custname.fetchall()

            prodname = mydb.cursor()
            prodname.execute(
                "select prodname from productsmain1 where prodid in (select prodid from returnorder);")
            prodnameres = prodname.fetchall()

            return render_template('returnorder.html', roir=returnorderidres, roirsize=returnorderidres.__len__(), cn=custnameres, pn=prodnameres)


@ app.route('/cart', methods=['POST', 'GET'])
def cart():
    if 'user' in session:
        if request.method == 'POST':

            cartid = request.form['cartid']

            cart1 = mydb.cursor()
            cart1.execute(
                "select * from productsmain1 where prodid in (select prodid from cart where custid = %s);", (cartid,))
            cart1res = cart1.fetchall()

            cart2 = mydb.cursor()
            cart2.execute(
                "select amount from productsmain2 where prodtype in (select prodtype from productsmain1 where prodid in (select prodid from cart where custid = %s));", (cartid,))
            cart2res = cart2.fetchall()

            cart3 = mydb.cursor()
            cart3.execute("select qty from cart where custid = %s;", (cartid,))
            cart3res = cart3.fetchall()

            cartsize = len(cart1res)

            sum = 0

            for i in range(cartsize):
                sum += (cart2res[i][0] * cart3res[i][0])

            return render_template('usercart.html', c1r=cart1res, c2r=cart2res, c3r=cart3res, csize=cartsize, sum=sum)
        else:
            return render_template('cart.html')


@app.route('/employee')
def employee():
    if 'user' in session:

        empdat1 = mydb.cursor()
        empdat1.execute("select * from employeeDetails order by emprolerank;")
        empdat1res = empdat1.fetchall()

        empdat2 = mydb.cursor()
        empdat2.execute(
            "select empPassword from employeeLogin, employeeDetails where employeeLogin.empUsername = employeeDetails.empUsername order by employeeDetails.emprolerank;")
        empdat2res = empdat2.fetchall()

        empdat3 = mydb.cursor()
        empdat3.execute(
            "select * from employeePhone where empid in (select empid from employeeDetails order by emprolerank);")
        empdat3res = empdat3.fetchall()

        sizeofemp = len(empdat1res)
        sizeph = len(empdat3res)

        return render_template('employee.html', ed1r=empdat1res, ed2r=empdat2res, ed3r=empdat3res, edsize=sizeofemp, phsize=sizeph)
    else:
        return redirect(url_for('user'))


@app.route('/EmpAdd', methods=['POST', 'GET'])
def EmpAdd():
    if 'user' in session:

        if request.method == 'POST':
            id = request.form['empid']
            Name = request.form['empname']
            Username = request.form['empuname']
            passwd = request.form['emppass']
            cl = request.form['empclr']
            p = request.form['empphno']
            phoneNo = []
            phoneNo = p.split(',')

            addanewemp1 = mydb.cursor()
            addanewemp1.execute(
                "INSERT INTO employeeDetails (empid, empname, empUsername, emprolerank) VALUES (%s, %s, %s, %s)", (id, Name, Username, cl))
            mydb.commit()

            addanewemp2 = mydb.cursor()
            addanewemp2.execute(
                "INSERT INTO employeeLogin (empUsername, empPassword) VALUES (%s, %s)", (Username, passwd))
            mydb.commit()

            addnewcustphone = mydb.cursor()
            for x in phoneNo:
                addnewcustphone.execute(
                    "INSERT INTO employeePhone (empid, empPhone) VALUES (%s, %s)", (id, x))
                mydb.commit()

            return redirect(url_for('employee'))

        else:
            return render_template('EmpAdd.html')


@app.route('/EmpDel', methods=['POST', 'GET'])
def EmpDel():
    if 'user' in session:

        if request.method == 'POST':
            delId = request.form['delempid']

            delemp = mydb.cursor()
            delemp.execute("DELETE FROM employeeLogin, employeeDetails USING employeeLogin INNER JOIN employeeDetails ON employeeLogin.empUsername = employeeDetails.empUsername  WHERE employeeDetails.empid= %s;", (delId,))
            mydb.commit()

            delempphno = mydb.cursor()
            delempphno.execute(
                "DELETE FROM employeePhone WHERE empid= %s;", (delId,))
            mydb.commit()

            return redirect(url_for('employee'))

        else:
            return render_template('EmpDel.html')


@app.route('/EmpMod', methods=['POST', 'GET'])
def EmpMod():
    if 'user' in session:

        if request.method == 'POST':
            modId = request.form['modempid']
            modName = request.form['modempname']
            modUsername = request.form['modempuname']
            modPasswd = request.form['modemppass']
            modClr = request.form['modempclr']
            modPhnoold = request.form['modempphnoold']
            modPhno = request.form['modempphno']

            if modPhnoold == "" and modPhno == "":
                modemp = mydb.cursor()
                modemp.execute(
                    "UPDATE employeeDetails SET empname = %s, empUsername = %s , emprolerank = %s WHERE empid = %s;", (modName, modUsername, modClr, modId))
                mydb.commit()

                modemp1 = mydb.cursor()
                modemp1.execute(
                    "UPDATE employeeLogin SET empPassword = %s WHERE empUsername = %s;", (modPasswd, modUsername))
                mydb.commit()
            else:
                modemp2 = mydb.cursor()
                modemp2.execute(
                    "UPDATE employeePhone SET empPhone = %s WHERE empid = %s AND empPhone = %s;", (modPhno, modId, modPhnoold))
                mydb.commit()

            return redirect(url_for('employee'))

        else:
            return render_template('EmpMod.html')


@app.route('/modInv', methods=['POST', 'GET'])
def modInv():
    if 'user' in session:

        if request.method == 'POST':
            modId = request.form['pid']
            color = request.form['pc']
            qistock = request.form['qis']
            size = request.form['ds']

            modinv = mydb.cursor()
            modinv.execute(
                "update productssecondary set qtyinstock = %s, dresssize = %s  where prodid = %s and dresscolor = %s;", (qistock, size, modId, color))
            mydb.commit()

            return redirect(url_for('products'))

        else:
            return render_template('modInv.html')


@ app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
