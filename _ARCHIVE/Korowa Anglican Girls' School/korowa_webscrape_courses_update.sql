-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'commence at Korowa in 2027 or 2028.',
    updated_at = NOW()
WHERE cricos_provider_code = '01022G';

-- Secondary Years 7-12 Girls Only
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Secondary Years 7-12 Girls Only</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 223800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1200,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '011306B';

-- Primary Years P-6 (Girls Only)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Primary Years P-6 (Girls Only)</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 261100,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1330,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '018172K';