from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def info():
    return f'''
    <h2>Request Details</h2>
    <p>Method: {request.method}</p>
    <p>URL: {request.url}</p>
    <p>Host: {request.host}</p>
    <p>Remote Addr: {request.remote_addr}</p>
    <p>Referrer: {request.referrer}</p>
    '''

if __name__ == "__main__":
    app.run(debug=True)
