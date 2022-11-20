import json


def load_candidates_from_json():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


def get_candidate_by_pk(pk):
    for i in load_candidates_from_json():
        if i['id'] == pk:
            return i


def get_candidates_by_name(candidate_name):
    result = []
    for i in load_candidates_from_json():
        if candidate_name in i['name'].lower():
            result.append(i)
    return result


def get_candidates_by_skill(skill_name):
    result = []
    for i in load_candidates_from_json():
        if skill_name in i['skills'].lower():
            result.append(i)
    return result