import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.DEBUG)

def singleton(cls):
    instances = {}
    def instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return instance

@singleton    
class IreceBase:
  _instance = {}
  _base = None

  def __init__(self):
    self._instance = None
  
  def getBase(self) :
    if self._base is None:
      logging.info('Loading the final data base')
      self._base = pd.read_excel('files/CADASTRO_MESTRE_JOIN_AT_IND_GEST_HIP_DIAB_JOIN_UNIDADES_CLEAN_PAINEL.xlsx')
      logging.info('Base loaded')
    print(self._base)
    return self._base

  def countGender(self): 

    gender  = {
      "Masculino": self._base[ self._base['ds_sexo'] == 'Masculino'].shape[0],
      "Feminino": self._base[ self._base['ds_sexo'] == 'Feminino'].shape[0]
    }
    return gender
  
