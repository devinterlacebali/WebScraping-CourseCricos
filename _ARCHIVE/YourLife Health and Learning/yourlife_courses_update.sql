-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '03733E';

UPDATE courses SET
    course_duration_per_week = 84,
    offshore_tuition_fee = 26000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 4000,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '111142G';

UPDATE courses SET
    course_duration_per_week = 19,
    offshore_tuition_fee = 6500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 700,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '116167B';

