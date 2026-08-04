-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 2 (April), Term 3 (July), Term 4 (October)',
    updated_at = NOW()
WHERE cricos_provider_code = '00150G';

UPDATE courses SET
    course_description = '<h4>Kingswood College - International Program</h4><p>Kingswood College warmly welcomes international students in Prep to Year 12 with a dedicated International Student Coordinator and ESL support.</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = 35376,
    materials_fee = NULL,
    entry_requirements = 'AEAS test, academic transcripts, interview with Head of School and/or International Student Coordinator. English language proficiency: IELTS or equivalent.',
    apply_form = 'https://www.kingswoodcollege.vic.edu.au/enrolment-and-tours/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '001105E';

UPDATE courses SET
    course_description = '<h4>Kingswood College - International Program</h4><p>Kingswood College warmly welcomes international students in Prep to Year 12 with a dedicated International Student Coordinator and ESL support.</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = 42460,
    materials_fee = NULL,
    entry_requirements = 'AEAS test, academic transcripts, interview with Head of School and/or International Student Coordinator. English language proficiency: IELTS or equivalent.',
    apply_form = 'https://www.kingswoodcollege.vic.edu.au/enrolment-and-tours/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '011348C';

