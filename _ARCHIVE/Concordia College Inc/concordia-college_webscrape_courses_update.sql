-- Concordia College Inc (00360J) - Web-scraped course data
-- Generated: from https://www.concordia.sa.edu.au

-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'May',
    updated_at = NOW()
WHERE cricos_provider_code = '00360J';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 106000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11020,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '004774K';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 53000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 5460,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '004775J';

UPDATE courses SET
    course_duration_per_week = 416,
    offshore_tuition_fee = 122500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 9700,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '094906B';

