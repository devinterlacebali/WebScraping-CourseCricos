-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '00649C';

-- Secondary Years 7 - 12
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Secondary Years 7 - 12</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 43945,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1720,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '016259G';

-- Primary Years P - 6
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Primary Years P - 6</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 206500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1500,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '041900B';