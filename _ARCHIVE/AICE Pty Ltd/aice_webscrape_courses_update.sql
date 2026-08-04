-- AICE Pty Ltd (04298M) - Webscrape Update
UPDATE provider_institution SET intake_date='May', updated_at=NOW() WHERE cricos_provider_code='04298M';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 20000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 700,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.aice.edu.au/courses',
    updated_at = NOW()
WHERE cricos_course_code = '116971G';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 9990,
    onshore_tuition_fee = NULL,
    enrolment_fee = 850,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.aice.edu.au/courses',
    updated_at = NOW()
WHERE cricos_course_code = '116972F';
UPDATE courses SET
    course_duration_per_week = 39,
    offshore_tuition_fee = 8990,
    onshore_tuition_fee = NULL,
    enrolment_fee = 850,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.aice.edu.au/courses',
    updated_at = NOW()
WHERE cricos_course_code = '116973E';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 15990,
    onshore_tuition_fee = NULL,
    enrolment_fee = 850,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.aice.edu.au/courses',
    updated_at = NOW()
WHERE cricos_course_code = '116974D';
UPDATE courses SET
    course_duration_per_week = 65,
    offshore_tuition_fee = 16990,
    onshore_tuition_fee = NULL,
    enrolment_fee = 850,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.aice.edu.au/courses',
    updated_at = NOW()
WHERE cricos_course_code = '116975C';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 20000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 700,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.aice.edu.au/courses',
    updated_at = NOW()
WHERE cricos_course_code = '118862G';
