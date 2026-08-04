-- QLD Provider: St James College (00715J)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00715J';

UPDATE courses SET
    course_description = '<h4>Secondary Senior Yrs 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 50000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 39000,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.stjamescollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '007705K';
UPDATE courses SET
    course_description = '<h4>Secondary Junior Yrs 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 204,
    offshore_tuition_fee = 99600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 75000,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.stjamescollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082489B';
UPDATE courses SET
    course_description = '<h4>Primary School Studies Years 5 - 6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 40000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 42000,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.stjamescollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112582H';