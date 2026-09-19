from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>AI DevOps Release Dashboard</h1>
    <p>Application: Release Dashboard</p>
    <p>Version: 1.1.0</p>
    <p>Environment: Production</p>
    <p>Status: HEALTHY</p>
    """


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "version": "1.1.0"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
