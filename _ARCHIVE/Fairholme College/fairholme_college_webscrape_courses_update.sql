-- QLD Provider: Fairholme College (03726D)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '03726D';

UPDATE courses SET
    course_description = '<h4>Primary School Studies (Years 5 to 6)</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 45420,
    onshore_tuition_fee = NULL,
    enrolment_fee = 54392,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.fairholme.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '098508F';
UPDATE courses SET
    course_description = '<h4>Junior Secondary Studies (Years 7 to 10)</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 118730,
    onshore_tuition_fee = NULL,
    enrolment_fee = 105162,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.fairholme.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '098509E';
UPDATE courses SET
    course_description = '<h4>Senior Secondary Studies (Years 11 to 12)</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 62470,
    onshore_tuition_fee = NULL,
    enrolment_fee = 52478,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.fairholme.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '098510A';