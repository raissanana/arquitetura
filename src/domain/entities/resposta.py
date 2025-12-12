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
    
    def __init__(self, *args, **kwargs):
        raise TypeError("Use Resposta.criar() ou Resposta.from_persistence() para instanciar objetos")
    
    @classmethod
    def criar(cls, formulario_id: str, dados: Dict[str, Any], agente_nome: str = ""):
        """Factory method para criar NOVAS respostas (da API)"""
        if not formulario_id:
            raise ValueError("ID do formulário é obrigatório")
        
        if not dados:
            raise ValueError("Dados da resposta são obrigatórios")
        
        # Cria a instância usando __new__ para contornar o __init__
        instancia = cls.__new__(cls)
        
        # Configura os atributos manualmente
        instancia.id = str(uuid.uuid4())
        instancia.formulario_id = formulario_id
        instancia.agente_nome = agente_nome
        instancia.dados = dados
        instancia.criado_em = datetime.now()
        
        return instancia
    
    @classmethod
    def from_persistence(cls, data: Dict[str, Any]) -> 'Resposta':
        """
        Factory method para criar respostas a partir de dados PERSISTENTES
        (do banco de dados)
        """
        # Extrai dados do dicionário
        id = data['id']
        formulario_id = data['formulario_id']
        agente_nome = data.get('agente_nome', '')
        dados_resposta = data['dados']
        
        # Processa criado_em (pode ser string ISO ou datetime)
        criado_em = data.get('criado_em')
        if isinstance(criado_em, str):
            # Remove 'Z' e converte para datetime
            criado_em = criado_em.replace('Z', '+00:00')
            criado_em = datetime.fromisoformat(criado_em)
        
        # Cria a instância usando __new__
        instancia = cls.__new__(cls)
        
        # Configura atributos com dados do banco
        instancia.id = id
        instancia.formulario_id = formulario_id
        instancia.agente_nome = agente_nome
        instancia.dados = dados_resposta
        instancia.criado_em = criado_em
        
        return instancia
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """
        Alternativa: cria a partir de dicionário
        (Apenas aponta para from_persistence agora)
        """
        return cls.from_persistence(data)
    
    def to_dict(self):
        return {
            'id': self.id,
            'formulario_id': self.formulario_id,
            'agente_nome': self.agente_nome,
            'dados': self.dados,
            'criado_em': self.criado_em.isoformat()
        }