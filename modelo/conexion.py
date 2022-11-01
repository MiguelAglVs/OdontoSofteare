import sqlite3

class conexionDB:

	def run_query(self, query, parameters = ()):
		self.db_name = 'bd/odontosw.db'
		with sqlite3.connect(self.db_name) as conn:
			cursor = conn.cursor()
			result = cursor.execute(query, parameters)
			conn.commit
		return result