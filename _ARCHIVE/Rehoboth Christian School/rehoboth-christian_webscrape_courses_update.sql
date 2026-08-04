-- Rehoboth Christian School (01984B) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='01984B';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 132346,
    onshore_tuition_fee = NULL,
    enrolment_fee = 5870,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.rehoboth.wa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '0101458';
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 100028,
    onshore_tuition_fee = NULL,
    enrolment_fee = 4055,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.rehoboth.wa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '0101459';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 56685,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2704,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.rehoboth.wa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '0101460';
