# infrastructure/web/controllers/formulario_controller.py
from flask import Request, Response, jsonify
from application.usecases.criar_formulario import CriarFormularioUseCase
from application.usecases.listar_formularios import ListarFormulariosUseCase
from application.dto.formulario_dto import (
    CriarFormularioInputDTO,
    CriarFormularioOutputDTO,
    ListarFormulariosOutputDTO 
)

class FormularioController:
    
    def __init__(self,
                 criar_formulario_use_case: CriarFormularioUseCase,
                 listar_formularios_use_case: ListarFormulariosUseCase):
        
        self.criar_formulario_use_case = criar_formulario_use_case
        self.listar_formularios_use_case = listar_formularios_use_case
    
    def criar_formulario(self, request: Request) -> Response:
        try:
            data = request.get_json()
            
            input_dto = CriarFormularioInputDTO(
                titulo=data.get('titulo'),
                descricao=data.get('descricao', ''),
                campos=data.get('campos', [])
            )
            
            output_dto = self.criar_formulario_use_case.execute(input_dto)
            
            return jsonify({
                "data": {
                    "id": output_dto.id,
                    "titulo": output_dto.titulo,
                    "criado_em": output_dto.criado_em
                },
                "message": "Formulário criado com sucesso!"
            }), 201
            
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            print(f"Erro interno ao criar formulário: {e}")
            return jsonify({"error": "Internal server error"}), 500
    
    def listar_formularios(self) -> Response:
        try:
            output_dto = self.listar_formularios_use_case.execute()
            return jsonify(output_dto.formularios), 200
            
        except Exception as e:
            print(f"Erro interno ao listar formulários: {e}")
            return jsonify({"error": "Internal server error"}), 500