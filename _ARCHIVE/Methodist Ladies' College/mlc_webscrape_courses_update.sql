UPDATE provider_institution SET
    intake_date = 'January, April, July, October',
    updated_at = NOW()
WHERE cricos_provider_code = '00325A';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 270360,
    onshore_tuition_fee = NULL,
    enrolment_fee = 38660,
    materials_fee = NULL,
    entry_requirements = 'AEAS testing: Years 4-6 (61+), Years 7-9 (71+), Years 10-12 (80+). School reports and interview.',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005384E';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 301140,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1110,
    materials_fee = NULL,
    entry_requirements = 'AEAS testing: Years 4-6 (61+), Years 7-9 (71+), Years 10-12 (80+). School reports and interview.',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '027785F';

