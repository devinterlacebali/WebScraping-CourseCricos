-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '02137M';

-- English for Academic Purposes Program
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>English for Academic Purposes Program</p>',
    course_duration_per_week = 49,
    offshore_tuition_fee = 18720,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '0101685';

-- IELTS Mastery Program
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>IELTS Mastery Program</p>',
    course_duration_per_week = 25,
    offshore_tuition_fee = 9360,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '0101686';

-- Cambridge Mastery Program
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Cambridge Mastery Program</p>',
    course_duration_per_week = 37,
    offshore_tuition_fee = 14590,
    onshore_tuition_fee = NULL,
    enrolment_fee = 550,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '0101687';

-- General English Program
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>General English Program</p>',
    course_duration_per_week = 81,
    offshore_tuition_fee = 31750,
    onshore_tuition_fee = NULL,
    enrolment_fee = 550,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '0101688';

-- English Language Programs for International Students (Beginner to Advanced) (4-56 weeks)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>English Language Programs for International Students (Beginner to Advanced) (4-56 weeks)</p>',
    course_duration_per_week = 56,
    offshore_tuition_fee = 25840,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '060152J';

-- Diploma of Project Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Project Management</p>',
    course_duration_per_week = 66,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '104109M';

-- Diploma of Leadership and Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Leadership and Management</p>',
    course_duration_per_week = 64,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '104145G';

-- Diploma of Business
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Business</p>',
    course_duration_per_week = 76,
    offshore_tuition_fee = 12500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '104773A';

-- Certificate III in Business
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Business</p>',
    course_duration_per_week = 76,
    offshore_tuition_fee = 12500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '104774M';

-- Diploma of Marketing and Communication
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Marketing and Communication</p>',
    course_duration_per_week = 328,
    offshore_tuition_fee = 12500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '104775K';

-- Advanced Diploma of Leadership and Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Leadership and Management</p>',
    course_duration_per_week = 97,
    offshore_tuition_fee = 22480,
    onshore_tuition_fee = NULL,
    enrolment_fee = 480,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '104776J';

-- Certificate IV in Marketing and Communication
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Marketing and Communication</p>',
    course_duration_per_week = 76,
    offshore_tuition_fee = 12500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '104777H';

-- Certificate IV in Business
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Business</p>',
    course_duration_per_week = 76,
    offshore_tuition_fee = 12500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '104778G';

-- Certificate II in Workplace Skills
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate II in Workplace Skills</p>',
    course_duration_per_week = 68,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '105113G';

-- Certificate III in Entrepreneurship and New Business
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Entrepreneurship and New Business</p>',
    course_duration_per_week = 56,
    offshore_tuition_fee = 12480,
    onshore_tuition_fee = NULL,
    enrolment_fee = 480,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '107807E';

-- Advanced Diploma of Marketing and Communication
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Marketing and Communication</p>',
    course_duration_per_week = 100,
    offshore_tuition_fee = 22480,
    onshore_tuition_fee = NULL,
    enrolment_fee = 480,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '107808D';

-- English for Teaching Professionals
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>English for Teaching Professionals</p>',
    course_duration_per_week = 280,
    offshore_tuition_fee = 5850,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '112864J';

-- Diploma of Digital Marketing
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Digital Marketing</p>',
    course_duration_per_week = 66,
    offshore_tuition_fee = 12510,
    onshore_tuition_fee = NULL,
    enrolment_fee = 510,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '116737F';

-- Certificate IV in Environmentally Sustainable Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Environmentally Sustainable Management</p>',
    course_duration_per_week = 54,
    offshore_tuition_fee = 12510,
    onshore_tuition_fee = NULL,
    enrolment_fee = 510,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '116738E';

-- Diploma of Artificial Intelligence (AI)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Artificial Intelligence (AI)</p>',
    course_duration_per_week = 66,
    offshore_tuition_fee = 12510,
    onshore_tuition_fee = NULL,
    enrolment_fee = 510,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117286J';

-- Advanced Diploma of Hospitality Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Hospitality Management</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 16800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 800,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '120081G';

-- Diploma of Hospitality Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Hospitality Management</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 8800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 800,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '120082F';

-- Advanced Diploma of Digital Marketing
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Digital Marketing</p>',
    course_duration_per_week = 76,
    offshore_tuition_fee = 12250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '120083E';

-- Diploma of Digital Marketing
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Digital Marketing</p>',
    course_duration_per_week = 66,
    offshore_tuition_fee = 9250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '120460G';