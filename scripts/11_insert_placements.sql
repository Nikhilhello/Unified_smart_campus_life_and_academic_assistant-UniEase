-- ============================================
-- INSERT PLACEMENT OPPORTUNITIES
-- ============================================

INSERT INTO campus_placement (company_name, job_title, job_type, description, eligibility, required_skills, package, application_deadline, interview_date, posted_by_id, created_at)
VALUES
('Google', 'Software Engineer - Full Stack', 'fulltime',
 'Join Google as a Full Stack Software Engineer to work on cutting-edge projects that impact billions of users worldwide. You will design, develop, test, deploy, maintain, and enhance software solutions.',
 'B.Tech/M.Tech in Computer Science or related field with minimum 7.5 CGPA. No active backlogs.',
 'Python, Java, C++, Data Structures, Algorithms, System Design, Cloud Computing (GCP/AWS)',
 '₹45 LPA - ₹55 LPA', '2024-03-20', '2024-04-05', @admin_id, DATE_SUB(NOW(), INTERVAL 5 DAY)),

('Microsoft', 'Software Development Engineer', 'fulltime',
 'Microsoft is seeking talented SDEs to join our Azure cloud platform team. Work on distributed systems and scalable cloud infrastructure.',
 'B.Tech/M.Tech with minimum 7.0 CGPA. Strong programming skills required.',
 'C++, C#, .NET, Azure, Microservices, RESTful APIs, SQL',
 '₹42 LPA - ₹48 LPA', '2024-03-22', '2024-04-08', @admin_id, DATE_SUB(NOW(), INTERVAL 3 DAY)),

('Amazon', 'SDE Intern - Summer 2024', 'internship',
 'Amazon Web Services is looking for SDE interns to work on innovative cloud solutions. 3-month internship with possibility of full-time conversion.',
 'Pre-final year students (B.Tech 3rd year) with minimum 7.0 CGPA.',
 'Java/Python, Data Structures, Algorithms, OOP, Linux',
 '₹80,000 per month + benefits', '2024-03-18', '2024-04-01', @admin_id, DATE_SUB(NOW(), INTERVAL 7 DAY)),

('Adobe', 'Software Engineer - Frontend', 'fulltime',
 'Join Adobe''s Creative Cloud team to build next-generation creative tools used by millions of designers and artists worldwide.',
 'B.Tech/M.Tech with minimum 7.5 CGPA. Strong frontend development experience.',
 'React, JavaScript/TypeScript, HTML5, CSS3, Redux, Webpack',
 '₹38 LPA - ₹42 LPA', '2024-03-25', '2024-04-10', @admin_id, DATE_SUB(NOW(), INTERVAL 2 DAY)),

('Goldman Sachs', 'Technology Analyst', 'fulltime',
 'Work on critical financial systems and trading platforms at one of the world''s leading investment banks.',
 'B.Tech/M.Tech with minimum 8.0 CGPA. Strong analytical and programming skills.',
 'Java, Python, SQL, Data Structures, Algorithms, Financial Markets knowledge',
 '₹35 LPA - ₹40 LPA', '2024-03-28', '2024-04-12', @admin_id, DATE_SUB(NOW(), INTERVAL 1 DAY));

-- Get placement IDs
SET @placement1_id = (SELECT id FROM campus_placement WHERE company_name = 'Google');
SET @placement2_id = (SELECT id FROM campus_placement WHERE company_name = 'Amazon');

-- Insert placement applications
INSERT INTO campus_placementapplication (placement_id, user_id, resume, cover_letter, status, applied_at)
VALUES
(@placement1_id, @student1_id, 'resumes/rahul_sharma_resume.pdf',
 'I am writing to express my strong interest in the Software Engineer position at Google. With a solid foundation in full-stack development and a passion for creating scalable solutions, I am excited about the opportunity to contribute to Google''s innovative projects. My academic projects and internship experience have equipped me with strong skills in Python, Java, and cloud technologies. I am particularly interested in working on distributed systems and would love to be part of the team that impacts billions of users.',
 'applied', DATE_SUB(NOW(), INTERVAL 2 DAY)),

(@placement2_id, @student1_id, 'resumes/rahul_sharma_resume.pdf',
 'I am excited to apply for the SDE Intern position at Amazon Web Services. As a pre-final year Computer Science student with strong programming skills and cloud computing knowledge, I am eager to contribute to AWS''s innovative cloud solutions. My coursework in data structures, algorithms, and system design has prepared me well for this role. I am particularly interested in learning about scalable cloud infrastructure and distributed systems.',
 'shortlisted', DATE_SUB(NOW(), INTERVAL 4 DAY));
