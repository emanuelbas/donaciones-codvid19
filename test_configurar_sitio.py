import unittest
import app

class TestConfigurarSitio(unittest.TestCase):

    def setUp(self):
        """
        Inicializa la aplicación para pruebas de sitio
        """
        self.app = app.create_app()
        self.app.testing = True
        self.app = self.app.test_client(self)


    def test_sitio_deshabilitado(self):
        """
        Prueba de sitio deshabilitado
        """
        self.app.post('/login',
            data=dict(usuario='admin',clave='1234'),
            follow_redirects = True)

        configuracion = dict(usuario="test_user_1",
            titulo="Centros de Ayuda de la Provincia de Buenos Aires",
            descripcion="Centros de ayuda",
            mail="centros.de.ayuda@buenosaires.gov.ar",
            activo="0",
            cantPagina="5"
            )
        self.app.post('/configuracion/vista_configuracion',
            data=configuracion,
            follow_redirects = True)
        self.app.get('/logout')
        response = self.app.post('/login',
            data=dict(usuario='operador',clave='1234'),
            follow_redirects = True)
        self.assertTrue(b'Los sentimos, el sitio se encuentra en mantenimiento' in response.data)


    def test_sitio_habilitado(self):
        """
        Prueba de sitio habilitado
        """
        self.app.post('/login',
            data=dict(usuario='admin',clave='1234'),
            follow_redirects = True)

        configuracion = dict(usuario="test_user_1",
            titulo="Centros de Ayuda de la Provincia de Buenos Aires",
            descripcion="Centros de ayuda",
            mail="centros.de.ayuda@buenosaires.gov.ar",
            activo="1",
            cantPagina="5"
            )
        self.app.post('/configuracion/vista_configuracion',
            data=configuracion,
            follow_redirects = True)
        self.app.get('/logout')
        response = self.app.post('/login',
            data=dict(usuario='operador',clave='1234'),
            follow_redirects = True)
        self.assertTrue(b'Centros de Ayuda de la Provincia de Buenos Aires' in response.data)

    def tearDown(self):
        self.app.get('/logout')

if __name__ == '__main__':
    unittest.main()









    # Prueba con un modelo que tiene el mensaje existe_nombre(municipio_id,nombre)
    # def test_existe_centro(self):
    #    response = Centro_de_ayuda.existe_nombre(7,"Centro la esperanza")
    #    self.assertTrue(response)    