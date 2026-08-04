-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00140K';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Firbank Grammar School - International Program</h4><p>Firbank Grammar School offers a co-educational (Primary) and girls-only (Secondary) environment for international students. Located in Brighton, Victoria.</p></p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7000,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test results, previous school reports, interview. English language proficiency assessment required.</p>',
    apply_form = 'https://www.firbank.vic.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '005315G';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Firbank Grammar School - International Program</h4><p>Firbank Grammar School offers a co-educational (Primary) and girls-only (Secondary) environment for international students. Located in Brighton, Victoria.</p></p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7000,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test results, previous school reports, interview. English language proficiency assessment required.</p>',
    apply_form = 'https://www.firbank.vic.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '011303E';

