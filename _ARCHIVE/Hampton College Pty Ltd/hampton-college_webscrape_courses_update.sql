-- Hampton College Pty Ltd (04346H) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='04346H';

UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 15000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1250,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '117583M';
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 22500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1750,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '117584K';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 30000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2250,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '117585J';
UPDATE courses SET
    course_duration_per_week = 40,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 650,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '117586H';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 30000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2250,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '118867B';
