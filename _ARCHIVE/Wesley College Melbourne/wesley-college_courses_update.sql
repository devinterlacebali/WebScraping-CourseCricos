-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00354G';

UPDATE courses SET
    course_duration_per_week = 228,
    offshore_tuition_fee = 345044,
    onshore_tuition_fee = NULL,
    enrolment_fee = 5250,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005466C';

UPDATE courses SET
    course_duration_per_week = 266,
    offshore_tuition_fee = 340846,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '023290F';

