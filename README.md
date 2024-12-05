# Casting Agency Project
Udacity Full-Stack Web Developer Nanodegree Program Capstone Project

## Project Motivation
The Casting Agency Project models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process. 

This project is simply a workspace for practicing and showcasing different set of skills related with web development. These include data modelling, API design, authentication and authorization and cloud deployment.

You can checkout the project which is hosted in Render Cloud via this URL: https://render-cloud-example-366c.onrender.com/

### Running Locally

#### Installing Dependencies

##### Python 3.11

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

##### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

#### Database Setup
We are using Postgres, create the database using the `casting-agency-dump.sql` file provided. In terminal run:

```bash
psql -U postgres -d casting_agency -f casting-agency-dump.sql
```

#### Running Tests
To run the tests, run
```bash
psql -U postgres -d casting_agency_test -f casting-agency-dump.sql
python test_app.py
```

#### Environment Setup
First, we need to setup an Auth0 account and postgres database.

Second, we create a .env file in the root folder with content like below:

```bash
DB_URL='postgresql://student:student@localhost:5432/casting_agency' #Your postgres URL
DB_URL_TEST='postgresql://student:student@localhost:5432/casting_agency_test' #Your postgres URL for testing
AUTH0_DOMAIN= 'xxx.auth0.com' # Your Auth0 domain
ALGORITHMS='RS256'
API_AUDIENCE='casting_agency' # Your API Audience
```

##### Roles
Create roles:

* Casting Assistant
	* Can view actors and movies
* Casting Director
	* All permissions a Casting Assistant has and…
	* Add or delete an actor from the database
	* Modify actors or movies
* Executive Producer
	* All permissions a Casting Director has and…
	* Add or delete a movie from the database

##### Permissions
Create permissions:

* `get:actors`
* `post:actors`
* `patch:actors`
* `delete:actors`
* `get:movies`
* `post:movies`
* `patch:movies`
* `delete:movies`

##### Set JWT Tokens in `token_config.json`

Use the following link to create users and sign them in to generate the token

```
https://{{YOUR_DOMAIN}}/authorize?audience={{API_IDENTIFIER}}&response_type=token&client_id={{YOUR_CLIENT_ID}}&redirect_uri={{YOUR_CALLBACK_URI}}
```

#### Launching The App

1. Initialize and activate a virtualenv:

   ```bash
   python -m virtualenv env
   env/Scripts/activate
   ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Run the server:

    ```bash
    python app.py
    ```

## API Documentation

### Models
There are two models:
* Movie
	* title
	* release_date
* Actor
	* name
	* age
	* gender

### Error Handling

Errors are returned as JSON objects in the following format:
```json
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Resource Not Found
- 422: Not Processable 
- 500: Internal Server Error
- 405: Method Not Allowed

### Endpoints

#### GET /actors 
* Get all actors

* Requires `get:actors` permission

* Responds with a 404 error if no actor return

* **Example Request:** `curl 'http://127.0.0.1:5000/actors'`

* **Expected Result:**
    ```json
	{
		"actors": [
			{
				"age": 20,
				"gender": "Male",
				"id": 2,
				"movie_id": 1,
				"name": "Actor 6"
			}
		],
		"success": true
	}
	```

#### POST /actors
* Creates a new actor.

* Requires `post:actors` permission

* Responds with a 400 error if name or age or gender or movie_id is missing

* Requires the name, age, gender and movie of the actor.

* **Example Request:** (Create)
    ```json
	curl --location --request POST 'http://127.0.0.1:5000/actors' \
		--header 'Content-Type: application/json' \
		--data-raw '{
			"name": "Actor 6",
			"age": 20,
			"gender": "Male",
			"movie_id": 1
		}'
    ```
    
* **Example Response:**
    ```json
	{
		"actors": [
			{
				"age": 20,
				"gender": "Male",
				"id": 2,
				"movie_id": 1,
				"name": "Actor 6"
			}
		],
		"success": true
	}
    ```
