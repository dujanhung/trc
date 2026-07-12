import sys
import argparse
import re
from rich import print
URL_DOC='https://dujanhung.github.com/trc/blob/doc.md'
ARG_META={
 'description':'💱 convert files via regular expression.',
 'epilog':'📖 see full TRC doc at:'+' 🔗 '+URL_DOC
}
ARG_FLAG={
 '-t':{
  'help':'💱 path to the TRC file.',
  'default':'t.trc',
  'required':True
 },
 '-i':{
  'help':'📥 path to the input file.',
  'default':'i.txt',
  'required':True
 },
 '-o':{
  'help':'📤 path to the output file.',
  'default':'o.txt',
  'required':True
 }
}
CHAR_M=':=:'
CHAR_DELIM=':&:'
MODE_PRETTY=True
class Arg_Parser:
 def __init__(self):
  self.arg_meta=ARG_META
  self.arg_flag=ARG_FLAG
 def parse(self)->argparse.Namespace:
  p=argparse.ArgumentParser(description=self.arg_meta['description'],epilog=self.arg_meta['epilog'])
  for i in list(self.arg_flag.keys()):
   p.add_argument(i,type=str,default=self.arg_flag[i]['default'],required=self.arg_flag[i]['required'],help=self.arg_flag[i]['help'])
  s=sys.argv
  s.pop(0)
  return p.parse_args(s)
class File_Access:
 def __init__(self):
  self
 def load_file(self,path:str)->str:
  o=''
  with open(path,'r',encoding='utf-8') as f:
   o=f.read()
  return o
 def save_file(self,path:str,data:str)->None:
  with open(path,'w',encoding='utf-8') as f:
   f.write(data)
class Pattern_DB:
 def __init__(self):
  self
 def compile_spam1(self,M:str)->re.Pattern:
  return re.compile(rf'{M}+',re.M)
 def compile_spam2(self,M:str)->re.Pattern:
  return re.compile(rf'{M}(\s+{M})+',re.S)
class TRC_Formatter:
 def __init__(self):
  self
 def run(self,data_t:str)->str:
  o=data_t
  db=Pattern_DB()
  for i in [CHAR_DELIM,CHAR_M]:
   for j in [db.compile_spam1(i),db.compile_spam2(i)]:
    o=j.sub(i,o)
    o=o.strip()
   o=o.removeprefix(i).removesuffix(i)
   o=o.strip()
  oo=[]
  for i in o.split(CHAR_DELIM):
   ii=i.strip()
   if CHAR_M in ii:
    L,M,R=ii.partition(CHAR_M)
    if MODE_PRETTY:
     ooo=L.strip()+'\n'+M+'\n'+R.strip()
    else:
     ooo=L.strip()+M+R.strip()
    oo.append(ooo)
   else:
    oo.append(ii)
  if MODE_PRETTY:
   o=('\n'+CHAR_DELIM+'\n').join(oo)
   o=o.strip()
  else:
   o=CHAR_DELIM.join(oo)
  return o
class TRC_Handler:
 def __init__(self,data_t:str,data_i:str):
  self.data_t=data_t
  self.data_i=data_i
 def run(self)->str:
  o=self.data_i
  for i in self.data_t.split(CHAR_DELIM):
   ii=i.strip()
   if CHAR_M in ii:
    L,M,R=ii.partition(CHAR_M)
    L=L.strip()
    R=R.strip()
   else:
    L=ii
    R=''
   o=re.sub(rf'{L}',rf'{R}',o)
   o=o.strip()
  return o
def main()->None:
 p=Arg_Parser().parse()
 f=File_Access()
 t=f.load_file(p.t)
 i=f.load_file(p.i)
 f.save_file(p.o,'')
 clt=TRC_Formatter().run(t)
 f.save_file(p.t,clt)
 o=TRC_Handler(clt,i).run()
 f.save_file(p.o,o)
 print(clt)
 print(i)
 print(o)
main()