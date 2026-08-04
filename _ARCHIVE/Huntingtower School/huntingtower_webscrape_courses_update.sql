-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00145E';

UPDATE courses SET
    course_description = '<h4>Huntingtower School - International Program</h4><p>Huntingtower is a co-educational school from Prep to Year 12. International students join a nurturing academic community in Mount Waverley, Victoria.</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = 12520,
    materials_fee = NULL,
    entry_requirements = 'AEAS test results, academic transcripts, interview. English language proficiency assessment required.',
    apply_form = 'https://www.huntingtower.vic.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '017556B';

