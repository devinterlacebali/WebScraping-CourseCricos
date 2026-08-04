-- Prescott College Southern (01536D) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='01536D';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 133532,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3876,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.prescott.sa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '021480E';
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 96632,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2744,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.prescott.sa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '075800C';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 50464,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1576,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.prescott.sa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '089613B';
