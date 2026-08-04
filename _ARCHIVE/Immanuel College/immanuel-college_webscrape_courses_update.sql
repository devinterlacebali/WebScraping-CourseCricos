-- Immanuel College (00362G) - Web-scraped course data
-- Generated from: https://www.immanuel.sa.edu.au

UPDATE provider_institution SET
    intake_date = 'May',
    updated_at = NOW()
WHERE cricos_provider_code = '00362G';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 75363,
    onshore_tuition_fee = NULL,
    enrolment_fee = 63572,
    materials_fee = NULL,
    entry_requirements = 'AEAS test required (18)

English language proficiency required

A recognised English language test and entry interview must be completed prior to an offer of enrolment. This can be undertaken in the student’s home country through the Australian Education Assessment Services or an alternate recognised English prof',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '004780A';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 150726,
    onshore_tuition_fee = NULL,
    enrolment_fee = 127145,
    materials_fee = NULL,
    entry_requirements = 'AEAS test required (18)

English language proficiency required

A recognised English language test and entry interview must be completed prior to an offer of enrolment. This can be undertaken in the student’s home country through the Australian Education Assessment Services or an alternate recognised English prof',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '052966D';

