CREATE TABLE track(
    album_id integer,
    genre_id integer,
    artist_id integer,
    rlsyr integer,
    primary key(title),
    foreign key(album_id) references album(id) on delete cascade,
    foreign key(genre_id) references genre(id) on delete cascade,
    foreign key(artist_id) references artist(id) on delete cascade,
);