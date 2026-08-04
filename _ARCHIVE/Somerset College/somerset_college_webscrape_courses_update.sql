-- QLD Provider: Somerset College (00521G)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00521G';

UPDATE courses SET
    course_description = '<h4>Secondary Senior Yrs 11-12 Boys and Girls</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 64810,
    onshore_tuition_fee = NULL,
    enrolment_fee = 17134,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.somerset.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004957C';
UPDATE courses SET
    course_description = '<h4>International Baccalaureate Primary Years Program (Years 1  6)</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 190768,
    onshore_tuition_fee = NULL,
    enrolment_fee = 43000,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.somerset.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '118169F';
UPDATE courses SET
    course_description = '<h4>International Baccalaureate Middle Years Program (Years 7  10)</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 129136,
    onshore_tuition_fee = NULL,
    enrolment_fee = 29200,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.somerset.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '118170B';