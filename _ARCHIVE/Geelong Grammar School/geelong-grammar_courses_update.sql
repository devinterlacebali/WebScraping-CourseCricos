-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00143G';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 458014,
    onshore_tuition_fee = NULL,
    enrolment_fee = 24166,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005326D';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 312410,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7370,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '015229M';

