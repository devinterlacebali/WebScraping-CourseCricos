-- The Governors of Hale School (00438C) - Course updates
-- Source: https://www.hale.wa.edu.au/international-students/

UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00438C';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>The Governors of Hale School - Primary Education Years 1-6 (Accompanied By Parent)</h4><p>The Governors of Hale School offers primary education years 1-6 (accompanied by parent) for international students. Located in Perth, Western Australia. CRICOS course code: 018383K.</p></p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 247750,
    onshore_tuition_fee = NULL,
    enrolment_fee = 16174,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.hale.wa.edu.au/international-students/',
    updated_at = NOW()
WHERE cricos_course_code = '018383K';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>The Governors of Hale School - Secondary Education Years 7-10</h4><p>The Governors of Hale School offers secondary education years 7-10 for international students. Located in Perth, Western Australia. CRICOS course code: 099681G.</p></p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 172160,
    onshore_tuition_fee = NULL,
    enrolment_fee = 20864,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.hale.wa.edu.au/international-students/',
    updated_at = NOW()
WHERE cricos_course_code = '099681G';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>The Governors of Hale School - Senior Secondary Certificate of Education Years 11-12</h4><p>The Governors of Hale School offers senior secondary certificate of education years 11-12 for international students. Located in Perth, Western Australia. CRICOS course code: 099682F.</p></p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 86080,
    onshore_tuition_fee = NULL,
    enrolment_fee = 10609,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts. English proficiency. IELTS 5.5+ or equivalent.</p>',
    apply_form = 'https://www.hale.wa.edu.au/international-students/',
    updated_at = NOW()
WHERE cricos_course_code = '099682F';

