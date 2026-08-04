-- Major Blue Air Pty Ltd (03802G) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='03802G';

UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 80000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '109222C';
