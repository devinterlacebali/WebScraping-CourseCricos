-- School of Engineering Australia Pty Ltd (04224G) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='04224G';

UPDATE courses SET
    course_duration_per_week = 80,
    offshore_tuition_fee = 25000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '115216F';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 29000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '115217E';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 33000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2300,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '115218D';
UPDATE courses SET
    course_duration_per_week = 80,
    offshore_tuition_fee = 25000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '120046K';
