import os, random, string
from secrets import choice
from flask import Flask
from flask import render_template,request,redirect,url_for,flash

app = Flask(__name__)
app.secret_key="Developed"

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/generate', methods=['POST'])
def generate():
    #varibles que traemos del index.html
    try:
        length = request.form['txtNum']
        if length == '':
            flash('Recuerda dar el numero de caracteres')
            return redirect((url_for('index')))
        num = int(length)
    except:
        flash('Ne debes usar letras')
        return redirect((url_for('index')))
    _check = request.form.getlist('check')
    #variables para generar contraseñas
    Mayus = list(string.ascii_uppercase) #[2]
    Minus = list(string.ascii_lowercase) #[3]
    Digits = list(string.digits) # [1]
    Especial = list(string.punctuation) #[4]

    if num < 1 or num > 32:
        flash('Recuerda dar un numero Valido')
        return redirect((url_for('index')))
    
    if (_check == [] or _check == ['1','2','3','4']):
        chars = Mayus + Minus + Digits + Especial
    elif (_check ==['1']): #Solo numeros
        chars = Digits
    elif (_check ==['2']): #Solo mayusculas
        chars = Mayus
    elif (_check ==['3']): #Solo minusculas
        chars = Minus
    elif (_check ==['4']): #Solo caracteres especiales
        chars = Especial
    elif (_check == ['1','2']): # Digitos + mayusculas
        chars = Digits + Mayus
    elif (_check == ['1','3']): # Digitos + minisculas
        chars = Digits + Minus
    elif (_check == ['1','4']): # Digitos + caracteres especiales
        chars = Digits + Especial
    elif (_check == ['2','3']): # Mayusculas + Minusculas
        chars = Mayus + Minus
    elif (_check == ['2','4']): # Mayusculas + Caracteres especiales
        chars = Mayus + Especial
    elif (_check == ['3','4']): # Minisculas + Caracteres especiales 
        chars = Minus + Especial
    elif (_check == ['1','2','3']): #Digitos + Mayusculas + Minusculas
        chars = Digits + Mayus + Minus
    elif (_check == ['1','2','4']):
        chars = Digits + Mayus + Especial
    elif (_check == ['1','3','4']):
        chars = Digits + Minus + Especial
    elif (_check == ['2','3','4']):
        chars = Mayus + Minus + Especial
    
    password = ''.join(random.choice(chars) for i in range(num))
    return render_template('/pass.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
