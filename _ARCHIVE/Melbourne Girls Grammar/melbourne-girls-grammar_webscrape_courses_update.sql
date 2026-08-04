-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, April, July, October',
    updated_at = NOW()
WHERE cricos_provider_code = '00322D';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 329000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 50570,
    materials_fee = NULL,
    entry_requirements = 'AEAS test results, school reports, English proficiency',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '016077C';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 329000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 47750,
    materials_fee = NULL,
    entry_requirements = 'AEAS test results, school reports, English proficiency',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '021052C';

