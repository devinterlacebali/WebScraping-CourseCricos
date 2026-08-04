-- Lotus Learning and Trades Pty Ltd (04314E) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='04314E';

UPDATE courses SET
    course_duration_per_week = 87,
    offshore_tuition_fee = 21950,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2050,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '117187A';
UPDATE courses SET
    course_duration_per_week = 20,
    offshore_tuition_fee = 6500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '117188M';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 14900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '117221D';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 14900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '117222C';
