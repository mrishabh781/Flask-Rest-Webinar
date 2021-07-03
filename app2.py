from flask import Flask, request
import json

from flask.wrappers import Request

app = Flask(__name__)
login_map = {"abc955":{"dep":"IT", "roll":"19"}}
class_det = {
        "IT": {"19":"Rishabh", "43": "Aniket", "52":"Rik"}, 
        "CSE": {"128":"SHOURYA","117":"Soubhik"},
        "AEIE": {"23": "Kamal"},
        "ELECTRICAL": {"1": "Gaurav"}
        }

@app.route('/', methods=["POST", "GET", "PATCH", "DELETE"])
def home():
    if request.method == "POST":
        data = request.get_json()
        dep = data.get("department")
        roll = data.get("roll")
        name = data.get("name")
        print(class_det)
        class_det[dep][roll] = name
        return {"success":True, "message":"Added into the dictionary."}
    if request.method == "PATCH":
        data = request.get_json()
        api_key = data.get("api_key")
        new_name = data.get("new_name")
        if api_key in login_map:
            user_data = login_map[api_key]
            dep = user_data.get("dep")
            roll = user_data.get("roll")
            class_det[dep][roll] = new_name
            return {"success":True, "message":"Updated into the dictionary."}
        else:
            return {"success":False, "message":"Invalid user!"}
    if request.method == "DELETE":
        data = request.get_json()
        dep = data.get("department")
        roll = data.get("roll")
        del class_det[dep][roll]
        return {"success":True, "message":"Deleted from the dictionary."}
    data = request.get_json()
    api_key = data.get("api_key")
    user_data = login_map[api_key]
    dep = user_data.get("dep")
    roll = user_data.get("roll")
    name = class_det[dep][roll]
    return {"dep":dep, "roll":roll, "name": name}


if __name__ == '__main__':
    print(__name__)
    app.run(debug=True)