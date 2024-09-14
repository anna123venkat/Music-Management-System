CREATE TABLE Album(
    id integer auto_increment,
    album_name varchar(50) unique,
    artist_id integer,
    primary key(id),
    foreign key(artist_id) references artist(id) on delete cascade
);