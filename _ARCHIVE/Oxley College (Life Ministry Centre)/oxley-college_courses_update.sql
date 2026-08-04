-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00331C';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 165080,
    onshore_tuition_fee = NULL,
    enrolment_fee = 8350,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '016943K';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 227691,
    onshore_tuition_fee = NULL,
    enrolment_fee = 10150,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '016944J';

