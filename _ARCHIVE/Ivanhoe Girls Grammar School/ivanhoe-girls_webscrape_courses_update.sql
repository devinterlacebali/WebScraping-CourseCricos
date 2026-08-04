-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '00974A';

-- Secondary Years 7 - 12
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Secondary Years 7 - 12</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 247592,
    onshore_tuition_fee = NULL,
    enrolment_fee = 12896,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '016611G';

-- Primary Years P - 6
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Primary Years P - 6</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 221464,
    onshore_tuition_fee = NULL,
    enrolment_fee = 10128,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '018621A';