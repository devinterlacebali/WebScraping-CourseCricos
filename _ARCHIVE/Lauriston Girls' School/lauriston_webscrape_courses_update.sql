-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 2 (April), Term 3 (July), Term 4 (October)',
    updated_at = NOW()
WHERE cricos_provider_code = '00152F';

UPDATE courses SET
    course_description = '<h4>Lauriston Girls'' School - International Program</h4><p>Lauriston is one of Melbourne''s leading independent girls'' schools. International students access an outstanding education from Early Learning to Year 12.</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = 5000,
    materials_fee = NULL,
    entry_requirements = 'AEAS test results, academic transcripts, interview. English language proficiency required.',
    apply_form = 'https://www.lauriston.vic.edu.au/enrolment/',
    updated_at = NOW()
WHERE cricos_course_code = '005356J';

UPDATE courses SET
    course_description = '<h4>Lauriston Girls'' School - International Program</h4><p>Lauriston is one of Melbourne''s leading independent girls'' schools. International students access an outstanding education from Early Learning to Year 12.</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1700,
    materials_fee = NULL,
    entry_requirements = 'AEAS test results, academic transcripts, interview. English language proficiency required.',
    apply_form = 'https://www.lauriston.vic.edu.au/enrolment/',
    updated_at = NOW()
WHERE cricos_course_code = '015713K';

