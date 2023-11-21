import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv('JWT_SECRET', 'nothing')

print(JWT_SECRET)
