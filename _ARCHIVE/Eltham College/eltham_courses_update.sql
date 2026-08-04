-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00138D';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 171828,
    onshore_tuition_fee = NULL,
    enrolment_fee = 8868,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '016363G';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 215420,
    onshore_tuition_fee = NULL,
    enrolment_fee = 15680,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '016364G';

