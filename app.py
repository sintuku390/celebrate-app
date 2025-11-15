from flask import Flask, render_template_string, request

app = Flask(__name__)

html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Celebration App</title>

    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial;
            background: linear-gradient(45deg, #ff9a9e, #fad0c4);
            overflow-x: hidden;
            text-align: center;
        }

        /* Moving background animation */
        @keyframes bgMove {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        body {
            background-size: 400% 400%;
            animation: bgMove 10s ease infinite;
        }

        /* Input & Button */
        .box {
            margin-top: 70px;
        }
        input {
            padding: 12px;
            width: 250px;
            font-size: 18px;
            border-radius: 10px;
            border: 2px solid black;
            text-align: center;
        }
        button {
            padding: 12px 25px;
            background: red;
            color: white;
            border: none;
            border-radius: 10px;
            margin-top: 20px;
            font-size: 20px;
            cursor: pointer;
        }

        /* Glowing name */
        .glow {
            font-size: 45px;
            font-weight: bold;
            margin-top: 40px;
            color: #fff;
            text-shadow:
                0 0 10px #ff6a6a,
                0 0 20px #ff6a6a,
                0 0 30px #ff6a6a,
                0 0 40px #ff6a6a;
        }

        /* Fireworks */
        .firework {
            position: fixed;
            width: 15px;
            height: 15px;
            background: yellow;
            border-radius: 50%;
            animation: explode 1s linear infinite;
        }
        @keyframes explode {
            0% { transform: scale(1); opacity: 1; }
            100% { transform: scale(10); opacity: 0; }
        }

        /* Emoji rain */
        .emoji {
            position: fixed;
            top: -50px;
            font-size: 35px;
            animation: fall 3s linear infinite;
        }
        @keyframes fall {
            to { transform: translateY(120vh); }
        }

        /* Mobile responsive */
        @media (max-width: 600px) {
            input { width: 80%; }
            .glow { font-size: 35px; }
            button { font-size: 18px; }
        }
    </style>
</head>
<body>

<audio id="music" src="https://www.fesliyanstudios.com/play-mp3/387" preload="auto"></audio>

<div class="box">
    <h2 style="font-size:28px;">Enter Your Name</h2>

    <form method="POST">
        <input type="text" name="username" placeholder="Your name">
        <br>
        <button type="submit">Celebrate 🎉</button>
    </form>
</div>

{% if username %}
<h1 class="glow">🎉 Welcome {{ username }}! 🎉</h1>

<script>
document.getElementById("music").play();

/* Emoji rain */
for (let i = 0; i < 30; i++) {
    let emoji = document.createElement("div");
    emoji.classList.add("emoji");
    emoji.innerText = "🎊";
    emoji.style.left = Math.random() * 100 + "vw";
    emoji.style.animationDuration = (Math.random() * 3 + 2) + "s";
    document.body.appendChild(emoji);
    setTimeout(() => emoji.remove(), 5000);
}

/* Fireworks */
for (let i = 0; i < 20; i++) {
    let fw = document.createElement("div");
    fw.classList.add("firework");
    fw.style.left = Math.random() * window.innerWidth + "px";
    fw.style.top = Math.random() * window.innerHeight + "px";
    fw.style.background = "hsl(" + Math.random() * 360 + ",100%,50%)";
    document.body.appendChild(fw);
    setTimeout(() => fw.remove(), 1000);
}
</script>

{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    username = None
    if request.method == "POST":
        username = request.form.get("username")

    return render_template_string(html_page, username=username)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
