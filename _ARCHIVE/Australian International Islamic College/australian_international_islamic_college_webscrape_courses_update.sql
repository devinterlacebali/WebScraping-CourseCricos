-- QLD Provider: Australian International Islamic College (02724C)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '02724C';

UPDATE courses SET
    course_description = '<h4>Junior Secondary 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 59630,
    onshore_tuition_fee = NULL,
    enrolment_fee = 88300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.aiic.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082645F';
UPDATE courses SET
    course_description = '<h4>Senior Secondary Years 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 32865,
    onshore_tuition_fee = NULL,
    enrolment_fee = 45410,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.aiic.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082646E';
UPDATE courses SET
    course_description = '<h4>Primary Years Prep-6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 95470,
    onshore_tuition_fee = NULL,
    enrolment_fee = 8500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.aiic.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '089360G';