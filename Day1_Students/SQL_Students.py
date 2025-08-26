#Creating Database,Table And Inserting Values

#Step 1
CREATE DATABASE practice;
USE practice;

#Step 2
CREATE TABLE students (
  Name VARCHAR(50),
  Age INT,
  Gender ENUM('Male','Female'),
  Marks INT,
  Subject VARCHAR(50)
);

#Step 3
INSERT INTO students (Name, Age, Gender, Marks, Subject) VALUES
('Amit',18,'Male',85,'Math'),
('Rohit',19,'Male',78,'Science'),
('Priya',18,'Female',92,'Math'),
('Sneha',20,'Female',88,'English'),
('Karan',21,'Male',76,'Science'),
('Meera',19,'Female',95,'English'),
('Arjun',22,'Male',67,'Math'),
('Riya',20,'Female',80,'Science'),
('Kabir',21,'Male',90,'English'),
('Neha',18,'Female',72,'Math');

#Run Queries

#Top 5 Students with Highest Marks
SELECT Name, Marks 
FROM students 
ORDER BY Marks DESC 
LIMIT 5;

#Average Marks Per Subject
SELECT Subject, AVG(Marks) 
FROM students 
GROUP BY Subject;

#Students with Marks > 85
SELECT * 
FROM students 
WHERE Marks > 85;

#Exit MySQL
exit;

