-- Victory Life International Bible Training Ctr (02200J) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='02200J';

UPDATE courses SET
    course_duration_per_week = 48,
    offshore_tuition_fee = 5200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 450,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '107582F';
UPDATE courses SET
    course_duration_per_week = 48,
    offshore_tuition_fee = 5650,
    onshore_tuition_fee = NULL,
    enrolment_fee = 450,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '107583E';
