from flask import Flask,render_template
import get_json as g_json
app = Flask(__name__)


@app.route('/libc_address')
def libc_address():
    address,count_number=g_json.get_top()
    return render_template('index.html',address=address,count_number=count_number)


if __name__ == '__main__':
    app.run()
