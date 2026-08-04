-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00150G';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 306212,
    onshore_tuition_fee = NULL,
    enrolment_fee = 35376,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '001105E';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 351341,
    onshore_tuition_fee = NULL,
    enrolment_fee = 42460,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '011348C';

