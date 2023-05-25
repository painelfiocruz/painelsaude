import logging
import pandas as pd
import numpy as np
import collections
from ..helpers.str import treatNames, strToData
logging.basicConfig(level=logging.DEBUG)
from datetime import datetime
from dateutil.relativedelta import relativedelta

def singleton(cls):
    instances = {}

    def instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return instance


def extractLastYearDate(_data):
  _lastDate = _data["co_dim_tempo"]
  lastDate = _lastDate.max()  
  lastYear = lastDate - relativedelta(years=1)
  return ( lastYear, lastDate )

def filterLastYear( data):
    (lastYear, lastDate) = extractLastYearDate(data)
    return data[ (data['co_dim_tempo'] >= lastYear) & (data['co_dim_tempo'] <= lastDate) ]


class BaseEntity:

  def findByCnes(self, nu_cnes = None):
    _data = self.getBase()
    if nu_cnes is not None:
      mask = _data['nu_cnes'].str.startswith( f'{nu_cnes},', na=False)
      _data =  _data[mask]
    return _data

@singleton
class ArterialHypertensionBase(BaseEntity):
  _instance = {}
  _base = None

  def __init__(self):
    super().__init__()
    self._instance = None

  def getBase(self):
    if self._base is None:
      logging.info('Loading the pregnants final data base')
      self._base = pd.read_excel(
          'files/BASE_ATENDIMENTOS_X_HIPERTENSAO.xlsx', engine='openpyxl')
      logging.info('Base loaded')
    # print(self._base)
    return self._base


@singleton
class DiabetesBase(BaseEntity):
  _instance = {}
  _base = None

  def __init__(self):
    super().__init__()
    self._instance = None

  def getBase(self):
    if self._base is None:
      logging.info('Loading the pregnants final data base')
      self._base = pd.read_excel(
          'files/BASE_ATENDIMENTOS_X_DIABETICOS.xlsx', engine='openpyxl')
      logging.info('Base loaded')
    # print(self._base)
    return self._base