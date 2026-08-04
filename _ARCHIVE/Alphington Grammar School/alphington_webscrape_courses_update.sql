-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '01376D';

-- Secondary Senior Years 7 - 12
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Secondary Senior Years 7 - 12</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 159538,
    onshore_tuition_fee = NULL,
    enrolment_fee = 65240,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '018421J';

-- Primary Years P - 6
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Primary Years P - 6</p>',
    course_duration_per_week = 273,
    offshore_tuition_fee = 137120,
    onshore_tuition_fee = NULL,
    enrolment_fee = 54878,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '043106A';