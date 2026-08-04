-- Kennedy Baptist College Association Inc. (01688K) - Webscrape Update
UPDATE provider_institution SET intake_date='November', updated_at=NOW() WHERE cricos_provider_code='01688K';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 111590,
    onshore_tuition_fee = NULL,
    enrolment_fee = 13872,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.kennedy.wa.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '0100268';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 67264,
    onshore_tuition_fee = NULL,
    enrolment_fee = 9541,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.kennedy.wa.edu.au/international-students',
    updated_at = NOW()
WHERE cricos_course_code = '0100269';
