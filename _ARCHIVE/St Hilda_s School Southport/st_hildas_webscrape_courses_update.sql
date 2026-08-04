-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00510M';

UPDATE courses SET
    course_description = 'Course overview <p>Secondary Senior Years 11-12 at St Hilda_s School Southport. Other program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 160068,
    onshore_tuition_fee = NULL,
    enrolment_fee = 69698,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.sthildas.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004923B';
UPDATE courses SET
    course_description = 'Course overview <p>Primary Years P-6 at St Hilda_s School Southport. Primary program for international students.</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 266722,
    onshore_tuition_fee = NULL,
    enrolment_fee = 47479,
    materials_fee = NULL,
    entry_requirements = 'Academic transcripts, AEAS test recommended, school interview',
    apply_form = 'https://www.sthildas.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '086182M';
UPDATE courses SET
    course_description = 'Course overview <p>Secondary Junior Years 7-10 at St Hilda_s School Southport. Other program for international students.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 296377,
    onshore_tuition_fee = NULL,
    enrolment_fee = 125168,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.sthildas.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '086183K';