-- Masada College (00401E) - Web-scraped course data
-- Generated from: https://www.masada.nsw.edu.au

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00401E';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 174405,
    onshore_tuition_fee = NULL,
    enrolment_fee = 20853,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005057J';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 99645,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11109,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005058G';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 223545,
    onshore_tuition_fee = NULL,
    enrolment_fee = 31532,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '021164F';

