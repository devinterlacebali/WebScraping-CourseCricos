-- QLD Provider: Groves Christian College (03246J)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '03246J';

UPDATE courses SET
    course_description = '<h4>Senior Secondary School (Gr 11-12)</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 40380,
    onshore_tuition_fee = NULL,
    enrolment_fee = 8120,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.groves.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '072678B';
UPDATE courses SET
    course_description = '<h4>Primary School (Grades P to 6)</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 114100,
    onshore_tuition_fee = NULL,
    enrolment_fee = 28420,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.groves.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '086216F';
UPDATE courses SET
    course_description = '<h4>Junior Secondary School (Grades 7-10)</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 71400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 16240,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.groves.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '086217E';