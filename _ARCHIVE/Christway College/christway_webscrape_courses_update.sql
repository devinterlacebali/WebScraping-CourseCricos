-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '01894D';

-- Primary Years P - 6
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Primary Years P - 6</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 76475,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English-Language-Proficiency-and-Educational-Qualifications-Policy.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '030389C';

-- Secondary Years 7 - 12
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Secondary Years 7 - 12</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 70480,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English-Language-Proficiency-and-Educational-Qualifications-Policy.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '046659K';