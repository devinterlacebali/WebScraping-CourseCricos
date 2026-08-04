-- Seymour College Inc (00628G) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='00628G';

UPDATE courses SET
    course_duration_per_week = 416,
    offshore_tuition_fee = 292710,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '026371C';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 92820,
    onshore_tuition_fee = NULL,
    enrolment_fee = 64740,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '039622D';
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 137830,
    onshore_tuition_fee = NULL,
    enrolment_fee = 97035,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '097228M';
