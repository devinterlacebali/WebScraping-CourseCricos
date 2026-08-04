-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00018A';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 90720,
    onshore_tuition_fee = NULL,
    enrolment_fee = 8974,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '0101626';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 63520,
    onshore_tuition_fee = NULL,
    enrolment_fee = 5278,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '0101627';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 63520,
    onshore_tuition_fee = NULL,
    enrolment_fee = 5278,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '0101628';

UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 52320,
    onshore_tuition_fee = NULL,
    enrolment_fee = 4746,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '035548G';

UPDATE courses SET
    course_duration_per_week = 416,
    offshore_tuition_fee = 103680,
    onshore_tuition_fee = NULL,
    enrolment_fee = 10179,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '045804C';

UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 52320,
    onshore_tuition_fee = NULL,
    enrolment_fee = 4746,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '065441D';

