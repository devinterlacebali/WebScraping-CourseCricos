-- Toorak College (00349D) - Web-scraped course data
-- Generated: from https://www.toorakcollege.vic.edu.au

-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'May',
    updated_at = NOW()
WHERE cricos_provider_code = '00349D';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 240324,
    onshore_tuition_fee = NULL,
    enrolment_fee = 19470,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005454G';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 70768,
    onshore_tuition_fee = NULL,
    enrolment_fee = 8864,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '097816B';

