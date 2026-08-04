-- QLD Provider: Toowoomba Anglican School (00712A)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00712A';

UPDATE courses SET
    course_description = '<h4>Junior Secondary Years 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 119369,
    onshore_tuition_fee = NULL,
    enrolment_fee = 109526,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.taschool.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '081058M';
UPDATE courses SET
    course_description = '<h4>Senior Secondary Years 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 63303,
    onshore_tuition_fee = NULL,
    enrolment_fee = 58270,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.taschool.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '081059K';
UPDATE courses SET
    course_description = '<h4>Primary School Year 1-6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 137561,
    onshore_tuition_fee = NULL,
    enrolment_fee = 162908,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.taschool.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '085601E';