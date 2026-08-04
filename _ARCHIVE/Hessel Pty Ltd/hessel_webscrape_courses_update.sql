-- Hessel Pty Ltd (04363G) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='04363G';

UPDATE courses SET
    course_duration_per_week = 46,
    offshore_tuition_fee = 13650,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '117992E';
UPDATE courses SET
    course_duration_per_week = 46,
    offshore_tuition_fee = 7420,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '117993D';
UPDATE courses SET
    course_duration_per_week = 45,
    offshore_tuition_fee = 13700,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '117994C';
UPDATE courses SET
    course_duration_per_week = 45,
    offshore_tuition_fee = 13700,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '118681A';
UPDATE courses SET
    course_duration_per_week = 46,
    offshore_tuition_fee = 13650,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '119694K';
