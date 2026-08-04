-- Muirden Senior Secondary College (00366C) - Web-scraped course data
-- Generated from: https://muirden.sa.edu.au

UPDATE provider_institution SET
    intake_date = 'May, December',
    updated_at = NOW()
WHERE cricos_provider_code = '00366C';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 38240,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '004794F';

