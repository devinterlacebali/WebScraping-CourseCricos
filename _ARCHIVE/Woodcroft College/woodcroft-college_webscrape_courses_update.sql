-- Woodcroft College (01645K) - Webscrape Update
UPDATE provider_institution SET intake_date='May', updated_at=NOW() WHERE cricos_provider_code='01645K';

UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 23000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 25170,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'AEAS test required. Academic entry requirements apply.',
    apply_form = 'https://www.woodcroft.sa.edu.au/enrolment/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '057395E';
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 94000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 100910,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'AEAS test required. Academic entry requirements apply.',
    apply_form = 'https://www.woodcroft.sa.edu.au/enrolment/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '096554E';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 47000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 53760,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'AEAS test required. Academic entry requirements apply.',
    apply_form = 'https://www.woodcroft.sa.edu.au/enrolment/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '096555D';
UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 126000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 14500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'AEAS test required. Academic entry requirements apply.',
    apply_form = 'https://www.woodcroft.sa.edu.au/enrolment/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '097142F';
