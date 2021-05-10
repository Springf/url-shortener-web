from store.sqlite_store import SqliteStore
import pytest
import sqlite3

clean_sql = 'delete from url_store;'
conn = sqlite3.connect('tests/url-test-store.db', check_same_thread=False)
def clean_up():
    conn.execute(clean_sql)
    conn.commit()

def test_add():
    store = SqliteStore(conn)
    assert store.add('short', 'long')
    assert store.add('short1', 'long1')
    assert store.add('short1', 'long1')
    assert store.add('short1', 'long2') == False
    with pytest.raises(ValueError):
        store.add('', '')
    with pytest.raises(ValueError):
        store.add(None, '')
    clean_up()

def test_get():
    store = SqliteStore(conn)
    store.add('short', 'long')
    store.add('short1', 'long1')
    store.add('short1', 'longlong')
    store.add('short2', 'long2')

    assert store.get('short') == 'long'
    assert store.get('short1') == 'long1'
    assert store.get('short2') == 'long2'
    assert store.get('short3') is None
    with pytest.raises(ValueError):
        store.get('')
    with pytest.raises(ValueError):
        store.get(None)
    clean_up()

def test_update():
    store = SqliteStore(conn)
    assert store.add('short', 'long', 'user')
    assert store.add('short1', 'long1', 'user')
    assert store.add('short1', 'long1', 'user')
    assert store.get('short1') == 'long1'
    assert store.update('short1', 'long2', 'user')
    assert store.get('short1') == 'long2'
    assert store.add('short1', 'longlong') == False
    assert store.update('short', 'longlong', 'user2') == False
    with pytest.raises(ValueError):
        assert store.update('short1', '', '')
    clean_up()