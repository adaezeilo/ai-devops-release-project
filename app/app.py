from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>AI DevOps Release Dashboard</h1>
    <p>Application: Release Dashboard</p>
    <p>Version: 1.0.0</p>
    <p>Environment: Development</p>
    <p>Status: HEALTHY</p>
    """


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "version": "1.0.0"
    }


if __name__ == "__main__":
    app.run(debug=True)