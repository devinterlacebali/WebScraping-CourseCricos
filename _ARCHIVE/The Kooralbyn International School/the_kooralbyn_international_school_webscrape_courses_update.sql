-- QLD Provider: The Kooralbyn International School (02759C)
-- Courses sourced from CRICOS register (2 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '02759C';

UPDATE courses SET
    course_description = '<h4>Junior Secondary School 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 91504,
    onshore_tuition_fee = NULL,
    enrolment_fee = 96898,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.tkis.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '087651A';
UPDATE courses SET
    course_description = '<h4>Senior Secondary School 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 45752,
    onshore_tuition_fee = NULL,
    enrolment_fee = 51094,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.tkis.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '087657F';