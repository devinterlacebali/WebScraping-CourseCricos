-- St John's Catholic College (00466K) - Course updates
-- Source: https://www.stjohns.wa.edu.au/enrolment/international-students

UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00466K';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>St John''s Catholic College - Secondary Junior Yrs 7-9 Boys & Girls</h4><p>St John''s Catholic College offers secondary junior yrs 7-9 boys & girls for international students. Located in Perth, Western Australia. CRICOS course code: 004753D.</p></p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 35496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2730,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.stjohns.wa.edu.au/enrolment/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '004753D';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>St John''s Catholic College - Secondary Seniors Yrs 10 -12 Boys & Girls</h4><p>St John''s Catholic College offers secondary seniors yrs 10 -12 boys & girls for international students. Located in Perth, Western Australia. CRICOS course code: 004754C.</p></p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 37440,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3072,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.stjohns.wa.edu.au/enrolment/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '004754C';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>St John''s Catholic College - Intensive English Course (1-52 weeks)</h4><p>St John''s Catholic College offers intensive english course (1-52 weeks) for international students. Located in Perth, Western Australia. CRICOS course code: 058683M.</p></p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12424,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1055,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English proficiency assessment required. IELTS 5.0+ or equivalent.</p>',
    apply_form = 'https://www.stjohns.wa.edu.au/enrolment/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '058683M';

