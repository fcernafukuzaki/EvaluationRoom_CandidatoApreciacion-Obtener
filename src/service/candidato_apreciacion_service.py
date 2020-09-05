import pandas as pd
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr
from object.apreciacion import Apreciacion


class CandidatoApreciacionService():

    def validar_parametros(self, request):
        idcandidato = None
        idcliente_idpuestolaboral = None
        idreclutador = None

        try:
            idcandidato = request.json['idcandidato']
        except KeyError as e:
            print('No se envió identificador de candidato.')

        try:
            idcliente_idpuestolaboral = request.json['idcliente_idpuestolaboral']
        except KeyError as e:
            print('No se envió identificador de cliente.')

        try:
            idreclutador = request.json['idreclutador']
        except KeyError as e:
            print('No se envió identificador de reclutador.')

        return idcandidato, idcliente_idpuestolaboral, idreclutador

    def obtener_apreciacion_candidato(self, idcandidato=None, idcliente_idpuestolaboral=None, idreclutador=None, dynamodb=None):

        try:
            lista_idreclutador = []
            tabla = dynamodb.Table('Candidato_Apreciacion')

            if idcandidato:
                response = tabla.query(
                    KeyConditionExpression=Key('idcandidato').eq(idcandidato)
                )
            elif idcliente_idpuestolaboral:
                response = tabla.scan(
                    FilterExpression=Key('idcliente_idpuestolaboral').eq(idcliente_idpuestolaboral)
                )
            elif idreclutador:
                response = tabla.scan(
                    FilterExpression=Key('idreclutador').eq(idreclutador)
                )

            if len(response['Items']) > 0:
                for candidato_apreciacion in response['Items']:
                    lista_idreclutador.append(int(candidato_apreciacion['idreclutador']))

                lista_idreclutador = list(set(lista_idreclutador))
        except ClientError as e:
            print(e.response['Error']['Message'])
            return False, e.response['Error']['Message'], lista_idreclutador, 500
        else:
            return True, response['Items'], lista_idreclutador, 200

    def asignar_nombre_reclutadores(self, respuesta, lista_reclutador):
        if len(lista_reclutador) == 0:
            print('Lista de reclutadores vacía.')
            return respuesta

        df_reclutadores = pd.DataFrame(lista_reclutador)
        df_respuesta = pd.DataFrame(respuesta)

        merge = pd.merge(df_respuesta,
                         df_reclutadores[['idreclutador', 'nombre']],
                         on=['idreclutador'],
                         how='outer')
        merge = merge.sort_values(by=['idcandidato'])
        lista_resultado = [Apreciacion(**kwargs) for kwargs in merge.to_dict(orient='records')]
        return lista_resultado