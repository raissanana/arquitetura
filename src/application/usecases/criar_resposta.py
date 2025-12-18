from application.dto.resposta_dto import CriarRespostaInputDTO, CriarRespostaOutputDTO
from domain.entities.resposta import Resposta
from domain.repositories.resposta_repository import RespostaRepository
from .base_usecase import UseCase

class CriarRespostaUseCase(UseCase[CriarRespostaInputDTO, CriarRespostaOutputDTO]):
    """Use Case para criar resposta"""
    
    def __init__(self, resposta_repository: RespostaRepository):
        self.resposta_repository = resposta_repository
    
    def execute(self, input_dto: CriarRespostaInputDTO) -> CriarRespostaOutputDTO:
        # Cria a entidade Resposta
        resposta = Resposta.criar(
            formulario_id=input_dto.formulario_id,
            dados=input_dto.dados,
            agente_nome=input_dto.agente_nome
        )
        
        # Salva no repositório correto
        resposta_salva = self.resposta_repository.salvar_resposta(resposta)
        
        # Retorna DTO de saída
        return CriarRespostaOutputDTO(
            id=resposta_salva.id,
            formulario_id=resposta_salva.formulario_id,
            criado_em=resposta_salva.criado_em.isoformat()
        )