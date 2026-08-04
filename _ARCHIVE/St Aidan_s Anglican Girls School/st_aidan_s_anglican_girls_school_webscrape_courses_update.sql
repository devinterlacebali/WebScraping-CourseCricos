-- QLD Provider: St Aidan_s Anglican Girls School (01194K)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '01194K';

UPDATE courses SET
    course_description = '<h4>Secondary Senior Years 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 100888,
    onshore_tuition_fee = NULL,
    enrolment_fee = 52117,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.staidans.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '015541C';
UPDATE courses SET
    course_description = '<h4>Primary Years Prep-Year 6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 308280,
    onshore_tuition_fee = NULL,
    enrolment_fee = 17515,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.staidans.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082485F';
UPDATE courses SET
    course_description = '<h4>Junior Secondary Years 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 201776,
    onshore_tuition_fee = NULL,
    enrolment_fee = 98995,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.staidans.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082486E';