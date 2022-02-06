GRANT ALL PRIVILEGES ON *.* TO 'joojong'@'%' IDENTIFIED BY 'password';

if not exists create database willneedme_market;

use willneedme_market;

create table if not exists  willneedme_user(
    `id` int not null AUTO_INCREMENT PRIMARY KEY,
    `adminEmail` varchar(100) not null,
    `adminPassword` varchar(40) not null,
    `adminName` varchar(20) not null,
    `connectTime`datetime,
    `connectIp` varchar(100) not null
);

create table if not exists  tickers(
    `symbol` varchar(150) PRIMARY KEY,
    `country` varchar(100),
    `industry` varchar(200),
    `ipoYear` varchar(10),
    `sector` varchar(100),
    `marketCap` double,
    `name` varchar(250),
    `netChange` double,
    `logoUrl` text
);
create table if not exists  ticker_charts(
    `date` datetime,
    `symbol` varchar(150),
    `close` double not null,
    `high` double not null,
    `low` double not null,
    `open` double not null,
    `volume` integer not null,
    `symbolDate` varchar(180) PRIMARY KEY,
    foreign key(`symbol`) references tickers(`symbol`)
);

create table if not exists  ticker_infos(
    `symbol` varchar(150) PRIMARY KEY,
    `fiftyDayAverage` double, 
    `fiftyTwoWeekHigh` double, 
    `fiftyTwoWeekLow` double,
    `twoHundredDayAverage` double,
    `averageVolume10days` double,
    `averageVolume` double,
    `fiftyTwoWeekChange` double,
    `earningsGrowth` double,
    `earningsQuarterlyGrowth` double,
    `trailingPE` double,
    `trailingEps` double,
    foreign key(`symbol`) references tickers(`symbol`)
);
create table if not exists users(
    `displayName` varchar(200),
    `email` varchar(200) ,
    `emailVerified` boolean,
    `phoneNumber` varchar(50),
    `uid` varchar(100) not null PRIMARY KEY,
    `receiveFcm` boolean default false,
    `isAdmin` boolean default false,
    `deviceToken` text,
    `createdAt` datetime,
    `updatedAt` datetime,
    `loginType` varchar(20)
) --when google apple naver login

create table user_articles(
	`id` int not null AUTO_INCREMENT PRIMARY KEY,
	`uid` varchar(100) not null,
	`description` text,
    `displayName` varchar(200),
	`symbol` varchar(150) not null,
    `createdAt` datetime,
    `updatedAt` datetime,
	FOREIGN KEY(`uid`) REFERENCES users(`uid`),
	FOREIGN KEY(`symbol`) REFERENCES tickers(`symbol`)
)