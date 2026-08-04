-- Blackfriars Priory School (02485B) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='02485B';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 98920,
    onshore_tuition_fee = NULL,
    enrolment_fee = 10000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.blackfriars.sa.edu.au/enrolment/international',
    updated_at = NOW()
WHERE cricos_course_code = '096656K';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 57810,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7600,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.blackfriars.sa.edu.au/enrolment/international',
    updated_at = NOW()
WHERE cricos_course_code = '096657J';
