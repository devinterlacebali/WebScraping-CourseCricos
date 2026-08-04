-- QLD Provider: Hillcrest Christian College (01043C)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '01043C';

UPDATE courses SET
    course_description = '<h4>Primary Years (Prep to Year 6) Boys and Girls</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 212800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11200,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.hillcrest.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '085421J';
UPDATE courses SET
    course_description = '<h4>Junior Secondary Studies (Years 7 to 10) Boys and Girls</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 137000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 109290,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.hillcrest.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '085422G';
UPDATE courses SET
    course_description = '<h4>Senior Secondary Studies (Years 11 and 12) Boys and Girls</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 70200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 77340,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.hillcrest.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '085423G';