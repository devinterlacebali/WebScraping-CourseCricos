-- Guildford Grammar School (00437D) - Course updates
-- Source: https://www.ggs.wa.edu.au/enrol/international-students/

UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00437D';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Guildford Grammar School - Primary Education Pre-Primary - Year 6</h4><p>Guildford Grammar School offers primary education pre-primary - year 6 for international students. Located in Perth, Western Australia. CRICOS course code: 0101463.</p></p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 241980,
    onshore_tuition_fee = NULL,
    enrolment_fee = 10506,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.ggs.wa.edu.au/enrol/international-students/',
    updated_at = NOW()
WHERE cricos_course_code = '0101463';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Guildford Grammar School - Secondary Education Years 7 - 10</h4><p>Guildford Grammar School offers secondary education years 7 - 10 for international students. Located in Perth, Western Australia. CRICOS course code: 070204G.</p></p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 176769,
    onshore_tuition_fee = NULL,
    enrolment_fee = 129504,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.ggs.wa.edu.au/enrol/international-students/',
    updated_at = NOW()
WHERE cricos_course_code = '070204G';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Guildford Grammar School - Senior Secondary Certificate of Education Years 11 - 12</h4><p>Guildford Grammar School offers senior secondary certificate of education years 11 - 12 for international students. Located in Perth, Western Australia. CRICOS course code: 094493G.</p></p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 86768,
    onshore_tuition_fee = NULL,
    enrolment_fee = 73209,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts. English proficiency. IELTS 5.5+ or equivalent.</p>',
    apply_form = 'https://www.ggs.wa.edu.au/enrol/international-students/',
    updated_at = NOW()
WHERE cricos_course_code = '094493G';

