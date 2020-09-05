from .flask_config import api
from controller.candidatoapreciacionobtener_controller import *

api.add_resource(CandidatoApreciacionObtenerController,
    '/candidato/entrevista/apreciacion/obtener')
