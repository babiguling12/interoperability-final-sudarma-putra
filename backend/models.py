from database import get_db_connection

def get_all_events():
    conn = get_db_connection()
    events = conn.execute('SELECT * FROM events').fetchall()
    conn.close()
    return [dict(e) for e in events]

def create_event(title, date, location, quota):
    conn = get_db_connection()
    conn.execute('INSERT INTO events (title, date, location, quota) VALUES (?, ?, ?, ?)', (title, date, location, quota))
    conn.commit()
    conn.close()

def update_event(event_id, title, date, location, quota):
    conn = get_db_connection()
    conn.execute('UPDATE events SET title = ?, date = ?, location = ?, quota = ? WHERE id = ?', (title, date, location, quota, event_id))
    conn.commit()
    conn.close()

def delete_event(event_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM events WHERE id = ?', (event_id,))
    conn.commit()
    conn.close()

def register_participant(name, email, event_id):
    conn = get_db_connection()
    conn.execute('INSERT INTO participants (name, email, event_id) VALUES (?, ?, ?)', (name, email, event_id))
    conn.commit()
    conn.close()

def get_all_participants():
    conn = get_db_connection()
    participants = conn.execute("""
        SELECT p.id, p.name, p.email, e.title AS event_title
        FROM participants p
        JOIN events e ON p.event_id = e.id
    """).fetchall()
    conn.close()
    return [dict(p) for p in participants]

def get_participants_by_event(event_id):
    conn = get_db_connection()
    participants = conn.execute("""
        SELECT p.id, p.name, p.email, e.title AS event_title
        FROM participants p
        JOIN events e ON p.event_id = e.id
        WHERE e.id = ?
    """, (event_id,)).fetchall()
    conn.close()
    return [dict(p) for p in participants]  