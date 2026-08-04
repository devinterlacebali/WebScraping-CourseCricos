-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00149A';

UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 299498,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005349G';

UPDATE courses SET
    course_duration_per_week = 273,
    offshore_tuition_fee = 321748,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '019777F';

