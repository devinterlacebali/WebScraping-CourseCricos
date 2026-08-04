-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00499A';

UPDATE courses SET
    course_description = 'Course overview <p>Secondary Senior Yrs 11-12 Boys Only at Ipswich Grammar School. Other program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 138416,
    onshore_tuition_fee = NULL,
    enrolment_fee = 52840,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.ipswichgrammar.com',
    updated_at = NOW()
WHERE cricos_course_code = '004881G';
UPDATE courses SET
    course_description = 'Course overview <p>Junior Secondary Years 7-10 Boys Only at Ipswich Grammar School. Junior Secondary program for international students.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 261392,
    onshore_tuition_fee = NULL,
    enrolment_fee = 99950,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.ipswichgrammar.com',
    updated_at = NOW()
WHERE cricos_course_code = '082458J';
UPDATE courses SET
    course_description = 'Course overview <p>Primary School Studies Years P-6 at Ipswich Grammar School. Primary program for international students.</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 242925,
    onshore_tuition_fee = NULL,
    enrolment_fee = 20000,
    materials_fee = NULL,
    entry_requirements = 'Academic transcripts, AEAS test recommended, school interview',
    apply_form = 'https://www.ipswichgrammar.com',
    updated_at = NOW()
WHERE cricos_course_code = '096712G';