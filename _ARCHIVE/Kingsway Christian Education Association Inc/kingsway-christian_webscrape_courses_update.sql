-- Kingsway Christian Education Association Inc. (01855M) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='01855M';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 141744,
    onshore_tuition_fee = NULL,
    enrolment_fee = 9556,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'IELTS required. AEAS test required. Academic entry requirements apply.',
    apply_form = 'https://www.kingsway.wa.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '029263E';
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 117461,
    onshore_tuition_fee = NULL,
    enrolment_fee = 4618,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'IELTS required. AEAS test required. Academic entry requirements apply.',
    apply_form = 'https://www.kingsway.wa.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '096105G';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 58966,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2900,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'IELTS required. AEAS test required. Academic entry requirements apply.',
    apply_form = 'https://www.kingsway.wa.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '096107F';
