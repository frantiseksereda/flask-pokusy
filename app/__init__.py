from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.jsonxmlcomparator import bp as jsonxmlcomparator_bp
    app.register_blueprint(jsonxmlcomparator_bp, url_prefix="/jsonxmlcomparator")

    from app.graphs import bp as graphs_bp
    app.register_blueprint(graphs_bp, url_prefix="/graphs")

    from app.metmuseum import bp as metmuseum_bp
    app.register_blueprint(metmuseum_bp, url_prefix="/metmuseum")

    @app.route("/test/")
    def test_page():
        return "Kuk"

    return app

if __name__ == '__main__':
    create_app().run(debug=True)



