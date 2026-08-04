-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00344J';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 251865,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2400,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '019219C';

