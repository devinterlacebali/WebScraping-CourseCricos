-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00348E';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '016006G';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 183000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3668,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '095236E';

