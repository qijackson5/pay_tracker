from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        salary = float(request.form['salary'])
        return render_template('index.html', salary=salary)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)