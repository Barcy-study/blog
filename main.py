from flask import Flask, render_template
import requests


api_url = "https://api.npoint.io/89d0f24f3e23a9d152ba"
response = requests.get(api_url)

response.raise_for_status()
datas = response.json()
print(datas)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', datas=datas)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = datas[post_id-1]
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
