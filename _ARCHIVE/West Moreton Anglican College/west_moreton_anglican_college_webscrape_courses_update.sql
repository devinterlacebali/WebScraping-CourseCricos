-- QLD Provider: West Moreton Anglican College (01329M)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '01329M';

UPDATE courses SET
    course_description = '<h4>Primary School Studies (Prep to Year 6)</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 207648,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11105,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.wmac.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '084781D';
UPDATE courses SET
    course_description = '<h4>Secondary School Studies (Years 7 to 10)</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 142160,
    onshore_tuition_fee = NULL,
    enrolment_fee = 101735,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.wmac.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '084782C';
UPDATE courses SET
    course_description = '<h4>Senior Secondary School Studies (Years 11 & 12)</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 71080,
    onshore_tuition_fee = NULL,
    enrolment_fee = 53277,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.wmac.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '084783B';