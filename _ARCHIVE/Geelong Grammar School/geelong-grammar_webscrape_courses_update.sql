-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00143G';

UPDATE courses SET
    course_description = '<h4>Geelong Grammar School - International Program</h4><p>Geelong Grammar School is one of Australia''s leading co-educational boarding schools. International students benefit from world-class facilities and a rich co-curricular program.</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = 24166,
    materials_fee = NULL,
    entry_requirements = 'AEAS test results, academic transcripts, interview. English language proficiency assessment.',
    apply_form = 'https://www.ggs.vic.edu.au/enrolment',
    updated_at = NOW()
WHERE cricos_course_code = '005326D';

UPDATE courses SET
    course_description = '<h4>Geelong Grammar School - International Program</h4><p>Geelong Grammar School is one of Australia''s leading co-educational boarding schools. International students benefit from world-class facilities and a rich co-curricular program.</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7370,
    materials_fee = NULL,
    entry_requirements = 'AEAS test results, academic transcripts, interview. English language proficiency assessment.',
    apply_form = 'https://www.ggs.vic.edu.au/enrolment',
    updated_at = NOW()
WHERE cricos_course_code = '015229M';

