-- QLD Provider: Marist College Ashgrove (00670F)
-- Courses sourced from CRICOS register (2 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00670F';

UPDATE courses SET
    course_description = '<h4>Junior Secondary Years 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 151216,
    onshore_tuition_fee = NULL,
    enrolment_fee = 116080,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.marash.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082463A';
UPDATE courses SET
    course_description = '<h4>Senior Secondary Certificate of Education Years 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 85824,
    onshore_tuition_fee = NULL,
    enrolment_fee = 60210,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.marash.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082464M';