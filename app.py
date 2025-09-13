from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
        <html>
            <head>
                <title>Yêu bé Bông</title>
                <style>
                    body {
                        background-color: #ffe6f0;
                        text-align: center;
                        font-family: Arial, sans-serif;
                        margin-top: 100px;
                    }
                    h1 {
                        color: #ff3399;
                        font-size: 50px;
                    }
                    .heart {
                        font-size: 80px;
                        color: red;
                        animation: pulse 1s infinite;
                    }
                    @keyframes pulse {
                        0% { transform: scale(1); }
                        50% { transform: scale(1.2); }
                        100% { transform: scale(1); }
                    }
                </style>
            </head>
            <body>
                <h1>Anh yêu bé Bông ❤️</h1>
                <div class="heart">💖</div>
            </body>
        </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)