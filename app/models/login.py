import datetime
from app import db, ma


class UserLogin(db.Model):
  __tablename__ = ''

  unidadeSaude = db.Column(db.Integer)
  codigoIbge = db.Column(db.String("20"))
  municipio = db.Column(db.String("50"))
  codigoMunicipio = db.Column(db.Integer)
  uf = db.Column(db.String("2"))
  cns = db.Column(db.String("20"))
  cpf = db.Column(db.String("20"), primary_key=True)
  conselhoClasse = db.Column(db.String("20"), nullable=True)
  email = db.Column(db.String("20"), nullable=True)
  nome = db.Column(db.String("50"), nullable=True)

  def __init__(self, unidadeSaude, codigoIbge, municipio, codigoMunicipio,uf,cns, cpf, conselhoClasse, email, nome):
        self.unidadeSaude = unidadeSaude
        self.codigoIbge = codigoIbge
        self.municipio = municipio
        self.codigoMunicipio = codigoMunicipio
        self.uf = uf
        self.cns = cns
        self.cpf = cpf
        self.conselhoClasse = conselhoClasse
        self.email = email
        self.nome = nome
  

class LoginSchema(ma.Schema):
    class Meta:
        fields = ('unidadeSaude', 'municipio', 'cpf', 'email', 'nome')


login_schema = LoginSchema()
logins_schema = LoginSchema(many=True)
