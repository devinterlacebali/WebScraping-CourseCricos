-- QLD Provider: All Saints Anglican School (00979G)
-- Courses sourced from CRICOS register (4 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00979G';

UPDATE courses SET
    course_description = '<h4>Secondary Senior Yrs 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 60260,
    onshore_tuition_fee = NULL,
    enrolment_fee = 43170,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.asas.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '011990K';
UPDATE courses SET
    course_description = '<h4>High School Preparation</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 29480,
    onshore_tuition_fee = NULL,
    enrolment_fee = 21325,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.asas.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '079475A';
UPDATE courses SET
    course_description = '<h4>Primary Years P-6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 206360,
    onshore_tuition_fee = NULL,
    enrolment_fee = 145075,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.asas.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '084081K';
UPDATE courses SET
    course_description = '<h4>Secondary Junior Yrs 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 117920,
    onshore_tuition_fee = NULL,
    enrolment_fee = 82900,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.asas.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '084082J';