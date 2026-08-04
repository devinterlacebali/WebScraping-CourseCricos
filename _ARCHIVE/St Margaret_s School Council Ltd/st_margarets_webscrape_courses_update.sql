-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00511K';

UPDATE courses SET
    course_description = 'Course overview <p>Secondary Senior Yrs 11-12 at St Margaret_s School Council Ltd. Other program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 170744,
    onshore_tuition_fee = NULL,
    enrolment_fee = 70784,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.stmargarets.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004927J';
UPDATE courses SET
    course_description = 'Course overview <p>Primary Years 1-6 at St Margaret_s School Council Ltd. Primary program for international students.</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 331976,
    onshore_tuition_fee = NULL,
    enrolment_fee = 76804,
    materials_fee = NULL,
    entry_requirements = 'Academic transcripts, AEAS test recommended, school interview',
    apply_form = 'https://www.stmargarets.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '085888G';
UPDATE courses SET
    course_description = 'Course overview <p>Secondary Junior Years 7-10 at St Margaret_s School Council Ltd. Other program for international students.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 335458,
    onshore_tuition_fee = NULL,
    enrolment_fee = 135538,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.stmargarets.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '085889F';