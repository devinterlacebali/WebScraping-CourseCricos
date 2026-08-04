-- QLD Provider: Whitsunday Anglican School (00993J)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00993J';

UPDATE courses SET
    course_description = '<h4>Secondary Senior Yrs 11-12 Boys & Girls</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 52538,
    onshore_tuition_fee = NULL,
    enrolment_fee = 53012,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.was.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '010037D';
UPDATE courses SET
    course_description = '<h4>Primary School 5-6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 42108,
    onshore_tuition_fee = NULL,
    enrolment_fee = 50224,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.was.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '086180B';
UPDATE courses SET
    course_description = '<h4>Junior Secondary 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 94876,
    onshore_tuition_fee = NULL,
    enrolment_fee = 99128,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.was.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '086181A';