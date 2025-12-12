import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        # PEGA do .env ou usa fallback
        self.conn_string = os.getenv(
            'DATABASE_URL',
            'postgresql://neondb_owner:npg_K7CUBa8TeLim@ep-aged-block-admnp9g0-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require'
        )
    
    def _get_connection(self):
        """Cria uma nova conexão com o NeonDB"""
        return psycopg2.connect(self.conn_string)