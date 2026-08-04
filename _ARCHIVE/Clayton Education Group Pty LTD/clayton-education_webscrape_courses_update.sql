-- Clayton Education Group Pty LTD (03857D) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='03857D';

UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 24000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '102468D';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 14000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '104417K';
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 24000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '109583M';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 18000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '109895F';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 28000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2350,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '112575G';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 28000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2350,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '112576F';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 28000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2350,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '112577E';
