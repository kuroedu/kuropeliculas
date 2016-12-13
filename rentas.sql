create database rentas;
use rentas;

create table renta(
id_renta int not null auto_increment primary key,
pelicula varchar(40)not null,
formato varchar(10)not null,
tiempo int (4)not null,
total float(6,2)not null);