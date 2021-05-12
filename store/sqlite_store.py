from core.store.store import Store
import sqlite3

insert_sql = "INSERT INTO url_store VALUES(?,?,?,datetime('now', 'localtime'),null)"
select_sql = "SELECT url FROM url_store WHERE short_url = ?"
update_sql = "UPDATE url_store SET url = ?, updated_datetime = datetime('now', 'localtime') WHERE short_url = ? and user = ?"

class SqliteStore(Store):
    """
    Implement the backend store using sqlite
    """
    def __init__(self, conn) -> None:
        super().__init__()
        self.conn = conn
    
    def add(self, short_url:str, url:str, user:str = None) -> bool:
        if not short_url or not url:
            raise ValueError('URL cannot be empty.')
        try:
            args = (short_url, url, user)
            cursor = self.conn.execute(insert_sql, args)
            self.conn.commit()
            return True
        except sqlite3.Error as er:
            print(er)
            args = (short_url,)
            return url == self.conn.execute(select_sql, args).fetchone()[0]
        

    def get(self, short_url:str) -> str:
        if not short_url:
            raise ValueError('URL cannot be empty.')
        args = (short_url,)
        cursor = self.conn.execute(select_sql, args).fetchone()
        if cursor:
            return cursor[0]
        return None
    
    def update(self, short_url:str, url:str, user:str) -> bool:
        if not short_url or not url or not user:
            raise ValueError('URL or user cannot be empty.')
        args = (url, short_url, user)
        print(args)
        cursor = self.conn.execute(update_sql, args)
        self.conn.commit()
        print(cursor.rowcount)
        return cursor.rowcount == 1
