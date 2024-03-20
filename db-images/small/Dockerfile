FROM postgres:13
# Configurações específicas do flavor pequeno, como ajustes de memória e configurações do PostgreSQL
COPY custom-config.conf /etc/postgresql/postgresql.conf
CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]
