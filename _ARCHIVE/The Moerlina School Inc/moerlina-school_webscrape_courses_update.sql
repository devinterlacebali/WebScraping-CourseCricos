-- The Moerlina School Inc. (02527G) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='02527G';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 129388,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3550,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '049690J';
