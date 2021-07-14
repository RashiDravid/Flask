from flask import Flask,jsonify,request

app = Flask(__name__)

contacts =[
    {
        "id" : 1,
        "name": u"Rasika",
        "contact":u"1234567890",
        "done": False
    },
    {
        "id" : 2,
        "name": u"Swara",
        "contact":u"2345679810",
        "done": False
}]
@app.route("/add-data",methods =["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        },400)

    contact = {
        "id" : contacts[-1]["id"]+1,
        "name": request.json["name"],
        "contact": request.json["contact",""],
        "done": False
    }    
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/add-data")
def get_contact():
    return jsonify({
        "data" : contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)