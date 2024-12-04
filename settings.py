from dotenv import load_dotenv 
import os

load_dotenv()

DB_URL=os.environ.get("DB_URL") 
DB_URL_TEST=os.environ.get("DB_URL") 
AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN")
ALGORITHMS = os.environ.get("ALGORITHMS")
API_AUDIENCE = os.environ.get("API_AUDIENCE")

