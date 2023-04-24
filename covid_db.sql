-- Criando a tabela DimensaoData
CREATE TABLE DimensaoData (
  idData INT NOT NULL AUTO_INCREMENT,
  data DATE NOT NULL,
  ano INT NOT NULL,
  mes INT NOT NULL,
  dia INT NOT NULL,
  semana INT NOT NULL,
  trimestre INT NOT NULL,
  semestre INT NOT NULL,
  PRIMARY KEY (idData)
);

-- Criando a tabela DimensaoLocal
CREATE TABLE DimensaoLocal (
  idLocal INT NOT NULL AUTO_INCREMENT,
  cidade VARCHAR(50) NOT NULL,
  estado VARCHAR(2) NOT NULL,
  regiao VARCHAR(20) NOT NULL,
  PRIMARY KEY (idLocal)
);

-- Criando a tabela DimensaoFaixaEtaria
CREATE TABLE DimensaoFaixaEtaria (
  idFaixaEtaria INT NOT NULL AUTO_INCREMENT,
  faixa_etaria VARCHAR(20) NOT NULL,
  PRIMARY KEY (idFaixaEtaria)
);

-- Criando a tabela DimensaoSexo
CREATE TABLE DimensaoSexo (
  idSexo INT NOT NULL AUTO_INCREMENT,
  sexo VARCHAR(10) NOT NULL,
  PRIMARY KEY (idSexo)
);

-- Criando a tabela FatoCovid
CREATE TABLE FatoCovid (
  idData INT NOT NULL,
  idLocal INT NOT NULL,
  idFaixaEtaria INT NOT NULL,
  idSexo INT NOT NULL,
  casos_confirmados INT NOT NULL,
  obitos INT NOT NULL,
  valor INT NOT NULL,
  PRIMARY KEY (idData, idLocal, idFaixaEtaria, idSexo),
  FOREIGN KEY (idData) REFERENCES DimensaoData(idData),
  FOREIGN KEY (idLocal) REFERENCES DimensaoLocal(idLocal),
  FOREIGN KEY (idFaixaEtaria) REFERENCES DimensaoFaixaEtaria(idFaixaEtaria),
  FOREIGN KEY (idSexo) REFERENCES DimensaoSexo(idSexo)
);