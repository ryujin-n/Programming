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

# --------------
delimiter //
create procedure alunos_por_curso(in idCurso int)
begin
    select  a.nome, c.titulo
    from matriculas m
    join alunos a on m.aluno_id = a.aluno_id
    join cursos c on m.curso_id = c.curso_id
    where c.curso_id = idCurso;
end; //

call alunos_por_curso(100);

create procedure lista_cursos()
begin
    select * from cursos;
end;
call alunos_por_curso(100);

create view vw_info_alunos as
    select a.nome, c.titulo,m.data_matricula
    from matriculas m
    join alunos a on m.aluno_id = a.aluno_id
    join cursos c on m.curso_id = c.curso_id;
select * from vw_info_alunos;

# --------

create table log_matriculas(
  aluno_id int,
  curso_id int
);

create trigger tg_insert_matricula
    after insert  on matriculas
    for each row
    begin
        insert into log_matriculas(aluno_id,curso_id)
            values(NEW.aluno_id, NEW.curso_id);
    end;

INSERT INTO matriculas VALUES
                           (2, 101, '2025-01-20');

select * from log_matriculas;

# -----------



start transaction;

insert cursos(cu)