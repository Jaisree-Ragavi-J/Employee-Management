import sys
import os

# ✅ FIRST fix path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ THEN import
from database import init_db

# ✅ Initialize DB
init_db()