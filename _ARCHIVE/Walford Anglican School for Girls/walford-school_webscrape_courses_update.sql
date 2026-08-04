-- Walford Anglican School for Girls (00563J) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='00563J';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 75500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 70000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '004818C';
UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 155000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '040065G';
UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 173000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 168000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '065777B';
