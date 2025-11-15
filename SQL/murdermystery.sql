--check report
SELECT * FROM crime_scene_report WHERE date=20180115 AND type="murder";
-- check interview from witnesses
SELECT * from interview WHERE person_id IN(
SELECT id FROM person WHERE address_street_name="Northwestern Dr" OR address_street_name="Franklin Ave");
--14887	I heard a gunshot and then saw a man run out. He had a "Get Fit Now Gym" bag. The membership number on the bag started with "48Z".
--Only gold members have those bags. The man got into a car with a plate that included "H42W".
--16371	I saw the murder happen, and I recognized the killer from my gym when I was working out last week on January the 9th.
--check gym record
SELECT * FROM get_fit_now_check_in WHERE membership_id LIKE "48Z%" AND check_in_date = "20180109";
--get person_id of suspects
SELECT person_id FROM get_fit_now_member WHERE id IN (
SELECT membership_id FROM get_fit_now_check_in WHERE membership_id LIKE "48Z%" AND
check_in_date = "20180109");
--67318 28819
--cross check with license plate
SELECT * FROM person WHERE id= "67318" OR id="28819" AND license_id IN(
  SELECT id FROM drivers_license WHERE plate_number LIKE "%H42W%");
--check result
INSERT INTO solution VALUES (1, 'Jeremy Bowers');
        SELECT value FROM solution;
--Congrats, you found the murderer! But wait, there's more... If you think you're up for a challenge, try querying the interview transcript of the murderer to find the real villain behind this crime.
--If you feel especially confident in your SQL skills, try to complete this final step with no more than 2 queries. Use this same INSERT statement with your new suspect to check your answer.
SELECT * FROM interview WHERE person_id = "67318"
--I was hired by a woman with a lot of money. I don't know her name but I know she's around 5'5" (65") or 5'7" (67"). She has red hair and she drives a Tesla Model S.
--I know that she attended the SQL Symphony Concert 3 times in December 2017.
SELECT person.name FROM person
JOIN drivers_license ON person.license_id= drivers_license.id
JOIN facebook_event_checkin ON person.id= facebook_event_checkin.person_id
WHERE drivers_license.gender="female" AND drivers_license.height IN ("65", "66", "67")
AND drivers_license.hair_color="red" AND drivers_license.car_make ="Tesla"
AND drivers_license.car_model= "Model S"
AND facebook_event_checkin.event_name = "SQL Symphony Concert"
AND facebook_event_checkin.date LIKE "201712%";
--check result
INSERT INTO solution VALUES (1, 'Miranda Priestly');
        SELECT value FROM solution;
--Congrats, you found the brains behind the murder! Everyone in SQL City hails you as the greatest SQL detective of all time. Time to break out the champagne!



