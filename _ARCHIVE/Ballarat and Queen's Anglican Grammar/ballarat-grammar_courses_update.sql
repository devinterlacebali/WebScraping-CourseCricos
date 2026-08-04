-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00129E';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 304390,
    onshore_tuition_fee = NULL,
    enrolment_fee = 10000,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '017448F';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 165800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 5000,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '087632D';

