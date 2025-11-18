create table alunos
(
    aluno_id int primary key,
    nome     varchar(100),
    email    varchar(100)
);

create table professores
(
    professor_id int primary key,
    nome         varchar(100),
    area         varchar(100)
);

create table cursos
(
    curso_id     int primary key,
    titulo       varchar(100),
    professor_id int,

    foreign key (professor_id) references professores (professor_id)
);

create table matriculas
(
    aluno_id       int,
    curso_id       int,
    data_matricula date,
    primary key (aluno_id, curso_id),

    foreign key (aluno_id) references alunos (aluno_id),
    foreign key (curso_id) references cursos (curso_id)
);

insert into alunos
values (1, 'Alice', 'alice@email.com'),
       (2, 'Bruno', 'bruno@email.com'),
       (3, 'Carla', 'carla@email.com');

insert into professores
values (10, 'Professor João', 'Programação'),
       (11, 'Professor Marcos', 'Design');

insert into cursos
values (100, 'HTML e CSS', 11),
       (101, 'Lógica de Programação', 10),
       (102, 'Banco de Dados', 10);

insert into matriculas
values (1, 100, '2025-01-10'),
       (1, 101, '2025-01-15'),
       (2, 102, '2025-01-20');

select a.nome   as aluno,
       c.titulo as curso,
       m.data_matricula
from matriculas m
         inner join alunos a on m.aluno_id = a.aluno_id
         inner join cursos c on m.curso_id = c.curso_id;

select a.nome as aluno,
       c.titulo as curso
from alunos a
left join matriculas m on a.aluno_id = m.aluno_id
left join cursos c on m.curso_id = c.curso_id;

select a.nome as aluno,
       c.titulo as curso
from alunos a
right join matriculas m on a.aluno_id = m.aluno_id
right join cursos c on m.curso_id = c.curso_id;

select a.nome as aluno,
     c.titulo as curso,
     p.nome as professor
from matriculas m
join alunos a on a.aluno_id = m.aluno_id
join cursos c on m.curso_id = c.curso_id
join professores p on c.professor_id = p.professor_id;

select a.nome as aluno,
       c.titulo as curso
from alunos a
left join matriculas m on a.aluno_id= m.aluno_id
left join cursos c on m.curso_id = c.curso_id
union
select a.nome as aluno,
       c.titulo as curso
from alunos a
right join matriculas m on a.aluno_id = m.aluno_id
right join cursos c on m.curso_id = c.curso_id;

select c.titulo, count(m.aluno_id) as total_matriculas
from cursos c
left join matriculas m on c.curso_id = m.curso_id
group by c.titulo;

select a.nome
from alunos a
join matriculas m on a.aluno_id = m.aluno_id
join cursos c on m.curso_id = c.curso_id
join professores p on c.professor_id = p.professor_id
where p.nome = 'Professor João'

