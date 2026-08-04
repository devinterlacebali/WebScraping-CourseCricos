-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00131M';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 202395,
    onshore_tuition_fee = NULL,
    enrolment_fee = 27330,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '011407G';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 185275,
    onshore_tuition_fee = NULL,
    enrolment_fee = 29470,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '040679K';

