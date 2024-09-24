from projeto.models.endereco import Endereco
from projeto.models.enum.estadoCivil import EstadoCivil 
from projeto.models.enum.sexo import Sexo
from projeto.models.enum.setor import Setor
from projeto.models.funcionario import Funcionario

class Advogado (Funcionario):
   def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float,oab:str) -> None:
      self.oab= oab
      super().__init__(id,nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario)

   def __str__(self) -> str:
      return super().__str__() + f"\nOAB{self.oab}"
   
   def _Verifica__Id(self,id:int)-> int: 
     return super()._Verifica__Id(id)
   
   def _verifica_salario(self, salario:float)->float:
      return super()._verifica_salario(salario)
   
   
        
   
   

   
      

    