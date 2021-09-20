from flask import Flask, render_template, request, redirect, send_from_directory
import json
import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def intro():
    year = datetime.datetime.today().year
    with open('data.json') as file:
        data = json.load(file)
        length = len(data)
    with open('skill.json', encoding='utf-8') as skill:
        skill_data = json.load(skill)
        skill_length = len(skill_data)
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        print(name, email, phone, message)
        return redirect(f'mailto: warlord2952@gmail.com?subject=Please Contact &body= Name:{name}\n Phone: {phone}\n Message: {message}')
        
    return render_template("index.html", project_data=data, length=length, skill_data=skill_data,
                               skill_length=skill_length,year=year)

@app.route("/download")
def download():
    return send_from_directory('static', path='files/Satyam-Resume.pdf')



if __name__ == "__main__":
    app.run(debug=True)
