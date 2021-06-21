import unittest
import app

# Documentacion 
# https://docs.google.com/document/d/1GDrzEtolStBImfXEI2jKENAkLT4u4f9AFRKcALE79LM/edit
class TestAplicacionArriba(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app()
        self.app.testing = True
        self.app = self.app.test_client(self)
        
    def test_flask_arriba(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.app.get('/login')
        self.assertTrue(b'Login' in response.data)

    # Probar que logue correctamente
    def test_login_in(self):
        response = self.app.post('/login',
            data=dict(usuario='admin',clave='1234'),
            follow_redirects = True)
        self.assertTrue(b'Se logueo correctamente' in response.data)

    # Probar error en credenciales
    def test_login_wrong_credentials(self):
        response = self.app.post('/login',
            data=dict(usuario='admin',clave='12345'),
            follow_redirects = True)
        self.assertTrue(b'No logro autenticarse, vuelva a intentarlo.' in response.data)

    # Probar que des-logue correctamente
    def test_logout(self):
        response = self.app.get('/logout')
        self.assertTrue(b'Su sesion fue cerrada correctamente.' in response.data)

    # Probar que cierta ubicacion solo este disponible para usuario logueado

if __name__ == '__main__':
    unittest.main()









    # Prueba con un modelo que tiene el mensaje existe_nombre(municipio_id,nombre)
    # def test_existe_centro(self):
    #    response = Centro_de_ayuda.existe_nombre(7,"Centro la esperanza")
    #    self.assertTrue(response)    