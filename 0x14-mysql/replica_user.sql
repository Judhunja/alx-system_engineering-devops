-- creates replica user and gives them permission to replicate my primary MySQL server
CREATE USER 'replica_user'@'%' identified by 'password';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%' IDENTIFIED BY 'password';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
