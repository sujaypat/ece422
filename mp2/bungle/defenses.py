import re, os
from bottle import FormsDict, HTTPError
from hashlib import md5

############################################################
# XSS Defenses

class XSSNone(object):
    """ this class just returns user_input """

    name = "No defense"
    @staticmethod
    def init(response):
        response.set_header("X-XSS-Protection", "0");           
    @staticmethod
    def filter(user_input):
        return user_input

class XSSEncodeAngles(object):
    """ this class encodes < and > into &lt; and &gt; """

    name = "Encode &lt; and &gt;"
    @staticmethod
    def init(response):
        response.set_header("X-XSS-Protection", "0");
    @staticmethod
    def filter(user_input):
        #TODO: complete this filter definition
        return user_input	

############################################################
# CSRF Defenses

class CSRFNone(object):
    """ this class provides no defense against CSRF """

    name = "No defense"
    @staticmethod
    def init(request, response):
        return None
    @staticmethod
    def formHTML(token):
        return ""
    @staticmethod
    def validate(request, token):
        pass

class CSRFToken(object):
    """ token validation class against CSRF """

    name = "Token validation"
    @staticmethod
    def init(request, response):
        token = request.get_cookie("csrf_token")

        #TODO: implement Token validation

        return token
    @staticmethod
    def formHTML(token):
        return "<input type='hidden' name='csrf_token' value='" + token + "'>"
    @staticmethod
    def validate(request, token):
        if request.forms.get('csrf_token') != token:
            raise HTTPError(403, "CSRF Attack Detected (bad or missing token)")        

############################################################

xssDefenses = [XSSNone,XSSEncodeAngles]
csrfDefenses = [CSRFNone,CSRFToken]

xssDefense = xssDefenses[0]
csrfDefense = csrfDefenses[0]

def setCookies(response):
    response.set_cookie("xssdefense", str(xssDefenses.index(xssDefense)))
    response.set_cookie("csrfdefense", str(csrfDefenses.index(csrfDefense)))

def setup(request, response):
    def getDefense(request, name):
        if name in request.forms:
            return int(request.forms.get(name))
        elif name in request.query:
            return int(request.query.get(name))
        else:
            return int(request.get_cookie(name,0))
    global xssDefense, csrfDefense
    xss = getDefense(request, "xssdefense")
    if xss not in range(len(xssDefenses)):
        raise HTTPError(output="Invalid XSS Defense (%d)" % xss)
    csrf = getDefense(request, "csrfdefense")
    if csrf not in range(len(csrfDefenses)):
        raise HTTPError(output="Invalid CSRF Defense (%d)" % csrf)
    xssDefense = xssDefenses[xss]
    csrfDefense = csrfDefenses[csrf]
    setCookies(response)

def selectors():
    def getSelector(defenseList, selectedDefense=None):
        return "".join("<option value=%d%s>%d - %s</option>" % \
                           (i,(defenseList[i].name==selectedDefense.name and " selected" or ""), i, defenseList[i].name) \
                           for i in range(len(defenseList)))
    return FormsDict(xssoptions=getSelector(xssDefenses,xssDefense),
                     csrfoptions=getSelector(csrfDefenses,csrfDefense))

