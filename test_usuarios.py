import unittest
import app

# Documentacion 
# https://docs.google.com/document/d/1GDrzEtolStBImfXEI2jKENAkLT4u4f9AFRKcALE79LM/edit
class TestUsuarios(unittest.TestCase):

    def setUp(self):
        """
        Inicializa la aplicación para pruebas de usuario
        """
        self.app = app.create_app()
        self.app.testing = True
        self.app = self.app.test_client(self)
        self.app.post('/login',
            data=dict(usuario='admin',clave='1234'),
            follow_redirects = True)

    def test_alta_existe_email(self):
        """
        Prueba que se muestre error al ingresar un mail existente
        """
        datos_usuario = dict(usuario="test_user_1",
            clave="1234",
            nombre="Usuario2",
            apellido="Prueba",
            email="test_user2@gmail.com"
            )
        self.app.post('/usuario/crear_usuario',
            data=datos_usuario,
            follow_redirects = True)
        datos_usuario = dict(usuario="test_user_2",
            clave="1234",
            nombre="Usuario3",
            apellido="Prueba",
            email="test_user2@gmail.com"
            )
        response = self.app.post('/usuario/crear_usuario',
            data=datos_usuario,
            follow_redirects = True)
        
        self.assertTrue(b'El email ya existe' in response.data)
        
    def test_alta_exitosa(self):
        """
        Prueba el alta de un nuevo usuario
        """
        datos_usuario = dict(usuario="test_user_1",
            clave="1234",
            nombre="Usuario2",
            apellido="Prueba",
            email="test_user@gmail.com"
            )
        response = self.app.post('/usuario/crear_usuario',
            data=datos_usuario,
            follow_redirects = True)
        self.assertTrue(b'Usuario creado exitosamente' in response.data)

    def tearDown(self):
        """
        Limpia la Base de Datos
        """
        self.app.get('/usuarios/borrar_usuario_por_nombre/test_user_1')

if __name__ == '__main__':
    unittest.main()









    # Prueba con un modelo que tiene el mensaje existe_nombre(municipio_id,nombre)
    # def test_existe_centro(self):
    #    response = Centro_de_ayuda.existe_nombre(7,"Centro la esperanza")
    #    self.assertTrue(response)    