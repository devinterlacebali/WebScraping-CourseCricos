-- Methodist Ladies' College (WA) (00441G) - Course updates
-- Source: https://www.mlc.wa.edu.au/enrolment/international-students/

UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00441G';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Methodist Ladies'' College (WA) - Primary Education Years 1-6</h4><p>Methodist Ladies'' College (WA) offers primary education years 1-6 for international students. Located in Perth, Western Australia. CRICOS course code: 031322C.</p></p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 272031,
    onshore_tuition_fee = NULL,
    enrolment_fee = 43924,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.mlc.wa.edu.au/enrolment/international-students/',
    updated_at = NOW()
WHERE cricos_course_code = '031322C';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Methodist Ladies'' College (WA) - Secondary Education Years 7-10</h4><p>Methodist Ladies'' College (WA) offers secondary education years 7-10 for international students. Located in Perth, Western Australia. CRICOS course code: 099693C.</p></p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 234112,
    onshore_tuition_fee = NULL,
    enrolment_fee = 139090,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.mlc.wa.edu.au/enrolment/international-students/',
    updated_at = NOW()
WHERE cricos_course_code = '099693C';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Methodist Ladies'' College (WA) - Senior Secondary Certificate of Education Years 11-12</h4><p>Methodist Ladies'' College (WA) offers senior secondary certificate of education years 11-12 for international students. Located in Perth, Western Australia. CRICOS course code: 099694B.</p></p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 124730,
    onshore_tuition_fee = NULL,
    enrolment_fee = 75646,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts. English proficiency. IELTS 5.5+ or equivalent.</p>',
    apply_form = 'https://www.mlc.wa.edu.au/enrolment/international-students/',
    updated_at = NOW()
WHERE cricos_course_code = '099694B';

