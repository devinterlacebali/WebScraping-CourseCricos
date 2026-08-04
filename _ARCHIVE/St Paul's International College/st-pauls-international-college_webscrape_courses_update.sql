-- St Paul's International College (00379J) - Web-scraped course data
-- Generated from: https://www.spic.nsw.edu.au

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00379J';

UPDATE courses SET
    course_duration_per_week = 50,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '031263J';

UPDATE courses SET
    course_duration_per_week = 80,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '039233F';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 76300,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6411,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '063101G';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 44500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2456,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '063102F';

UPDATE courses SET
    course_duration_per_week = 10,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '064612J';

