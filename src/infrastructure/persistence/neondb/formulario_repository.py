import json
from typing import List
from domain.entities.formulario import Formulario
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

    def _campos_para_dict(self, campos):
        """Converte lista de CampoFormulario para lista de dicionários"""
        campos_dict = []
        for campo in campos:
            if hasattr(campo, 'to_dict'):  # Se tiver método to_dict()
                campos_dict.append(campo.to_dict())
            elif hasattr(campo, '__dict__'):  # Se for objeto
                campos_dict.append(campo.__dict__)
            elif isinstance(campo, dict):  # Já é dicionário
                campos_dict.append(campo)
            else:  # Outro tipo (string, etc)
                campos_dict.append(campo)
        return campos_dict

    def salvar_formulario(self, formulario: Formulario) -> Formulario:
        conn = self.db._get_connection()
        cur = conn.cursor()
        
        try:
            campos_serializaveis = self._campos_para_dict(formulario.campos)
            campos_json = json.dumps(campos_serializaveis)
            
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
            raise Exception(f"Erro ao salvar formulário: {e}")
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
                campos_data = self._parse_json(row[3])
                if not isinstance(campos_data, list):
                    campos_data = []
                
                formulario = Formulario.from_persistence({
                    'id': str(row[0]),
                    'titulo': row[1] if row[1] else '',
                    'descricao': row[2] if row[2] else '',
                    'campos': campos_data,
                    'criado_em': row[4]
                })
                
                formularios.append(formulario)
            
            return formularios
            
        except Exception as e:
            raise Exception(f"Erro ao listar formulários: {e}")
        finally:
            cur.close()
            conn.close()