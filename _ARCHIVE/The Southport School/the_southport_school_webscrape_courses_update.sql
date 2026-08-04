-- QLD Provider: The Southport School (00523F)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00523F';

UPDATE courses SET
    course_description = '<h4>Secondary Senior Yrs 11-12 Boys</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 91922,
    onshore_tuition_fee = NULL,
    enrolment_fee = 82008,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.tss.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004963E';
UPDATE courses SET
    course_description = '<h4>Primary Years Prep-6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 279272,
    onshore_tuition_fee = NULL,
    enrolment_fee = 22875,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.tss.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '085935E';
UPDATE courses SET
    course_description = '<h4>Secondary Years 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 177632,
    onshore_tuition_fee = NULL,
    enrolment_fee = 154326,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.tss.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '085936D';