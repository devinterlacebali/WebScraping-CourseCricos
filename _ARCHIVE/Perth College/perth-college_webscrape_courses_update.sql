-- Perth College Inc (00445D) - Course updates
-- Source: https://www.pc.wa.edu.au/enrolment/international-students

UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00445D';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Perth College Inc - Secondary Education Years 7 - 10</h4><p>Perth College Inc offers secondary education years 7 - 10 for international students. Located in Perth, Western Australia. CRICOS course code: 0101297.</p></p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 180396,
    onshore_tuition_fee = NULL,
    enrolment_fee = 23885,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.pc.wa.edu.au/enrolment/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '0101297';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Perth College Inc - Secondary Education Years 11 - 12</h4><p>Perth College Inc offers secondary education years 11 - 12 for international students. Located in Perth, Western Australia. CRICOS course code: 0101298.</p></p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 91908,
    onshore_tuition_fee = NULL,
    enrolment_fee = 13343,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.pc.wa.edu.au/enrolment/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '0101298';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Perth College Inc - Primary Education Years 1 - 6</h4><p>Perth College Inc offers primary education years 1 - 6 for international students. Located in Perth, Western Australia. CRICOS course code: 021509G.</p></p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 194688,
    onshore_tuition_fee = NULL,
    enrolment_fee = 23149,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.pc.wa.edu.au/enrolment/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '021509G';

