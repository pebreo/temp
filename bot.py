# http://stackoverflow.com/questions/11747527/how-to-connect-javascript-to-python-sharing-data-with-json-format-in-both-ways
from bottle import hook, response, route, run, static_file, request
import json
import socket

#These lines are needed for avoiding the "Access-Control-Allow-Origin" errors
@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'

#If you have to send parameters, the right sintax is as calling the resoure
# with a kind of path, with the parameters separed with slash ( / ) and they 
# MUST to be written inside the lesser/greater than signs  ( <parameter_name> ) 
# @route('/dataQuery/<name>/<age>')
# def myQuery(name,age):
#     connection= sqlite3.connect("C:/folder/data.db")
#     mycursor = connection.cursor()
#     mycursor.execute("select * from client where name = ? and age= ?",(name, age))
#     results = mycursor.fetchall()
#     theQuery = []
#     for tuple in results:
#         theQuery.append({"name":tuple[0],"age":tuple[1]})
#     return json.dumps(theQuery)

@route('/<first>/<second>/')
def foo(first, second):
    s = "You said {} {}".format(first,second)
    print s
    return json.dumps(s)

@route('/add/<num1>/<num2>/')
def bar(num1, num2):
    sum = int(num1) + int(num2)
    print "the sum {}".format(sum)
    return json.dumps(sum)


#And the MOST important line to set this program as a web service provider is this
#run(host=socket.gethostname(), port=8000)
run(host='localhost',port=8000)