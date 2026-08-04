-- Loreto College (00629G) - Webscrape Update
UPDATE provider_institution SET intake_date='May', updated_at=NOW() WHERE cricos_provider_code='00629G';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 64030,
    onshore_tuition_fee = NULL,
    enrolment_fee = 48420,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.loreto.sa.edu.au/international/',
    updated_at = NOW()
WHERE cricos_course_code = '006548D';
UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 152870,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11120,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.loreto.sa.edu.au/international/',
    updated_at = NOW()
WHERE cricos_course_code = '096450B';
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 114790,
    onshore_tuition_fee = NULL,
    enrolment_fee = 93170,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.loreto.sa.edu.au/international/',
    updated_at = NOW()
WHERE cricos_course_code = '097289J';
