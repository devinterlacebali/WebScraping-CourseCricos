-- QLD Provider: The Springfield Anglican College (03658M)
-- Courses sourced from CRICOS register (2 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '03658M';

UPDATE courses SET
    course_description = '<h4>Junior Secondary Studies - Yrs 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 125400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 86860,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.tsac.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '096675G';
UPDATE courses SET
    course_description = '<h4>Senior Secondary Studies - Yrs 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 62700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 45045,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.tsac.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '096676F';