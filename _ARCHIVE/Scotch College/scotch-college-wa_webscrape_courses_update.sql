-- Scotch College (WA) (00449M) - Course updates
-- Source: https://www.scotch.wa.edu.au/admissions/international

UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00449M';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Scotch College (WA) - International Baccalaureate Diploma Programme (Years 11+12)</h4><p>Scotch College (WA) offers international baccalaureate diploma programme (years 11+12) for international students. Located in Perth, Western Australia. CRICOS course code: 072396A.</p></p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 101324,
    onshore_tuition_fee = NULL,
    enrolment_fee = 8172,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test, English proficiency, academic transcripts. Interview may be required.</p>',
    apply_form = 'https://www.scotch.wa.edu.au/admissions/international',
    updated_at = NOW()
WHERE cricos_course_code = '072396A';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Scotch College (WA) - Western Australian Certificate of Education (WACE)(Years 11+12)</h4><p>Scotch College (WA) offers western australian certificate of education (wace)(years 11+12) for international students. Located in Perth, Western Australia. CRICOS course code: 072397M.</p></p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 101324,
    onshore_tuition_fee = NULL,
    enrolment_fee = 8172,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts. English proficiency. IELTS 5.5+ or equivalent.</p>',
    apply_form = 'https://www.scotch.wa.edu.au/admissions/international',
    updated_at = NOW()
WHERE cricos_course_code = '072397M';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Scotch College (WA) - International Baccalaureate Primary Years Programme (PYP) (Years 1-5)</h4><p>Scotch College (WA) offers international baccalaureate primary years programme (pyp) (years 1-5) for international students. Located in Perth, Western Australia. CRICOS course code: 082211K.</p></p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 222070,
    onshore_tuition_fee = NULL,
    enrolment_fee = 13327,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test, English proficiency, academic transcripts. Interview may be required.</p>',
    apply_form = 'https://www.scotch.wa.edu.au/admissions/international',
    updated_at = NOW()
WHERE cricos_course_code = '082211K';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Scotch College (WA) - Western Australian Curriculum Year 6</h4><p>Scotch College (WA) offers western australian curriculum year 6 for international students. Located in Perth, Western Australia. CRICOS course code: 119211A.</p></p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 46170,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11657,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.scotch.wa.edu.au/admissions/international',
    updated_at = NOW()
WHERE cricos_course_code = '119211A';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Scotch College (WA) - Western Australian Curriculum Years 7 - 10</h4><p>Scotch College (WA) offers western australian curriculum years 7 - 10 for international students. Located in Perth, Western Australia. CRICOS course code: 119214J.</p></p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 202648,
    onshore_tuition_fee = NULL,
    enrolment_fee = 13161,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.scotch.wa.edu.au/admissions/international',
    updated_at = NOW()
WHERE cricos_course_code = '119214J';

