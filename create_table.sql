/*
	Note: You do not actually need to execute this script as this table has already been created.
	This is more for documentary purposes.
*/

create table DOWNLOADED_SOLAX_INFO (
	time_of_request 	TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL PRIMARY KEY,
	success 		boolean,
	inverterSN 		varchar(14),
	sn 			varchar(10),
	acpower 		decimal(5,1),
	yieldtoday 		decimal(5,1),
	yieldtotal 		decimal(5,1),
	feedinpower 		decimal(5,1),
	feedinenergy 		decimal(5,1),
	consumeenergy 		decimal(6,2),
	feedinpowerM2 		decimal(5,1),
	soc 			decimal(5,1),
	peps1 			decimal(5,1),
	peps2 			decimal(5,1),
	peps3 			decimal(5,1),
	inverterType 		varchar(2),
	inverterStatus 		varchar(3),
	uploadTime 		TIMESTAMP,
	batPower 		decimal(6,2),
	powerdc1 		decimal(5,1),
	powerdc2 		decimal(5,1),
	powerdc3 		decimal(5,1),
	powerdc4 		decimal(5,1),
	batStatus 		char(1)	
)
