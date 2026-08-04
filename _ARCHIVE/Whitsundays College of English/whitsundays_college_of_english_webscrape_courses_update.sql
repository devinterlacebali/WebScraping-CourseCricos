-- QLD Provider: Whitsundays College of English (02500G)
-- Courses sourced from CRICOS register (5 courses)

UPDATE provider_institution SET
    intake_date = 'January, February, April, July, October',
    updated_at = NOW()
WHERE cricos_provider_code = '02500G';

UPDATE courses SET
    course_description = '<h4>General Intensive English</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 50,
    offshore_tuition_fee = 12700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.wce.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '048122E';
UPDATE courses SET
    course_description = '<h4>International Secondary School Bridging Programme</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 48,
    offshore_tuition_fee = 17000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.wce.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '048123D';
UPDATE courses SET
    course_description = '<h4>Cambridge B2 First (FCE) Preparation</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 12,
    offshore_tuition_fee = 3800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.wce.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '048124C';
UPDATE courses SET
    course_description = '<h4>English for Tertiary Study</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 24,
    offshore_tuition_fee = 6200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.wce.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '048125B';
UPDATE courses SET
    course_description = '<h4>IELTS Preparation</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 12,
    offshore_tuition_fee = 3200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.wce.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '060147F';