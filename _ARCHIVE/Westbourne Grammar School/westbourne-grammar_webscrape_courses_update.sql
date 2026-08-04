-- Westbourne Grammar School (00355F) - Web-scraped course data
-- Generated: from https://www.westbournegrammar.com

-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00355F';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 199410,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = 'For those seeking a longer journey, we welcome international students from Years 7 to 11, offering clear entry requirements, homestay options for older students, and dedicated support to help every student feel at home from day one.',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '011401C';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 209286,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = 'For those seeking a longer journey, we welcome international students from Years 7 to 11, offering clear entry requirements, homestay options for older students, and dedicated support to help every student feel at home from day one.',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '016541F';

