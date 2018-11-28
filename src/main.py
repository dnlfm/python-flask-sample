from flask import Flask, jsonify
import movie_client as client


app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"message": "Hello World!"}), 200


@app.route("/movie/<mid>", methods=['GET'])
def get_movie(mid):
    movie = client.get_movie(mid)
    if movie is not None:
        return jsonify(movie), 200
    else:
        return jsonify({"message": "movie_not_found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

