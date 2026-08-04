-- QLD Provider: All Souls St Gabriels School (02025G)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '02025G';

UPDATE courses SET
    course_description = '<h4>Primary Education (Year 6)</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 28880,
    onshore_tuition_fee = NULL,
    enrolment_fee = 22822,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.allsouls.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '084935B';
UPDATE courses SET
    course_description = '<h4>Middle School Education (Years 7-10)</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 147381,
    onshore_tuition_fee = NULL,
    enrolment_fee = 99697,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.allsouls.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '084936A';
UPDATE courses SET
    course_description = '<h4>Secondary School Education (Years 11-12)</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 75024,
    onshore_tuition_fee = NULL,
    enrolment_fee = 45582,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.allsouls.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '084937M';