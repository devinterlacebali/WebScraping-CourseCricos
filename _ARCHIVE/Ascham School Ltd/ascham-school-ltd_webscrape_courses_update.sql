-- Ascham School Ltd (00380E) - Web-scraped course data
-- Generated from: https://www.ascham.nsw.edu.au

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00380E';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 132100,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7400,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '004994J';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 69000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7400,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '007713K';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 171500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7000,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '074001J';

