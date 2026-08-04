-- St Leonard's College (00343K) - Web-scraped course data
-- Generated: from https://www.stleonards.vic.edu.au

-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00343K';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '020074E';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 124974,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1500,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '099424B';

