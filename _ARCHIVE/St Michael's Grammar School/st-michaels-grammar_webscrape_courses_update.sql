-- St Michael's Grammar School (00345G) - Web-scraped course data
-- Generated: from https://www.stmichaels.vic.edu.au

-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'Term 2 (Apr/May)',
    updated_at = NOW()
WHERE cricos_provider_code = '00345G';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '016053M';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '016054K';

