# infrastructure/web/controllers/resposta_controller.py
from flask import Request, Response, jsonify
from application.usecases.criar_resposta import CriarRespostaUseCase
from application.usecases.listar_respostas import ListarRespostasUseCase
from application.dto.resposta_dto import (
    CriarRespostaInputDTO,
    CriarRespostaOutputDTO,
    ListarRespostasOutputDTO
)

class RespostaController:
    
    def __init__(self,
                 criar_resposta_use_case: CriarRespostaUseCase,
                 listar_respostas_use_case: ListarRespostasUseCase):
        
        self.criar_resposta_use_case = criar_resposta_use_case
        self.listar_respostas_use_case = listar_respostas_use_case
    
    def criar_resposta(self, request: Request) -> Response:
        try:
            data = request.get_json()
            
            input_dto = CriarRespostaInputDTO(
                formulario_id=data.get('formulario_id'),
                dados=data.get('dados'),
                agente_nome=data.get('agente_nome', '')
            )
            
            output_dto = self.criar_resposta_use_case.execute(input_dto)

            return jsonify({
                "data": {
                    "id": output_dto.id,
                    "formulario_id": output_dto.formulario_id,
                    "criado_em": output_dto.criado_em
                },
                "message": "Resposta criada com sucesso!"
            }), 201
            
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            print(f"Erro interno ao criar resposta: {e}")
            return jsonify({"error": "Internal server error"}), 500
    
    def listar_respostas(self) -> Response:
        try:
            output_dto = self.listar_respostas_use_case.execute()
            return jsonify(output_dto.respostas), 200
            
        except Exception as e:
            print(f"Erro interno ao listar respostas: {e}")
            return jsonify({"error": "Internal server error"}), 500