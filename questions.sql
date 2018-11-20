BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `Questions` (
	`QuestionID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`QuestionText`	TEXT NOT NULL
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
COMMIT;
