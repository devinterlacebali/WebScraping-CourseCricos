-- QLD Provider: Redlands College (00923A)
-- Courses sourced from CRICOS register (2 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00923A';

UPDATE courses SET
    course_description = '<h4>Secondary Senior Years 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 48300,
    onshore_tuition_fee = NULL,
    enrolment_fee = 4340,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.redlands.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '009083G';
UPDATE courses SET
    course_description = '<h4>Junior Secondary 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 92900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6200,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.redlands.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082468G';