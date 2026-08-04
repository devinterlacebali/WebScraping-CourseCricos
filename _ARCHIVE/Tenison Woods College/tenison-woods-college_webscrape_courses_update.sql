-- Tenison Woods College (01751G) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='01751G';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 37800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1450,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '026373A';
UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 94500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1100,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '091930D';
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 75600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1100,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '097227A';
