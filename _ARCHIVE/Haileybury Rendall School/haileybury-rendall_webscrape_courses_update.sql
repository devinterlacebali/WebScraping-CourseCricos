-- Haileybury Rendall School (00971D) - Webscrape Update
UPDATE provider_institution SET intake_date='May, June, July', updated_at=NOW() WHERE cricos_provider_code='00971D';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 64482,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.haileyburyrendall.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '0100358';
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 128964,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.haileyburyrendall.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '0100359';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 64590,
    onshore_tuition_fee = NULL,
    enrolment_fee = 34000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.haileyburyrendall.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '119871J';
