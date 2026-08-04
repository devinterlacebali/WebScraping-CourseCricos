-- Greenhouse Education Pty Ltd (04378M) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='04378M';

UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 9500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '119107A';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 14500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1750,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '119108M';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 9500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '119148C';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 9500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '119697G';
