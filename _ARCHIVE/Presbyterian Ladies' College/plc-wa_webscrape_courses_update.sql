-- Presbyterian Ladies College (WA) (00447B) - Course updates
-- Source: https://www.plc.wa.edu.au/enrolling/international-students

UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00447B';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Presbyterian Ladies College (WA) - Primary Education Years PP-6</h4><p>Presbyterian Ladies College (WA) offers primary education years pp-6 for international students. Located in Perth, Western Australia. CRICOS course code: 018990J.</p></p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 232792,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6800,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.plc.wa.edu.au/enrolling/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '018990J';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Presbyterian Ladies College (WA) - International Baccalaureate Primary Years Programme (PYP)</h4><p>Presbyterian Ladies College (WA) offers international baccalaureate primary years programme (pyp) for international students. Located in Perth, Western Australia. CRICOS course code: 089588J.</p></p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 232792,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6800,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test, English proficiency, academic transcripts. Interview may be required.</p>',
    apply_form = 'https://www.plc.wa.edu.au/enrolling/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '089588J';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Presbyterian Ladies College (WA) - International Baccalaureate Diploma Programme (Years 11+12)</h4><p>Presbyterian Ladies College (WA) offers international baccalaureate diploma programme (years 11+12) for international students. Located in Perth, Western Australia. CRICOS course code: 089590D.</p></p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 101580,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6800,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test, English proficiency, academic transcripts. Interview may be required.</p>',
    apply_form = 'https://www.plc.wa.edu.au/enrolling/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '089590D';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Presbyterian Ladies College (WA) - Secondary Education Years 7 - 10</h4><p>Presbyterian Ladies College (WA) offers secondary education years 7 - 10 for international students. Located in Perth, Western Australia. CRICOS course code: 097045G.</p></p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 203160,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6800,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.plc.wa.edu.au/enrolling/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '097045G';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Presbyterian Ladies College (WA) - Senior Secondary Certificate of Education Years 11 - 12</h4><p>Presbyterian Ladies College (WA) offers senior secondary certificate of education years 11 - 12 for international students. Located in Perth, Western Australia. CRICOS course code: 097046F.</p></p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 101580,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6800,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts. English proficiency. IELTS 5.5+ or equivalent.</p>',
    apply_form = 'https://www.plc.wa.edu.au/enrolling/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '097046F';

