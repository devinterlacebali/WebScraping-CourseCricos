-- QLD Provider: Somerville House (00522G)
-- Courses sourced from CRICOS register (4 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00522G';

UPDATE courses SET
    course_description = '<h4>Secondary Senior Yrs 11-12 Girls Only</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 98800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 74050,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.somerville.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '010337C';
UPDATE courses SET
    course_description = '<h4>Years 1-6 (Primary)</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 262200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 87540,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.somerville.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082483G';
UPDATE courses SET
    course_description = '<h4>Years 7-10 (Junior Secondary)</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 197600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 144280,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.somerville.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082484G';
UPDATE courses SET
    course_description = '<h4>International Baccalaureate Diploma Program (Years 11 & 12)</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 98800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 73740,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.somerville.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '119879A';