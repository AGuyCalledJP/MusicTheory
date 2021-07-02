export DB_IP=127.0.0.1
export PGPASSWORD=''
DOCKER_CMD="docker run \
     --net=host -e PGUSER=postgres -e PGPASSWORD=$PGPASSWORD \
     --rm -i -t postgres:12.1"

function psql_command {
 $DOCKER_CMD psql -h $DB_IP -p 5432 -c "$1"
}

psql_command 'drop database if exists theory'
psql_command 'create database theory'
psql_command "drop role if exists theory"
psql_command "create user theory with login password 'theory'";
psql_command 'grant all privileges on database theory to theory'

# docker exec -i docker_db_1 psql -U theory -d theory < backups/theory_backup.gz