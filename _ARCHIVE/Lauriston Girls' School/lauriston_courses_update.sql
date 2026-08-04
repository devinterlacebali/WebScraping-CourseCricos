-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00152F';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 310000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 5000,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005356J';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 90000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1700,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '015713K';

