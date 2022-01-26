import pandas as pd
import numpy as np
from ..models.generateBases import  cadIndividual, familiaTerritorio, cadDomiciliar, cidadaoTerritorio, cidadaoPec

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def criarCadastroMestre(con):
        
    # cidadao_pec = pd.read_csv('../../files/tb_fat_cidadao_pec_202011181154.csv',sep=';',engine='python', decimal = ',',keep_default_na=False)
    # cidadao_territorio = pd.read_csv('../../files/tb_fat_cidadao_territorio_202011181154.csv',sep=';',engine='python', decimal = ',')
    # familia_territorio = pd.read_csv('../../files/tb_fat_familia_territorio_202011181154.csv',sep=';',engine='python', decimal = ',')
    # cad_domiciliar = pd.read_csv('../../files/tb_fat_cad_domiciliar.csv',sep=';',engine='python', decimal = ',')
    # cad_individual = pd.read_csv('../../files/tb_fat_cad_individual.csv',sep=';',engine='python', decimal = ',')
    cad_individual =  cadIndividual( con)
    cad_domiciliar = cadDomiciliar(con)
    familia_territorio = familiaTerritorio(con)
    cidadao_territorio = cidadaoTerritorio(con)
    cidadao_pec = cidadaoPec(con)

    cad_individual_SELECTED = cad_individual[['co_seq_fat_cad_individual','nu_cns','dt_nascimento','co_dim_unidade_saude','co_dim_equipe','co_dim_tempo','co_dim_sexo',
            'co_dim_raca_cor','co_dim_nacionalidade','nu_cns_responsavel','st_responsavel_familiar',
            'st_frequenta_creche','st_plano_saude_privado','st_deficiencia','st_defi_auditiva','st_defi_intelectual_cognitiva','st_defi_outra','st_defi_visual',
            'st_defi_fisica','st_gestante','st_doenca_respiratoria','st_doenca_respira_asma','st_doenca_respira_dpoc_enfisem','st_doenca_respira_outra',
            'st_doenca_respira_n_sabe','st_fumante','st_alcool','st_outra_droga','st_hipertensao_arterial','st_diabete','st_avc','st_infarto','st_hanseniase',
            'st_tuberculose','st_cancer','st_internacao_12','st_tratamento_psiquiatra','st_acamado','st_domiciliado','st_doenca_cardiaca',
            'st_doenca_card_insuficiencia','st_problema_rins','st_problema_rins_insuficiencia','st_morador_rua','co_dim_tipo_parentesco',
            'co_dim_tipo_escolaridade','co_dim_situacao_trabalho','co_dim_tipo_orientacao_sexual','co_dim_tipo_condicao_peso','co_dim_tempo_morador_rua',
            'co_dim_etnia','co_dim_identidade_genero','co_dim_faixa_etaria','nu_micro_area','co_fat_cidadao_pec','co_fat_cidadao_pec_responsvl',
            'nu_cpf_cidadao','nu_cpf_responsavel']]
    cad_individual_SELECTED.shape

    cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'co_dim_unidade_saude': 'co_dim_unidade_saude_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'co_dim_equipe': 'co_dim_equipe_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'dt_nascimento': 'dt_nascimento_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'co_dim_faixa_etaria': 'co_dim_faixa_etaria_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'co_dim_sexo': 'co_dim_sexo_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'nu_cns': 'nu_cns_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'co_dim_identidade_genero': 'co_dim_identidade_genero_CI'})
    cad_individual_SELECTED = cad_individual_SELECTED.rename(columns={'nu_cpf_cidadao': 'nu_cpf_cidadao_CI'})

    cidadao_pec_SELECTED = cidadao_pec.drop(columns=['co_cidadao','no_social_cidadao','nu_telefone_celular','st_faleceu','st_lookup_etl','st_deletar'])
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_seq_fat_cidadao_pec':'co_fat_cidadao_pec'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'nu_cns': 'nu_cns_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_dim_unidade_saude_vinc': 'co_dim_unidade_saude_vinc_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_dim_equipe_vinc': 'co_dim_equipe_vinc_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_dim_sexo': 'co_dim_sexo_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_dim_equipe_vinc': 'co_dim_equipe_vinc_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_dim_identidade_genero': 'co_dim_identidade_genero_CP'})
    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'nu_cpf_cidadao': 'nu_cpf_cidadao_CP'})

    cidadao_territorio_SELECTED = cidadao_territorio.drop(columns=['co_dim_equipe','nu_micro_area',
                                                                                'st_responsavel','st_responsavel_informado','st_mudou_se','st_vivo',
                                                                                'st_responsavel_com_fci','st_cns_null','st_cidadao_consistente',
                                                                                'co_fat_ciddo_terrtrio_resp','st_processado_cidadao_respnsvl'])

    cidadao_territorio_SELECTED = cidadao_territorio_SELECTED.rename(columns={'co_fat_familia_territorio':'co_seq_fat_familia_territorio'})

    columns = ['co_seq_fat_familia_territorio','co_fat_cidadao_pec','co_fat_cad_domiciliar','nu_prontuario','co_fat_cidadao_territorio']
    familia_territorio_SELECTED = pd.DataFrame(familia_territorio, columns=columns)

    columns = ['co_seq_fat_cad_domiciliar','co_dim_unidade_saude','co_dim_equipe','co_dim_tempo','qt_morador','nu_comodo','co_dim_tipo_imovel',
            'co_dim_tipo_logradouro','co_dim_tipo_situacao_moradia','co_dim_tipo_localizacao','co_dim_tipo_domicilio','co_dim_tipo_posse_terra',
            'co_dim_tipo_acesso_domicilio','co_dim_tipo_material_parede','co_dim_tipo_abastecimento_agua','co_dim_tipo_tratamento_agua',
            'co_dim_tipo_escoamento_sanitar','co_dim_tipo_destino_lixo','st_disp_energia','st_animal_domiciliar','nu_micro_area','ds_filtro_tipo_renda_familiar']
    cad_domiciliar_SELECTED = pd.DataFrame(cad_domiciliar, columns=columns)

    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(columns={'co_dim_unidade_saude': 'co_dim_unidade_saude_CD'})
    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(columns={'co_dim_equipe': 'co_dim_equipe_CD'})
    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(columns={'co_dim_tempo': 'co_dim_tempo_CD'})
    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(columns={'nu_micro_area': 'nu_micro_area_CD'})

    print(cad_domiciliar_SELECTED.shape)

    cad_individual_SELECTED ['co_dim_tempo_CI'] = pd.to_datetime(cad_individual_SELECTED ['co_dim_tempo'].astype(str), format='%Y%m%d')
    cad_individual_SELECTED_group = cad_individual_SELECTED.groupby(
    ['co_fat_cidadao_pec'],as_index=False
    ).agg(
        {
            'co_dim_tempo_CI': 'max',  # get the first date per group
        }
    )
    cad_individual_merge = pd.merge(cad_individual_SELECTED, cad_individual_SELECTED_group, how="right", on=['co_fat_cidadao_pec', 'co_dim_tempo_CI'])

    # To keep discard the duplicated row with a condition to keep only those with an higher amount of CPF
    cad_individual_merge = cad_individual_merge.sort_values('nu_cpf_cidadao_CI',ascending=True).drop_duplicates(subset=['co_fat_cidadao_pec', 'co_dim_tempo_CI'],keep = 'last')

    cidadao_pec_SELECTED = cidadao_pec_SELECTED.rename(columns={'co_seq_fat_cidadao_pec': 'co_fat_cidadao_pec'})

    cidadao_territorio_SELECTED_group = cidadao_territorio_SELECTED.groupby(
    ['co_fat_cidadao_pec'],as_index=False
    ).agg(
        {
            'co_seq_fat_cidadao_territorio': 'max',  # get the first date per group
        }
    )

    cidadao_territorio_merge = pd.merge(cidadao_territorio_SELECTED, cidadao_territorio_SELECTED_group, how="right", on=['co_fat_cidadao_pec', 'co_seq_fat_cidadao_territorio'])

    familia_territorio_SELECTED = familia_territorio_SELECTED.rename(columns={'co_seq_fat_familia_territorio': 'co_fat_familia_territorio'})

    familia_territorio_SELECTED = familia_territorio_SELECTED.rename(columns={'co_fat_cidadao_pec': 'co_fat_cidadao_pec_FT'})

    cad_domiciliar_SELECTED['co_dim_tempo_CD'] = pd.to_datetime(cad_domiciliar_SELECTED['co_dim_tempo_CD'].astype(str), format='%Y%m%d')
    cad_domiciliar_SELECTED = cad_domiciliar_SELECTED.rename(columns={'co_seq_fat_cad_domiciliar': 'co_fat_cad_domiciliar'})

    cad_domiciliar_SELECTED_group = cad_domiciliar_SELECTED.groupby(
    ['co_fat_cad_domiciliar'],as_index=False
    ).agg(
        {
            'co_dim_tempo_CD': 'max',  # get the first date per group
        }
    )
    cad_domiciliar_merge = pd.merge(cad_domiciliar_SELECTED, cad_domiciliar_SELECTED_group, how="right", on=['co_fat_cad_domiciliar', 'co_dim_tempo_CD'])

    linkage_A = cidadao_pec_SELECTED.merge(cad_individual_merge, on='co_fat_cidadao_pec', how='left', indicator=True)

    linkage_A = linkage_A.rename (columns={'_merge': '_mergeA'})

    linkage_B = linkage_A.merge(cidadao_territorio_merge, on='co_fat_cidadao_pec', how='left', indicator=True)

    linkage_B = linkage_B.rename (columns={'_merge': '_mergeB'})

    linkage_B = linkage_B.rename (columns={'co_seq_fat_familia_territorio': 'co_fat_familia_territorio'})

    linkage_C = linkage_B.merge(familia_territorio_SELECTED, on='co_fat_familia_territorio', how='left', indicator=True)

    linkage_C = linkage_C.rename (columns={'_merge': '_mergeC'})

    linkage_D = linkage_C.merge(cad_domiciliar_merge, on='co_fat_cad_domiciliar', how='left', indicator=True)

    Cadastro_Mestre_Pessoas = linkage_D

    Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CI'] = Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CI'].astype(str)

    Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas.assign(**{
        'CO_DIM_IDENTIDADE_GENERO': Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CI'].mask(
            lambda x: x == 'nan', Cadastro_Mestre_Pessoas['co_dim_identidade_genero_CP'])})

    Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO']=pd.to_numeric(Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO'])
    Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO']=Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO'].astype(str)
    Cadastro_Mestre_Pessoas_MERGE['CO_DIM_IDENTIDADE_GENERO'].value_counts()

    Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CI'] = Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CI'].astype(str)
    Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CI'].value_counts()

    Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.assign(**{
        'CO_DIM_SEXO': Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CI'].mask(
            lambda x: x == 'nan', Cadastro_Mestre_Pessoas_MERGE['co_dim_sexo_CP'])})

    Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO']=pd.to_numeric(Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO'])
    Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO']=Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO'].astype(str)
    Cadastro_Mestre_Pessoas_MERGE['CO_DIM_SEXO'].value_counts()

    Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.drop(columns=['co_fat_cidadao_pec_FT'])

    # Cadastro_Mestre_Pessoas_MERGE['nu_cns_CI'] = Cadastro_Mestre_Pessoas_MERGE['nu_cns_CI'].astype('Int64')
    Cadastro_Mestre_Pessoas_MERGE['nu_cns_CI'].value_counts()

    # merge same column of two dataframe in only 1
    Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.assign(**{
        'NU_CNS': Cadastro_Mestre_Pessoas_MERGE['nu_cns_CP'].mask(
            lambda x: x == '', Cadastro_Mestre_Pessoas_MERGE['nu_cns_CI'])})

    Cadastro_Mestre_Pessoas_MERGE['nu_cpf_cidadao_CI'] = Cadastro_Mestre_Pessoas_MERGE['nu_cpf_cidadao_CI'].astype('str')
    Cadastro_Mestre_Pessoas_MERGE['nu_cpf_cidadao_CI'] = Cadastro_Mestre_Pessoas_MERGE['nu_cpf_cidadao_CI'].apply(lambda x: x.zfill(11))
    Cadastro_Mestre_Pessoas_MERGE['nu_cpf_cidadao_CI'].value_counts()

    # merge same column of two dataframe in only 1
    Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.assign(**{
        'NU_CPF': Cadastro_Mestre_Pessoas_MERGE['nu_cpf_cidadao_CP'].mask(
            lambda x: x == '', Cadastro_Mestre_Pessoas_MERGE['nu_cpf_cidadao_CI'])})

    Cadastro_Mestre_Pessoas_MERGE['co_dim_tempo_nascimento'] = pd.to_datetime(Cadastro_Mestre_Pessoas_MERGE['co_dim_tempo_nascimento'].astype(str), format='%Y-%m-%d',errors='coerce')
    Cadastro_Mestre_Pessoas_MERGE['co_dim_tempo_nascimento'].isnull().sum()

    Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'] = pd.to_datetime(Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'].astype(str), format='%Y-%m-%d',errors='coerce')
    Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'].fillna(pd.NaT, inplace=True)

    # merge same column of two dataframe in only 1
    Cadastro_Mestre_Pessoas_MERGE = Cadastro_Mestre_Pessoas_MERGE.assign(**{
        'DT_NASCIMENTO': Cadastro_Mestre_Pessoas_MERGE['dt_nascimento_CI'].mask(
            lambda x: x == 'NaT', Cadastro_Mestre_Pessoas_MERGE['co_dim_tempo_nascimento'])})


    Cadastro_Mestre_Pessoas_MERGE.to_excel('files/IRECE_CADASTRO_MESTRE_PESSOAS.xlsx')        