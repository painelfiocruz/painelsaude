import psycopg2


class Conexao(object):
	_db = None
	def __init__(self, mhost, db, usr, pwd, port):
		self._db = psycopg2.connect(
			host=mhost, dbname=db, user=usr,  password=pwd, port=port)

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
		# 	if self._db:
		# 		self._db.close()
		return True

	def consultar(self, sql):
		rs=None
		try:
			cur=self._db.cursor()
			cur.execute(sql)
			rs=cur.fetchall()
		except Exception as e:
			print(f'Error {e}')
			return None
		# finally:
		# 	if self._db:
		# 		self._db.close()
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
            # trace("testConect", "connection.py", "", "Conexão ao banco", "Iniciando")
            _db = Conexao(self._config['host'], self._config['dataBase'], self._config['user'], self._config['pwd'], self._config['port'])
            # trace("testConect", "connection.py", "", "Conexão ao banco", "Realizado")
            # trace("testConect", "connection.py", "", "Teste de conexão ao banco", "Iniciando")
            if _db.testConection():
                # trace("testConect", "connection.py", "", "Teste de conexão ao banco", "Realizado")
                # trace("testConect", "connection.py", "", "Fechando conexão com o banco", "Iniciando")
                _db.close()
                # trace("testConect", "connection.py", "", "Fechando conexão com o banco", "Realizado")
                return True
            else:
                # trace("testConect", "connection.py", "", "Teste de conexão ao banco", "Não realizado")
                # trace("testConect", "connection.py", "", "Fechando conexão com o banco", "Iniciando")
                _db.close()
                # trace("testConect", "connection.py", "", "Fechando conexão com o banco", "Realizado")
                return False
        except Exception as e:
            # trace("testConect", "connection.py", "", "Teste de conexão ao banco", "Erro")
            # trace("testConect", "connection.py", "", "Erro", e)
            print(e)
            return False

    def conectar(self):
        # Realiza a conexão com o banco de dados no banco
        try:
            # trace("conectar", "connection.py", "", "Conexão ao banco", "Iniciando")
            
            _db = Conexao(self._config['host'], self._config['dataBase'], self._config['user'], self._config['pwd'], self._config['port'])
            # trace("conectar", "connection.py", "", "Conexão ao banco", "Realizado")
            # trace("conectar", "connection.py", "", "Teste de conexão ao banco", "Iniciando")
            if _db.testConection():
                # trace("conectar", "connection.py", "", "Fechando conexão com o banco", "Realizado")
                return _db
            else:
                # trace("conectar", "connection.py", "", "Teste de conexão ao banco", "Não realizado")
                return False
        except Exception as e:
            # trace("conectar", "connection.py", "", "Teste de conexão ao banco", "Erro")
            # trace("conectar", "connection.py", "", "Erro", e)
            return False    