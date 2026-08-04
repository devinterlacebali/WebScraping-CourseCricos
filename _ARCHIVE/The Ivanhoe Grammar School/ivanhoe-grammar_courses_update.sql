-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00147C';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 225460,
    onshore_tuition_fee = NULL,
    enrolment_fee = 37142,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005345A';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 205896,
    onshore_tuition_fee = NULL,
    enrolment_fee = 18569,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '011398D';

