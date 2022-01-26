from app import  con


def getUnits(): 
  return con.consultar(''' select
	co_dim_unidade_saude_1 ,
	nu_cnes , 
	no_unidade_saude 
from
	tb_dim_unidade_saude tdus
join (
	select
		co_dim_unidade_saude_1
	from
		tb_fat_atendimento_individual tfai
	group by
		1 ) as tfai on
	tdus.co_seq_dim_unidade_saude = tfai.co_dim_unidade_saude_1    ''', True) 

