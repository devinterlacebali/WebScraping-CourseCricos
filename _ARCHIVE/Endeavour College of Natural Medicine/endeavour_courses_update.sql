-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00231G';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 79000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11000,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '028648G';

UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 64500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 8500,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '089452C';

UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 66000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6500,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '106485D';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 88000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 8500,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '106486C';

UPDATE courses SET
    course_duration_per_week = 108,
    offshore_tuition_fee = 33000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 4500,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '106487B';

