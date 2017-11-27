from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "hello everyone"



@app.route('/about-me')
def aboutme():
    return ''' Name: Do Viet Anh/
                Age :19/
                UNI: BK/
                My cat: MO/
                My crush:secret '''

@app.route('/school')
def school():
    return direct ("http://techkids.vn")

if __name__ == '__main__':
  app.run( debug=True)
