-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 2 (April), Term 3 (July), Term 4 (October)',
    updated_at = NOW()
WHERE cricos_provider_code = '00141J';

UPDATE courses SET
    course_description = '<h4>Camberwell Girls Grammar School - International Program</h4><p>CGGS offers an outstanding education for international students in a supportive, inclusive environment. Students benefit from a strong academic program and ESL support.</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 339300,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2600,
    materials_fee = NULL,
    entry_requirements = 'AEAS test, conducted through an external provider (',
    apply_form = 'https://cggs.vic.edu.au/international/',
    updated_at = NOW()
WHERE cricos_course_code = '005303M';

