-- QLD Provider: Coomera Anglican College (02423E)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '02423E';

UPDATE courses SET
    course_description = '<h4>Junior Secondary School Studies (Yr 7-10)</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 94080,
    onshore_tuition_fee = NULL,
    enrolment_fee = 74790,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.cac.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '085040M';
UPDATE courses SET
    course_description = '<h4>Senior Secondary School Studies (Yr 11-12)</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 47440,
    onshore_tuition_fee = NULL,
    enrolment_fee = 37510,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cac.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '085041K';
UPDATE courses SET
    course_description = '<h4>Primary School Studies (Years 3-6)</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 70344,
    onshore_tuition_fee = NULL,
    enrolment_fee = 8000,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.cac.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '107416J';