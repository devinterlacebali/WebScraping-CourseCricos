-- St Dominic's Priory College (01102G) - Webscrape Update
UPDATE provider_institution SET intake_date='February, May', updated_at=NOW() WHERE cricos_provider_code='01102G';

UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 92000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 60000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://stdominics.sa.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '013901M';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 48000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 31600,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://stdominics.sa.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '013902K';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 42000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 30600,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://stdominics.sa.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '054985G';
