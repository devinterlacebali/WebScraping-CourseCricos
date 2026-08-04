-- Knox Grammar School (00399E) - Web-scraped course data
-- Generated from: https://www.knox.nsw.edu.au

UPDATE provider_institution SET
    intake_date = 'March, June, July, September',
    updated_at = NOW()
WHERE cricos_provider_code = '00399E';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 200280,
    onshore_tuition_fee = NULL,
    enrolment_fee = 15870,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005050E';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 105840,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7230,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005051D';

