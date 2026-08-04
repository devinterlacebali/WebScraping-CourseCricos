-- QLD Provider: St Laurence_s College (00972C)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00972C';

UPDATE courses SET
    course_description = '<h4>Senior Secondary School Yrs 11&12 Boys Only</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 76100,
    onshore_tuition_fee = NULL,
    enrolment_fee = 48286,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.slc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '001567G';
UPDATE courses SET
    course_description = '<h4>Middle School Years 7-10 Boys only</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 152200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 95500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.slc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '084070B';
UPDATE courses SET
    course_description = '<h4>Primary School Years 5 - 6 Boys Only</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 63660,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2700,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.slc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '108465C';