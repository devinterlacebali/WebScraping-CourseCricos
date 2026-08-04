-- QLD Provider: Peace Lutheran College (01260E)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '01260E';

UPDATE courses SET
    course_description = '<h4>Senior Secondary Studies 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 72000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 67200,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.plc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '018202J';
UPDATE courses SET
    course_description = '<h4>Junior School Studies Years P-6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 182000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 4400,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.plc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '086286C';
UPDATE courses SET
    course_description = '<h4>Junior Secondary School Studies Years 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 132000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 129200,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.plc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '086287B';