-- Skills Training College Pty Ltd (03884A) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='03884A';

UPDATE courses SET
    course_duration_per_week = 1,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '104639G';
UPDATE courses SET
    course_duration_per_week = 7,
    offshore_tuition_fee = 999,
    onshore_tuition_fee = NULL,
    enrolment_fee = 200,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '108132B';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 8300,
    onshore_tuition_fee = NULL,
    enrolment_fee = 700,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '114362D';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 20150,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3850,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '118067A';
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 11300,
    onshore_tuition_fee = NULL,
    enrolment_fee = 700,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '118332M';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 20150,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3850,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '118799J';
