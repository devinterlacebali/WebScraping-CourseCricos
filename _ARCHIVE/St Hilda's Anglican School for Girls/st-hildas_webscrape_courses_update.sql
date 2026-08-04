-- St Hilda's Anglican School for Girls (00452E) - Course updates
-- Source: https://www.sthildas.wa.edu.au/enrolment/international/

UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00452E';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>St Hilda''s Anglican School for Girls - Secondary Education Years 7-10</h4><p>St Hilda''s Anglican School for Girls offers secondary education years 7-10 for international students. Located in Perth, Western Australia. CRICOS course code: 0101403.</p></p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 232992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 147098,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.sthildas.wa.edu.au/enrolment/international/',
    updated_at = NOW()
WHERE cricos_course_code = '0101403';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>St Hilda''s Anglican School for Girls - Senior Secondary Certificate of Education Years 11-12</h4><p>St Hilda''s Anglican School for Girls offers senior secondary certificate of education years 11-12 for international students. Located in Perth, Western Australia. CRICOS course code: 0101404.</p></p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 116496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 81580,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts. English proficiency. IELTS 5.5+ or equivalent.</p>',
    apply_form = 'https://www.sthildas.wa.edu.au/enrolment/international/',
    updated_at = NOW()
WHERE cricos_course_code = '0101404';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>St Hilda''s Anglican School for Girls - Primary Education Years PP - 6</h4><p>St Hilda''s Anglican School for Girls offers primary education years pp - 6 for international students. Located in Perth, Western Australia. CRICOS course code: 016947F.</p></p>',
    course_duration_per_week = 416,
    offshore_tuition_fee = 271985,
    onshore_tuition_fee = NULL,
    enrolment_fee = 22662,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.sthildas.wa.edu.au/enrolment/international/',
    updated_at = NOW()
WHERE cricos_course_code = '016947F';

