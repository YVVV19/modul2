from fastapi import FastAPI, Query


app=FastAPI(debug=True)

names=[]


@app.get("/create/")
def create(name: str = Query(None, description="Input your name:")):
    names.append(name)
    return f"List:{names}"

@app.get("/read/")
def read():
    return f"{names}"

@app.post("/delete/")
def delete(index: int = Query(None, description="Input index:")):
    if index:
        names.pop(index)
        return f"{names}"
    else:
        return f"No information by your index:{index}"

@app.get("/update/")
def update(name: str = Query(None, description="Input your name:")):
    for i in names:
        if name == i:
            return f"The name {name} is already in LIST "
        else:
            names.append(name)
        
# uvicorn app:app  