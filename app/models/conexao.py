import psycopg2
import pandas as pd
import numpy as np

class Conexao(object):
    _db = None
    def __init__(self, mhost, db, usr, pwd, port):
        self.mhost = mhost
        self.db = db
        self.usr = usr
        self.pwd = pwd
        self.port = port
        self.connect()

    def connect(self):
        print('pwd: {}'.format(self.pwd))
        self._db = psycopg2.connect(
            host=self.mhost,
            dbname=self.db,
            user=self.usr,
            password=self.pwd,
            port=self.port,
            connect_timeout=3,
            keepalives=1,
            keepalives_idle=5,
            keepalives_interval=2,
            keepalives_count=2
            )

    def testConection(self):
        return self.consultar("""SELECT table_name FROM information_schema.tables
                                 WHERE table_schema = 'public'""")

    def manipular(self, sql):
        try:
            cur = self._db.cursor()
            cur.execute(sql)
            cur.close()
            self._db.commit()
        except Exception as e:
            print(f'Error {e}')
            return False
        # finally:
        #     if self._db:
        #         self._db.close()
        return True

    def consultar(self, sql, Dataframe=False):
        rs=None
        cur = None
        try:
            self.connect()
            if Dataframe:
                rs=pd.read_sql( sql, self._db )
            else:
                cur=self._db.cursor()
                cur.execute(sql)
                rs=cur.fetchall()
                cur.close()
        except (Exception, Error) as e:
            print(f'Error {e}')
        finally:
            if self._db:
                self._db.close()
            if cur is not None:
                cur.close()
        return rs
    
    def close(self):
        self._db.close()

class Connection():
    _db = None
    _config = None
    def __init__(self, conf):
        self._config = conf
        
    def testConect(self):
        try:
            _db = Conexao(self._config['host'], self._config['dataBase'], self._config['user'], self._config['pwd'], self._config['port'])
            if _db.testConection():
                _db.close()
                return True
            else:
                _db.close()
                return False
        except Exception as e:
            print(e)
            return False

    def conectar(self):
        try:
            _db = Conexao(self._config['host'], self._config['dataBase'], self._config['user'], self._config['pwd'], self._config['port'])
            if _db.testConection():
                return _db
            else:
                return False
        except Exception as e:
            return False    