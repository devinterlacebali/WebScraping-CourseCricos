-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00496D';

UPDATE courses SET
    course_description = 'Course overview <p>Senior Secondary Years 11 to 12 at The Glennie School. Senior Secondary program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 132871,
    onshore_tuition_fee = NULL,
    enrolment_fee = 67235,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.glennie.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004872G';
UPDATE courses SET
    course_description = 'Course overview <p>Junior Secondary Years 7 to 10 at The Glennie School. Junior Secondary program for international students.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 255185,
    onshore_tuition_fee = NULL,
    enrolment_fee = 123913,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.glennie.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '084571C';