
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASIGNACION BULEANO CADENA COMENTARIO DELIMITADOR DIFERENTE_DE ENTERO ENTONCES ENTRE FLOTANTE FUNCION ID IGUAL_A MAYOR_O_IGUAL_QUE MAYOR_QUE MENOR_O_IGUAL_QUE MENOR_QUE MENOS MIENTRAS MULTIPLICACION NUMERO PARA PARENTESIS_DER PARENTESIS_IZQ RESERVED SALTO_LINEA SI SUMAinicio : principalprincipal    : variable_declaracion principal\n                    | variable_asignacion principal\n                    | exp_aritmetica principal\n                    | variable_declaracion\n                    | variable_asignacion \n                    | exp_aritmetica variable_declaracion     : ENTERO ID DELIMITADOR\n                                | FLOTANTE ID DELIMITADOR\n                                | BULEANO ID DELIMITADORvariable_asignacion  : ID ASIGNACION NUMERO DELIMITADOR\n                            | ID ASIGNACION ID DELIMITADORexp_aritmetica   : expresion DELIMITADOR\n                        expresion    : expresion SUMA termino\n                        | expresion MENOS termino\n                        | terminotermino  : termino MULTIPLICACION factor\n                | termino ENTRE factor\n                | factorfactor   : NUMERO \n                | PARENTESIS_IZQ expresion PARENTESIS_DER'
    
_lr_action_items = {'ENTERO':([0,3,4,5,22,28,31,32,38,39,],[6,6,6,6,-13,-8,-9,-10,-12,-11,]),'FLOTANTE':([0,3,4,5,22,28,31,32,38,39,],[8,8,8,8,-13,-8,-9,-10,-12,-11,]),'BULEANO':([0,3,4,5,22,28,31,32,38,39,],[9,9,9,9,-13,-8,-9,-10,-12,-11,]),'ID':([0,3,4,5,6,8,9,19,22,28,31,32,38,39,],[7,7,7,7,18,20,21,29,-13,-8,-9,-10,-12,-11,]),'NUMERO':([0,3,4,5,14,19,22,23,24,25,26,28,31,32,38,39,],[10,10,10,10,10,30,-13,10,10,10,10,-8,-9,-10,-12,-11,]),'PARENTESIS_IZQ':([0,3,4,5,14,22,23,24,25,26,28,31,32,38,39,],[14,14,14,14,14,-13,14,14,14,14,-8,-9,-10,-12,-11,]),'$end':([1,2,3,4,5,15,16,17,22,28,31,32,38,39,],[0,-1,-5,-6,-7,-2,-3,-4,-13,-8,-9,-10,-12,-11,]),'ASIGNACION':([7,],[19,]),'MULTIPLICACION':([10,12,13,33,34,35,36,37,],[-20,25,-19,25,25,-17,-18,-21,]),'ENTRE':([10,12,13,33,34,35,36,37,],[-20,26,-19,26,26,-17,-18,-21,]),'DELIMITADOR':([10,11,12,13,18,20,21,29,30,33,34,35,36,37,],[-20,22,-16,-19,28,31,32,38,39,-14,-15,-17,-18,-21,]),'SUMA':([10,11,12,13,27,33,34,35,36,37,],[-20,23,-16,-19,23,-14,-15,-17,-18,-21,]),'MENOS':([10,11,12,13,27,33,34,35,36,37,],[-20,24,-16,-19,24,-14,-15,-17,-18,-21,]),'PARENTESIS_DER':([10,12,13,27,33,34,35,36,37,],[-20,-16,-19,37,-14,-15,-17,-18,-21,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'principal':([0,3,4,5,],[2,15,16,17,]),'variable_declaracion':([0,3,4,5,],[3,3,3,3,]),'variable_asignacion':([0,3,4,5,],[4,4,4,4,]),'exp_aritmetica':([0,3,4,5,],[5,5,5,5,]),'expresion':([0,3,4,5,14,],[11,11,11,11,27,]),'termino':([0,3,4,5,14,23,24,],[12,12,12,12,12,33,34,]),'factor':([0,3,4,5,14,23,24,25,26,],[13,13,13,13,13,13,13,35,36,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> principal','inicio',1,'p_inicio','Analizador_SINTACTICO_V2.py',6),
  ('principal -> variable_declaracion principal','principal',2,'p_principal','Analizador_SINTACTICO_V2.py',10),
  ('principal -> variable_asignacion principal','principal',2,'p_principal','Analizador_SINTACTICO_V2.py',11),
  ('principal -> exp_aritmetica principal','principal',2,'p_principal','Analizador_SINTACTICO_V2.py',12),
  ('principal -> variable_declaracion','principal',1,'p_principal','Analizador_SINTACTICO_V2.py',13),
  ('principal -> variable_asignacion','principal',1,'p_principal','Analizador_SINTACTICO_V2.py',14),
  ('principal -> exp_aritmetica','principal',1,'p_principal','Analizador_SINTACTICO_V2.py',15),
  ('variable_declaracion -> ENTERO ID DELIMITADOR','variable_declaracion',3,'p_variable_declaracion','Analizador_SINTACTICO_V2.py',18),
  ('variable_declaracion -> FLOTANTE ID DELIMITADOR','variable_declaracion',3,'p_variable_declaracion','Analizador_SINTACTICO_V2.py',19),
  ('variable_declaracion -> BULEANO ID DELIMITADOR','variable_declaracion',3,'p_variable_declaracion','Analizador_SINTACTICO_V2.py',20),
  ('variable_asignacion -> ID ASIGNACION NUMERO DELIMITADOR','variable_asignacion',4,'p_variable_asignacion','Analizador_SINTACTICO_V2.py',27),
  ('variable_asignacion -> ID ASIGNACION ID DELIMITADOR','variable_asignacion',4,'p_variable_asignacion','Analizador_SINTACTICO_V2.py',28),
  ('exp_aritmetica -> expresion DELIMITADOR','exp_aritmetica',2,'p_exp_aritmetica','Analizador_SINTACTICO_V2.py',32),
  ('expresion -> expresion SUMA termino','expresion',3,'p_expresion','Analizador_SINTACTICO_V2.py',37),
  ('expresion -> expresion MENOS termino','expresion',3,'p_expresion','Analizador_SINTACTICO_V2.py',38),
  ('expresion -> termino','expresion',1,'p_expresion','Analizador_SINTACTICO_V2.py',39),
  ('termino -> termino MULTIPLICACION factor','termino',3,'p_termino','Analizador_SINTACTICO_V2.py',43),
  ('termino -> termino ENTRE factor','termino',3,'p_termino','Analizador_SINTACTICO_V2.py',44),
  ('termino -> factor','termino',1,'p_termino','Analizador_SINTACTICO_V2.py',45),
  ('factor -> NUMERO','factor',1,'p_factor','Analizador_SINTACTICO_V2.py',48),
  ('factor -> PARENTESIS_IZQ expresion PARENTESIS_DER','factor',3,'p_factor','Analizador_SINTACTICO_V2.py',49),
]