Informações do SQLite retiradas [deste vídeo.](https://www.youtube.com/watch?v=dFsMjaTt-VU)

Projeto rodou com a ajuda [deste repositório.](https://github.com/skill-curb/Text-To-SQL-LLM-App-with-MYSQL-SteamLit-LangChain-using-Google-Palm/tree/main)

# Acessar o terminal do Sqlite

```hash
.\sqlite3 ecommerce.db
```

# Populando tabelas
```hash
create table cliente ( id Intger Primary Key, Nome Text Not Null);
```

# Verificando os dados
```
select * from cliente;

# Para criar uma janela  no SQLITE aperte CTRL+SHIFT+P

# Run query CTRL+SHIFT+Q

# Rodar script .py
python .\ecommerce_connect.py