-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00341A';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 196460,
    onshore_tuition_fee = NULL,
    enrolment_fee = 8350,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '082924K';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 119680,
    onshore_tuition_fee = NULL,
    enrolment_fee = 102620,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '082925J';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 55840,
    onshore_tuition_fee = NULL,
    enrolment_fee = 57872,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '082926G';

