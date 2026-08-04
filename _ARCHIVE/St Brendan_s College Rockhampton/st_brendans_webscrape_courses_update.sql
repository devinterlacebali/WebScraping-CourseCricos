-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00506G';

UPDATE courses SET
    course_description = 'Course overview <p>Secondary Senior Yrs 11-12 Boys & Girls at St Brendan_s College Rockhampton. Other program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 87996,
    onshore_tuition_fee = NULL,
    enrolment_fee = 38518,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.tccr.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '007379G';
UPDATE courses SET
    course_description = 'Course overview <p>Secondary Junior Years 7-10 Boys & Girls at St Brendan_s College Rockhampton. Other program for international students.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 170062,
    onshore_tuition_fee = NULL,
    enrolment_fee = 74668,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.tccr.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '082647D';