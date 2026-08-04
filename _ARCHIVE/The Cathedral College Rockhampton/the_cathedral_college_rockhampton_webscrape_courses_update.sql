-- QLD Provider: The Cathedral College Rockhampton (00506G)
-- Courses sourced from CRICOS register (2 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00506G';

UPDATE courses SET
    course_description = '<h4>Secondary Senior Yrs 11-12 Boys & Girls</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 49478,
    onshore_tuition_fee = NULL,
    enrolment_fee = 38518,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.tccr.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '007379G';
UPDATE courses SET
    course_description = '<h4>Secondary Junior Years 7-10 Boys & Girls</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 95394,
    onshore_tuition_fee = NULL,
    enrolment_fee = 74668,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.tccr.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '082647D';