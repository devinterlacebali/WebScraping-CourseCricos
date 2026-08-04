-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00500B';

UPDATE courses SET
    course_description = 'Course overview <p>Senior Secondary (Year 11 and 12) at John Paul College Limited. Senior Secondary program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 133840,
    onshore_tuition_fee = NULL,
    enrolment_fee = 68060,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.jpc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004885C';
UPDATE courses SET
    course_description = 'Course overview <p>High School Preparation Course at John Paul College Limited. Primary program for international students.</p>',
    course_duration_per_week = 66,
    offshore_tuition_fee = 82630,
    onshore_tuition_fee = NULL,
    enrolment_fee = 42225,
    materials_fee = NULL,
    entry_requirements = 'English language proficiency assessment, placement test',
    apply_form = 'https://www.jpc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '0100089';
UPDATE courses SET
    course_description = 'Course overview <p>Primary (Prep to Year 6) at John Paul College Limited. Primary program for international students.</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 413627,
    onshore_tuition_fee = NULL,
    enrolment_fee = 211096,
    materials_fee = NULL,
    entry_requirements = 'Academic transcripts, AEAS test recommended, school interview',
    apply_form = 'https://www.jpc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '010139J';
UPDATE courses SET
    course_description = 'Course overview <p>Junior Secondary Years 7 to 10 at John Paul College Limited. Junior Secondary program for international students.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 259226,
    onshore_tuition_fee = NULL,
    enrolment_fee = 129930,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.jpc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082662E';
UPDATE courses SET
    course_description = 'Course overview <p>Primary School Preparation at John Paul College Limited. Primary program for international students.</p>',
    course_duration_per_week = 38,
    offshore_tuition_fee = 49777,
    onshore_tuition_fee = NULL,
    enrolment_fee = 25534,
    materials_fee = NULL,
    entry_requirements = 'English language proficiency assessment, placement test',
    apply_form = 'https://www.jpc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '120138F';