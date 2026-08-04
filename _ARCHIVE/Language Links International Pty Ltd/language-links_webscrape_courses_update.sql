-- Language Links International Pty Ltd (02139J) - Webscrape Update
UPDATE provider_institution SET intake_date='January, March, June, September', updated_at=NOW() WHERE cricos_provider_code='02139J';

UPDATE courses SET
    course_duration_per_week = 112,
    offshore_tuition_fee = 40320,
    onshore_tuition_fee = NULL,
    enrolment_fee = 600,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'IELTS required.',
    apply_form = 'https://www.languagelinks.wa.edu.au/courses',
    updated_at = NOW()
WHERE cricos_course_code = '097129C';
UPDATE courses SET
    course_duration_per_week = 44,
    offshore_tuition_fee = 15120,
    onshore_tuition_fee = NULL,
    enrolment_fee = 600,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'IELTS required.',
    apply_form = 'https://www.languagelinks.wa.edu.au/courses',
    updated_at = NOW()
WHERE cricos_course_code = '097774G';
UPDATE courses SET
    course_duration_per_week = 44,
    offshore_tuition_fee = 15120,
    onshore_tuition_fee = NULL,
    enrolment_fee = 600,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'IELTS required.',
    apply_form = 'https://www.languagelinks.wa.edu.au/courses',
    updated_at = NOW()
WHERE cricos_course_code = '098071G';
