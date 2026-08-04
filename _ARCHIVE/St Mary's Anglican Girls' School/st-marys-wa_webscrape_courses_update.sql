-- St Mary's Anglican Girls' School (00454C) - Course updates
-- Source: https://www.stmarys.wa.edu.au/enrol/international-students/

UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00454C';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>St Mary''s Anglican Girls'' School - Secondary Education Years 11-12</h4><p>St Mary''s Anglican Girls'' School offers secondary education years 11-12 for international students. Located in Perth, Western Australia. CRICOS course code: 0101299.</p></p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 78938,
    onshore_tuition_fee = NULL,
    enrolment_fee = 8142,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.stmarys.wa.edu.au/enrol/international-students/',
    updated_at = NOW()
WHERE cricos_course_code = '0101299';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>St Mary''s Anglican Girls'' School - Secondary Education Year 7 - 10</h4><p>St Mary''s Anglican Girls'' School offers secondary education year 7 - 10 for international students. Located in Perth, Western Australia. CRICOS course code: 0101300.</p></p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 163498,
    onshore_tuition_fee = NULL,
    enrolment_fee = 9798,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.stmarys.wa.edu.au/enrol/international-students/',
    updated_at = NOW()
WHERE cricos_course_code = '0101300';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>St Mary''s Anglican Girls'' School - Primary Education Years 1-6</h4><p>St Mary''s Anglican Girls'' School offers primary education years 1-6 for international students. Located in Perth, Western Australia. CRICOS course code: 021986A.</p></p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 254080,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11573,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.stmarys.wa.edu.au/enrol/international-students/',
    updated_at = NOW()
WHERE cricos_course_code = '021986A';

