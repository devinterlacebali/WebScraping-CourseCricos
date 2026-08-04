-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00489C';

UPDATE courses SET
    course_description = 'Course overview <p>Junior Secondary Studies Years 7-10 Boys Only at Brisbane Grammar School. Junior Secondary program for international students.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 344609,
    onshore_tuition_fee = NULL,
    enrolment_fee = 147249,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.brisbanegrammar.com',
    updated_at = NOW()
WHERE cricos_course_code = '084786K';
UPDATE courses SET
    course_description = 'Course overview <p>Senior Secondary Studies Years 11 & 12 Boys Only at Brisbane Grammar School. Senior Secondary program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 175969,
    onshore_tuition_fee = NULL,
    enrolment_fee = 76589,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.brisbanegrammar.com',
    updated_at = NOW()
WHERE cricos_course_code = '084787J';
UPDATE courses SET
    course_description = 'Course overview <p>Primary Studies Years 5 & 6 Boys Only at Brisbane Grammar School. Primary program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 142559,
    onshore_tuition_fee = NULL,
    enrolment_fee = 61319,
    materials_fee = NULL,
    entry_requirements = 'Academic transcripts, AEAS test recommended, school interview',
    apply_form = 'https://www.brisbanegrammar.com',
    updated_at = NOW()
WHERE cricos_course_code = '084788G';