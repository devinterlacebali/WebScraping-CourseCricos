-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00488D';

UPDATE courses SET
    course_description = 'Course overview <p>Secondary Junior Yrs 9-10 Boys & Girls at Blackheath and Thornburgh College. Other program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 103640,
    onshore_tuition_fee = NULL,
    enrolment_fee = 38064,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.btc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004846K';
UPDATE courses SET
    course_description = 'Course overview <p>Secondary Senior Yrs 11-12 Boys & Girls at Blackheath and Thornburgh College. Other program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 108620,
    onshore_tuition_fee = NULL,
    enrolment_fee = 38064,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.btc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004847J';
UPDATE courses SET
    course_description = 'Course overview <p>Secondary Junior Years 7-8 Boys & Girls at Blackheath and Thornburgh College. Other program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 97892,
    onshore_tuition_fee = NULL,
    enrolment_fee = 38064,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.btc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '016451G';
UPDATE courses SET
    course_description = 'Course overview <p>Primary School Year 4-6 at Blackheath and Thornburgh College. Primary program for international students.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 82688,
    onshore_tuition_fee = NULL,
    enrolment_fee = 4250,
    materials_fee = NULL,
    entry_requirements = 'Academic transcripts, AEAS test recommended, school interview',
    apply_form = 'https://www.btc.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '086201B';