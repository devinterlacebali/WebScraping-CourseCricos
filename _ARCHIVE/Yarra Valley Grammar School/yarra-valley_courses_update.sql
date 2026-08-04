-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00356E';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 224324,
    onshore_tuition_fee = NULL,
    enrolment_fee = 9750,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '005473D';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 214548,
    onshore_tuition_fee = NULL,
    enrolment_fee = 10500,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '054535M';

