-- Fox Endeavours Pty Ltd (03920B) - Webscrape Update
UPDATE provider_institution SET intake_date='May, July, September, October', updated_at=NOW() WHERE cricos_provider_code='03920B';

UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 33402,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3900,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'http://www.fox.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '113088C';
UPDATE courses SET
    course_duration_per_week = 28,
    offshore_tuition_fee = 7500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1300,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'http://www.fox.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '113089B';
