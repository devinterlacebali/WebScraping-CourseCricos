-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '01100K';

-- Secondary Years 7 -12
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Secondary Years 7 -12</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 194244,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '013879D';