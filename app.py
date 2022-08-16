from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {"name": "store1",
     "items": [
         {"name": "i1",
          "price": 1},
         {"name": "i2",
          "price": 2}
     ]
     }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message": "store not found"})


@app.route("/store")
def get_stores():
    return jsonify({"stores": stores})


@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    pass


# @app.route("/store/<string:name>/item")
# def create_item_in_store(name):
#    pass


app.run(port=5000)
