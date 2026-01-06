from fastapi import FastAPI, Request
import hashlib
import base64

app = FastAPI()

urls = {}

@app.get("/shorten")
def shorten(url, request: Request):
    print(urls)

    # shortening urls through hashes
    hash_object = hashlib.sha256(url.encode())
    urls[url] = hash_object.hexdigest()[:6]

    # getting the port of your own server
    port = request.scope.get("server")[1]

    return f"localhost:{port}/{urls[url]}"

@app.get("/debug")
def show_database():
    # returns the stored data to browser
    return urls

@app.get("/{url}")
def redirect(url):
    for key, value in urls.items():
        if value == url:
            return key