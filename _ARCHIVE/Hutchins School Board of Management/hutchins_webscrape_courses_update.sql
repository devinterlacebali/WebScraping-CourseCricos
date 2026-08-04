-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00478F';

UPDATE courses SET
    course_description = 'Course overview <p>Secondary Junior Grades 7-12 at Hutchins School Board of Management. Other program for international students.</p>',
    course_duration_per_week = 304,
    offshore_tuition_fee = 464443,
    onshore_tuition_fee = NULL,
    enrolment_fee = 203162,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.hutchins.tas.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004729D';
UPDATE courses SET
    course_description = 'Course overview <p>Primary Prep - 6 at Hutchins School Board of Management. Primary program for international students.</p>',
    course_duration_per_week = 356,
    offshore_tuition_fee = 257876,
    onshore_tuition_fee = NULL,
    enrolment_fee = 22776,
    materials_fee = NULL,
    entry_requirements = 'Academic transcripts, AEAS test recommended, school interview',
    apply_form = 'https://www.hutchins.tas.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '042917G';