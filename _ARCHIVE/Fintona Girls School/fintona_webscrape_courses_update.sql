-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'Term 1 (January), Term 2 (April), Term 3 (July), Term 4 (October)',
    updated_at = NOW()
WHERE cricos_provider_code = '00139C';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Fintona Girls School - International Program</h4><p>Fintona offers a quality education for international students in 7-12. The school provides a supportive learning environment with ESL support.</p></p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 355620,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1800,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required.</p>',
    apply_form = 'https://www.fintona.vic.edu.au/enrolment',
    updated_at = NOW()
WHERE cricos_course_code = '005313J';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p><h4>Fintona Girls School - International Program</h4><p>Fintona offers a quality education for international students in P-6. The school provides a supportive learning environment with ESL support.</p></p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 326060,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1800,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>AEAS test and interview. Minimum English proficiency required.</p>',
    apply_form = 'https://www.fintona.vic.edu.au/enrolment',
    updated_at = NOW()
WHERE cricos_course_code = '016256M';

