-- QLD Provider: Gold Coast Christian College (02708C)
-- Courses sourced from CRICOS register (4 courses)

UPDATE provider_institution SET
    intake_date = 'January, February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '02708C';

UPDATE courses SET
    course_description = '<h4>Senior Secondary School (Years 11 & 12)</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 55360,
    onshore_tuition_fee = NULL,
    enrolment_fee = 61290,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoastchristiancollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082537K';
UPDATE courses SET
    course_description = '<h4>Primary School (Years 1-6)</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 115020,
    onshore_tuition_fee = NULL,
    enrolment_fee = 61730,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.goldcoastchristiancollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082956B';
UPDATE courses SET
    course_description = '<h4>Junior Secondary School (Years 7-10)</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 101960,
    onshore_tuition_fee = NULL,
    enrolment_fee = 117160,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.goldcoastchristiancollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082957A';
UPDATE courses SET
    course_description = '<h4>Preparatory</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 18960,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11105,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.goldcoastchristiancollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '084893G';