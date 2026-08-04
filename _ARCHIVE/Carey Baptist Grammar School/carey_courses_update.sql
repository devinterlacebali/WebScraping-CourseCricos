-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00135G';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 211338,
    onshore_tuition_fee = NULL,
    enrolment_fee = 18480,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005308F';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 181528,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11616,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '013010B';

