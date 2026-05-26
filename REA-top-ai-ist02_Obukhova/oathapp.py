from flask import Flask, redirect, request
import requests

app = Flask(__name__)

CLIENT_ID = "268689012696-eslr826bufe7kl8925bnvp5ffb6u35c7.apps.googleusercontent.com"
CLIENT_SECRET = "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"
REDIRECT_URI = "http://localhost:5000/callback"


# 1. Главная страница с кнопкой
@app.route("/")
def index():
    return '''
        <h1 style='color: rgb(219, 112, 147); text-align: center;'>Войдите с помощью Google</h1>
        <div style='text-align: center;'>
            <a href="/login">
                <button style="
                background-color: rgb(219, 112, 147); 
                color: white;
                padding: 20px 40px; 
                font-size: 24px; 
                border-radius: 10px;
                ">Войти через Google</button>
            </a>
        </div>
    '''


# 2. Редирект на Google
@app.route("/login")
def login():
    google_auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth"
        f"?client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        "&response_type=code"
        "&scope=openid email profile"
    )
    return redirect(google_auth_url)


# 3. Callback от Google
@app.route("/callback")
def callback():
    code = request.args.get("code")

    # Обмениваем code на токен
    token_url = "https://oauth2.googleapis.com/token"

    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    token_response = requests.post(token_url, data=data)
    token_json = token_response.json()

    access_token = token_json.get("access_token")

    # Получаем инфу о пользователе
    userinfo_response = requests.get(
        "https://www.googleapis.com/oauth2/v1/userinfo",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    user_info = userinfo_response.json()
    return f"""
            <h1 style='color: rgb(219, 112, 147); text-align: center;'>Успешно!</h1>
            <p style='color: rgb(219, 112, 147); text-align: center;'>Ваш email: {user_info.get('email')}</p>
            <div style='text-align: center;'>
                <img width="300" src='https://tse1.mm.bing.net/th/id/OIP.Qpfz12j4C5riZasKjxXOqQHaHX?rs=1&pid=ImgDetMain&o=7&rm=3'>
            </div>
        """


if __name__ == "__main__":
    app.run(port=5000)
