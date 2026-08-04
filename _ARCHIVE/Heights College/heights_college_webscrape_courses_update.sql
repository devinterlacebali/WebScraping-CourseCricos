-- QLD Provider: Heights College (01664G)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '01664G';

UPDATE courses SET
    course_description = '<h4>Primary Years P-6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 100562,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7110,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.heights.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '072970J';
UPDATE courses SET
    course_description = '<h4>Junior Secondary Years 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 66680,
    onshore_tuition_fee = NULL,
    enrolment_fee = 78904,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.heights.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '097562G';
UPDATE courses SET
    course_description = '<h4>Senior Secondary Years 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 35056,
    onshore_tuition_fee = NULL,
    enrolment_fee = 41566,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.heights.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '097563G';