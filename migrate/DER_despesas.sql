CREATE DATABASE controlador_despesas;

USE controlador_despesas;

-- 1. Usuários
CREATE TABLE tb_usuarios (
    login VARCHAR(50) NOT NULL PRIMARY KEY,
    senha VARCHAR(200)
);

-- 2. Categorias
CREATE TABLE tb_categorias (
    id_categoria INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_categoria VARCHAR(50),
    login VARCHAR(50),
    CONSTRAINT FK_tb_categorias_0 FOREIGN KEY (login) REFERENCES tb_usuarios (login)
);

-- 3. Despesas
CREATE TABLE tb_despesas (
    id_despesa SMALLINT NOT NULL PRIMARY KEY,
    valor DECIMAL(7,2),
    dt_cadastro DATE,
    id_categoria INT,
    descricao_despesa VARCHAR(255),
    login VARCHAR(50),
    CONSTRAINT FK_tb_despesas_0 FOREIGN KEY (id_categoria) REFERENCES tb_categorias (id_categoria),
    CONSTRAINT FK_tb_despesas_1 FOREIGN KEY (login) REFERENCES tb_usuarios (login)
);