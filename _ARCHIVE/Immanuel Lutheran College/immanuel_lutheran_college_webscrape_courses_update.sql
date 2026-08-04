-- QLD Provider: Immanuel Lutheran College (01457C)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '01457C';

UPDATE courses SET
    course_description = '<h4>Primary School Studies Years P-6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 206500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 18450,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.immanuel.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '063036M';
UPDATE courses SET
    course_description = '<h4>Junior Secondary Studies Years 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 150000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11800,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.immanuel.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '098501B';
UPDATE courses SET
    course_description = '<h4>Senior Secondary Years 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 75000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 9200,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.immanuel.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '098502A';