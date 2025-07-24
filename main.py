from flask import Flask
import scratchattach
import threading
import os
from dotenv import load_dotenv

load_dotenv()
cookie = os.getenv("SCRATCH_COOKIE")

print("hello")

print("Cookie =", os.getenv("SCRATCH_COOKIE"))

if cookie is None:
    print("⚠️ Le cookie n’a pas été chargé correctement.")
else:
    print("✅ Cookie bien récupéré.")


app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Scratch actif ✅"

def start_scratch_bot():
    username = os.getenv("SCRATCH_USERNAME")
    password = os.getenv("SCRATCH_PASSWORD")
    session = scratchattach.login(username, password)

#Returns a sa.Session object
    conn = session.connect_cloud("1201314467")

    @conn.on("set")
    def when_cloud_variable_changes(variable, value):
        print(f"{variable} changée en : {value}")

    conn.run()  # commence l’écoute des variables cloud

# Lancer le bot Scratch dans un thread séparé
threading.Thread(target=start_scratch_bot).start()

# Lancer le serveur Flask (pingable via UptimeRobot)
app.run(host='0.0.0.0', port=8080)
