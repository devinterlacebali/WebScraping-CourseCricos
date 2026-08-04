-- QLD Provider: Suncoast Christian College (00539J)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00539J';

UPDATE courses SET
    course_description = '<h4>Secondary Senior Yrs 11-12 Boys & Girls</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 53100,
    onshore_tuition_fee = NULL,
    enrolment_fee = 41400,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.suncoastcc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004975A';
UPDATE courses SET
    course_description = '<h4>Primary Years 1-6 Boys & Girls</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 112200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.suncoastcc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '085035G';
UPDATE courses SET
    course_description = '<h4>Secondary Junior Years 7-10 Boys & Girls</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 99792,
    onshore_tuition_fee = NULL,
    enrolment_fee = 79100,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.suncoastcc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '085036G';