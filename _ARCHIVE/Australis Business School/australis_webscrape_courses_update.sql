-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'Intake-and-Semester-dates-2026-2027.',
    updated_at = NOW()
WHERE cricos_provider_code = '04289A';

-- Bachelor of Business (Accounting)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Bachelor of Business (Accounting)</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 55800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '116856K';

-- Graduate Diploma of Early Childhood Education
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Graduate Diploma of Early Childhood Education</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 29100,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117596F';

-- Master of Business Administration
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Master of Business Administration</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 45050,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '118355D';

-- Master of Business Research
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Master of Business Research</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 56250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '119126J';