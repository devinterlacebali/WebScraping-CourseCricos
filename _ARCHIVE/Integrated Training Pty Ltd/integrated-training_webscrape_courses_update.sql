-- Integrated Training Pty Ltd (03901E) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='03901E';

UPDATE courses SET
    course_duration_per_week = 6,
    offshore_tuition_fee = 899,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '105329B';
