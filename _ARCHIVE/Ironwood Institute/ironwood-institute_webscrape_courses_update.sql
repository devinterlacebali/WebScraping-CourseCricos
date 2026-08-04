-- Ironwood Institute (03039E) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='03039E';

UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 24500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.ironwood.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '090828K';
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 19400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 600,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.ironwood.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '097347D';
UPDATE courses SET
    course_duration_per_week = 48,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.ironwood.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '112488F';
UPDATE courses SET
    course_duration_per_week = 24,
    offshore_tuition_fee = 7200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.ironwood.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '112489E';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 14250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.ironwood.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '113092G';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 14250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.ironwood.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '113093F';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 19500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.ironwood.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '113094E';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 19500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.ironwood.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '113095D';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 14250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact provider for entry requirements',
    apply_form = 'https://www.ironwood.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '117238F';
