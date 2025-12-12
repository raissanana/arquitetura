# src/application/usecases/criar_resposta.py
from ..dto.formulario_dto import CriarRespostaInputDTO, CriarRespostaOutputDTO
from domain.entities.resposta import Resposta
from domain.repositories.formulario_repository import FormularioRepository
from .base_usecase import UseCase

class CriarRespostaUseCase(UseCase[CriarRespostaInputDTO, CriarRespostaOutputDTO]):
    """Use Case para criar resposta"""
    
    def __init__(self, formulario_repository: FormularioRepository):
        self.formulario_repository = formulario_repository
    
    def execute(self, input_dto: CriarRespostaInputDTO) -> CriarRespostaOutputDTO:
        # Cria a entidade Resposta
        resposta = Resposta.criar(
            formulario_id=input_dto.formulario_id,
            dados=input_dto.dados,
            agente_nome=input_dto.agente_nome
        )
        
        # Salva no repositório
        resposta_salva = self.formulario_repository.salvar_resposta(resposta)
        
        # Retorna DTO de saída
        return CriarRespostaOutputDTO(
            id=resposta_salva.id,
            formulario_id=resposta_salva.formulario_id,
            criado_em=resposta_salva.criado_em.isoformat()
        )