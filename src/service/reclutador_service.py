from configs.flask_config import db
from object.usuario import Usuario


class ReclutadorService():

    def obtener_nombre_reclutadores(self, lista_idreclutador):
        reclutadores = db.session.query(Usuario
                                   ).filter(Usuario.idusuario.in_(lista_idreclutador)).all()

        if reclutadores:
            dict_datos_reclutador = [{'idreclutador': reclutador.idusuario, 'nombre': reclutador.nombre} for reclutador in reclutadores]
            print('Se encontró reclutador con los identificadores {}'.format(lista_idreclutador))
            return True, 'Existe reclutador', dict_datos_reclutador
        print('No existe reclutador con los identificadores {}'.format(lista_idreclutador))
        return False, 'No existe reclutador.', None