drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  entry text not null,
);