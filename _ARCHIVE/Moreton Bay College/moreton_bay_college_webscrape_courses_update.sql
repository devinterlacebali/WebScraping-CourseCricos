-- QLD Provider: Moreton Bay College (03771K)
-- Courses sourced from CRICOS register (5 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '03771K';

UPDATE courses SET
    course_description = '<h4>Junior Secondary Studies (Years 7-10)</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 158744,
    onshore_tuition_fee = NULL,
    enrolment_fee = 115777,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.mbc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '0100272';
UPDATE courses SET
    course_description = '<h4>Senior Secondary Studies (QCE) Years 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 79372,
    onshore_tuition_fee = NULL,
    enrolment_fee = 65209,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.mbc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '0100273';
UPDATE courses SET
    course_description = '<h4>International Baccalaureate Primary Years Program</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 241082,
    onshore_tuition_fee = NULL,
    enrolment_fee = 26545,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.mbc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '0101301';
UPDATE courses SET
    course_description = '<h4>High School Preparation</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 28,
    offshore_tuition_fee = 20143,
    onshore_tuition_fee = NULL,
    enrolment_fee = 18237,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.mbc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112309C';
UPDATE courses SET
    course_description = '<h4>Primary School Preparation Years 3 - 6</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 28,
    offshore_tuition_fee = 17827,
    onshore_tuition_fee = NULL,
    enrolment_fee = 4635,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.mbc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '116205A';