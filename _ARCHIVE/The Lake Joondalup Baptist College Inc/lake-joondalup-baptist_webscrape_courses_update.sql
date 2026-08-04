-- The Lake Joondalup Baptist College Inc (01529C) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='01529C';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 142746,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.ljbc.wa.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '038919F';
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 122404,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6800,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.ljbc.wa.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '094549G';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 61202,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3400,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.ljbc.wa.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '094550C';
