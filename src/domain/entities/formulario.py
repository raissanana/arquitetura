from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Any
import uuid

@dataclass
class CampoFormulario:
    nome: str
    tipo: str  # 'texto', 'numero', 'data', 'selecao'
    obrigatorio: bool = False
    opcoes: List[str] = None

@dataclass
class Formulario:
    id: str
    titulo: str
    descricao: str
    campos: List[CampoFormulario]
    criado_em: datetime
    
    def __init__(self, *args, **kwargs):
        """
        Bloqueia o construtor DIRETO
        Força usar Formulario.criar() ou Formulario.from_persistence()
        """
        raise TypeError(
            "Use Formulario.criar() ou Formulario.from_persistence() em vez do construtor direto. "
            "Exemplo: Formulario.criar(titulo='Meu Formulário')"
        )
    
    @classmethod
    def criar(cls, titulo: str, descricao: str = "", campos: List[Dict[str, Any]] = None):
        """Factory method público para criar NOVOS formulários"""
        if not titulo or not titulo.strip():
            raise ValueError("Título é obrigatório")
        
        # Converte dicionários para objetos CampoFormulario
        campos_objetos = []
        if campos:
            for campo_dict in campos:
                campos_objetos.append(CampoFormulario(
                    nome=campo_dict.get('nome', ''),
                    tipo=campo_dict.get('tipo', 'texto'),
                    obrigatorio=campo_dict.get('obrigatorio', False),
                    opcoes=campo_dict.get('opcoes')
                ))
        
        # Usa __new__ para criar instância sem chamar __init__
        instancia = cls.__new__(cls)
        
        # Configura atributos MANUALMENTE
        instancia.id = str(uuid.uuid4())
        instancia.titulo = titulo
        instancia.descricao = descricao
        instancia.campos = campos_objetos
        instancia.criado_em = datetime.now()
        
        return instancia
    
    @classmethod
    def from_persistence(cls, data: Dict[str, Any]) -> 'Formulario':
        """
        Factory method para criar Formulario a partir de dados PERSISTENTES
        (do banco de dados)
        """
        # Cria instância sem __init__
        instancia = cls.__new__(cls)
        
        # Converte campos de dict para objetos CampoFormulario
        campos_objetos = []
        if data.get('campos'):
            for campo_dict in data['campos']:
                campos_objetos.append(CampoFormulario(
                    nome=campo_dict.get('nome', ''),
                    tipo=campo_dict.get('tipo', 'texto'),
                    obrigatorio=campo_dict.get('obrigatorio', False),
                    opcoes=campo_dict.get('opcoes')
                ))
        
        criado_em = data.get('criado_em')
        if isinstance(criado_em, str):
            criado_em = criado_em.replace('Z', '+00:00')
            criado_em = datetime.fromisoformat(criado_em)
        
        # Configura atributos com dados do banco
        instancia.id = data['id']
        instancia.titulo = data['titulo']
        instancia.descricao = data.get('descricao', '')
        instancia.campos = campos_objetos
        instancia.criado_em = criado_em
        
        return instancia
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Formulario':
        """
        Alternativa: cria a partir de dicionário (para compatibilidade)
        """
        return cls.from_persistence(data)
    
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