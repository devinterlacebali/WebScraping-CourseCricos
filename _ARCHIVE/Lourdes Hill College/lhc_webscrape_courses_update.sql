-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00503K';

UPDATE courses SET
    course_description = 'Course overview <p>Senior Secondary Years 11-12 Girls Only at Lourdes Hill College. Senior Secondary program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 118873,
    onshore_tuition_fee = NULL,
    enrolment_fee = 55633,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.lhc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '088020B';
UPDATE courses SET
    course_description = 'Course overview <p>Primary School Studies Years 5-6 Girls Only at Lourdes Hill College. Primary program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 63250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6650,
    materials_fee = NULL,
    entry_requirements = 'Academic transcripts, AEAS test recommended, school interview',
    apply_form = 'https://www.lhc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '115592D';
UPDATE courses SET
    course_description = 'Course overview <p>Junior Secondary Studies Years 7-10 Girls Only at Lourdes Hill College. Junior Secondary program for international students.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 229111,
    onshore_tuition_fee = NULL,
    enrolment_fee = 106231,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.lhc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '115593C';