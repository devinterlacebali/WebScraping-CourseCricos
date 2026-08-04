-- Our Lady of the Sacred Heart College (02209M) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='02209M';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 64950,
    onshore_tuition_fee = NULL,
    enrolment_fee = 114395,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.olsh.catholic.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '096726A';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 33000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 48100,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.olsh.catholic.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '096727M';
