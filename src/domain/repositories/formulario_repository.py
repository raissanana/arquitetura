# src/domain/repositories/formulario_repository.py
from abc import ABC, abstractmethod
from typing import List
from ..entities.formulario import Formulario
from ..entities.resposta import Resposta

class FormularioRepository(ABC):
    
    @abstractmethod
    def salvar_formulario(self, formulario: Formulario) -> Formulario:
        """Salva um formulário no banco (POST /formularios)"""
        pass
    
    @abstractmethod
    def listar_formularios(self) -> List[Formulario]:
        """Lista todos os formulários (GET /formularios)"""
        pass
    
    @abstractmethod
    def salvar_resposta(self, resposta: Resposta) -> Resposta:
        """Salva uma resposta no banco (POST /respostas)"""
        pass
    
    @abstractmethod
    def listar_respostas(self) -> List[Resposta]:
        """Lista todas as respostas (GET /respostas)"""
        pass
