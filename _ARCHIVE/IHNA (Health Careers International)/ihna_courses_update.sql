-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '03386G';

UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '093193E';

UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 7700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '103695G';

UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 35700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '108323F';

UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 5700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '112921E';

UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 17700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '112923C';

UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 7700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '120052A';

UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 17700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '120058F';

