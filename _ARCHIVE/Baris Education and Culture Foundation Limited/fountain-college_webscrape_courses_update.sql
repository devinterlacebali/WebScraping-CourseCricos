-- Baris Education and Culture Foundation Limited (03370E) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='03370E';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 154000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2645,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'http://fountain.wa.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '0100720';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 52800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 801,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'http://fountain.wa.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '082251B';
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 101800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1828,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'http://fountain.wa.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '094088J';
