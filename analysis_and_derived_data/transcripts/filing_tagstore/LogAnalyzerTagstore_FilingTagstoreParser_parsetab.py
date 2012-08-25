
# LogAnalyzerTagstore_FilingTagstoreParser_parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xf1e\xb7{\x88x\n\x10c\xb2\xb5\x96\x1eOU\xbd'
    
_lr_action_items = {'ENDCOMMENT':([28,30,33,35,37,39,81,83,85,87,89,91,],[48,53,54,55,56,57,97,98,99,100,101,102,]),'TAGDEFAULT':([43,],[62,]),'WORD':([9,11,12,14,49,50,51,52,],[17,20,22,25,68,70,72,74,]),'ENDFACILITATOR':([45,47,93,95,],[66,67,103,104,]),'TIMESTAMP':([0,3,4,7,10,17,18,20,21,22,23,24,25,26,27,29,31,32,34,36,38,40,41,42,44,46,48,53,54,55,56,57,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,84,86,88,90,92,94,96,97,98,99,100,101,102,103,104,],[1,5,5,5,19,28,30,33,35,37,39,43,45,47,-18,-17,-6,-10,-9,-14,-13,43,5,43,-22,-21,-19,-20,-11,-12,-15,-16,-41,-42,43,43,-47,43,-7,-8,81,83,85,87,89,91,93,95,43,-45,-46,-44,-36,-35,-28,-27,-32,-31,-40,-39,-43,-33,-34,-25,-26,-29,-30,-37,-38,]),'STARTTAGGINGTASK':([1,],[3,]),'ENDINSPECTION':([19,],[31,]),'NUMBER':([13,61,],[24,76,]),'BEGININSPECTION':([5,43,],[10,10,]),'ENDOFTAGGING':([43,],[64,]),'BEGINCOMMENTTP':([5,28,30,33,35,37,39,43,45,47,81,83,85,87,89,91,93,95,],[9,49,49,49,49,49,49,9,49,49,49,49,49,49,49,49,49,49,]),'BEGINCOMMENTFACILITATOR':([5,28,30,33,35,37,39,43,45,47,81,83,85,87,89,91,93,95,],[11,50,50,50,50,50,50,11,50,50,50,50,50,50,50,50,50,50,]),'BEGINCOMMENTLOGGER':([5,28,30,33,35,37,39,43,45,47,81,83,85,87,89,91,93,95,],[12,51,51,51,51,51,51,12,51,51,51,51,51,51,51,51,51,51,]),'TAGPROPOSED':([43,],[65,]),'WORDS':([9,11,12,14,49,50,51,52,],[18,21,23,26,69,71,73,75,]),'TAGCOMPLETION':([43,],[63,]),'MOVEFILETOTAGSTOREDRIVE':([5,],[13,]),'BEGINFACILITATOR':([5,28,30,33,35,37,39,43,45,47,81,83,85,87,89,91,93,95,],[14,52,52,52,52,52,52,14,52,52,52,52,52,52,52,52,52,52,]),'ENDTAGGINGTASK':([5,],[15,]),'ASSIGNTAGS':([43,],[61,]),'$end':([2,6,8,15,16,59,],[0,-1,-4,-3,-5,-2,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'multiplecomments':([17,18,20,21,22,23,25,26,68,69,70,71,72,73,74,75,],[27,29,32,34,36,38,44,46,80,82,84,86,88,90,92,94,]),'distractions':([3,4,7,24,40,41,42,62,63,65,76,],[4,4,4,40,40,4,40,40,40,40,40,]),'filemgt':([3,4,7,41,],[6,8,16,59,]),'tagstore_storage_task':([0,],[2,]),'commentdistractions':([3,4,7,24,40,41,42,62,63,65,76,],[7,7,7,42,42,7,42,42,42,42,42,]),'tagging':([24,40,42,62,63,65,76,],[41,58,60,77,78,79,96,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> tagstore_storage_task","S'",1,None,None,None),
  ('tagstore_storage_task -> TIMESTAMP STARTTAGGINGTASK filemgt','tagstore_storage_task',3,'p_expression_task_tagstore_storage','../scripts/LogAnalyzerTagstore.py',415),
  ('filemgt -> TIMESTAMP MOVEFILETOTAGSTOREDRIVE NUMBER tagging filemgt','filemgt',5,'p_expression_filemgt','../scripts/LogAnalyzerTagstore.py',589),
  ('filemgt -> TIMESTAMP ENDTAGGINGTASK','filemgt',2,'p_expression_filemgt','../scripts/LogAnalyzerTagstore.py',590),
  ('filemgt -> distractions filemgt','filemgt',2,'p_expression_filemgt','../scripts/LogAnalyzerTagstore.py',591),
  ('filemgt -> commentdistractions filemgt','filemgt',2,'p_expression_filemgt','../scripts/LogAnalyzerTagstore.py',592),
  ('distractions -> TIMESTAMP BEGININSPECTION TIMESTAMP ENDINSPECTION','distractions',4,'p_expression_distractions','../scripts/LogAnalyzerTagstore.py',624),
  ('distractions -> TIMESTAMP BEGINFACILITATOR WORD TIMESTAMP ENDFACILITATOR','distractions',5,'p_expression_distractions','../scripts/LogAnalyzerTagstore.py',625),
  ('distractions -> TIMESTAMP BEGINFACILITATOR WORDS TIMESTAMP ENDFACILITATOR','distractions',5,'p_expression_distractions','../scripts/LogAnalyzerTagstore.py',626),
  ('commentdistractions -> TIMESTAMP BEGINCOMMENTFACILITATOR WORDS multiplecomments','commentdistractions',4,'p_expression_commentdistractions','../scripts/LogAnalyzerTagstore.py',657),
  ('commentdistractions -> TIMESTAMP BEGINCOMMENTFACILITATOR WORD multiplecomments','commentdistractions',4,'p_expression_commentdistractions','../scripts/LogAnalyzerTagstore.py',658),
  ('commentdistractions -> TIMESTAMP BEGINCOMMENTFACILITATOR WORD TIMESTAMP ENDCOMMENT','commentdistractions',5,'p_expression_commentdistractions','../scripts/LogAnalyzerTagstore.py',659),
  ('commentdistractions -> TIMESTAMP BEGINCOMMENTFACILITATOR WORDS TIMESTAMP ENDCOMMENT','commentdistractions',5,'p_expression_commentdistractions','../scripts/LogAnalyzerTagstore.py',660),
  ('commentdistractions -> TIMESTAMP BEGINCOMMENTLOGGER WORDS multiplecomments','commentdistractions',4,'p_expression_commentdistractions','../scripts/LogAnalyzerTagstore.py',661),
  ('commentdistractions -> TIMESTAMP BEGINCOMMENTLOGGER WORD multiplecomments','commentdistractions',4,'p_expression_commentdistractions','../scripts/LogAnalyzerTagstore.py',662),
  ('commentdistractions -> TIMESTAMP BEGINCOMMENTLOGGER WORD TIMESTAMP ENDCOMMENT','commentdistractions',5,'p_expression_commentdistractions','../scripts/LogAnalyzerTagstore.py',663),
  ('commentdistractions -> TIMESTAMP BEGINCOMMENTLOGGER WORDS TIMESTAMP ENDCOMMENT','commentdistractions',5,'p_expression_commentdistractions','../scripts/LogAnalyzerTagstore.py',664),
  ('commentdistractions -> TIMESTAMP BEGINCOMMENTTP WORDS multiplecomments','commentdistractions',4,'p_expression_commentdistractions','../scripts/LogAnalyzerTagstore.py',665),
  ('commentdistractions -> TIMESTAMP BEGINCOMMENTTP WORD multiplecomments','commentdistractions',4,'p_expression_commentdistractions','../scripts/LogAnalyzerTagstore.py',666),
  ('commentdistractions -> TIMESTAMP BEGINCOMMENTTP WORD TIMESTAMP ENDCOMMENT','commentdistractions',5,'p_expression_commentdistractions','../scripts/LogAnalyzerTagstore.py',667),
  ('commentdistractions -> TIMESTAMP BEGINCOMMENTTP WORDS TIMESTAMP ENDCOMMENT','commentdistractions',5,'p_expression_commentdistractions','../scripts/LogAnalyzerTagstore.py',668),
  ('commentdistractions -> TIMESTAMP BEGINFACILITATOR WORDS multiplecomments','commentdistractions',4,'p_expression_commentdistractions','../scripts/LogAnalyzerTagstore.py',669),
  ('commentdistractions -> TIMESTAMP BEGINFACILITATOR WORD multiplecomments','commentdistractions',4,'p_expression_commentdistractions','../scripts/LogAnalyzerTagstore.py',670),
  ('commentdistractions -> TIMESTAMP BEGINFACILITATOR WORD TIMESTAMP ENDFACILITATOR','commentdistractions',5,'p_expression_commentdistractions','../scripts/LogAnalyzerTagstore.py',671),
  ('commentdistractions -> TIMESTAMP BEGINFACILITATOR WORDS TIMESTAMP ENDFACILITATOR','commentdistractions',5,'p_expression_commentdistractions','../scripts/LogAnalyzerTagstore.py',672),
  ('multiplecomments -> TIMESTAMP BEGINCOMMENTFACILITATOR WORD TIMESTAMP ENDCOMMENT','multiplecomments',5,'p_expression_multiplecomments','../scripts/LogAnalyzerTagstore.py',688),
  ('multiplecomments -> TIMESTAMP BEGINCOMMENTFACILITATOR WORDS TIMESTAMP ENDCOMMENT','multiplecomments',5,'p_expression_multiplecomments','../scripts/LogAnalyzerTagstore.py',689),
  ('multiplecomments -> TIMESTAMP BEGINCOMMENTFACILITATOR WORDS multiplecomments','multiplecomments',4,'p_expression_multiplecomments','../scripts/LogAnalyzerTagstore.py',690),
  ('multiplecomments -> TIMESTAMP BEGINCOMMENTFACILITATOR WORD multiplecomments','multiplecomments',4,'p_expression_multiplecomments','../scripts/LogAnalyzerTagstore.py',691),
  ('multiplecomments -> TIMESTAMP BEGINCOMMENTLOGGER WORD TIMESTAMP ENDCOMMENT','multiplecomments',5,'p_expression_multiplecomments','../scripts/LogAnalyzerTagstore.py',692),
  ('multiplecomments -> TIMESTAMP BEGINCOMMENTLOGGER WORDS TIMESTAMP ENDCOMMENT','multiplecomments',5,'p_expression_multiplecomments','../scripts/LogAnalyzerTagstore.py',693),
  ('multiplecomments -> TIMESTAMP BEGINCOMMENTLOGGER WORDS multiplecomments','multiplecomments',4,'p_expression_multiplecomments','../scripts/LogAnalyzerTagstore.py',694),
  ('multiplecomments -> TIMESTAMP BEGINCOMMENTLOGGER WORD multiplecomments','multiplecomments',4,'p_expression_multiplecomments','../scripts/LogAnalyzerTagstore.py',695),
  ('multiplecomments -> TIMESTAMP BEGINCOMMENTTP WORD TIMESTAMP ENDCOMMENT','multiplecomments',5,'p_expression_multiplecomments','../scripts/LogAnalyzerTagstore.py',696),
  ('multiplecomments -> TIMESTAMP BEGINCOMMENTTP WORDS TIMESTAMP ENDCOMMENT','multiplecomments',5,'p_expression_multiplecomments','../scripts/LogAnalyzerTagstore.py',697),
  ('multiplecomments -> TIMESTAMP BEGINCOMMENTTP WORDS multiplecomments','multiplecomments',4,'p_expression_multiplecomments','../scripts/LogAnalyzerTagstore.py',698),
  ('multiplecomments -> TIMESTAMP BEGINCOMMENTTP WORD multiplecomments','multiplecomments',4,'p_expression_multiplecomments','../scripts/LogAnalyzerTagstore.py',699),
  ('multiplecomments -> TIMESTAMP BEGINFACILITATOR WORD TIMESTAMP ENDFACILITATOR','multiplecomments',5,'p_expression_multiplecomments','../scripts/LogAnalyzerTagstore.py',700),
  ('multiplecomments -> TIMESTAMP BEGINFACILITATOR WORDS TIMESTAMP ENDFACILITATOR','multiplecomments',5,'p_expression_multiplecomments','../scripts/LogAnalyzerTagstore.py',701),
  ('multiplecomments -> TIMESTAMP BEGINFACILITATOR WORDS multiplecomments','multiplecomments',4,'p_expression_multiplecomments','../scripts/LogAnalyzerTagstore.py',702),
  ('multiplecomments -> TIMESTAMP BEGINFACILITATOR WORD multiplecomments','multiplecomments',4,'p_expression_multiplecomments','../scripts/LogAnalyzerTagstore.py',703),
  ('tagging -> distractions tagging','tagging',2,'p_expression_tagging','../scripts/LogAnalyzerTagstore.py',715),
  ('tagging -> commentdistractions tagging','tagging',2,'p_expression_tagging','../scripts/LogAnalyzerTagstore.py',716),
  ('tagging -> TIMESTAMP ASSIGNTAGS NUMBER tagging','tagging',4,'p_expression_tagging','../scripts/LogAnalyzerTagstore.py',717),
  ('tagging -> TIMESTAMP TAGPROPOSED tagging','tagging',3,'p_expression_tagging','../scripts/LogAnalyzerTagstore.py',718),
  ('tagging -> TIMESTAMP TAGDEFAULT tagging','tagging',3,'p_expression_tagging','../scripts/LogAnalyzerTagstore.py',719),
  ('tagging -> TIMESTAMP TAGCOMPLETION tagging','tagging',3,'p_expression_tagging','../scripts/LogAnalyzerTagstore.py',720),
  ('tagging -> TIMESTAMP ENDOFTAGGING','tagging',2,'p_expression_tagging','../scripts/LogAnalyzerTagstore.py',721),
]