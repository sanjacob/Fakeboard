import json
from pathlib import Path

db = {}

with open(Path(__file__).parent / "db.json") as f:
    db = json.load(f)
