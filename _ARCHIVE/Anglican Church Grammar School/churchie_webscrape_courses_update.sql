-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00487E';

UPDATE courses SET
    course_description = 'Course overview <p>Junior Secondary Studies (Years 7-10) Boys Only at Anglican Church Grammar School. Junior Secondary program for international students.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 380683,
    onshore_tuition_fee = NULL,
    enrolment_fee = 177123,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.churchie.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '0100111';
UPDATE courses SET
    course_description = 'Course overview <p>Senior Secondary Studies (Years 11-12) Boys Only at Anglican Church Grammar School. Senior Secondary program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 191781,
    onshore_tuition_fee = NULL,
    enrolment_fee = 92501,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.churchie.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '0100112';
UPDATE courses SET
    course_description = 'Course overview <p>International Baccalaureate Diploma (Years 11-12) Boys Only at Anglican Church Grammar School. IB Diploma program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 190070,
    onshore_tuition_fee = NULL,
    enrolment_fee = 90790,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.churchie.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '0100118';
UPDATE courses SET
    course_description = 'Course overview <p>International Baccalaureate Primary Years Program (Prep to Year 6) at Anglican Church Grammar School. Primary program for international students.</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 303823,
    onshore_tuition_fee = NULL,
    enrolment_fee = 12199,
    materials_fee = NULL,
    entry_requirements = 'Academic transcripts, AEAS test recommended, school interview',
    apply_form = 'https://www.churchie.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '112749A';