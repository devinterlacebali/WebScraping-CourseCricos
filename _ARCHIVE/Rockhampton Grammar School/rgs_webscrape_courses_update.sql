-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00507F';

UPDATE courses SET
    course_description = 'Course overview <p>Secondary Senior Yrs 11-12 at Rockhampton Grammar School. Other program for international students.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 140184,
    onshore_tuition_fee = NULL,
    enrolment_fee = 62372,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.rgs.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004909M';
UPDATE courses SET
    course_description = 'Course overview <p>High School Preparation Programme at Rockhampton Grammar School. Primary program for international students.</p>',
    course_duration_per_week = 48,
    offshore_tuition_fee = 56615,
    onshore_tuition_fee = NULL,
    enrolment_fee = 27410,
    materials_fee = NULL,
    entry_requirements = 'English language proficiency assessment, placement test',
    apply_form = 'https://www.rgs.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '0101732';
UPDATE courses SET
    course_description = 'Course overview <p>Secondary Years 7-10 at Rockhampton Grammar School. Other program for international students.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 270194,
    onshore_tuition_fee = NULL,
    enrolment_fee = 114570,
    materials_fee = NULL,
    entry_requirements = 'AEAS test or IELTS 5.5-6.0, academic transcripts, school interview, previous school reports',
    apply_form = 'https://www.rgs.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '086204K';
UPDATE courses SET
    course_description = 'Course overview <p>Primary School Studies (Years P-6) at Rockhampton Grammar School. Primary program for international students.</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 280942,
    onshore_tuition_fee = NULL,
    enrolment_fee = 40730,
    materials_fee = NULL,
    entry_requirements = 'Academic transcripts, AEAS test recommended, school interview',
    apply_form = 'https://www.rgs.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '109137M';