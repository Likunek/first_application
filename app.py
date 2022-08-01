from flask import Flask
import json

with open('candidates.json') as f:
    people = json.load(f)

app = Flask(__name__)

@app.route("/")
def page_index():
    list = ''
    for candidates in people:
        list += f'<pre>\nИмя кандидата - {candidates["name"]}'\
           f'\nПозиция кандидата: {candidates["position"]}' \
           f'\nНавыки: {candidates["skills"]}\n</pre>'
    return list

@app.route("/candidate/<int:x>")
def page_candidate(x):
    candidates = people[x]
    return f'<img src = "{candidates["picture"]}">\n<pre>' \
           f'\nИмя кандидата - {candidates["name"]}' \
           f'\nПозиция кандидата: {candidates["position"]}' \
           f'\nНавыки: {candidates["skills"]}</pre>'

@app.route("/skill/<x>")
def page_skill(x):
    list = ''
    for candidates in people:
        if x in candidates['skills']:
            list += f'<pre>\nИмя кандидата - {candidates["name"]}' \
           f'\nПозиция кандидата: {candidates["position"]}' \
           f'\nНавыки: {candidates["skills"]}\n</pre>'
    return list



app.run()
