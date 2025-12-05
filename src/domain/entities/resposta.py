from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any
import uuid

@dataclass
class Resposta:
    id: str
    formulario_id: str
    agente_nome: str
    dados: Dict[str, Any]  # Respostas dos campos
    criado_em: datetime
    
    @classmethod
    def criar(cls, formulario_id: str, dados: Dict[str, Any], agente_nome: str = ""):
        if not formulario_id:
            raise ValueError("ID do formulário é obrigatório")
        
        if not dados:
            raise ValueError("Dados da resposta são obrigatórios")
        
        return cls(
            id=str(uuid.uuid4()),
            formulario_id=formulario_id,
            agente_nome=agente_nome,
            dados=dados,
            criado_em=datetime.now()
        )
    
    def to_dict(self):
        return {
            'id': self.id,
            'formulario_id': self.formulario_id,
            'agente_nome': self.agente_nome,
            'dados': self.dados,
            'criado_em': self.criado_em.isoformat()
        }