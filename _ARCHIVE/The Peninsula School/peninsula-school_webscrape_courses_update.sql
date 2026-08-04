UPDATE provider_institution SET
    intake_date = 'January, April, July, October',
    updated_at = NOW()
WHERE cricos_provider_code = '00333A';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 218528,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11782,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '016642A';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '058453C';

