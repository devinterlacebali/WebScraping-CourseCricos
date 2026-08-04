-- Westminster School Inc (00602G) - Webscrape Update
UPDATE provider_institution SET intake_date='July', updated_at=NOW() WHERE cricos_provider_code='00602G';

UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 155374,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6992,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.westminster.sa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '096654A';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 82132,
    onshore_tuition_fee = NULL,
    enrolment_fee = 796,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.westminster.sa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '096655M';
UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 202192,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7016,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.westminster.sa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '114586K';
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 155374,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6992,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.westminster.sa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '114587J';
