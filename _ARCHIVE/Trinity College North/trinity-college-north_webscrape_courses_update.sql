-- Trinity College North (00374C) - Web-scraped course data
-- Generated from: https://www.trinity.sa.edu.au

UPDATE provider_institution SET
    intake_date = 'August',
    updated_at = NOW()
WHERE cricos_provider_code = '00374C';

UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 66360,
    onshore_tuition_fee = NULL,
    enrolment_fee = 59000,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '004815F';

