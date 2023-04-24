import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import datetime
import csv

# df = pd.read_csv(r"C:\Users\DAN\Downloads\Trabalho Business Inteligence - Copia\db.csv")
df = pd.read_csv(r"C:\Users\DAN\Downloads\Trabalho Business Inteligence - Copia\db.csv",sep=';',encoding='latin-1',low_memory=False)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="covid_db"
)

cursor = conn.cursor()

# Função para criar a tabela dimensão município
try:
    cursor.execute("""
                CREATE TABLE dim_municipio (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    municipio VARCHAR(255) NOT NULL
                )
                """
            )
    print("Tabela dim_municipio criada com sucesso!")
except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Tabela dim_municipio já existe.")
        else:
            print(err.msg)

# Função para criar a tabela dimensão DataDiagnostico
try:
    cursor.execute(
        """
                CREATE TABLE dim_data_diagnostico (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    data_diagnostico DATE NOT NULL
                )
                """
            )
    print("Tabela dim_data_diagnostico criada com sucesso!")
except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Tabela dim_data_diagnostico já existe.")
        else:
            print(err.msg)

# Função para criar a tabela dimensão faixaetaria
try:
    cursor.execute(
        """
                CREATE TABLE dim_faixaetaria (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    faixa_etaria VARCHAR(255) NOT NULL
                )
                """
            )
    print("Tabela dim_faixaetaria criada com sucesso!")
except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Tabela dim_faixaetaria já existe.")
        else:
            print(err.msg)

# Função para criar a tabela fato
try:
    cursor.execute(
                """
                CREATE TABLE fato (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    id_municipio INT NOT NULL,
                    id_data_diagnostico INT NOT NULL,
                    id_faixa_etaria INT NOT NULL,
                    casos_confirmados INT,
                    casos_descartados INT,
                    casos_suspeitos INT,
                    casos_totais INT,
                    FOREIGN KEY (id_municipio) REFERENCES dim_municipio (id),
                    FOREIGN KEY (id_data_diagnostico) REFERENCES dim_data_diagnostico (id),
                    FOREIGN KEY (id_faixa_etaria) REFERENCES dim_faixaetaria (id)
                )
                """
            )
    print("Tabela fato criada com sucesso!")
except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Tabela fato já existe.")
        else:
            print(err.msg)

# Insere os dados na tabela de dimensão município
with open(r'C:\Users\DAN\Downloads\Trabalho Business Inteligence - Copia\db.csv', newline="", encoding="ISO-8859-1") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        for i, row in df.iterrows():
            insert_query = f"INSERT INTO dim_municipio (municipio) VALUES (%s)"
            cursor.execute(insert_query, (row["Municipio"],))
        print(">>>>> DADOS DE MUNICIPIO INSERIDOS COM SUCESSO!")

# Insere os dados na tabela de dimensão DataDiagnostico
with open(r'C:\Users\DAN\Downloads\Trabalho Business Inteligence - Copia\db.csv', newline="", encoding="ISO-8859-1") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        for i, row in df.iterrows():
            insert_query = f"INSERT INTO dim_data_diagnostico (data_diagnostico) VALUES (%s)"
            cursor.execute(insert_query, (row["DataDiagnostico"],))
        print(">>>>> DADOS DE DATA DE DIAGNOSTICO INSERIDOS COM SUCESSO!")

# Insere os dados na tabela dimensão faixaetaria
with open(r'C:\Users\DAN\Downloads\Trabalho Business Inteligence - Copia\db.csv', newline="", encoding="ISO-8859-1") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        for i, row in df.iterrows():
            insert_query = f"INSERT INTO dim_faixaetaria (faixa_etaria) VALUES (%s)"
            cursor.execute(insert_query, (row["FaixaEtaria"],))
        print(">>>>> DADOS DE FAIXA ETÁRIA INSERIDOS COM SUCESSO!")


# Salva as mudanças no banco de dados
conn.commit()

# Fecha a conexão com o servidor MySQL
conn.close()
