-- Aroha College Pty Ltd (04377A) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='04377A';

UPDATE courses SET
    course_duration_per_week = 48,
    offshore_tuition_fee = 8900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 400,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '118953D';
UPDATE courses SET
    course_duration_per_week = 48,
    offshore_tuition_fee = 8000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 400,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '118954C';
UPDATE courses SET
    course_duration_per_week = 58,
    offshore_tuition_fee = 11500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '118955B';
UPDATE courses SET
    course_duration_per_week = NULL,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '118956A';
UPDATE courses SET
    course_duration_per_week = NULL,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '118957M';
UPDATE courses SET
    course_duration_per_week = NULL,
    offshore_tuition_fee = 110,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '118958K';
UPDATE courses SET
    course_duration_per_week = 58,
    offshore_tuition_fee = 11500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '119032D';
UPDATE courses SET
    course_duration_per_week = 48,
    offshore_tuition_fee = 8900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 400,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '119696H';
