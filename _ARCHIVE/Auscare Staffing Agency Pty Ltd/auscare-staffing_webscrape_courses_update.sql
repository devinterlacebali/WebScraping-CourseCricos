-- Auscare Staffing Agency Pty Ltd (04055H) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='04055H';

UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 4000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '111051K';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 8000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '111052J';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 9500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '112344M';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 7000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '112345K';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 21000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 900,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '112346J';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 9500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '112347H';
UPDATE courses SET
    course_duration_per_week = 31,
    offshore_tuition_fee = 5000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '112706A';
UPDATE courses SET
    course_duration_per_week = 80,
    offshore_tuition_fee = 15500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 700,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '112707M';
UPDATE courses SET
    course_duration_per_week = 35,
    offshore_tuition_fee = 6500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '115227C';
UPDATE courses SET
    course_duration_per_week = 30,
    offshore_tuition_fee = 6500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '116182C';
UPDATE courses SET
    course_duration_per_week = 80,
    offshore_tuition_fee = 15500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 700,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '118835K';
UPDATE courses SET
    course_duration_per_week = 30,
    offshore_tuition_fee = 6500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '120057G';
