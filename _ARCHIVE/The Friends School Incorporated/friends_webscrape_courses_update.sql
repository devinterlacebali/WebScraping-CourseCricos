-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00477G';

UPDATE courses SET
    course_description = 'Course overview <p>Secondary Senior Yrs 11-12 at The Friends School Incorporated. Other program for international students.</p>',
    course_duration_per_week = 96,
    offshore_tuition_fee = 157701,
    onshore_tuition_fee = NULL,
    enrolment_fee = 81181,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.friends.tas.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004728E';
UPDATE courses SET
    course_description = 'Course overview <p>Secondary Junior Years 8-10 at The Friends School Incorporated. Other program for international students.</p>',
    course_duration_per_week = 153,
    offshore_tuition_fee = 223858,
    onshore_tuition_fee = NULL,
    enrolment_fee = 111718,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.friends.tas.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '021270D';
UPDATE courses SET
    course_description = 'Course overview <p>Secondary Junior Year 7 at The Friends School Incorporated. Junior Secondary program for international students.</p>',
    course_duration_per_week = 47,
    offshore_tuition_fee = 107455,
    onshore_tuition_fee = NULL,
    enrolment_fee = 71895,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.friends.tas.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '021271C';
UPDATE courses SET
    course_description = 'Course overview <p>Primary Years 4-6 at The Friends School Incorporated. Primary program for international students.</p>',
    course_duration_per_week = 153,
    offshore_tuition_fee = 96683,
    onshore_tuition_fee = NULL,
    enrolment_fee = 12973,
    materials_fee = NULL,
    entry_requirements = 'Academic transcripts, AEAS test recommended, school interview',
    apply_form = 'https://www.friends.tas.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '030826J';
UPDATE courses SET
    course_description = 'Course overview <p>Secondary Senior Years 10 - 12 at The Friends School Incorporated. Other program for international students.</p>',
    course_duration_per_week = 153,
    offshore_tuition_fee = 225691,
    onshore_tuition_fee = NULL,
    enrolment_fee = 111791,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.friends.tas.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '043008C';
UPDATE courses SET
    course_description = 'Course overview <p>International Baccalaureate Years 11-12 at The Friends School Incorporated. IB Diploma program for international students.</p>',
    course_duration_per_week = 96,
    offshore_tuition_fee = 157596,
    onshore_tuition_fee = NULL,
    enrolment_fee = 81176,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.friends.tas.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '051385M';