from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Any
import uuid

@dataclass
class CampoFormulario:
    nome: str
    tipo: str  # 'texto', 'numero', 'data', 'selecao'
    obrigatorio: bool = False
    opcoes: List[str] = None  # para tipo 'selecao'

@dataclass
class Formulario:
    id: str
    titulo: str
    descricao: str
    campos: List[CampoFormulario]
    criado_em: datetime
    
    @classmethod
    def criar(cls, titulo: str, descricao: str = "", campos: List[Dict[str, Any]] = None):
        if not titulo or not titulo.strip():
            raise ValueError("Título é obrigatório")
        
        # converte dicionários para objetos CampoFormulario
        campos_objetos = []
        if campos:
            for campo_dict in campos:
                campos_objetos.append(CampoFormulario(
                    nome=campo_dict.get('nome', ''),
                    tipo=campo_dict.get('tipo', 'texto'),
                    obrigatorio=campo_dict.get('obrigatorio', False),
                    opcoes=campo_dict.get('opcoes')
                ))
        
        return cls(
            id=str(uuid.uuid4()),
            titulo=titulo,
            descricao=descricao,
            campos=campos_objetos,
            criado_em=datetime.now()
        )
    
    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'campos': [
                {
                    'nome': campo.nome,
                    'tipo': campo.tipo,
                    'obrigatorio': campo.obrigatorio,
                    'opcoes': campo.opcoes
                } for campo in self.campos
            ],
            'criado_em': self.criado_em.isoformat()
        }