-- QLD Provider: Mueller College (01095B)
-- Courses sourced from CRICOS register (4 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '01095B';

UPDATE courses SET
    course_description = '<h4>Secondary Senior Years 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 46000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 4800,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.mueller.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '026423G';
UPDATE courses SET
    course_description = '<h4>Primary School Studies Years 1-6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 121500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 8700,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.mueller.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082465K';
UPDATE courses SET
    course_description = '<h4>Secondary Junior Years 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 92000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7600,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.mueller.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082466J';
UPDATE courses SET
    course_description = '<h4>Primary School Studies P-6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 161000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 10150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.mueller.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112884E';