from flask import Flask, jsonify



def create_app():

    app = Flask(__name__)

    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(error=str(e)), 404


    @app.route('/')
    def index():
        return 'This is a test app'

    @app.route('/health')
    def health():
        try:
            return "Healthy", 200
        except Exception as e:
            return e,500
    
    return app
    

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=81)