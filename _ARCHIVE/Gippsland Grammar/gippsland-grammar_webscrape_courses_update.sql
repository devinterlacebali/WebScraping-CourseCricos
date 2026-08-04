UPDATE provider_institution SET
    intake_date = 'January, April, July, October',
    updated_at = NOW()
WHERE cricos_provider_code = '00340B';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 156680,
    onshore_tuition_fee = NULL,
    enrolment_fee = 27100,
    materials_fee = NULL,
    entry_requirements = 'School reports, English proficiency, interview',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005424B';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 140000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 27100,
    materials_fee = NULL,
    entry_requirements = 'School reports, English proficiency, interview',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '067257K';

