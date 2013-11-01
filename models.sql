drop table if exists url_entry;
create table url_entry (
       id integer primary key autoincrement,
       long_url text not null,
       short_url text not null
);
