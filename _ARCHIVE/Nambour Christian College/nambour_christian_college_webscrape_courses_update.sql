-- QLD Provider: Nambour Christian College (01461G)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '01461G';

UPDATE courses SET
    course_description = '<h4>Junior Secondary Studies Years 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 102372,
    onshore_tuition_fee = NULL,
    enrolment_fee = 128382,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.ncc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '097646D';
UPDATE courses SET
    course_description = '<h4>Senior Secondary Studies (QCE) Years 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 52230,
    onshore_tuition_fee = NULL,
    enrolment_fee = 67884,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ncc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '097647C';
UPDATE courses SET
    course_description = '<h4>Primary School Studies P-6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 138117,
    onshore_tuition_fee = NULL,
    enrolment_fee = 59332,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.ncc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '115532E';