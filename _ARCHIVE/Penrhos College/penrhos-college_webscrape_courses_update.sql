-- Penrhos College (00444E) - Course updates
-- Source: https://www.penrhos.wa.edu.au/enrolment/international-students

UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00444E';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Penrhos College - Primary Education Years 1 - 6</h4><p>Penrhos College offers primary education years 1 - 6 for international students. Located in Perth, Western Australia. CRICOS course code: 027975M.</p></p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 232152,
    onshore_tuition_fee = NULL,
    enrolment_fee = 4820,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.penrhos.wa.edu.au/enrolment/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '027975M';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Penrhos College - Secondary Education Years 7 - 10</h4><p>Penrhos College offers secondary education years 7 - 10 for international students. Located in Perth, Western Australia. CRICOS course code: 094106A.</p></p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 194744,
    onshore_tuition_fee = NULL,
    enrolment_fee = 4100,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.penrhos.wa.edu.au/enrolment/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '094106A';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Penrhos College - Senior Secondary Certificate of Education Years 11-12</h4><p>Penrhos College offers senior secondary certificate of education years 11-12 for international students. Located in Perth, Western Australia. CRICOS course code: 094119G.</p></p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 97372,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1900,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts. English proficiency. IELTS 5.5+ or equivalent.</p>',
    apply_form = 'https://www.penrhos.wa.edu.au/enrolment/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '094119G';

