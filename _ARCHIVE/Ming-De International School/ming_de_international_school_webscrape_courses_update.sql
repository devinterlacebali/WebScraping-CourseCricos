-- QLD Provider: Ming-De International School (04063H)
-- Courses sourced from CRICOS register (2 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '04063H';

UPDATE courses SET
    course_description = '<h4>Primary School Studies (Prep to Year 6)</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 128800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 33302,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.ming-de.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '111235B';
UPDATE courses SET
    course_description = '<h4>Junior Secondary Studies Years 7-8</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 43200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 9372,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.ming-de.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '117185C';