#### PATCH /actors/<actor_id>
* Updates the actor where <actor_id> is the existing actor id

* Require `patch:actors`

* Responds with a 404 error if <actor_id> is not found

* Update the given fields for Actor with id <actor_id>

* **Example Request:** 
	```json
    curl --location --request PATCH 'http://127.0.0.1:5000/actors/1' \
		--header 'Content-Type: application/json' \
		--data-raw '{
			"name": "Actor 1 update",
			"age": 25,
			"gender": "Male"
		}'
  ```
  
* **Example Response:**
    ```json
	{
		"actors": [
			{
				"age": 25,
				"gender": "Male",
				"id": 1,
				"movie_id": 1,
				"name": "Actor 1 update"
			}
		],
		"success": true
	}
	```

#### DELETE /actors/<int:actor_id>
* Deletes the actor with given id 

* Responds with a 404 error if <actor_id> is not found

* Require `delete:actors` permission

* **Example Request:** `curl --request DELETE 'http://127.0.0.1:5000/actors/1'`

* **Example Response:**
    ```json
	{
		"deleted": 1,
		"success": true
    }
    ```

#### GET /movies 
* Get all movies

* Responds with a 404 error if no movie return

* Require `get:movies` permission

* **Example Request:** `curl 'http://127.0.0.1:5000/movies'`

* **Expected Result:**
    ```json
	{
		"movies": [
			{
				"actors": [
					{
						"age": 20,
						"gender": "Male",
						"id": 2,
						"movie_id": 1,
						"name": "Actor 6"
					}
				],
				"id": 1,
				"release_date": "Mon, 01 Jan 2024 00:00:00 GMT",
				"title": "Movie 1"
			}
		],
		"success": true
	}
    ```
	
#### POST /movies
* Creates a new movie.

* Requires `post:movies` permission

* Responds with a 400 error if title or release date is missing

* Requires the title and release date.

* **Example Request:** (Create)
    ```json
	curl --location --request POST 'http://127.0.0.1:5000/movies' \
		--header 'Content-Type: application/json' \
		--data-raw '{
			"title": "Movie 1",
			"release_date": "2024-01-01T00:00:00.000000"
		}'
    ```
    
* **Example Response:**
    ```json
	{
		"movies": [
			{
				"actors": [],
				"id": 1,
				"release_date": "Mon, 01 Jan 2024 00:00:00 GMT",
				"title": "Movie 1"
			}
		],
		"success": true
	}
    ```

#### PATCH /movies/<movie_id>
* Updates the movie where <movie_id> is the existing movie id

* Require `patch:movies` permission

* Responds with a 404 error if <movie_id> is not found

* Update the corresponding fields for Movie with id <movie_id>

* **Example Request:** 
	```json
    curl --location --request PATCH 'http://127.0.0.1:5000/movies/1' \
		--header 'Content-Type: application/json' \
		--data-raw '{
			"title": "Movie 1 update",
			"release_date": "2024-01-01T00:00:00.000000"
		}'
  ```
  
* **Example Response:**
    ```json
	{
		"movies": [
			{
				"actors": [
					{
						"age": 25,
						"gender": "Male",
						"id": 2,
						"movie_id": 1,
						"name": "Actor 1 update"
					}
				],
				"id": 1,
				"release_date": "Mon, 01 Jan 2024 00:00:00 GMT",
				"title": "Movie 1 update"
			}
		],
		"success": true
	}
    ```

#### DELETE /movies/<int:movie_id>
* Deletes the movie with given id 

* Responds with a 404 error if <movie_id> is not found

* Require `delete:movies` permission

* **Example Request:** `curl --request DELETE 'http://127.0.0.1:5000/movies/1'`

* **Example Response:**
    ```json
	{
		"deleted": 1,
		"success": true
    }
    ```