-- Department of Education (WA Schools) (01723A) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='01723A';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 37960,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.tafeinternational.wa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '025727K';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 21980,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.tafeinternational.wa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '025728J';
UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 87450,
    onshore_tuition_fee = NULL,
    enrolment_fee = 9000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.tafeinternational.wa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '044283J';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 17575,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.tafeinternational.wa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '044286F';
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 69144,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.tafeinternational.wa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '052150M';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 20286,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.tafeinternational.wa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '052152J';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 14575,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.tafeinternational.wa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '065529G';
