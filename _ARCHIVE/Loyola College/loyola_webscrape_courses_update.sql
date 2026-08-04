-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '00558F';

-- Secondary Senior Years 7 - 12 VCE
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Secondary Senior Years 7 - 12 VCE</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 83640,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '005362M';