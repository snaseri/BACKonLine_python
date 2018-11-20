BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `Questions` (
	`QuestionID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`QuestionText`	TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS `Options` (
	`QuestionID`	INTEGER NOT NULL,
	`OptionID`	INTEGER NOT NULL AUTOINCREMENT,
	`OptionText`	TEXT NOT NULL,
	`Score`	INTEGER,
	PRIMARY KEY(`OptionID`)
);

CREATE TABLE `Response` (
	`ResponseID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`OptionID`	INTEGER NOT NULL UNIQUE,
	`QuestionID`	INTEGER NOT NULL UNIQUE,
	`PatientID`	INTEGER NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS `Patients` (
	`PatientID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`surename`	TEXT NOT NULL,
	`firstname`	TEXT NOT NULL,
	`dob`	INTEGER NOT NULL,
	`email`	TEXT NOT NULL,
	`gender`	TEXT NOT NULL
);

INSERT INTO `Options` (QuestionID,OptionID,OptionText,Score) VALUES (1,1,'Yes',0),
 (1,2,'No',2),
 (1,3,'Not Sure',1),
 (2,4,'Car accident',1),
 (2,5,'Sport injury',0),
 (2,6,'Lifting/bending accident',0),
 (2,7,'Falling down',0),
 (2,8,'Other trauma',0),
 (2,9,'Work related',1),
 (2,10,'Other',0),
 (2,11,'Nothing specific',1),
 (4,12,'Yes, I was satisfied with the treatment',0),
 (4,13,'I was neither satisfied nor dissatisfied with the treatment',1),
 (4,14,'No, I was not satisfied with the treatment',2),
 (4,15,'I was never treated for back pain',NULL),
 (5,16,'Paracetamol',1),
 (5,17,'Ibuprofen',1),
 (5,18,'Codeine',NULL),
 (5,19,'Diazepam',NULL),
 (5,20,'Amitriptyline',NULL),
 (5,21,'Duloxetine/Cymbalta',NULL),
 (5,22,'Gubapentin',NULL),
 (5,23,'Tramadol',NULL),
 (5,24,'Hydrocodone',NULL),
 (5,25,'Cortisone',NULL),
 (5,26,'',NULL),
 (5,27,'',NULL),
 (5,28,'',NULL),
 (5,29,'',NULL),
 (5,30,'',NULL),
 (5,31,'',NULL),
 (5,32,'',NULL);
COMMIT;
