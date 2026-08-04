-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00509D';

UPDATE courses SET
    course_description = 'Course overview <p>Secondary Senior Yrs 11-12 Boys Only at St Augustine_s College Cairns. Other program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102154,
    onshore_tuition_fee = NULL,
    enrolment_fee = 47250,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.sac.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004918K';
UPDATE courses SET
    course_description = 'Course overview <p>Secondary Junior Years 7-10 Boys Only at St Augustine_s College Cairns. Other program for international students.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 194993,
    onshore_tuition_fee = NULL,
    enrolment_fee = 88972,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.sac.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082949A';