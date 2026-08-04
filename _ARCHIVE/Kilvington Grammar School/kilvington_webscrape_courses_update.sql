-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 2 (April), Term 3 (July), Term 4 (October)',
    updated_at = NOW()
WHERE cricos_provider_code = '00149A';

UPDATE courses SET
    course_description = '<h4>Kilvington Grammar School - International Program</h4><p>Kilvington Grammar School offers a co-educational environment with strong academic record and ESL support. International students fully integrate into the Australian culture.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = 'Previous school reports, interview. English language proficiency required. International Student Handbook available.',
    apply_form = 'https://www.kilvington.vic.edu.au/enrol/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '005349G';

UPDATE courses SET
    course_description = '<h4>Kilvington Grammar School - International Program</h4><p>Kilvington Grammar School offers a co-educational environment with strong academic record and ESL support. International students fully integrate into the Australian culture.</p>',
    course_duration_per_week = 273,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = 'Previous school reports, interview. English language proficiency required. International Student Handbook available.',
    apply_form = 'https://www.kilvington.vic.edu.au/enrol/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '019777F';

