create database edulearn22;
use edulearn22;

CREATE TABLE alunos (
                        aluno_id INT PRIMARY KEY,
                        nome VARCHAR(100),
                        email VARCHAR(100)
);

CREATE TABLE professores (
                             professor_id INT PRIMARY KEY,
                             nome VARCHAR(100),
                             area VARCHAR(50)
);


CREATE TABLE cursos (
                        curso_id INT PRIMARY KEY,
                        titulo VARCHAR(100),
                        professor_id INT,
                        FOREIGN KEY (professor_id) REFERENCES professores(professor_id)
);

CREATE TABLE matriculas (
                            aluno_id INT,
                            curso_id INT,
                            data_matricula DATE,
                            PRIMARY KEY (aluno_id, curso_id),
                            FOREIGN KEY (aluno_id) REFERENCES alunos(aluno_id),
                            FOREIGN KEY (curso_id) REFERENCES cursos(curso_id)
);


INSERT INTO alunos VALUES
                       (1, 'Alice', 'alice@mail.com'),
                       (2, 'Bruno', 'bruno@mail.com'),
                       (3, 'Carla', 'carla@mail.com');


INSERT INTO professores VALUES
                            (10, 'Professor João', 'Programação'),
                            (11, 'Professor Marcos', 'Design');


INSERT INTO cursos VALUES
                       (100, 'HTML e CSS', 11),
                       (101, 'Lógica de Programação', 10),
                       (102, 'Banco de Dados', 10);


INSERT INTO matriculas VALUES
                           (1, 100, '2025-01-10'),
                           (1, 101, '2025-01-15'),
                           (2, 102, '2025-01-20');
