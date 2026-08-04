-- Golden Wattle Group Pty Ltd (03551M) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='03551M';

UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 7600,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '104305G';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 10000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2250,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '106030B';
UPDATE courses SET
    course_duration_per_week = 35,
    offshore_tuition_fee = 6500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '109475D';
UPDATE courses SET
    course_duration_per_week = 30,
    offshore_tuition_fee = 6900,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '109518J';
UPDATE courses SET
    course_duration_per_week = 58,
    offshore_tuition_fee = 13000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '109743M';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '109854D';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 17000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '110136B';
UPDATE courses SET
    course_duration_per_week = 30,
    offshore_tuition_fee = 7900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '110237H';
UPDATE courses SET
    course_duration_per_week = 30,
    offshore_tuition_fee = 7900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '110238G';
