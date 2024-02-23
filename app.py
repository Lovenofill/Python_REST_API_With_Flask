# การส่งค่าเป็น {} เพื่อให้เป็น Json Format หากส่งมาเป็น list ค่าจะอ่านได้เท่าที่ส่งมา 1 list เท่านั้นไม่สามารถแนบข้อความหรือสถานะติดมาด้วยได้
from flask import Flask , request

app = Flask(__name__)

stores = [
    {
        "name" : "LNF Stores",
        "item" :[
            {
            "name":"item 1",
            "price" : 18.99
            }
        ]
    }
]

#methon 
@app.get ("/store")
def get_stores():
    return {"stores":stores}

@app.post ("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name" : request_data["name"],"item":[]}
    stores.append(new_store)
    return new_store , 201

@app.post ("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if  store["name"] == name :
            new_item = {"name" : request_data["name"], "price": request_data["price"]}
            store["item"].append(new_item)
            return new_item, 201
    return {"message":"store not found"}, 404

@app.get ("/store/<string:name>")
def get_store(name):
    for store in stores:          
        if  store["name"] == name :
            return store
    return {"message":"store not found"}, 404

@app.get ("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:          
        if  store["name"] == name :
            return {"items" : store["item"] , "message" : "This is item in" + " " +store["name"]}
    return {"message":"store not found"}, 404
