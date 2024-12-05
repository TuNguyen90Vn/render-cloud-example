import unittest
import json

from app import create_app
from dotenv import load_dotenv
import os

load_dotenv()
DB_URL_TEST = os.environ.get("DB_TEST_URL")

class CastingAgency(unittest.TestCase):

    def setUp(self):
        self.database_path = DB_URL_TEST
        self.app = create_app({
            "SQLALCHEMY_DATABASE_URI": self.database_path
        })
        self.client = self.app.test_client

        self.create_new_actor = {"name": "Actor 11", "age":25, "gender": "Male", "movie_id": 3}
        self.create_new_actor_400 = {"name": "Actor 1", "age":25}
        self.update_actor = {"name":"Actor 11 update", "age":25, "gender":"Male", "movie_id": 3}

        self.create_new_movie = {"title": "Movie 1", "release_date": "2024-10-01T00:00:00.000000"}
        self.create_new_movie_400 = {"title": "Movie 1"}
        self.update_movie = {"title":"Movie 1 update", "release_date":"2024-10-01T00:00:00.000000"}

        with open('token_config.json', 'r') as f:
            self.auth = json.loads(f.read())

        casting_assistant_jwt = self.auth["Casting Assistant"]["token"]
        casting_director_jwt = self.auth["Casting Director"]["token"]
        executive_producer_jwt = self.auth["Executive Producer"]["token"]
        self.auth_headers = {
            "Casting Assistant": f'Bearer {casting_assistant_jwt}',
            "Casting Director": f'Bearer {casting_director_jwt}',
            "Executive Producer": f'Bearer {executive_producer_jwt}'
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_successful_create_actor(self):
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().post("/actors", headers=header_obj, json=self.create_new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_400_create_actor(self):
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().post("/actors", headers=header_obj, json=self.create_new_actor_400)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Bad Request")
        self.assertEqual(data["error"], 400)

    def test_successful_get_actor(self):
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().get("/actors", headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_successful_update_actor(self):
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().patch("/actors/2", headers=header_obj, json=self.update_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_404_update_actor(self):
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().patch("/actors/999", headers=header_obj, json=self.update_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")
        self.assertEqual(data["error"], 404)

    def test_successful_delete_actor(self):
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().delete("/actors/1", headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["delete"], 1)

    def test_404_delete_actor(self):
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().delete("/actors/999", headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")
        self.assertEqual(data["error"], 404)

    def test_successful_create_movie(self):
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().post("/movies", headers=header_obj, json=self.create_new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])

    def test_400_create_movie(self):
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().post("/movies", headers=header_obj, json=self.create_new_movie_400)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Bad Request")
        self.assertEqual(data["error"], 400)

    def test_successful_get_movie(self):
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().get("/movies", headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])

    def test_successful_update_movie(self):
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().patch("/movies/2", headers=header_obj, json=self.update_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])

    def test_404_update_movie(self):
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().patch("/movies/999", headers=header_obj, json=self.update_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")
        self.assertEqual(data["error"], 404)

    def test_successful_delete_movie(self):
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().delete("/movies/1", headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["delete"], 1)

    def test_404_delete_movie(self):
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().delete("/movies/999", headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")
        self.assertEqual(data["error"], 404)

    def test_successful_casting_director(self):
        header_obj = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        res = self.client().post("/actors", headers=header_obj, json=self.create_new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_unauthorized_casting_director(self):
        header_obj = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        res = self.client().delete("/movies/2", headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["message"], "Permission not found.")

    def test_successful_casting_assistant(self):
        header_obj = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        res = self.client().get("/actors", headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_unauthorized_casting_assistant(self):
        header_obj = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        res = self.client().delete("/actors/1", headers=header_obj)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["message"], "Permission not found.")

    def test_successful_executive_producer(self):
        header_obj = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().post("/movies", headers=header_obj, json=self.create_new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])

if __name__ == "__main__":
    unittest.main()