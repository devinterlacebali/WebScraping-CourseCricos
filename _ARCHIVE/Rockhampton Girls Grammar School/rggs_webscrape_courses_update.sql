-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00508E';

UPDATE courses SET
    course_description = 'Course overview <p>Secondary Senior Years 11-12 at Rockhampton Girls Grammar School. Other program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 133651,
    onshore_tuition_fee = NULL,
    enrolment_fee = 61899,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.rggs.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004913D';
UPDATE courses SET
    course_description = 'Course overview <p>Primary Years 4-6 at Rockhampton Girls Grammar School. Primary program for international students.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 125670,
    onshore_tuition_fee = NULL,
    enrolment_fee = 37608,
    materials_fee = NULL,
    entry_requirements = 'Academic transcripts, AEAS test recommended, school interview',
    apply_form = 'https://www.rggs.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082472M';
UPDATE courses SET
    course_description = 'Course overview <p>Secondary Junior Years 7-10 at Rockhampton Girls Grammar School. Other program for international students.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 249560,
    onshore_tuition_fee = NULL,
    enrolment_fee = 109914,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.rggs.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082474J';