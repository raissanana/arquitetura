from typing import List
from ..dto.formulario_dto import CriarFormularioInputDTO, CriarFormularioOutputDTO
from domain.entities.formulario import Formulario
from domain.repositories.formulario_repository import FormularioRepository
from .base_usecase import UseCase

class CriarFormularioUseCase(UseCase[CriarFormularioInputDTO, CriarFormularioOutputDTO]):
    """Use Case para criar formulário"""
    
    def __init__(self, formulario_repository: FormularioRepository):
        self.formulario_repository = formulario_repository
    
    def execute(self, input_dto: CriarFormularioInputDTO) -> CriarFormularioOutputDTO:
        # Cria a entidade Formulário
        formulario = Formulario.criar(
            titulo=input_dto.titulo,
            descricao=input_dto.descricao,
            campos=input_dto.campos
        )
        
        # Salva no repositório
        formulario_salvo = self.formulario_repository.salvar_formulario(formulario)
        
        # Retorna DTO de saída
        return CriarFormularioOutputDTO(
            id=formulario_salvo.id,
            titulo=formulario_salvo.titulo,
            criado_em=formulario_salvo.criado_em.isoformat()
        )