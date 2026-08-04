-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00494F';

UPDATE courses SET
    course_description = 'Course overview <p>Secondary Senior Yrs 11-12 Girls & Boys at Downlands College Ltd. Other program for international students.</p>',
    course_duration_per_week = 102,
    offshore_tuition_fee = 102000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 47000,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.downlands.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004867E';
UPDATE courses SET
    course_description = 'Course overview <p>Secondary Junior Years 7-10 Girls and Boys at Downlands College Ltd. Other program for international students.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 194000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 89000,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.downlands.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082457K';