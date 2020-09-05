from flask import request
from flask_restful import Resource
from configs.dynamodb_config import dynamodb
from common.DecimalEncoder import *
from service.autorizador_service import AutorizadorService
from service.candidato_apreciacion_service import CandidatoApreciacionService
from service.reclutador_service import ReclutadorService
from object.apreciacion import ApreciacionSchema
import ast

autorizador_service = AutorizadorService()
candidato_apreciacion_service = CandidatoApreciacionService()
reclutador_service = ReclutadorService()


class CandidatoApreciacionObtenerController(Resource):

    def post(self):
        token = request.json['headers']['Authorization']
        email = request.json['headers']['correoelectronico']
        flag, respuesta, codigo = autorizador_service.reclutador_identificador_validar(token, email)
        if not flag:
            return {
                'statusCode': codigo,
                'body': respuesta
            }

        idcandidato, idcliente_idpuestolaboral, idreclutador = candidato_apreciacion_service.validar_parametros(request)

        flag, respuesta, lista_idreclutador, codigo = candidato_apreciacion_service.obtener_apreciacion_candidato(idcandidato, idcliente_idpuestolaboral, idreclutador, dynamodb)
        if flag:
            flag, mensaje, reclutadores = reclutador_service.obtener_nombre_reclutadores(lista_idreclutador)
            respuesta = candidato_apreciacion_service.asignar_nombre_reclutadores(respuesta, reclutadores)

            return {
                'statusCode': codigo,
                'body': ast.literal_eval(ApreciacionSchema().to_json(respuesta))
            }

        return {
            'statusCode': 500,
            'body': 'Error al registrar apreciación del candidato.'
        }
