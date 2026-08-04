-- Mercy Education Limited (St Brigid's) (00451F) - Course updates
-- Source: https://www.stbrigids.wa.edu.au/international-students/

UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00451F';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Mercy Education Limited (St Brigid''s) - Senior Secondary Certificate of Education Years 11 - 12</h4><p>Mercy Education Limited (St Brigid''s) offers senior secondary certificate of education years 11 - 12 for international students. Located in Perth, Western Australia. CRICOS course code: 005233J.</p></p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 36193,
    onshore_tuition_fee = NULL,
    enrolment_fee = 58251,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts. English proficiency. IELTS 5.5+ or equivalent.</p>',
    apply_form = 'https://www.stbrigids.wa.edu.au/international-students/',
    updated_at = NOW()
WHERE cricos_course_code = '005233J';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Mercy Education Limited (St Brigid''s) - Secondary Education Years 7 - 10</h4><p>Mercy Education Limited (St Brigid''s) offers secondary education years 7 - 10 for international students. Located in Perth, Western Australia. CRICOS course code: 102424E.</p></p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 83393,
    onshore_tuition_fee = NULL,
    enrolment_fee = 137611,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.stbrigids.wa.edu.au/international-students/',
    updated_at = NOW()
WHERE cricos_course_code = '102424E';

