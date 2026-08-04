-- QLD Provider: Trinity Lutheran College (00878A)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00878A';

UPDATE courses SET
    course_description = '<h4>Secondary Senior Yrs 11-12 Co-educational</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 51294,
    onshore_tuition_fee = NULL,
    enrolment_fee = 38773,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.tlc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '008219E';
UPDATE courses SET
    course_description = '<h4>Primary Education P-6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 143255,
    onshore_tuition_fee = NULL,
    enrolment_fee = 36990,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.tlc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '0100056';
UPDATE courses SET
    course_description = '<h4>Secondary Junior Years 7-10 Co-educational</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 94435,
    onshore_tuition_fee = NULL,
    enrolment_fee = 72040,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.tlc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '085671B';