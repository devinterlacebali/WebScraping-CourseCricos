-- Bunbury Cathedral Grammar School (00431K) - Course updates
-- Source: https://www.bcgs.wa.edu.au/enrolment/international-students

UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00431K';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Bunbury Cathedral Grammar School - Primary Education Pre-Primary - Year 6</h4><p>Bunbury Cathedral Grammar School offers primary education pre-primary - year 6 for international students. Located in Perth, Western Australia. CRICOS course code: 0101461.</p></p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 137000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6775,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.bcgs.wa.edu.au/enrolment/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '0101461';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Bunbury Cathedral Grammar School - Secondary Education Years 7 - 10</h4><p>Bunbury Cathedral Grammar School offers secondary education years 7 - 10 for international students. Located in Perth, Western Australia. CRICOS course code: 094168J.</p></p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 108500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 89900,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required. Academic transcripts.</p>',
    apply_form = 'https://www.bcgs.wa.edu.au/enrolment/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '094168J';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Bunbury Cathedral Grammar School - Senior Secondary Certificate of Education Years 11 - 12</h4><p>Bunbury Cathedral Grammar School offers senior secondary certificate of education years 11 - 12 for international students. Located in Perth, Western Australia. CRICOS course code: 094169G.</p></p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 56000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 46350,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts. English proficiency. IELTS 5.5+ or equivalent.</p>',
    apply_form = 'https://www.bcgs.wa.edu.au/enrolment/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '094169G';

