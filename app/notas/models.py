from ..conexion import get_db

class Nota:
    def __init__(self, id=None, usuario_id=None, titulo=None, descripcion=None, fecha=None):
        self.id = id
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha

    def create(self):
        cursor, db = get_db()
        try:
            query = """
                INSERT INTO notas (usuario_id, titulo, descripcion)
                VALUES (%s, %s, %s)
            """
            values = (self.usuario_id, self.titulo, self.descripcion)
            cursor.execute(query, values)
            db.commit()
            print("Nota creada con éxito")
        except Exception as e:
            print(f"Error al crear nota: {e}")  

    def read(self):
        cursor, _ = get_db()
        try:
            query = "SELECT * FROM notas WHERE id = %s"
            cursor.execute(query, (self.id,))
            result = cursor.fetchone()
            if result:
                self.id, self.usuario_id, self.titulo, self.descripcion, self.fecha = result.values()
            return result
        except Exception as e:
            print(f"Error al leer nota: {e}")

    def update(self):
        cursor, db = get_db()
        try:
            query = """
                UPDATE notas
                SET usuario_id = %s, titulo = %s, descripcion = %s
                WHERE id = %s
            """
            values = (self.usuario_id, self.titulo, self.descripcion, self.id)
            cursor.execute(query, values)
            db.commit()
            print("Nota actualizada con éxito")
        except Exception as e:
            print(f"Error al actualizar nota: {e}")

    def delete(self):
        cursor, db = get_db()
        try:
            query = "DELETE FROM notas WHERE id = %s"
            cursor.execute(query, (self.id,))
            db.commit()
            print("Nota eliminada con éxito")
        except Exception as e:
            print(f"Error al eliminar nota: {e}")

    @staticmethod
    def get_all():
        cursor, _ = get_db()
        try:
            query = "SELECT * FROM notas"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener notas: {e}")

    @staticmethod
    def get_by_usuario_id(usuario_id):
        cursor, _ = get_db()
        try:
            query = "SELECT * FROM notas WHERE usuario_id = %s"
            cursor.execute(query, (usuario_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener notas por usuario_id: {e}")