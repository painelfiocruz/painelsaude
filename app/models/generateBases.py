
def cadIndividual(con):
  return con.consultar(''' SELECT * FROM tb_fat_cad_individual tfci  ''', True).to_csv( path_or_buf="files/tb_fat_cad_individual.csv", sep=";", decimal = ',',header=True, index=False)

def cadDomiciliar(con):
  return con.consultar(''' SELECT * FROM tb_fat_cad_domiciliar  ''', True).to_csv(path_or_buf="files/tb_fat_cad_domiciliar.csv", sep=";", decimal = ',',header=True, index=False)

def familiaTerritorio(con):
  return con.consultar(''' SELECT * FROM tb_fat_familia_territorio  ''', True).to_csv(path_or_buf="files/tb_fat_familia_territorio.csv", sep=";", decimal = ',',header=True, index=False)

def cidadaoTerritorio(con):
  con.consultar(''' SELECT * FROM tb_fat_cidadao_territorio  ''', True).to_csv(path_or_buf="files/tb_fat_cidadao_territorio.csv", sep=";", decimal = ',',header=True, index=False)
  
def cidadaoPec(con):
  return con.consultar(''' SELECT * FROM tb_fat_cidadao_pec  ''', True).to_csv(path_or_buf="files/tb_fat_cidadao_pec.csv", sep=";", decimal = ',',header=True, index=False)

def atendimentoIndividual(con):
  return con.consultar(''' SELECT * FROM tb_fat_atendimento_individual  ''', True).to_csv(path_or_buf="files/tb_fat_atendimento_individual.csv", sep=";", decimal = ',',header=True, index=False)

def municipio(con):
  return con.consultar(''' SELECT * FROM tb_dim_municipio  ''', True).to_csv(path_or_buf="files/tb_dim_municipio.csv", sep=";", decimal = ',',header=True, index=False)

def unidades(con):
  return con.consultar(''' select co_seq_dim_unidade_saude, nu_cnes, no_unidade_saude from tb_dim_unidade_saude tdus    ''', True).to_csv(path_or_buf="files/tb_dim_unidade_saude.csv", sep=";", decimal = ',',header=True, index=False)



def generateAll(con):
  cadIndividual(con)
  cadDomiciliar(con)
  familiaTerritorio(con)
  cidadaoTerritorio(con)
  cidadaoPec(con)
  atendimentoIndividual(con)
  municipio(con)
  unidades(con)