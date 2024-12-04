from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Actor, Movie
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    if test_config is None:
        setup_db(app)
    else:
        database_path = test_config.get('SQLALCHEMY_DATABASE_URI')
        setup_db(app, database_path=database_path)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    # Routes
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actor(payload):
        actors = Actor.query.all()
        if len(actors) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'actors': [actor.format() for actor in actors]
        })

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(payload):
        request_data = request.get_json()
        new_name = request_data.get("name", None)
        new_age = request_data.get("age", None)
        new_gender = request_data.get("gender", None)
        movie_id = request_data.get("movie_id", None)

        if new_name == None or new_age == None or new_gender == None or movie_id == None:
            abort(400)

        try:
            actor = Actor(new_name, new_age, new_gender, movie_id)
            actor.insert()

            return jsonify({
                'success': True,
                'actors': [actor.format()]
            })
        except:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(payload, actor_id):
        actor = Actor.query.filter_by(id=actor_id).first()
        if actor is None:
            abort(404)

        try:
            request_data = request.get_json()
            update_name = request_data.get('name', None)
            update_age = request_data.get('age', None)
            update_gender = request_data.get('gender', None)
            update_movie_id = request_data.get('movie_id', None)

            if update_name:
                actor.name = update_name
            if update_age:
                actor.age = update_age
            if update_gender:
                actor.gender = update_gender
            if update_movie_id:
                actor.movie_id = update_movie_id
            actor.update()

            return jsonify({
                'success': True,
                'actors': [actor.format()]
            })
        except:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, actor_id):
        actor = Actor.query.filter_by(id=actor_id).first()
        if actor is None:
            abort(404)

        try:
            actor.delete()

            return jsonify({
                'success': True,
                'delete': actor_id
            })
        except:
            abort(422)

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movie(payload):
        movies = Movie.query.all()
        if len(movies) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'movies': [movie.format() for movie in movies]
        })

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(payload):
        request_data = request.get_json()
        new_title = request_data.get("title", None)
        new_release_date = request_data.get("release_date", None)

        if new_title == None or new_release_date == None:
            abort(400)
        try:
            movie = Movie(new_title, new_release_date)
            movie.insert()

            return jsonify({
                'success': True,
                'movies': [movie.format()]
            })
        except:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(payload, movie_id):
        movie = Movie.query.filter_by(id=movie_id).first()
        if movie is None:
            abort(404)

        try:
            request_data = request.get_json()
            update_title = request_data.get('title', None)
            update_release_date = request_data.get('release_date', None)
            if update_title:
                movie.title = update_title
            if update_release_date:
                movie.release_date = update_release_date
            movie.update()

            return jsonify({
                'success': True,
                'movies': [movie.format()]
            })
        except:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, movie_id):
        movie = Movie.query.filter_by(id=movie_id).first()
        if movie is None:
            abort(404)

        try:
            movie.delete()

            return jsonify({
                'success': True,
                'delete': movie_id
            })
        except:
            abort(422)

    # Error Handling
    @app.errorhandler(AuthError)
    def auth_error(error):
        print(error)
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "resource not found"}),
            404,
        )

    @app.errorhandler(401)
    def unauthorized(error):
        print(error)
        return jsonify({
            "success": False,
            "error": 401,
            "message": 'Unathorized'
        }), 401

    @app.errorhandler(500)
    def internal_server_error(error):
        print(error)
        return jsonify({
            "success": False,
            "error": 500,
            "message": 'Internal Server Error'
        }), 500

    @app.errorhandler(400)
    def bad_request(error):
        print(error)
        return jsonify({
            "success": False,
            "error": 400,
            "message": 'Bad Request'
        }), 400

    @app.errorhandler(405)
    def method_not_allowed(error):
        print(error)
        return jsonify({
            "success": False,
            "error": 405,
            "message": 'Method Not Allowed'
        }), 405

    return app


app = create_app()

if __name__ == '__main__':
    app.run()