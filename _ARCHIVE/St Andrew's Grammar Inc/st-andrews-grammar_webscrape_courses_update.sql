-- St Andrew's Grammar Inc. (01488G) - Webscrape Update
UPDATE provider_institution SET intake_date='May', updated_at=NOW() WHERE cricos_provider_code='01488G';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 129264,
    onshore_tuition_fee = NULL,
    enrolment_fee = 5560,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'AEAS test required. Academic entry requirements apply.',
    apply_form = 'https://www.sag.wa.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '099697K';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 63736,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2780,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'AEAS test required. Academic entry requirements apply.',
    apply_form = 'https://www.sag.wa.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '099698J';
UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 211211,
    onshore_tuition_fee = NULL,
    enrolment_fee = 9730,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'AEAS test required. Academic entry requirements apply.',
    apply_form = 'https://www.sag.wa.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '104950M';
