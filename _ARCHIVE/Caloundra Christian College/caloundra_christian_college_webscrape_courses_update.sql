-- QLD Provider: Caloundra Christian College (01434K)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '01434K';

UPDATE courses SET
    course_description = '<h4>Junior Secondary Years 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 110900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 80100,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.calcc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '0101447';
UPDATE courses SET
    course_description = '<h4>Senior Secondary Years 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 58200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 41704,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.calcc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '0101448';
UPDATE courses SET
    course_description = '<h4>Primary School Studies P-6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 169000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 10360,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.calcc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '0101543';