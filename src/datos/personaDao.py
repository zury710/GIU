from src.datos.conexion import Conexion


class PersonaDao:
        _INSERT = ("insert into Persona(nombre, apellido, cedula, sexo,email)"
               "values('Zury', 'Gomez', '0959445834', 'F', 'dprez@mail.com')")

        @classmethod
        def insertar_persona(cls):
            try:
                with Conexion.obtenerCursor() as cursor:
                    registros= cursor.execute(cls._INSERT)
                    return registros
            except Exception as e:
                print(e)
if __name__ == '__main__':
    PersonaDao.insertar_persona()