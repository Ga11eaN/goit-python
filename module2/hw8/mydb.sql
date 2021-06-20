/*
--5 студентов с наибольшим средним баллом по всем предметам.
SELECT s.id, s.name, s.surname, s.group, avg(mark) AS total_mark FROM student_to_subjects AS sts 
JOIN student AS s ON s.id = sts.student_id
JOIN subjects AS sub ON sub.id = sts.subjects_id
GROUP BY s.id
ORDER BY total_mark DESC
LIMIT 5
*/

/*
--1 студент с наивысшим средним баллом по одному предмету
SELECT s.id, s.name, s.surname, s.group, sub.title, avg(mark) AS total_mark FROM student_to_subjects AS sts 
JOIN student AS s ON s.id = sts.student_id
JOIN subjects AS sub ON sub.id = sts.subjects_id
GROUP BY s.id, sub.title
ORDER BY total_mark DESC
LIMIT 1
*/

/*
--средний балл в группе по одному предмету.
SELECT s.group, sub.title, avg(mark) AS total_mark FROM student_to_subjects AS sts 
JOIN student AS s ON s.id = sts.student_id
JOIN subjects AS sub ON sub.id = sts.subjects_id
GROUP BY s.group, sub.title
ORDER BY s.group
*/

/*
--Средний балл в потоке
SELECT sub.title, avg(mark) AS total_mark FROM student_to_subjects AS sts 
JOIN student AS s ON s.id = sts.student_id
JOIN subjects AS sub ON sub.id = sts.subjects_id
GROUP BY  sub.title
ORDER BY total_mark DESC
*/

/*
--Какие курсы читает преподаватель
SELECT sub.teacher,sub.title FROM subjects AS sub
GROUP BY sub.teacher, sub.title
ORDER BY sub.teacher
*/

/*
--Список студентов в группе
SELECT * FROM student as s
ORDER BY s.group
*/

/*
--Оценки студентов в группе по предмету
SELECT s.id, s.name, s.surname, s.group, sts.mark, sts.date, sub.title FROM student_to_subjects AS sts
JOIN student AS s ON s.id = sts.student_id
JOIN subjects AS sub ON sub.id = sts.subjects_id
WHERE "group" = 1 AND title = 'geometriia'
GROUP BY s.group, sub.title, sts.mark, sts.date, s.id
*/

/*
--Оценки студентов в группе по предмету на последнем занятии
SELECT s.id, s.name, s.surname, s.group, sts.mark, sts.date, sub.title FROM student_to_subjects AS sts
JOIN student AS s ON s.id = sts.student_id
JOIN subjects AS sub ON sub.id = sts.subjects_id
WHERE "group" = 1 AND date = (
	SELECT max(date) AS max_date FROM student_to_subjects AS sts
	JOIN subjects AS sub ON sub.id = sts.subjects_id
	WHERE sub.title = 'geometriia'
	)
GROUP BY s.group, sub.title, sts.mark, sts.date, s.id
ORDER BY sts.date DESC
*/

/*
--Список курсов, которые посещает студент
SELECT s.id, s.name, s.surname, s.group, sub.title FROM student_to_subjects AS sts 
JOIN student AS s ON s.id = sts.student_id
JOIN subjects AS sub ON sub.id = sts.subjects_id
WHERE s.id = 2
GROUP BY s.id, sub.title
*/

/*
--Список курсов, которые студенту читает преподаватель
SELECT s.id, s.name, s.surname, s.group, sub.title, sub.teacher FROM student_to_subjects AS sts 
JOIN student AS s ON s.id = sts.student_id
JOIN subjects AS sub ON sub.id = sts.subjects_id
WHERE s.id = 1 AND sub.teacher = 'Matematik'
GROUP BY s.id, sub.title, sub.teacher
*/

/*
--Средний балл, который преподаватель ставит студенту
SELECT s.id, s.name, s.surname, s.group, sub.teacher, avg(mark) AS total_mark FROM student_to_subjects AS sts 
JOIN student AS s ON s.id = sts.student_id
JOIN subjects AS sub ON sub.id = sts.subjects_id
WHERE s.id = 1 AND sub.teacher = 'Matematik'
GROUP BY s.id, sub.teacher
ORDER BY total_mark DESC
*/

/*
--Средний балл, который ставит преподаватель
SELECT sub.teacher, avg(mark) AS total_mark FROM student_to_subjects AS sts 
JOIN subjects AS sub ON sub.id = sts.subjects_id
WHERE sub.teacher = 'Matematik'
GROUP BY sub.teacher
*/