-- St George College Inc (02799F) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='02799F';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 133000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 9100,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.sgc.sa.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '096720G';
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 79000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 5200,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.sgc.sa.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '096721F';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 42000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2600,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.sgc.sa.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '096722E';
