from cassandra.cluster import Cluster, NoHostAvailable
import socket

from flask import Flask
app = Flask(__name__)

session_ = None
db_host_ = "db-service"


def get_session():
	global session_
	if session_:
		return session_
	try:
		socket.gethostbyname(db_host_)
		cluster = Cluster([db_host_])
		session_ = cluster.connect()
	except socket.error:
		print("DB host is not found")
	except NoHostAvailable:
		print("DB host is up but the DB service is not available")
	return session_
		
@app.route("/", methods = ["get", "post"])
def hello():
    return "Hello world"

@app.route("/init")
def init():
    session = get_session()
    if session:
        session.execute("CREATE KEYSPACE IF NOT EXISTS demo WITH replication = {'class': 'SimpleStrategy','replication_factor': 1}")
        session.execute("CREATE TABLE IF NOT EXISTS demo.counters(name text primary key, count counter)")
        return "DB has been initialized"
    return "DB Session is not active"

@app.route("/counter")
def counter():
    session = get_session()
    session.execute("update demo.counters  set count += 1 where name = 'home'")
    count = session.execute("select count from demo.counters where name = 'home'").one()[0]
    return "Page view count: " + str(count)

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5000)
