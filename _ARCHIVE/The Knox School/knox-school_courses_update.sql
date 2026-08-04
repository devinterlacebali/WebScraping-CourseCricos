-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00151G';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 214270,
    onshore_tuition_fee = NULL,
    enrolment_fee = 14208,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005355K';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 191514,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11934,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '016939F';

