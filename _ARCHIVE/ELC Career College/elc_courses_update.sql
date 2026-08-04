-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00051M';

UPDATE courses SET
    course_duration_per_week = 36,
    offshore_tuition_fee = 6000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '103913B';

UPDATE courses SET
    course_duration_per_week = 36,
    offshore_tuition_fee = 6000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '103938D';

UPDATE courses SET
    course_duration_per_week = 48,
    offshore_tuition_fee = 8000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '104098J';

UPDATE courses SET
    course_duration_per_week = 48,
    offshore_tuition_fee = 8000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '104121D';

UPDATE courses SET
    course_duration_per_week = 48,
    offshore_tuition_fee = 8000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '104466A';

UPDATE courses SET
    course_duration_per_week = 48,
    offshore_tuition_fee = 8000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 125,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '105980H';

UPDATE courses SET
    course_duration_per_week = 76,
    offshore_tuition_fee = 9600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 645,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '108567H';

UPDATE courses SET
    course_duration_per_week = 76,
    offshore_tuition_fee = 9600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 645,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '108568G';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 20000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 645,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '112708K';

