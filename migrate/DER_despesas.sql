CREATE DATABASE controlador_despesas;

USE controlador_despesas;

-- 1. Usuários
CREATE TABLE tb_usuarios (
    login VARCHAR(50) NOT NULL,
    senha VARCHAR(200)
);

ALTER TABLE tb_usuarios ADD CONSTRAINT PK_tb_usuarios PRIMARY KEY (login);


-- 2. Categorias
CREATE TABLE tb_categorias (
    id_categoria INT NOT NULL,
    nome_categoria VARCHAR(50),
    login VARCHAR(50)
);

ALTER TABLE tb_categorias ADD CONSTRAINT PK_tb_categorias PRIMARY KEY (id_categoria);
ALTER TABLE tb_categorias MODIFY id_categoria INT AUTO_INCREMENT;


-- 3. Despesas
CREATE TABLE tb_despesas (
    id_despesa SMALLINT NOT NULL,
    valor DECIMAL(7,2),
    dt_cadastro DATE,
    id_categoria INT,
    login VARCHAR(50)
);

ALTER TABLE tb_despesas ADD CONSTRAINT PK_tb_despesas PRIMARY KEY (id_despesa);


-- 4. Chaves Estrangeiras
ALTER TABLE tb_categorias ADD CONSTRAINT FK_tb_categorias_0 FOREIGN KEY (login) REFERENCES tb_usuarios (login);

ALTER TABLE tb_despesas ADD CONSTRAINT FK_tb_despesas_0 FOREIGN KEY (id_categoria) REFERENCES tb_categorias (id_categoria);
ALTER TABLE tb_despesas ADD CONSTRAINT FK_tb_despesas_1 FOREIGN KEY (login) REFERENCES tb_usuarios (login);