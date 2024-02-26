create database t14_MiniProjeto
use t14_MiniProjeto

create table usuario
(
	id_usuario int not null  auto_increment primary key,
	nome_usuario varchar(50) not null  ,
	login_usuario varchar(30) not null unique ,
	senha_usuario varchar(30) not null  ,
	data_usuario timestamp not null   ,
	obs_usuario varchar(255) null  ,
	status_usuario varchar(20) not null default 'ATIVO' 
)

create table funcionario
(
ID_Funcionario	int	not null	 auto_increment	primary key,
nome_Funcionario	varchar(50)	not null		,
nasc_Funcionario	date	not null		,
data_Funcionario	timestamp	not null	 	,
cpf_Funcionario	char(14)	not null	unique	,
logradouro_Funcionario	varchar(50)	not null		,
numero_Funcionario	int	not null		,
comp_funcionario	varchar(20)	null		,
cep_Funcionario	char(9)	not null		,
bairro_Funcionario	varchar(50)	not null		,
cidade_Funcionario	varchar(50)	not null		,
uf_Funcionario	char(2)	not null		,
telefone1_Funcionario	char(16)	not null		,
obs_Funcionario	varchar(200)	null		,
status_Funcionario	varchar(20)	not null default 'ATIVO'	

)

create table produto
(
ID_Produto	int	not null	 auto_increment	primary key,
nome_Produto	varchar(30)	not null	unique	,
data_Produto	timestamp	not null	 	,
qtde_Produto	int	not null		,
Vcusto_Produto	decimal(10,2)	not null		,
Vvenda_Produto	decimal(10,2)	not null		,
obs_Produto	varchar(200)	null		,
status_Produto	varchar(20)	not null	default 'ATIVO'
)

create table fornecedor
(
ID_Fornecedor	int	not null	 auto_increment	primary key,
nome_Fornecedor	varchar(50)	not null		,
nasc_Fornecedor	date	not null		,
data_Fornecedor	timestamp	not null	 	,
cnpj_Fornecedor	char(14)	not null	unique	,
logradouro_Fornecedor	varchar(50)	not null		,
numero_Fornecedor	int	not null		,
cep_Fornecedor	varchar(20)	null		,
bairro_Fornecedor	char(9)	not null		,
cidade_Fornecedor	varchar(50)	not null		,
uf_Fornecedor	varchar(50)	not null		,
telefone1_Fornecedor	char(2)	not null		,
contato_Fornecedor	char(16)	null		,
obs_Fornecedor	varchar(200)	null		,
status_Fornecedor	varchar(20)	not null	default 'ATIVO'	

)

create table localestoque
(
id_LocalEstoque	int	not null	 auto_increment	primary key,
nome_LocalEstoque	varchar(50)	not null		,
data_LocalEstoque	timestamp	not null	 	,
obs_LocalEstoque	varchar(200)	null		,
status_LocalEstoque	varchar(20)	not null	default 'ATIVO'	

)

