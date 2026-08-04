-- QLD Provider: St Peters Lutheran College (00516E)
-- Courses sourced from CRICOS register (4 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00516E';

UPDATE courses SET
    course_description = '<h4>Secondary Junior Yrs 7-10 Boys and Girls</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 205544,
    onshore_tuition_fee = NULL,
    enrolment_fee = 137149,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.stpeters.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082965A';
UPDATE courses SET
    course_description = '<h4>Secondary Senior Yrs 11-12 Boys and Girls</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 101252,
    onshore_tuition_fee = NULL,
    enrolment_fee = 72628,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.stpeters.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082966M';
UPDATE courses SET
    course_description = '<h4>International Baccalaureate Diploma Programme Years 11 & 12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 101252,
    onshore_tuition_fee = NULL,
    enrolment_fee = 73216,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.stpeters.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '093792D';
UPDATE courses SET
    course_description = '<h4>Primary Years Prep - 6 Boys and Girls</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 247193,
    onshore_tuition_fee = NULL,
    enrolment_fee = 53542,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.stpeters.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '094780M';