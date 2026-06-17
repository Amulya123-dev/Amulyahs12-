from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['math_logic_ai']
users = list(db['users'].find())
for u in users:
    print(f"User: {u['username']}")
    for h in u.get('history', [])[:3]:
        print(f"  - {h['original']} -> {h['status']} | {h.get('latex', '')}")
