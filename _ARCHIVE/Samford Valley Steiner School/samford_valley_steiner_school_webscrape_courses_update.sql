-- QLD Provider: Samford Valley Steiner School (03326J)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '03326J';

UPDATE courses SET
    course_description = '<h4>Primary Education (Class 5-6)</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 26490,
    onshore_tuition_fee = NULL,
    enrolment_fee = 34090,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.samfordsteiner.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082478E';
UPDATE courses SET
    course_description = '<h4>Junior Secondary Education (Class 7-10)</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 59214,
    onshore_tuition_fee = NULL,
    enrolment_fee = 67830,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.samfordsteiner.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082479D';
UPDATE courses SET
    course_description = '<h4>New Zealand Certificate of Steiner Education (Class 11-12)</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 31012,
    onshore_tuition_fee = NULL,
    enrolment_fee = 33992,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.samfordsteiner.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '105371M';