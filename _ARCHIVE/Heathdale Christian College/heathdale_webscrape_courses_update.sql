-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '00578B';

-- Secondary Years 7-12
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Secondary Years 7-12</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 158820,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1110,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '013017F';

-- Primary Years P - 6
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Primary Years P - 6</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 161102,
    onshore_tuition_fee = NULL,
    enrolment_fee = 610,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '053839C';