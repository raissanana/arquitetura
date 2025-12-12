import json
from typing import List, Optional
from domain.entities.formulario import Formulario
from domain.entities.resposta import Resposta
from domain.repositories.formulario_repository import FormularioRepository
from .database import Database

class NeonDBFormularioRepository(FormularioRepository):
    
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

    def salvar_formulario(self, formulario: Formulario) -> Formulario:
        conn = self.db._get_connection()
        cur = conn.cursor()
        
        try:
            # Converte campos para JSON string
            campos_json = json.dumps([
                {
                    'nome': campo.nome,
                    'tipo': campo.tipo,
                    'obrigatorio': campo.obrigatorio,
                    'opcoes': campo.opcoes
                } for campo in formulario.campos
            ])
            
            cur.execute(
                """INSERT INTO formularios (id, titulo, descricao, campos, criado_em) 
                   VALUES (%s, %s, %s, %s, %s)""",
                (formulario.id, formulario.titulo, formulario.descricao, 
                 campos_json, formulario.criado_em)
            )
            
            conn.commit()
            return formulario
            
        except Exception as e:
            conn.rollback()
            raise Exception(f"Erro ao salvar formulário no NeonDB: {e}")
        finally:
            cur.close()
            conn.close()
    
    def listar_formularios(self) -> List[Formulario]:
        conn = self.db._get_connection()
        cur = conn.cursor()
        
        try:
            cur.execute("""
                SELECT id, titulo, descricao, campos, criado_em 
                FROM formularios 
                ORDER BY criado_em DESC
            """)
            
            formularios = []
            for row in cur.fetchall():
                # Parse JSON dos campos
                campos_data = self._parse_json(row[3])
                if not isinstance(campos_data, list):
                    campos_data = []
                
                formulario = Formulario.from_persistence({
                    'id': str(row[0]),  # Garante que é string
                    'titulo': row[1] if row[1] else '',
                    'descricao': row[2] if row[2] else '',
                    'campos': campos_data,
                    'criado_em': row[4]  # psycopg2 já retorna datetime
                })
                
                formularios.append(formulario)
            
            return formularios
            
        except Exception as e:
            raise Exception(f"Erro ao listar formulários do NeonDB: {e}")
        finally:
            cur.close()
            conn.close()
    

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
            raise Exception(f"Erro ao salvar resposta no NeonDB: {e}")
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
                # Parse JSON dos dados
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
            raise Exception(f"Erro ao listar respostas do NeonDB: {e}")
        finally:
            cur.close()
            conn.close()
    