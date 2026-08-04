-- Woodstock International Pty Ltd (03999A) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='03999A';

UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 16350,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '109184D';
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 9350,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '109185C';
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 9350,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '109186B';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 9850,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '109187A';
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 12850,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '109188M';
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 9350,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '120337K';
