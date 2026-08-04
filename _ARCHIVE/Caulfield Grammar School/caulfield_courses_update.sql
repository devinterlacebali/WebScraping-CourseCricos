-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00136F';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 251000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 15000,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '017557A';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 228000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 15000,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '017558M';

