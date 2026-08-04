-- AUCTUS Consulting Pty Ltd (04213K) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='04213K';

UPDATE courses SET
    course_duration_per_week = 56,
    offshore_tuition_fee = 10950,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '114966J';
UPDATE courses SET
    course_duration_per_week = 27,
    offshore_tuition_fee = 6500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 800,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '114967H';
UPDATE courses SET
    course_duration_per_week = 19,
    offshore_tuition_fee = 6800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '114968G';
UPDATE courses SET
    course_duration_per_week = 48,
    offshore_tuition_fee = 11500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 800,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '117316H';
UPDATE courses SET
    course_duration_per_week = 56,
    offshore_tuition_fee = 10950,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '118854G';
