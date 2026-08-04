-- St Peter's Collegiate Girls' School (00373D) - Web-scraped course data
-- Generated from: https://www.stpetersgirls.sa.edu.au

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00373D';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 77800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6000,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '004814G';

UPDATE courses SET
    course_duration_per_week = 416,
    offshore_tuition_fee = 234400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 8000,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '020167M';

UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 110700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 4000,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '052969A';

