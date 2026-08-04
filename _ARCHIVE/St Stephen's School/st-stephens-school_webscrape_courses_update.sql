-- St Stephen's School (03719C) - Webscrape Update
UPDATE provider_institution SET intake_date='May', updated_at=NOW() WHERE cricos_provider_code='03719C';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 114160,
    onshore_tuition_fee = NULL,
    enrolment_fee = 26840,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.ststephens.wa.edu.au/admissions/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '098324C';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 57080,
    onshore_tuition_fee = NULL,
    enrolment_fee = 13420,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.ststephens.wa.edu.au/admissions/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '098325B';
UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 171605,
    onshore_tuition_fee = NULL,
    enrolment_fee = 32690,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.ststephens.wa.edu.au/admissions/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '108718J';
