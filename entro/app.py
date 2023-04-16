from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about/')
def about():
    return render_template('about.html')
@app.route('/gallery/')
def gallery():
    return render_template('gallery.html')
if __name__ == '__main__':
    app.run(debug=True,port=5000,host='192.168.106.109')