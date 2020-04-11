CREATE DATABASE scraping;
USE scraping;
CREATE TABLE weibo_tweets5 (content varchar(400) not null, url varchar(100) not null, uid varchar(50) not null, pid varchar(50) not null, mid smallint unsigned not null, pubdate varchar(20),
tested varchar(30), testdate varchar(20), status  varchar(20));

-- INSERT INTO weibo_tweets ( id, name ) VALUES ( null, 'Sample data' );

