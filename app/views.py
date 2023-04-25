from flask import Flask, render_template,redirect, url_for, request, session, abort

app = Flask(__name__)

def get_current_username():  # Kullanıcının oturum açmış olduğu sistemde, adını döndürmek için kullandığımız fonksiyon.
    email = ""
    login_auth = False
    if 'email' in session:
        email = session['email']
        login_auth = True
    return email, login_auth



@app.route('/')  #@app.route() ile sayfamızı oluşturduk.
def Index():
    email, login_auth = get_current_username()
    return render_template("index.html", email=email, login_auth=login_auth)


@app.route('/signup')   # Sayfamıza vermek istediğimiz dizini "('/')" ile ifade ettik.
def SignUp():
    email, login_auth = get_current_username()
    return render_template("signup.html", email=email, login_auth=login_auth)

@app.route('/login', methods =['GET','POST'])
def Login():
    if request.method == 'POST':             # Sunucuya kullanıcının verilerini göndermek için 'POST' istek yöntemini kullandık.
        if request.form:
            if 'email' in request.form and 'password' == request.form:
                email = request.form['email']
                password = request.form['password']
                if email == 'admin' and password == 'admin':
                    session['email']=email
                    return redirect(url_for('Index'))
                else:
                    return redirect(url_for('Login'))
        abort(400)
    email, login_auth = get_current_username()
    return render_template("login.html", email = email, login_auth = login_auth)

@app.route('/product')
def Product():
    email, login_auth = get_current_username()
    return render_template("product.html", email=email, login_auth=login_auth)

@app.route('/about')
def About():
    email, login_auth = get_current_username()
    return render_template("about.html", email=email, login_auth=login_auth)

@app.route('/services')
def Services():
    email, login_auth = get_current_username()
    return render_template("services.html", email=email, login_auth=login_auth)

@app.route('/blog')
def Blog():
    email, login_auth = get_current_username()
    return render_template("blog.html", email=email, login_auth=login_auth)

@app.route('/contact')
def Contact():
    email, login_auth = get_current_username()
    return render_template("contact.html", email=email, login_auth=login_auth)










