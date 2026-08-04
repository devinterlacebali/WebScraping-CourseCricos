-- Goldthorn International Pty Ltd (03928E) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='03928E';

UPDATE courses SET
    course_duration_per_week = 108,
    offshore_tuition_fee = 26250,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '106741D';
UPDATE courses SET
    course_duration_per_week = 93,
    offshore_tuition_fee = 23250,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '109602B';
UPDATE courses SET
    course_duration_per_week = 67,
    offshore_tuition_fee = 16750,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '109909E';
UPDATE courses SET
    course_duration_per_week = 108,
    offshore_tuition_fee = 26000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '113005M';
