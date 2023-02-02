CREATE TABLE IF NOT EXISTS shoes (
    id int not null,
    volume_id varchar (15) not null,
    name varchar (50),
    brand varchar (50),
    thumbnail varchar (255),
    style varchar (255),
    state varchar (6),
    price int,
    sale_price int,
    detail varchar (255),
    PRIMARY KEY (id)
);
