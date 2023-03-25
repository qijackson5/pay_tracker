from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        salary = float(request.form['salary'])
        return render_template('index.html', salary=salary)
    return render_template('index.html')


@app.route('/earnings')
def get_earnings():
    salary = float(request.args.get('salary'))
    elapsed_time = float(request.args.get('elapsed_time'))
    earnings_per_second = salary / 31536000  # 365 days * 24 hours * 60 minutes * 60 seconds
    earnings = earnings_per_second * elapsed_time
    return jsonify({'earnings': earnings})


if __name__ == '__main__':
    app.run(debug=True)