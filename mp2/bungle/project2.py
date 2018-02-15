#!/usr/bin/python2
import sys, os, re, bottle
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from bottle import get, post, run, debug, request, response, redirect, view, FormsDict, HTTPError
import defenses
import database

#a cookie which tracks user login
authSecret = "77da94627587ed9ef35081b28ee5d06ee758a242ffded59efa7687b04873c89d"

@get("/")
@view("index")
def index():
    defenses.setup(request, response)
    csrftoken = defenses.csrfDefense.init(request, response)
    return dict(v=FormsDict(defenses=defenses.selectors(),
                            user=getUser(),
                            csrfcode=defenses.csrfDefense.formHTML(csrftoken)))

@get("/search")
@view("search")
def search():
    defenses.setup(request, response)
    csrftoken = defenses.csrfDefense.init(request, response)
    defenses.xssDefense.init(response)
    query = defenses.xssDefense.filter(request.query.q)
    user = getUser()
    if user and user.id:
        if query != "":
            database.addHistory(user.id, query)
        history = database.getHistory(user.id)
    else:
        history = None
    return dict(v=FormsDict(defenses=defenses.selectors(),
                            user=getUser(),
                            query=query,
                            history=history,
                            csrfcode=defenses.csrfDefense.formHTML(csrftoken)))

@post("/login")
def login(create=False):
    defenses.setup(request, response)
    csrftoken = defenses.csrfDefense.init(request, response)
    defenses.csrfDefense.validate(request, csrftoken)
    username = request.forms.get("username")
    password = request.forms.get("password")
    if not username or not password:
        raise HTTPError(400, "Required field is empty")
    if not re.match("[A-Za-z0-9]+$", username):
        raise HTTPError(400, "Invalid username")
    if create:
        if database.fetchUser(username):
            raise HTTPError(400, "User already exists")
        if len(password) < 4:
            raise HTTPError(400, "Password too short")
        database.createUser(username, password)
    if not database.validateUser(username, password):
        raise HTTPError(403, "Login unsuccessful")
    response.set_cookie("authuser", username, authSecret, httponly=True)
    redirect("./")

@post("/logout")
def logout():
    defenses.setup(request, response)
    csrftoken = defenses.csrfDefense.init(request, response)
    defenses.csrfDefense.validate(request, csrftoken)
    response.delete_cookie("authuser")
    redirect("./")

@post("/create")
def create():
    login(create=True)
       
def getUser():
    username = request.get_cookie("authuser", None, secret=authSecret)
    if username is None:
        return None
    return database.fetchUser(username)

@post("/setdefenses")
def setdefenses():
    defenses.setup(request, response)
    if request.forms.get("location"):
        redirect(request.forms.get("location"))
    else:
        redirect("./")

if __name__ == "__main__":
    debug(True)
    run(host='127.0.0.1', reloader=True)
