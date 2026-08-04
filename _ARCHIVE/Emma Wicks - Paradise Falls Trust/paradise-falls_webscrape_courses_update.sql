-- Emma Wicks - Paradise Falls Trust (03839F) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='03839F';

UPDATE courses SET
    course_duration_per_week = 4,
    offshore_tuition_fee = 840,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '102198K';
