-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '03723G';

-- General English
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>General English</p>',
    course_duration_per_week = 76,
    offshore_tuition_fee = 20890,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '098438D';

-- Diploma of Leadership and Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Leadership and Management</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12650,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '104378A';

-- Certificate IV in Marketing and Communication
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Marketing and Communication</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12650,
    onshore_tuition_fee = NULL,
    enrolment_fee = 650,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '107063G';

-- Diploma of Marketing and Communication
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Marketing and Communication</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12650,
    onshore_tuition_fee = NULL,
    enrolment_fee = 650,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '107064F';

-- Advanced Diploma of Leadership and Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Leadership and Management</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 18850,
    onshore_tuition_fee = NULL,
    enrolment_fee = 850,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '107065E';

-- Advanced Diploma of Marketing and Communication
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Marketing and Communication</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 18850,
    onshore_tuition_fee = NULL,
    enrolment_fee = 850,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '107066D';

-- Certificate III in Individual Support
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Individual Support</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 13250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '116372H';

-- Certificate IV in Ageing Support
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Ageing Support</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 19750,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1750,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '116423B';

-- Diploma of Community Services
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Community Services</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 26250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '116424A';

-- Graduate Diploma of Management (Learning)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Graduate Diploma of Management (Learning)</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 26250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '116425M';

-- Diploma of Community Services
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Community Services</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 26250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '118780J';

-- Certificate III in Cabinet Making and Timber Technology
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Cabinet Making and Timber Technology</p>',
    course_duration_per_week = 96,
    offshore_tuition_fee = 38300,
    onshore_tuition_fee = NULL,
    enrolment_fee = 5300,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '119791J';

-- Certificate III in Carpentry
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Carpentry</p>',
    course_duration_per_week = 66,
    offshore_tuition_fee = 26300,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3800,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '119792H';

-- Certificate III in Painting and Decorating
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Painting and Decorating</p>',
    course_duration_per_week = 66,
    offshore_tuition_fee = 26300,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3800,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '119793G';

-- Diploma of Building and Construction (Building)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Building and Construction (Building)</p>',
    course_duration_per_week = 66,
    offshore_tuition_fee = 26300,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3800,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '119794F';