-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 3 (July)',
    updated_at = NOW()
WHERE cricos_provider_code = '00142G';

UPDATE courses SET
    course_description = '<h4>The Geelong College - International Program</h4><p>The Geelong College is a co-educational boarding and day school. International students join a vibrant community with strong pastoral care.</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = 104160,
    materials_fee = NULL,
    entry_requirements = 'AEAS test, academic transcripts, English proficiency assessment, interview.',
    apply_form = 'https://www.tgc.vic.edu.au/enrolment/',
    updated_at = NOW()
WHERE cricos_course_code = '016075E';

