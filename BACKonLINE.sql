BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `Response` (
	`ResponseID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`OptionID`	INTEGER NOT NULL UNIQUE,
	`QuestionID`	INTEGER NOT NULL UNIQUE,
	`PatientID`	INTEGER NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS `Questions` (
	`QuestionID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`QuestionText`	TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS `Patient` (
	`PatientID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`surname`	TEXT NOT NULL,
	`first name`	TEXT NOT NULL,
	`dob`	INTEGER NOT NULL,
	`email`	TEXT NOT NULL,
	`gender`	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Options` (
	`QuestionID`	INTEGER NOT NULL,
	`OptionID`	INTEGER NOT NULL,
	`OptionText`	TEXT NOT NULL,
	`Score`	INTEGER,
	PRIMARY KEY(`OptionID`)
);
INSERT INTO `Questions` (QuestionID,QuestionText) VALUES (1,'Do you know what caused your current back pain?'),
 (2,'If yes, choose an option from the list below:'),
 (3,'What do you think is wrong with your back?'),
 (4,'If you have been treated for back pain, were you
satisfied with your treatment? '),
 (5,'What medication do you take to manage your back pain?'),
 (6,'How effective is the medication in reducing your back pain?'),
 (7,'Where is your pain?'),
 (8,'Is your pain there all the time? '),
 (9,'What type of pain is it?'),
 (10,'When is your pain at its worst? '),
 (11,'Can you ease your back pain?'),
 (12,'How do you ease your back pain? Please tick all options that apply'),
 (13,'In general, is your back pain getting better, staying the
same or getting worse?'),
 (14,'From the list below, please tick all the activities that make your pain worse.'),
 (15,'From the list below, please tick all the activities that stop or decrease your pain.'),
 (16,'Is this the first time you have experienced this type of pain?'),
 (17,'If you had a previous episode of back pain, what helped in making your pain better?'),
 (18,'Other than your back pain, do you experience other odd
sensations in your back or legs (for example: crawling
sensation, stinging, pressure)'),
 (19,'Please tick all the areas where you experience this feeling:'),
 (20,'On average, how many hours do you sleep?'),
 (21,'Does your back pain wake you up every night?'),
 (22,'If you wake up with back pain, can you get back to sleep? '),
 (23,'How strongly do you agree with this statement : ‘I believe that my job caused /contributed to my back pain’ '),
 (24,'Do you feel supported by your boss and/or co-workers? '),
 (25,'How is your back pain affecting your work? '),
 (26,'Are you off work right now because of your back pain?'),
 (27,'How long have you been off work?'),
 (28,'How likely it is that you would return to work within sixmonths? '),
 (29,'‘I can’t do my normal daily activities because of my back pain’'),
 (30,'‘My back pain is negatively affecting my social life’'),
 (31,'‘My back pain is affecting my relationship with my
significant other'''),
 (32,'‘I don’t know what makes my back pain worse or what
eases it ‘
'),
 (33,'‘My back pain makes me feel stressed/anxious’'),
 (34,'‘Stress increases my back pain’
'),
 (35,'‘Physical activity increases my back pain’'),
 (36,'‘Since my back pain started, I feel more tired’'),
 (37,'‘I have lost interest and/or pleasure in doing things because of my back pain’
'),
 (38,' ‘I don’t think my family and friends understand what I’m going through with my back pain.’'),
 (39,'‘I don’t think my back pain will ever go away.’');

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
 (5,18,'Codeine',1),
 (5,19,'Diazepam',1),
 (5,20,'Amitriptyline',1),
 (5,21,'Duloxetine/Cymbalta',1),
 (5,22,'Gabapentin',1),
 (5,23,'Tramadol',1),
 (5,24,'Hydrocodone',1),
 (5,25,'Cortisone',1),
 (5,26,'Acetaminophen',1),
 (5,27,'Glucosamine',1),
 (5,28,'Valium',1),
 (5,29,'Naproxen',1),
 (5,30,'Other',1),
 (5,31,'I don''t take any medication for my back pain',0),
 (6,32,'Effective',0),
 (6,33,'Not sure',1),
 (6,34,'Ineffective',2),
 (7,35,'Neck',1),
 (7,36,'Right-shoulder',1),
 (7,37,'Left-shoulder',1),
 (7,38,'Right-arm',1),
 (7,39,'Left-arm',1),
 (7,40,'Upper-back',1),
 (7,41,'Lower-back',1),
 (7,42,'Right buttock',1),
 (7,43,'Left buttock',1),
 (7,44,'Right hip',1),
 (7,45,'Left hip',1),
 (7,46,'Right leg',1),
 (7,47,'Left leg',1),
 (8,48,'My pain is there all the time',2),
 (8,49,'My pain comes and goes',0),
 (8,50,'Not sure',1),
 (9,51,'Deep',1),
 (9,52,'Nagging',1),
 (9,53,'Dull',1),
 (9,54,'Sharp',1),
 (9,55,'Shooting',1),
 (9,56,'Dull ache',1),
 (9,57,'Like lighting',1),
 (9,58,'Burning',1),
 (9,59,'Pressure',1),
 (9,60,'Stinging',1),
 (9,61,'Aching',1),
 (9,62,'Throbbing',1),
 (9,63,'Spread over a wide area',2),
 (10,64,'in the morning',1),
 (10,65,'at the end of the day',1),
 (10,66,'My pain is there all day long',2),
 (11,67,'Yes',0),
 (11,68,'Sometimes',1),
 (11,69,'No',2),
 (12,70,'Medication/pain killers',0),
 (12,71,'Rest',0),
 (12,72,'Walking',0),
 (12,73,'Standing',0),
 (12,74,'Sitting',0),
 (12,75,'Exercise',0),
 (12,76,'Massage',0),
 (12,77,'Hot pack',0),
 (12,78,'Cold pack',0),
 (12,79,'Other',0),
 (12,80,'I am unable to ease my back pain',2),
 (13,81,'My pain is getting better',0),
 (13,82,'My pain has stayed the same',1),
 (13,83,'My pain is getting worse',2),
 (14,84,'Sitting relaxed',0),
 (14,85,'Sitting up straight',0),
 (14,86,'Standing',0),
 (14,87,'Walking',0),
 (14,88,'Lifting',0),
 (14,89,'Forward bending',0),
 (14,90,'Any activity that I do for a long period of time increases my back pain',1),
 (14,91,'Everything I do causes me pain',2),
 (15,92,'Walking',0),
 (15,93,'Changing positions',0),
 (15,94,'Sitting down',0),
 (15,95,'Avoiding activities that causes me pain ',2),
 (15,96,'Stretching my back',0),
 (15,97,'Moving about',0),
 (15,98,'Painkillers',1),
 (15,99,'Nothing I do stops my pain',2),
 (16,100,'Yes',0),
 (16,101,'No',2),
 (16,102,'Not sure',1),
 (17,103,'Medication/painkillers/injejctoins',1),
 (17,104,'Rest',1),
 (17,105,'Exercise',0),
 (17,106,'massage/phzsiotherapy/chiropractic/osteopathy',1),
 (17,107,'Nothing helped',2),
 (18,108,'Yes',2),
 (18,109,'No',0),
 (18,110,'I don''t know',1),
 (19,111,'Neck',1),
 (19,112,'Right-shoulder',1),
 (19,113,'Left-shoulder',1),
 (19,114,'Right-arm',1),
 (19,115,'Left-arm',1),
 (19,116,'Upper back',1),
 (19,117,'Lower back',1),
 (19,118,'Right buttock',1),
 (19,119,'Left buttock',1),
 (19,120,'Right hip',1),
 (19,121,'Left hip',1),
 (19,122,'Right leg',1),
 (19,123,'Left leg',1),
 (20,124,'0',2),
 (20,125,'1',2),
 (20,126,'2',2),
 (20,127,'3',2),
 (20,128,'4',2),
 (20,129,'5',1),
 (20,130,'6',1),
 (20,131,'7',1),
 (20,132,'8',1),
 (20,133,'9',0),
 (20,134,'10',0),
 (21,135,'Yes',2),
 (21,136,'No',0),
 (22,137,'Yes',0),
 (22,138,'Sometimes',1),
 (22,139,'No',2),
 (23,140,'Agree',2),
 (23,141,'Neither agree nor disagree',1),
 (23,142,'Disagree',0),
 (23,143,'I don''t work',NULL),
 (24,144,'Yes',0),
 (24,145,'No',2),
 (24,146,'I don''t know',1),
 (24,147,'Not applicable',NULL),
 (25,148,'Not at all',0),
 (25,149,'Sometimes',0),
 (25,150,'Frequently',1),
 (25,151,'I am unable to work because of my back pain',2),
 (26,152,'Yes',2),
 (26,153,'No',0),
 (26,154,'I don''t work',0),
 (27,155,'Less than 3 months',0),
 (27,156,'Between 1 to 6 months',1),
 (27,157,'More than 6 months',2),
 (28,158,'Likely',0),
 (28,159,'Not sure',1),
 (28,160,'Unlikely',2),
 (29,161,'agree',2),
 (29,162,'neither agree nor disagree',1),
 (29,163,'disagree',0),
 (30,164,'agree',2),
 (30,165,'neither agree nor disagree',1),
 (30,166,'disagree',0),
 (31,167,'agree',2),
 (31,168,'neither agree nor disagree',1),
 (31,169,'disagree',0),
 (32,170,'agree',2),
 (32,171,'neither agree nor disagree',1),
 (32,172,'disagree',0),
 (33,173,'agree',2),
 (33,174,'neither agree nor disagree',1),
 (33,175,'disagree',0),
 (34,176,'agree',2),
 (34,177,'neither agree nor disagree',1),
 (34,178,'disagree',0),
 (35,179,'agree',2),
 (35,180,'neither agree nor disagree',1),
 (35,181,'disagree',0),
 (36,182,'agree',2),
 (36,183,'neither agree nor disagree',1),
 (36,184,'disagree',0),
 (37,185,'agree',2),
 (37,186,'neither agree nor disagree',1),
 (37,187,'disagree',0),
 (38,188,'agree',2),
 (38,189,'neither agree nor disagree',1),
 (38,190,'disagree',0),
 (39,191,'agree',2),
 (39,192,'neither agree nor disagree',1),
 (39,193,'disagree',0);
COMMIT;
