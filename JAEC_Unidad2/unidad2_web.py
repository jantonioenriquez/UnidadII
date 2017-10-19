from flask import Flask, render_template, request, redirect
from unidad2_module import area, volumen

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Evaluation U2')


@app.route('/exec_equation', methods=['GET', 'POST'])
def execute() -> 'html':
    l = float(request.form['l'])
    #y = int(request.form['y'])
    title = 'This is the equation\'s result'
    result1 = area(l)
    result2 = volumen(l)
    return render_template('result.html',
                           the_title=title,
                           #the_x=x,
                           the_l=l,
                           the_result1=result1,
                           the_result2=result2, )


if __name__ == '__main__':
    app.run('localhost', 5002, debug=True)
