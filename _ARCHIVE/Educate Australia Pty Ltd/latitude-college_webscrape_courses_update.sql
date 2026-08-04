-- Educate Australia Pty Ltd (04033C) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='04033C';

UPDATE courses SET
    course_duration_per_week = 70,
    offshore_tuition_fee = 11500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.latitude.edu.au/courses',
    updated_at = NOW()
WHERE cricos_course_code = '110596G';
UPDATE courses SET
    course_duration_per_week = 70,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.latitude.edu.au/courses',
    updated_at = NOW()
WHERE cricos_course_code = '111452D';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 16500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.latitude.edu.au/courses',
    updated_at = NOW()
WHERE cricos_course_code = '113075H';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 14500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.latitude.edu.au/courses',
    updated_at = NOW()
WHERE cricos_course_code = '113090J';
UPDATE courses SET
    course_duration_per_week = 90,
    offshore_tuition_fee = 14500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.latitude.edu.au/courses',
    updated_at = NOW()
WHERE cricos_course_code = '118447M';
UPDATE courses SET
    course_duration_per_week = 55,
    offshore_tuition_fee = 15500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.latitude.edu.au/courses',
    updated_at = NOW()
WHERE cricos_course_code = '120424M';
