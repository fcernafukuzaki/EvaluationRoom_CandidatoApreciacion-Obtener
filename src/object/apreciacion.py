import json


class Apreciacion():

    def __init__(self, idreclutador, nombre, idcandidato, idcliente_idpuestolaboral, idcliente, idpuestolaboral, apreciacion, fecha):
        self.idreclutador = int(idreclutador)
        self.nombre = nombre
        self.idcandidato = int(idcandidato)
        self.idcliente_idpuestolaboral = idcliente_idpuestolaboral
        self.idcliente = int(idcliente)
        self.idpuestolaboral = int(idpuestolaboral)
        self.apreciacion = apreciacion
        self.fecha = fecha


class ApreciacionSchema():

    def to_json(self, apreciacion):
        return json.dumps([ob.__dict__ for ob in apreciacion])
