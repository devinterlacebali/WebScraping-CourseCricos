-- QLD Provider: Citipointe Christian College (00996F)
-- Courses sourced from CRICOS register (4 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00996F';

UPDATE courses SET
    course_description = '<h4>Senior Secondary Years 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 74920,
    onshore_tuition_fee = NULL,
    enrolment_fee = 74462,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.citipointe.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '010045D';
UPDATE courses SET
    course_description = '<h4>Secondary School Preparation Program (Elementary to Upper Intermediate)</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 50,
    offshore_tuition_fee = 37460,
    onshore_tuition_fee = NULL,
    enrolment_fee = 37895,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.citipointe.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '043173A';
UPDATE courses SET
    course_description = '<h4>Primary Years P-6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 187670,
    onshore_tuition_fee = NULL,
    enrolment_fee = 68765,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.citipointe.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '071487F';
UPDATE courses SET
    course_description = '<h4>Junior Secondary Studies Years 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 143540,
    onshore_tuition_fee = NULL,
    enrolment_fee = 141850,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.citipointe.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '097391M';