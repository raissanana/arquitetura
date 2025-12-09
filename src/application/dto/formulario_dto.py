from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class CriarFormularioInputDTO:
    titulo: str
    descricao: str = ""
    campos: List[Dict[str, Any]] = None

@dataclass
class CriarFormularioOutputDTO:
    id: str
    titulo: str
    criado_em: str

@dataclass
class ListarFormulariosOutputDTO:
    formularios: List[Dict[str, Any]]

@dataclass
class CriarRespostaInputDTO:
    formulario_id: str
    dados: Dict[str, Any]
    agente_nome: str = ""

@dataclass
class CriarRespostaOutputDTO:
    id: str
    formulario_id: str
    criado_em: str

@dataclass
class ListarRespostasOutputDTO:
    respostas: List[Dict[str, Any]]