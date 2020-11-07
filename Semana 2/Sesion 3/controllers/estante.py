from flask_restful import Resource, reqparse
from models.estante import EstanteModel
# @app.route("/estante",methods=["get","post"])
class EstantesController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "capacidad",
        type=int,
        required=True,
        help="Falta la capacidad del estante"
    )
    parser.add_argument(
        "ubicacion",
        type=str,
        required=True,
        help="Falta la ubicacion del estante"
    )
    parser.add_argument(
        "descripcion",
        type=str,
        required=True,
        help="Falta la descripcion"
    )
    def get(self):
        estantes = EstanteModel.query.all()
        # print(estantes)
        resultado = []
        for estante in estantes:
            # print(estante)
            resultado.append(estante.mostrar_json())
        return {
            'ok':True,
            'content': resultado,
            'message': None
        }
    
    def post(self):
        data = self.parser.parse_args()
        estante = EstanteModel(data['capacidad'],data['ubicacion'], data['descripcion'])
        try:
            estante.guardar_bd()
            print(estante)
            return {
                'ok':True,
                'message':'Se guardo exitosamente el estante',
                'content': estante.mostrar_json()
            }
        except:
            return {
                'ok':False,
                'message':'No se pudo guardar el estante en la bd'
            },500

class EstanteController(Resource):
    def get(self, est_id):
        estante = EstanteModel.query.filter_by(id=est_id).first()
        # print(estante)
        if estante:
            return {
                'ok':True,
                'content':estante.mostrar_json(),
                'message': None
            }
        else:
            return {
                'ok': False,
                'content': None,
                'message': 'No existe el estante con id: '+str(est_id)
            }, 404
    def put(self, est_id):
        estante = EstanteModel.query.filter_by(id=est_id).first()
        if estante:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "capacidad",
                type=int,
                required=True,
                help="Falta la capacidad del estante"
            )
            parser.add_argument(
                "ubicacion",
                type=str,
                required=True,
                help="Falta la ubicacion del estante"
            )
            parser.add_argument(
                "descripcion",
                type=str,
                required=True,
                help="Falta la descripcion"
            )
            data = parser.parse_args()
            estante.capacidad= data['capacidad']
            estante.ubicacion= data['ubicacion']
            estante.descripcion= data['descripcion']
            estante.guardar_bd()

            return {
                'ok':True,
                'content':estante.mostrar_json(),
                'message': None
            }
        else:
            return {
                'ok': False,
                'content': None,
                'message': 'No existe el estante con id: '+str(est_id)
            }, 404