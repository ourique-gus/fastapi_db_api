import uvicorn
from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get('/')
async def index():
    with sqlite3.connect('db.db') as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        
        query = 'select * from frutas'
        
        cur.execute(query)
        
        data = [dict(d) for d in cur.fetchall()]
        return data
    
if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=7777)
