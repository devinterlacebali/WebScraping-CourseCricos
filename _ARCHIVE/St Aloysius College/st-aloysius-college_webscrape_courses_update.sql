-- St Aloysius College (00371F) - Web-scraped course data
-- Generated from: https://www.sac.sa.edu.au

UPDATE provider_institution SET
    intake_date = 'Term 3',
    updated_at = NOW()
WHERE cricos_provider_code = '00371F';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 94000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 72000,
    materials_fee = NULL,
    entry_requirements = 'Thank you for your interest in St Aloysius College, to submit an Application for Enrolment, please follow the below process:',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '004807F';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 53000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 48000,
    materials_fee = NULL,
    entry_requirements = 'Thank you for your interest in St Aloysius College, to submit an Application for Enrolment, please follow the below process:',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '004808E';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 140000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 168000,
    materials_fee = NULL,
    entry_requirements = 'Thank you for your interest in St Aloysius College, to submit an Application for Enrolment, please follow the below process:',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '020166A';

