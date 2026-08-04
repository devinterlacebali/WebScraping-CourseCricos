-- ANZ College Pty Ltd (03997C) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='03997C';

UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 16000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1750,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '109623H';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 11000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1750,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '109921J';
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 16000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '110573C';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 22000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '110574B';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 23000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '114135D';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 13500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '114136C';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 14500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '114137B';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 24500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '116285G';
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 18000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '116516H';
