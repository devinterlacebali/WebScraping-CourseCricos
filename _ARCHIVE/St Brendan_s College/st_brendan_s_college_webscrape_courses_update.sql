-- QLD Provider: St Brendan_s College (03745A)
-- Courses sourced from CRICOS register (2 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '03745A';

UPDATE courses SET
    course_description = '<h4>Junior Secondary Studies Years 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 106200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 91200,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.stbrendans.qld.edu.au/',
    updated_at = NOW()
WHERE cricos_course_code = '099326D';
UPDATE courses SET
    course_description = '<h4>Senior Secondary Studies (QCE) Years 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 53100,
    onshore_tuition_fee = NULL,
    enrolment_fee = 46500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.stbrendans.qld.edu.au/',
    updated_at = NOW()
WHERE cricos_course_code = '099327C';