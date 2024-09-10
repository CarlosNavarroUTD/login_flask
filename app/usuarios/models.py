from ..conexion import get_db
from app.funciones import hash_password
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

class Usuario(UserMixin):
    def __init__(self, id, nombre, apellidos, email, password=None):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    @staticmethod
    def iniciar_sesion(email, contrasena):
        cursor, _ = get_db()
        if cursor:
            query = "SELECT id, nombre, apellidos, email, password FROM usuarios WHERE email = %s"
            cursor.execute(query, (email,))
            
            usuario_data = cursor.fetchone()
            
            if usuario_data:
                hashed_password = usuario_data['password']
                if bcrypt.check_password_hash(hashed_password, contrasena):
                    return Usuario(
                        usuario_data['id'], 
                        usuario_data['nombre'], 
                        usuario_data['apellidos'], 
                        usuario_data['email']
                    )
                else:
                    print("Correo electrónico o contraseña incorrectos.")
                    return None
            else:
                print("Usuario no encontrado.")
                return None
        else:
            print("No se pudo establecer la conexión con la base de datos.")
            return None

    @staticmethod
    def registrarse(nombre, apellidos, email, contrasena):
        cursor, db = get_db()
        if cursor and db:
            query = "SELECT email FROM usuarios WHERE email = %s"
            cursor.execute(query, (email,))
            if cursor.fetchone():
                print("El correo electrónico ya está registrado.")
                return None
            
            query = """
            INSERT INTO usuarios (nombre, apellidos, email, password)
            VALUES (%s, %s, %s, %s)
            """
            hashed_password = bcrypt.generate_password_hash(contrasena)
            cursor.execute(query, (nombre, apellidos, email, hashed_password))
            db.commit()

            id_usuario = cursor.lastrowid

            nuevo_usuario = Usuario(id_usuario, nombre, apellidos, email, hashed_password)
            print("Registro exitoso.")
            return nuevo_usuario
        else:
            print("No se pudo establecer la conexión con la base de datos.")
            return None

    @staticmethod
    def get_by_id(user_id):
        cursor, _ = get_db()
        if cursor:
            query = "SELECT id, nombre, apellidos, email FROM usuarios WHERE id = %s"
            cursor.execute(query, (user_id,))
            user_data = cursor.fetchone()
            if user_data:
                return Usuario(
                    user_data['id'],
                    user_data['nombre'],
                    user_data['apellidos'],
                    user_data['email']
                )
        return None