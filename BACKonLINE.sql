BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS `Questions` (
    `QuestionID`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `QuestionText`  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS `Response` (
    `ResponseID`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `patientID` INTEGER NOT NULL,
    `optionID`  TEXT NOT NULL,
    `questionID`    INTEGER NOT NULL,
    `score` INTEGER,
    `extraInput` TEXT,
    `date`  TEXT
);

CREATE TABLE IF NOT EXISTS `Patient` (
    `PatientID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`   TEXT NOT NULL,
    `gender`    TEXT NOT NULL,
    `age`   INTEGER NOT NULL,
    `email` TEXT NOT NULL,
    `password`  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS `Options` (
    `QuestionID`    INTEGER NOT NULL,
    `OptionID`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `OptionText`    TEXT NOT NULL,
    `Score` INTEGER,
    `QuestionType` TEXT NOT NULL
);

INSERT INTO `Questions` (QuestionID, QuestionText)
VALUES (1, 'Do you know what caused your current back pain?'),
       (2, 'If yes, choose an option from the list below:'),
       (3, 'What do you think is wrong with your back?'),
       (4, 'If you have been treated for back pain, were you satisfied with your treatment?'),
       (5, 'What medication do you take to manage your back pain? Please tick all options that apply'),
       (6, 'How effective is the medication in reducing your back pain?'),
       (7, 'Where is your pain? Please tick all body areas that apply'),
       (8, 'Is your pain there all the time?'),
       (9, 'What type of pain is it? Please tick all options that apply'),
       (10, 'When is your pain at its worst?'),
       (11, 'Can you ease your back pain?'),
       (12, 'How do you ease your back pain? Please tick all options that apply'),
       (13, 'In general, is your back pain getting better, staying the same or getting worse?'),
       (14, 'From the list below, please tick all the activities that make your pain worse.'),
       (15, 'From the list below, please tick all the activities that stop or decrease your pain.'),
       (16, 'Is this the first time you have experienced this type of pain?'),
       (17, 'If you had a previous episode of back pain, what helped in making your pain better? Please tick all options that apply'),
       (18, 'Other than your back pain, do you experience other odd sensations in your back or legs (for example: crawling sensation, stinging, pressure)'),
       (19, 'Please tick all the areas where you experience this feeling:'),
       (20, 'On average, how many hours do you sleep?'),
       (21, 'Does your back pain wake you up every night?'),
       (22, 'If you wake up with back pain, can you get back to sleep?'),
       (23, 'How strongly do you agree with this statement: ''I believe that my job caused /contributed to my back pain'''),
       (24, 'Do you feel supported by your boss and/or co-workers?'),
       (25, 'How is your back pain affecting your work?'),
       (26, 'Are you off work right now because of your back pain?'),
       (27, 'How long have you been off work?'),
       (28, 'How likely it is that you would return to work within six months?'),
       (29, '''I can''t do my normal daily activities because of my back pain'''),
       (30, '''My back pain is negatively affecting my social life'''),
       (31, '''My back pain is affecting my relationship with my significant other'''),
       (32, '''I don''t know what makes my back pain worse or what eases it'''),
       (33, '''My back pain makes me feel stressed/anxious'''),
       (34, '''Stress increases my back pain'''),
       (35, '''Physical activity increases my back pain'''),
       (36, '''Since my back pain started, I feel more tired'''),
       (37, '''I have lost interest and/or pleasure in doing things because of my back pain'''),
       (38, '''I don''t think my family and friends understand what I''m going through with my back pain'''),
       (39, '''I don''t think my back pain will ever go away''');

INSERT INTO `Options` (QuestionID, OptionID, OptionText, Score, QuestionType)
VALUES (1,1,'Yes',0,'Radiobox'),
       (1,2,'No',2,'Radiobox'),
       (1,3,'Not sure',1,'Radiobox'),
       (2,4,'Car accident',1,'Radiobox'),
       (2,5,'Sport injury',0,'Radiobox'),
       (2,6,'Lifting/bending accident',0,'Radiobox'),
       (2,7,'Falling down',0,'Radiobox'),
       (2,8,'Other trauma',0,'Radiobox'),
       (2,9,'Work related',1,'Radiobox'),
       (2,10,'Other',0,'Radiobox'),
       (2,11,'Nothing specific',1,'Radiobox'),
       (3,12,'Write here...',0,'Textbox'),
       (4,13,'Yes, I was satisfied with the treatment',0,'Radiobox'),
       (4,14,'I was neither satisfied nor dissatisfied with the treatment',1,'Radiobox'),
       (4,15,'No, I was not satisfied with the treatment',2,'Radiobox'),
       (4,16,'I was never treated for back pain',0,'Radiobox'),
       (5,17,'Paracetamol',1,'Tickbox'),
       (5,18,'Ibuprofen',1,'Tickbox'),
       (5,19,'Codeine',1,'Tickbox'),
       (5,20,'Diazepam',1,'Tickbox'),
       (5,21,'Amitriptyline',1,'Tickbox'),
       (5,22,'Duloxetine/Cymbalta',1,'Tickbox'),
       (5,23,'Gabapentin',1,'Tickbox'),
       (5,24,'Tramadol',1,'Tickbox'),
       (5,25,'Hydrocodone',1,'Tickbox'),
       (5,26,'Cortisone',1,'Tickbox'),
       (5,27,'Acetaminophen',1,'Tickbox'),
       (5,28,'Glucosamine',1,'Tickbox'),
       (5,29,'Valium',1,'Tickbox'),
       (5,30,'Naproxen',1,'Tickbox'),
       (5,31,'Other',1,'Tickbox'),
       (5,32,'I don''t take any medication for my back pain',0,'Tickbox'),
       (6,33,'Effective',0,'Radiobox'),
       (6,34,'Not sure',1,'Radiobox'),
       (6,35,'Ineffective',2,'Radiobox'),
       (7,36,'Neck',1,'Tickbox'),
       (7,37,'Right shoulder',1,'Tickbox'),
       (7,38,'Left shoulder',1,'Tickbox'),
       (7,39,'Right arm',1,'Tickbox'),
       (7,40,'Left arm',1,'Tickbox'),
       (7,41,'Upper back',1,'Tickbox'),
       (7,42,'Lower back',1,'Tickbox'),
       (7,43,'Right buttock',1,'Tickbox'),
       (7,44,'Left buttock',1,'Tickbox'),
       (7,45,'Right hip',1,'Tickbox'),
       (7,46,'Left hip',1,'Tickbox'),
       (7,47,'Right leg',1,'Tickbox'),
       (7,48,'Left leg',1,'Tickbox'),
       (8,49,'My pain is there all the time',2,'Radiobox'),
       (8,50,'My pain comes and goes',0,'Radiobox'),
       (8,51,'Not sure',1,'Radiobox'),
       (9,52,'Deep',1,'Tickbox'),
       (9,53,'Nagging',1,'Tickbox'),
       (9,54,'Dull',1,'Tickbox'),
       (9,55,'Sharp',1,'Tickbox'),
       (9,56,'Shooting',1,'Tickbox'),
       (9,57,'Dull ache',1,'Tickbox'),
       (9,58,'Like lighting',1,'Tickbox'),
       (9,59,'Burning',1,'Tickbox'),
       (9,60,'Pressure',1,'Tickbox'),
       (9,61,'Stinging',1,'Tickbox'),
       (9,62,'Aching',1,'Tickbox'),
       (9,63,'Throbbing',1,'Tickbox'),
       (9,64,'Spread over a wide area',2,'Tickbox'),
       (10,65,'In the morning',1,'Radiobox'),
       (10,66,'At the end of the day',1,'Radiobox'),
       (10,67,'My pain is there all day long',2,'Radiobox'),
       (11,68,'Yes',0,'Radiobox'),
       (11,69,'Sometimes',1,'Radiobox'),
       (11,70,'No',2,'Radiobox'),
       (12,71,'Medication/painkillers',0,'Tickbox'),
       (12,72,'Rest',0,'Tickbox'),
       (12,73,'Walking',0,'Tickbox'),
       (12,74,'Standing',0,'Tickbox'),
       (12,75,'Sitting',0,'Tickbox'),
       (12,76,'Exercise',0,'Tickbox'),
       (12,77,'Massage',0,'Tickbox'),
       (12,78,'Hot pack',0,'Tickbox'),
       (12,79,'Cold pack',0,'Tickbox'),
       (12,80,'Other',0,'Tickbox'),
       (12,81,'I am unable to ease my back pain',2,'Tickbox'),
       (13,82,'My pain is getting better',0,'Radiobox'),
       (13,83,'My pain has stayed the same',1,'Radiobox'),
       (13,84,'My pain is getting worse',2,'Radiobox'),
       (14,85,'Sitting relaxed',0,'Tickbox'),
       (14,86,'Sitting up straight',0,'Tickbox'),
       (14,87,'Standing',0,'Tickbox'),
       (14,88,'Walking',0,'Tickbox'),
       (14,89,'Lifting',0,'Tickbox'),
       (14,90,'Forward bending',0,'Tickbox'),
       (14,91,'Any activity that I do for a long period of time increases my back pain',1,'Tickbox'),
       (14,92,'Everything I do causes me pain',2,'Tickbox'),
       (15,93,'Walking',0,'Tickbox'),
       (15,94,'Changing positions',0,'Tickbox'),
       (15,95,'Sitting down',0,'Tickbox'),
       (15,96,'Avoiding activities that causes me pain ',2,'Tickbox'),
       (15,97,'Stretching my back',0,'Tickbox'),
       (15,98,'Moving about',0,'Tickbox'),
       (15,99,'Painkillers',1,'Tickbox'),
       (15,100,'Nothing I do stops my pain',2,'Tickbox'),
       (16,101,'Yes',0,'Radiobox'),
       (16,102,'No',2,'Radiobox'),
       (16,103,'Not sure',1,'Radiobox'),
       (17,104,'Medication/painkillers/injections',1,'Tickbox'),
       (17,105,'Rest',1,'Tickbox'),
       (17,106,'Exercise',0,'Tickbox'),
       (17,107,'Massage/physiotherapy/chiropractic/osteopathy',1,'Tickbox'),
       (17,108,'Nothing helped',2,'Tickbox'),
       (18,109,'Yes',2,'Radiobox'),
       (18,110,'No',0,'Radiobox'),
       (18,111,'I don''t know',1,'Radiobox'),
       (19,112,'Neck',1,'Tickbox'),
       (19,113,'Right shoulder',1,'Tickbox'),
       (19,114,'Left shoulder',1,'Tickbox'),
       (19,115,'Right arm',1,'Tickbox'),
       (19,116,'Left arm',1,'Tickbox'),
       (19,117,'Upper back',1,'Tickbox'),
       (19,118,'Lower back',1,'Tickbox'),
       (19,119,'Right buttock',1,'Tickbox'),
       (19,120,'Left buttock',1,'Tickbox'),
       (19,121,'Right hip',1,'Tickbox'),
       (19,122,'Left hip',1,'Tickbox'),
       (19,123,'Right leg',1,'Tickbox'),
       (19,124,'Left leg',1,'Tickbox'),
       (19,125,'BodyDisplay',0,'BodyDisplay'),
       (20,126,'Slider',0, 'Slider'),
       (21,127,'Yes',2,'Radiobox'),
       (21,128,'No',0,'Radiobox'),
       (22,129,'Yes',0,'Radiobox'),
       (22,130,'Sometimes',1,'Radiobox'),
       (22,131,'No',2,'Radiobox'),
       (23,132,'Agree',2,'Radiobox'),
       (23,133,'Neither agree nor disagree',1,'Radiobox'),
       (23,134,'Disagree',0,'Radiobox'),
       (23,135,'I don''t work',0,'Radiobox'),
       (24,136,'Yes',0,'Radiobox'),
       (24,137,'No',2,'Radiobox'),
       (24,138,'I don''t know',1,'Radiobox'),
       (24,139,'Not applicable',0,'Radiobox'),
       (25,140,'Not at all',0,'Radiobox'),
       (25,141,'Sometimes',0,'Radiobox'),
       (25,142,'Frequently',1,'Radiobox'),
       (25,143,'I am unable to work because of my back pain',2,'Radiobox'),
       (26,144,'Yes',2,'Radiobox'),
       (26,145,'No',0,'Radiobox'),
       (26,146,'I don''t work',0,'Radiobox'),
       (27,147,'Less than 3 months',0,'Radiobox'),
       (27,148,'Between 1 to 6 months',1,'Radiobox'),
       (27,149,'More than 6 months',2,'Radiobox'),
       (28,150,'Likely',0,'Radiobox'),
       (28,151,'Not sure',1,'Radiobox'),
       (28,152,'Unlikely',2,'Radiobox'),
       (29,153,'Agree',2,'Radiobox'),
       (29,154,'Neither agree nor disagree',1,'Radiobox'),
       (29,155,'Disagree',0,'Radiobox'),
       (30,156,'Agree',2,'Radiobox'),
       (30,157,'Neither agree nor disagree',1,'Radiobox'),
       (30,158,'Disagree',0,'Radiobox'),
       (31,159,'Agree',2,'Radiobox'),
       (31,160,'Neither agree nor disagree',1,'Radiobox'),
       (31,161,'Disagree',0,'Radiobox'),
       (32,162,'Agree',2,'Radiobox'),
       (32,163,'Neither agree nor disagree',1,'Radiobox'),
       (32,164,'Disagree',0,'Radiobox'),
       (33,165,'Agree',2,'Radiobox'),
       (33,166,'Neither agree nor disagree',1,'Radiobox'),
       (33,167,'Disagree',0,'Radiobox'),
       (34,168,'Agree',2,'Radiobox'),
       (34,169,'Neither agree nor disagree',1,'Radiobox'),
       (34,170,'Disagree',0,'Radiobox'),
       (35,171,'Agree',2,'Radiobox'),
       (35,172,'Neither agree nor disagree',1,'Radiobox'),
       (35,173,'Disagree',0,'Radiobox'),
       (36,174,'Agree',2,'Radiobox'),
       (36,175,'Neither agree nor disagree',1,'Radiobox'),
       (36,176,'Disagree',0,'Radiobox'),
       (37,177,'Agree',2,'Radiobox'),
       (37,178,'Neither agree nor disagree',1,'Radiobox'),
       (37,179,'Disagree',0,'Radiobox'),
       (38,180,'Agree',2,'Radiobox'),
       (38,181,'Neither agree nor disagree',1,'Radiobox'),
       (38,182,'Disagree',0,'Radiobox'),
       (39,183,'Agree',2,'Radiobox'),
       (39,184,'Neither agree nor disagree',1,'Radiobox'),
       (39,185,'Disagree',0,'Radiobox');

COMMIT;
