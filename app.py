from flask import Flask, render_template, session
from routes.auth import auth_bp
from routes.game import game_bp
from routes.online import online_bp
from routes.history import history_bp
from socketio_instance import socketio  # import instance chung
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = "secret123"

# Khởi tạo SocketIO với app
socketio.init_app(app, cors_allowed_origins="*")

# Đăng ký blueprint
app.register_blueprint(auth_bp)
app.register_blueprint(game_bp)
app.register_blueprint(online_bp)
app.register_blueprint(history_bp)

# Trang mặc định
@app.route("/")
def index():
    if "user_id" in session:
        return render_template("menu.html", username=session.get("username"))
    return render_template("login.html")

if __name__ == "__main__":
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
