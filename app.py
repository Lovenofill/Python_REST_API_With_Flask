# การส่งค่าเป็น {} เพื่อให้เป็น Json Format หากส่งมาเป็น list ค่าจะอ่านได้เท่าที่ส่งมา 1 list เท่านั้นไม่สามารถแนบข้อความหรือสถานะติดมาด้วยได้
import uuid
from flask import Flask , request
from db import items , stores

app = Flask(__name__)

#methon 
# @app.get ("/store")
# def get_stores():
#     return {"stores":stores}

# @app.post ("/store")
# def create_store():
#     request_data = request.get_json()
#     new_store = {"name" : request_data["name"],"item":[]}
#     stores.append(new_store)
#     return new_store , 201

# @app.post ("/store/<string:name>/item")
# def create_item(name):
#     request_data = request.get_json()
#     for store in stores:
#         if  store["name"] == name :
#             new_item = {"name" : request_data["name"], "price": request_data["price"]}
#             store["item"].append(new_item)
#             return new_item, 201
#     return {"message":"store not found"}, 404

# @app.get ("/store/<string:name>")
# def get_store(name):
#     for store in stores:          
#         if  store["name"] == name :
#             return store
#     return {"message":"store not found"}, 404

# @app.get ("/store/<string:name>/item")
# def get_item_in_store(name):
#     for store in stores:          
#         if  store["name"] == name :
#             return {"items" : store["item"] , "message" : "This is item in" + " " +store["name"]}
#     return {"message":"store not found"}, 404

@app.get ("/store")
def get_stores():
    return {"stores":list(stores.values())}

@app.post ("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id":store_id}
    stores[store_id] = store
    return store , 201

@app.post ("/item")
def create_item(name):
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        return {"message":"store not found"}, 404
    
    item_id = uuid.uuid4().hex
    item = {**item_data,"id": item_id}
    item[item_id] = item
    return item , 201

@app.get ("/item")
def get_all_items():
    return {"stores":list(stores.values())}

@app.get ("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except:
        return {"message":"store not found"}, 404
    
@app.get ("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"message":"store not found"}, 404