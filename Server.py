from flask import Flask
from random import randint
app=Flask(__name__)
number=randint(0,9)
def toBold(fun):
    def wrap(*args,**kwargs):
        result=fun(*args,**kwargs)
        return f'<b>{result}<b>'
    return wrap

@app.route('/')
@toBold
def Home():
    return '<h1 style="text-align:center">Guess a number between 0 and 9</h1>'\
            '<div style="width: 50%; margin: auto; text-align: center;"><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></div>'

@app.route('/<int:num>')
def guessed(num):
    if num==number:
        return '<b><h1 style="text-align:center">Correct number! HURRAYYY!<h1></b>'\
                '<div style="width: 50%; margin: auto; text-align: center;"><img src="https://media.giphy.com/media/9uffe4HEa29LApTR14/giphy.gif?cid=ecf05e47tew9ylk7utduvmj6o07vu0k3aqkec09srm9mabgt&ep=v1_gifs_search&rid=giphy.gif&ct=g"></div>'
    elif num<number:
        return '<b><h1 style="text-align:center">:( THATS TOO LOWWWW!!!<h1></b>'\
            '<div style="width: 50%; margin: auto; text-align: center;"><img src="https://media.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif?cid=790b7611sbrtmdcz4wu2jxjvcmsyqr8ujzgd6bc6oabxyihg&ep=v1_gifs_search&rid=giphy.gif&ct=g"></div>'
    elif num>number:
        return '<b><h1 style="text-align:center">THATS TOO HIGHHHH!!!<h1></b>'\
            '<div style="width: 50%; margin: auto; text-align: center;"><img src="https://media.giphy.com/media/8wXHSMbCRXNuHSO44y/giphy.gif?cid=ecf05e473ezp919hrwwt9rutmd4za3uf0h0dmpanwo3nztks&ep=v1_gifs_search&rid=giphy.gif&ct=g"></div>'


if __name__=="__main__":
    app.run(debug=True)
