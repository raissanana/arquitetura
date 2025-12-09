from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.formulario import Formulario
from ..entities.resposta import Resposta

class FormularioRepository(ABC):
    """Interface para o repositório de formulários"""
    
    @abstractmethod
    def salvar_formulario(self, formulario: Formulario) -> Formulario:
        """Salva um formulário no banco"""
        pass
    
    @abstractmethod
    def listar_formularios(self) -> List[Formulario]:
        """Lista todos os formulários"""
        pass
    
    @abstractmethod
    def buscar_formulario_por_id(self, formulario_id: str) -> Optional[Formulario]:
        """Busca um formulário por ID"""
        pass
    
    @abstractmethod
    def salvar_resposta(self, resposta: Resposta) -> Resposta:
        """Salva uma resposta no banco"""
        pass
    
    @abstractmethod
    def listar_respostas(self) -> List[Resposta]:
        """Lista todas as respostas"""
        pass