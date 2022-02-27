from flask import Flask, request

def prime_test(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
        return True
    return False

app=Flask(__name__)
@app.route('/prime_test')

def prime():
    x= request.args.get('x')
    if prime_test(int(x))==True:
        return '<h1>Bingo </h1>'.format(x)
    else:
        return '<h1>{} is not a prime number.  </h1>'.format(x)


if __name__=='main':
    app.run(debug=True,host='0.0.0.0')