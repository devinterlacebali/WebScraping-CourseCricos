-- QLD Provider: Fraser Coast Anglican College (01592G)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '01592G';

UPDATE courses SET
    course_description = '<h4>Primary Education Years 4-6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 67071,
    onshore_tuition_fee = NULL,
    enrolment_fee = 70175,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.fcac.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '062997C';
UPDATE courses SET
    course_description = '<h4>Junior Secondary Education Years 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 95513,
    onshore_tuition_fee = NULL,
    enrolment_fee = 93960,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.fcac.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '085589G';
UPDATE courses SET
    course_description = '<h4>Senior Secondary Education Years 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 55130,
    onshore_tuition_fee = NULL,
    enrolment_fee = 48942,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.fcac.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '085590C';