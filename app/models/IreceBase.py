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
    # print(self._base)
    return self._base

  def gender(self, _data): 
    gender  = {
      "Masculino": _data[ _data['ds_sexo'] == 'Masculino'].shape[0],
      "Feminino": _data[ _data['ds_sexo'] == 'Feminino'].shape[0]
    }
    return gender
  
  def indicators(self, __data) :
    _data = __data.copy()
    return {
        "Hipertensão": _data[ _data['st_hipertensao'] == 1].shape[0],
        "Diabetes": _data[ _data['st_diabetes'] == 1].shape[0],
        "Gestantes": _data[ _data['st_gestante'] == 1].shape[0]
    }

  def locationArea(self,_data):
    return _data.groupby(['ds_tipo_localizacao']).size().to_dict()

  def ageGroup(self, __data ):
      _data =__data.copy()
      faixaEtaria ={
          "Faixa 1": "Faixa etária 0 a 17 anos",
          "Faixa 2": "Faixa etária 18 a 29 anos",
          "Faixa 3": "Faixa etária 30 a 44 anos",
          "Faixa 4": "Faixa etária 45 a 59 anos",
          "Faixa 5": "Faixa etária 60 + anos",
          "nan":"nan"
      }
      _data['ds_faixa_etaria'] = _data['ds_faixa_etaria'].map(faixaEtaria)
      piramide = pd.DataFrame({'count' : _data.groupby( [ "ds_sexo", "ds_faixa_etaria", "ds_tipo_localizacao"] ).size()}).reset_index()
      result = piramide \
                .groupby('ds_sexo')\
                  .apply(lambda x: 
                          [
                          x.groupby('ds_faixa_etaria').
                            apply( lambda y:
                                    dict( zip(y['ds_tipo_localizacao'], y['count']))
                                  ).to_dict()
                          ]
                        ) \
                .to_dict()
                
      # print( json.dumps(result, indent=4) )
      return result 

  def getDemographicInfo(self):
    return  {
    "IBGEpopulation": 74.050,
    "total": self._base.shape[0],
    "gender":self.gender(self._base),
    "locationArea": self.locationArea(self._base),
    "ageGroups": self.ageGroup(self._base),
    "indicators": self.indicators(self._base)
    }


