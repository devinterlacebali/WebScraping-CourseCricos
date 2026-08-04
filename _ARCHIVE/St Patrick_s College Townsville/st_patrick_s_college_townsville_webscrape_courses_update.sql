-- QLD Provider: St Patrick_s College Townsville (03317K)
-- Courses sourced from CRICOS register (2 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '03317K';

UPDATE courses SET
    course_description = '<h4>Secondary Senior - 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 46920,
    onshore_tuition_fee = NULL,
    enrolment_fee = 55502,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.stpatscollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '076358G';
UPDATE courses SET
    course_description = '<h4>Secondary Junior - 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 93840,
    onshore_tuition_fee = NULL,
    enrolment_fee = 107580,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.stpatscollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '083481B';