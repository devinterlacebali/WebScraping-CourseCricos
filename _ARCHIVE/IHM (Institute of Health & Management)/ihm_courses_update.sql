-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '03407G';

UPDATE courses SET
    course_duration_per_week = 56,
    offshore_tuition_fee = 14000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '096786M';

UPDATE courses SET
    course_duration_per_week = 28,
    offshore_tuition_fee = 7000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '096787K';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 48000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '105600C';

UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '107773K';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 96000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '108842E';

UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 108250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '118071E';

