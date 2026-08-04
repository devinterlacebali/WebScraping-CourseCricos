-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00491J';

UPDATE courses SET
    course_description = 'Course overview <p>Secondary Years 11-12 Boys Only at Brisbane Boys College. Other program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 202800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 95100,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.bbc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004857G';
UPDATE courses SET
    course_description = 'Course overview <p>Secondary Years 7 to 10 Boys Only at Brisbane Boys College. Other program for international students.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 402600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 187200,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.bbc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '084747F';
UPDATE courses SET
    course_description = 'Course overview <p>Lower Primary Years Prep to Year 3 Boys Only at Brisbane Boys College. Primary program for international students.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 235700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 24100,
    materials_fee = NULL,
    entry_requirements = 'Academic transcripts, AEAS test recommended, school interview',
    apply_form = 'https://www.bbc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '084748E';
UPDATE courses SET
    course_description = 'Course overview <p>Upper Primary Years 4 to 6 Boys Only at Brisbane Boys College. Primary program for international students.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 177900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 18800,
    materials_fee = NULL,
    entry_requirements = 'Academic transcripts, AEAS test recommended, school interview',
    apply_form = 'https://www.bbc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '084749D';