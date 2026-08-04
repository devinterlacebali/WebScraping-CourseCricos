UPDATE provider_institution SET
    intake_date = 'January, April, July, October',
    updated_at = NOW()
WHERE cricos_provider_code = '00334M';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 237384,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7344,
    materials_fee = NULL,
    entry_requirements = 'AEAS testing, school reports, interview. Contact enrolments@plc.vic.edu.au for details.',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '016361K';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 237384,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7344,
    materials_fee = NULL,
    entry_requirements = 'AEAS testing, school reports, interview. Contact enrolments@plc.vic.edu.au for details.',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '016362J';

