from dataclasses import dataclass
from typing import List, Dict, Any

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