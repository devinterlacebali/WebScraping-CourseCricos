-- Edmund Rice Education Australia (Aquinas College) (00428E) - Course updates
-- Source: https://www.aquinas.wa.edu.au/international-students

UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00428E';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Edmund Rice Education Australia (Aquinas College) - Primary Education Pre-Primary - Year 6</h4><p>Edmund Rice Education Australia (Aquinas College) offers primary education pre-primary - year 6 for international students. Located in Perth, Western Australia. CRICOS course code: 0101464.</p></p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 150003,
    onshore_tuition_fee = NULL,
    enrolment_fee = 49245,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.aquinas.wa.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '0101464';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Edmund Rice Education Australia (Aquinas College) - Secondary Education Years 7-10</h4><p>Edmund Rice Education Australia (Aquinas College) offers secondary education years 7-10 for international students. Located in Perth, Western Australia. CRICOS course code: 099689K.</p></p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 106812,
    onshore_tuition_fee = NULL,
    enrolment_fee = 139368,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.aquinas.wa.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '099689K';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Edmund Rice Education Australia (Aquinas College) - Senior Secondary Certificate of Education Years 11-12</h4><p>Edmund Rice Education Australia (Aquinas College) offers senior secondary certificate of education years 11-12 for international students. Located in Perth, Western Australia. CRICOS course code: 099690F.</p></p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 56088,
    onshore_tuition_fee = NULL,
    enrolment_fee = 68930,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts. English proficiency. IELTS 5.5+ or equivalent.</p>',
    apply_form = 'https://www.aquinas.wa.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '099690F';

