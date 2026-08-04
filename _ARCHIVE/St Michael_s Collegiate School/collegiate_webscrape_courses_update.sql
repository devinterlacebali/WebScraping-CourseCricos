-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00482K';

UPDATE courses SET
    course_description = 'Course overview <p>Secondary Studies Years 7 - 9 at St Michael_s Collegiate School. Other program for international students.</p>',
    course_duration_per_week = 150,
    offshore_tuition_fee = 97800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.collegiate.tas.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '028838A';
UPDATE courses SET
    course_description = 'Course overview <p>Secondary Studies Years 10 - 12 at St Michael_s Collegiate School. Other program for international students.</p>',
    course_duration_per_week = 150,
    offshore_tuition_fee = 97800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.collegiate.tas.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '029255E';
UPDATE courses SET
    course_description = 'Course overview <p>Primary Years Kindergarten - 6 at St Michael_s Collegiate School. Primary program for international students.</p>',
    course_duration_per_week = 410,
    offshore_tuition_fee = 185200,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = 'Academic transcripts, AEAS test recommended, school interview',
    apply_form = 'https://www.collegiate.tas.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '088056A';
UPDATE courses SET
    course_description = 'Course overview <p>Secondary School Year 7 - 10 at St Michael_s Collegiate School. Junior Secondary program for international students.</p>',
    course_duration_per_week = 202,
    offshore_tuition_fee = 130400,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.collegiate.tas.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '088057M';
UPDATE courses SET
    course_description = 'Course overview <p>Secondary School Year 11 - 12 at St Michael_s Collegiate School. Senior Secondary program for international students.</p>',
    course_duration_per_week = 98,
    offshore_tuition_fee = 65200,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.collegiate.tas.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '088058K';