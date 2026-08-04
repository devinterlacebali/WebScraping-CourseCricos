-- Prescott College (01611J) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='01611J';

UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 66300,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.prescott.sa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '023379G';
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 78240,
    onshore_tuition_fee = NULL,
    enrolment_fee = 12440,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.prescott.sa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '096703G';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 41300,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6220,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.prescott.sa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '096704G';
