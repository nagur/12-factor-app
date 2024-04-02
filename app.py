import os
from flask import Flask
from redis import Redis
app = Flask(__name__)
redis_Db = Redis(host=os.getenv('Host'),port=os.getenv('Port'))

@app.route('/')
def welcomePage():
    redis_Db.incr('visitorCount')
    visitorCount = str(redis_Db.get('visitorCount'),'utf-8')
    return "Welocme to 0 programming! Visitor Count: " +visitorCount
if __name__== "__main__":
    app.run(host="0.0.0.0", debug=True)
        


