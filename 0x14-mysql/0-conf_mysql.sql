CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT, SHOW DATABASES ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
