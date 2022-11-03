"""
  - Introducão ao Unittest (Testes Unitários)
   : módulo unittest
   : Testes unitários é a forma de se testar unidades indivuais do nosso código, quando falamos em
unidades individuais, podem ser : funcões, métodos, classes, módulos, etc. O objetivo do teste uni-
tário é verificar se a unidade está retornando o valor desejável.
   : Quando estamos falando de testes unitários, ñ estamos falando espeficicamente da linguagem Python,
os testes estão ligado a qualidade do software desenvolvido
   : O módulo unittest é super recomendado para testar nossos código pois tem o modo 'pythonico' de
aplicar os testes
   : Para utilizarmos o módulo unittest criamos classes que herdam de unittest.TestCase e a partir
de então ganhamos todos os 'assertions' presentes no módulo. Para rodar utilizamos:
    -> unittest.main()
   : O arquivo de teste faz parte do projeto, mas é um arquivo separado do arquivo principal

   : TestCase
     -> Casos de Testes para sua unidade
     -> Por convencão todos os TextCase deve
     comecar ter seu nome declarado test_NomeDaFuncao

   : CONHECENDO OS assertions
.___________________________________________________.
| MÓDULO :                  |  AVALIA-SE            |
|---------------------------------------------------|
|assertEqual(a, b)          |  a == b               |
|---------------------------------------------------|
|assertNotEqual(a, b)       |  a != b               |
|---------------------------------------------------|
|assertTrue(x)              |  bool(x) is True      |
|---------------------------------------------------|
|assertFalse(x)             |  bool(x) is False     |
|---------------------------------------------------|
|assertIs(a, b)             |  a is b               |
|---------------------------------------------------|
|assertIsNot(a, b)          |  a is not b           |
|---------------------------------------------------|
|assertIsNone(x)            |  x is None            |
|---------------------------------------------------|
|assertIsNotNone(x)         |  x is not None        |
|---------------------------------------------------|
|assertIn(a, b)             |  a in b               |
|---------------------------------------------------|
|assertNotIn(a, b)          |  a not in b           |
|---------------------------------------------------|
|assertIsInstance(a, b)     |  isinstance(a, b)     |
|---------------------------------------------------|
|assertNotIsInstance(a, b)  |  not isinstance(a, b) |
`---------------------------------------------------`
"""

#  Seguindo testes utilizando TDD