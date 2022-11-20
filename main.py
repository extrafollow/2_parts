from utils import load_candidates_from_json, get_candidate_by_pk, get_candidates_by_skill, get_candidates_by_name
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = load_candidates_from_json()
    return render_template('list.html',
                           candidates=candidates)


@app.route('/candidate/<int:pk>')
def get_candidate(pk):
    candidate = get_candidate_by_pk(pk)
    return render_template('single.html',
                           candidate=candidate)


@app.route('/search/<candidate_name>')
def get_candidate_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    count = len(candidates)
    return render_template('search.html',
                           candidates=candidates,
                           count=count)


@app.route('/skill/<skill_name>')
def get_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    count = len(candidates)
    return render_template('skill.html',
                           candidates=candidates,
                           count=count,
                           skill_name=skill_name)


app.run(debug=True)
