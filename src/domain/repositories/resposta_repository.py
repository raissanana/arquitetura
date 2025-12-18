from abc import ABC, abstractmethod
from typing import List
from domain.entities.resposta import Resposta

class RespostaRepository(ABC):
    
    @abstractmethod
    def salvar_resposta(self, resposta: Resposta) -> Resposta:
        """Salva uma resposta no banco"""
        pass
    
    @abstractmethod
    def listar_respostas(self) -> List[Resposta]:
        """Lista todas as respostas"""
        pass