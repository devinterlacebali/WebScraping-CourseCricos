-- QLD Provider: St Hilda's Anglican School for Girls Inc. (00452E)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00452E';

UPDATE courses SET
    course_description = '<h4>Secondary Education Years 7-10</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 232992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 147098,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.sthildas.wa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '0101403';
UPDATE courses SET
    course_description = '<h4>Senior Secondary Certificate of Education Years 11-12</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 116496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 81580,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.sthildas.wa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '0101404';
UPDATE courses SET
    course_description = '<h4>Primary Education Years PP - 6</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 416,
    offshore_tuition_fee = 271985,
    onshore_tuition_fee = NULL,
    enrolment_fee = 22662,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.sthildas.wa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '016947F';