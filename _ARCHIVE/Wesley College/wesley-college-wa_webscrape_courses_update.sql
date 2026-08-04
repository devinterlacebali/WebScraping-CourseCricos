-- Wesley College (WA) (00460E) - Course updates
-- Source: https://www.wesley.wa.edu.au/enrolment/international-students/

UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00460E';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Wesley College (WA) - Primary Education Pre-primary - Year 6</h4><p>Wesley College (WA) offers primary education pre-primary - year 6 for international students. Located in Perth, Western Australia. CRICOS course code: 016948E.</p></p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 201660,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6546,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.wesley.wa.edu.au/enrolment/international-students/',
    updated_at = NOW()
WHERE cricos_course_code = '016948E';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Wesley College (WA) - Secondary Education Years 7-10</h4><p>Wesley College (WA) offers secondary education years 7-10 for international students. Located in Perth, Western Australia. CRICOS course code: 098524F.</p></p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 165824,
    onshore_tuition_fee = NULL,
    enrolment_fee = 124994,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.wesley.wa.edu.au/enrolment/international-students/',
    updated_at = NOW()
WHERE cricos_course_code = '098524F';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Wesley College (WA) - Senior Secondary Education Years 11-12</h4><p>Wesley College (WA) offers senior secondary education years 11-12 for international students. Located in Perth, Western Australia. CRICOS course code: 098525E.</p></p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 82912,
    onshore_tuition_fee = NULL,
    enrolment_fee = 65770,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.wesley.wa.edu.au/enrolment/international-students/',
    updated_at = NOW()
WHERE cricos_course_code = '098525E';

