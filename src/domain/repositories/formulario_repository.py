# src/domain/repositories/formulario_repository.py
from abc import ABC, abstractmethod
from typing import List
from domain.entities.formulario import Formulario

class FormularioRepository(ABC):
    
    @abstractmethod
    def salvar_formulario(self, formulario: Formulario) -> Formulario:
        """Salva um formulário no banco"""
        pass
    
    @abstractmethod
    def listar_formularios(self) -> List[Formulario]:  # ✅ PLURAL
        """Lista todos os formulários"""
        pass