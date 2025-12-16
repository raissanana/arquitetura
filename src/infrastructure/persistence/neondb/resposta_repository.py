# infrastructure/persistence/neondb/resposta_repository.py
import json
from typing import List
from domain.entities.resposta import Resposta
from domain.repositories.resposta_repository import RespostaRepository
from .database import Database

class NeonDBRespostaRepository(RespostaRepository):
    
    def __init__(self, database: Database):
        self.db = database

    def _parse_json(self, json_field):
        """Converte campo JSON se necessário"""
        if json_field is None:
            return {}
        if isinstance(json_field, (dict, list)):
            return json_field
        if isinstance(json_field, str):
            try:
                return json.loads(json_field)
            except json.JSONDecodeError:
                return {}
        return json_field

    def salvar_resposta(self, resposta: Resposta) -> Resposta:
        conn = self.db._get_connection()
        cur = conn.cursor()
        
        try:
            dados_json = json.dumps(resposta.dados)
            
            cur.execute(
                """INSERT INTO respostas (id, formulario_id, agente_nome, dados, criado_em) 
                   VALUES (%s, %s, %s, %s, %s)""",
                (resposta.id, resposta.formulario_id, resposta.agente_nome, 
                 dados_json, resposta.criado_em)
            )
            
            conn.commit()
            return resposta
            
        except Exception as e:
            conn.rollback()
            raise Exception(f"Erro ao salvar resposta: {e}")
        finally:
            cur.close()
            conn.close()

    def listar_respostas(self) -> List[Resposta]:
        conn = self.db._get_connection()
        cur = conn.cursor()
        
        try:
            cur.execute("""
                SELECT id, formulario_id, agente_nome, dados, criado_em 
                FROM respostas 
                ORDER BY criado_em DESC
            """)
            
            respostas = []
            for row in cur.fetchall():
                dados = self._parse_json(row[3])
                if not isinstance(dados, dict):
                    dados = {}
                
                resposta = Resposta.from_persistence({
                    'id': str(row[0]),
                    'formulario_id': str(row[1]),
                    'agente_nome': row[2] if row[2] else '',
                    'dados': dados,
                    'criado_em': row[4] 
                })
                
                respostas.append(resposta)
        
            return respostas
            
        except Exception as e:
            raise Exception(f"Erro ao listar respostas: {e}")
        finally:
            cur.close()
            conn.close()