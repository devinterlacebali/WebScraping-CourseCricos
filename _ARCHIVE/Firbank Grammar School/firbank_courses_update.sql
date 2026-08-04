-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00140K';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 277584,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7000,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005315G';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 239750,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7000,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '011303E';

