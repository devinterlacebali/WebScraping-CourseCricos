-- Milner International College of English (00061J) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='00061J';

UPDATE courses SET
    course_duration_per_week = 48,
    offshore_tuition_fee = 18880,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'IELTS required. Academic entry requirements apply.',
    apply_form = 'https://www.milner.wa.edu.au/international/english',
    updated_at = NOW()
WHERE cricos_course_code = '010219J';
UPDATE courses SET
    course_duration_per_week = 12,
    offshore_tuition_fee = 5483,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'IELTS required. Academic entry requirements apply.',
    apply_form = 'https://www.milner.wa.edu.au/international/english',
    updated_at = NOW()
WHERE cricos_course_code = '074424G';
UPDATE courses SET
    course_duration_per_week = 16,
    offshore_tuition_fee = 6590,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'IELTS required. Academic entry requirements apply.',
    apply_form = 'https://www.milner.wa.edu.au/international/english',
    updated_at = NOW()
WHERE cricos_course_code = '098470D';
