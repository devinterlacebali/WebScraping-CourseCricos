-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '00557G';

-- Secondary Years 7 - 12
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Secondary Years 7 - 12</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 260310,
    onshore_tuition_fee = NULL,
    enrolment_fee = 94650,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '005286G';

-- Primary Years (Grade 5 and 6)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Primary Years (Grade 5 and 6)</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 45000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '093157J';