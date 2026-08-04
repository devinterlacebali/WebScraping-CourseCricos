-- Christ Church Grammar School (00433G) - Course updates
-- Source: https://www.ccgs.wa.edu.au/enrolments/international-students

UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00433G';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Christ Church Grammar School - Primary School Studies (Years PP-6)</h4><p>Christ Church Grammar School offers primary school studies (years pp-6) for international students. Located in Perth, Western Australia. CRICOS course code: 035561M.</p></p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 320969,
    onshore_tuition_fee = NULL,
    enrolment_fee = 12191,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.ccgs.wa.edu.au/enrolments/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '035561M';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Christ Church Grammar School - Senior Secondary Certificate of Education Years 11-12</h4><p>Christ Church Grammar School offers senior secondary certificate of education years 11-12 for international students. Located in Perth, Western Australia. CRICOS course code: 099033F.</p></p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 117654,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1723,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts. English proficiency. IELTS 5.5+ or equivalent.</p>',
    apply_form = 'https://www.ccgs.wa.edu.au/enrolments/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '099033F';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Christ Church Grammar School - Secondary Education Years 7-10</h4><p>Christ Church Grammar School offers secondary education years 7-10 for international students. Located in Perth, Western Australia. CRICOS course code: 099034E.</p></p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 235308,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11317,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.ccgs.wa.edu.au/enrolments/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '099034E';

