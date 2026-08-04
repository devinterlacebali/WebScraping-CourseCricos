-- Saint Ignatius' College (00603F) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='00603F';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 49254,
    onshore_tuition_fee = NULL,
    enrolment_fee = 9696,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.ignatius.sa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '006065A';
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 98508,
    onshore_tuition_fee = NULL,
    enrolment_fee = 19392,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.ignatius.sa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '026209B';
