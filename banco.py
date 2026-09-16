import sqlite3

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# 1. Criação das Tabelas
cursor.executescript('''
DROP TABLE IF EXISTS city;
DROP TABLE IF EXISTS country;

CREATE TABLE country (
    id INTEGER PRIMARY KEY,
    name TEXT,
    population INTEGER,
    area REAL
);

CREATE TABLE city (
    id INTEGER PRIMARY KEY,
    name TEXT,
    country_id INTEGER,
    rating INTEGER,
    FOREIGN KEY (country_id) REFERENCES country(id)
);
''')

# 2. Lista com 30 Países Reais (id, name, population, area)
paises_reais = [
    (1, 'Brasil', 214000000, 8515767),
    (2, 'Costa do Marfim', 66600000, 640679),
    (3, 'Alemanha', 80700000, 357080),
    (4, 'Japao', 125000000, 377975),
    (5, 'Estados Unidos', 331000000, 9833520),
    (6, 'Argentina', 45000000, 2780400),
    (7, 'Nigeria', 38000000, 9984670),
    (8, 'Itália', 59000000, 301340),
    (9, 'Espanha', 47000000, 505990),
    (10, 'Reino Unido', 67000000, 242495),
    (11, 'Portugal', 10000000, 92212),
    (12, 'Chile', 19000000, 756102),
    (13, 'Uruguai', 350000, 176215),
    (14, 'Paraguai', 7000000, 406752),
    (15, 'Colombia', 51000000, 1141748),
    (16, 'Peru', 33000000, 1285216),
    (17, 'Mexico', 128000000, 1964375),
    (18, 'Egitp', 104000000, 1010408),
    (19, 'Australia', 25000000, 7692024),
    (20, 'China', 1412000000, 9596960),
    (21, 'India', 1408000000, 3287263),
    (22, 'Coreia do Sul', 51000000, 100210),
    (23, 'Noruega', 5400000, 385207),
    (24, 'Suecia', 10400000, 450295),
    (25, 'Grecia', 10700000, 131957),
    (26, 'Holanda', 17500000, 41865),
    (27, 'Suica', 8700000, 41285),
    (28, 'Africa do Sul', 59000000, 1221037),
    (29, 'Nova Zelandia', 5100000, 268021),
    (30, 'Islandia', 350000, 103000)
]

# 3. Lista com 30 Cidades Reais (id, name, country_id, rating)
cidades_reais = [
    (1, 'Manaus', 1, 5),
    (2, 'Grand-Bassam', 1, 4),
    (3, 'Rio de Janeiro', 1, 5),
    (4, 'Paris', 2, 5),
    (5, 'Lyo', 2, 4),
    (6, 'Berlim', 3, 4),
    (7, 'Abuja', 3, 5),
    (8, 'Tóquio', 4, 5),
    (9, 'Osaka', 4, 4),
    (10, 'Nova York', 5, 5),
    (11, 'Los Angeles', 5, 4),
    (12, 'Buenos Aires', 6, 4),
    (13, 'Toronto', 7, 4),
    (14, 'Roma', 8, 5),
    (15, 'Milao', 8, 4),
    (16, 'Madri', 9, 5),
    (17, 'Barcelona', 9, 5),
    (18, 'Londres', 10, 5),
    (19, 'Lisboa', 11, 5),
    (20, 'Porto', 11, 4),
    (21, 'Santiago', 12, 3),
    (22, 'Montevideu', 13, 3),
    (23, 'Assuncao', 14, 2),
    (24, 'Bogota', 15, 3),
    (25, 'Lima', 16, 4),
    (26, 'Cidade do Mexico', 17, 4),
    (27, 'Cairop', 18, 3),
    (28, 'Sydney', 19, 5),
    (29, 'Pequim', 20, 4),
    (30, 'Atenas', 25, 5)
]

cursor.executemany('INSERT INTO country VALUES (?, ?, ?, ?);', paises_reais)
cursor.executemany('INSERT INTO city VALUES (?, ?, ?, ?);', cidades_reais)
conn.commit()

# 4. Execução dos 5 comandos SQL da folha
comandos = [
    ("1. Querying Single Table", "SELECT id, name FROM city;"),
    ("2. Filtering (WHERE)", "SELECT name, rating FROM city WHERE rating > 3;"),
    ("3. Text Operators (LIKE)", "SELECT name FROM city WHERE name LIKE 'M%';"),
    ("4. Inner Join", "SELECT city.name AS Cidade, country.name AS Pais FROM city INNER JOIN country ON city.country_id = country.id;"),
    ("5. Grouping (GROUP BY)", "SELECT country_id, COUNT(*) AS Total FROM city GROUP BY country_id;")
]

for titulo, query in comandos:
    print(f"\n--- {titulo} ---")
    cursor.execute(query)
    for linha in cursor.fetchall():
        print(linha)

conn.close()