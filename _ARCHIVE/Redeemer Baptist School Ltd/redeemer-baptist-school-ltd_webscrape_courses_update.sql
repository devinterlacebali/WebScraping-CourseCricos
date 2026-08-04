-- Redeemer Baptist School Ltd (00415K) - Web-scraped course data
-- Generated from: https://www.redeemer.nsw.edu.au

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00415K';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 115520,
    onshore_tuition_fee = NULL,
    enrolment_fee = 8320,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005105F';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 62720,
    onshore_tuition_fee = NULL,
    enrolment_fee = 10285,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005106E';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 133840,
    onshore_tuition_fee = NULL,
    enrolment_fee = 5880,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '008284G';

