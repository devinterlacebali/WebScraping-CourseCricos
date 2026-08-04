-- Wilderness School (00375B) - Web-scraped course data
-- Generated from: https://wilderness.com.au

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00375B';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 180161,
    onshore_tuition_fee = NULL,
    enrolment_fee = 140540,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '004821G';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 96992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 71570,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '004822G';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 237956,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11805,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '058392M';

