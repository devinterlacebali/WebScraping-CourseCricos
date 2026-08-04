-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'intakes, scholarships and bursaries, and how to apply for your child to attend.',
    updated_at = NOW()
WHERE cricos_provider_code = '00977J';

-- Secondary Years 7 - 12
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Secondary Years 7 - 12</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 243540,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '006536G';