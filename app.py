from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from morse import MorseCodeTranslator

TRANSLATOR = MorseCodeTranslator()

app = Flask(__name__)
app.config['SECRET_KEY']= '627474ba186e2bfcde98adc23942c60e4e'

class TransForm(FlaskForm):
    morse = TextAreaField("Morse Code Translate")
    submit_btn = SubmitField("Translate")

@app.route('/')
def home():
    return render_template('home.html', title="MrFnMorseTrans")


@app.route('/text-to-morse', methods=['GET', 'POST'])
def text_to_morse():
    form = TransForm()
    if form.validate_on_submit():
        data = form.data['morse']
        if data == "":
            return redirect(url_for('text_to_morse'))
        elif data != "":
            data = TRANSLATOR.translate_text(data)
            return render_template('text-to-morse.html', title='Text to Morse', form=form, data=data) 
    return render_template('text-to-morse.html', title='Text to Morse', form=form)


@app.route('/morse-to-text', methods=['GET', 'POST'])
def morse_to_text():
    form = TransForm()
    if form.validate_on_submit():
        data = form.data['morse']
        if data == "":
            return redirect(url_for('morse_to_text'))
        elif data != "":
            data = TRANSLATOR.translate_morse(data)
            return render_template('text-to-morse.html', title='Text to Morse', form=form, data=data)
    return render_template('morse-to-text.html', title='Morse to Text', form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

