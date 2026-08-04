-- Curtin College (WA) (02042G) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='02042G';

UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 16900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 225,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.curtincollege.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '066028J';
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.curtincollege.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '072496G';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 65300,
    onshore_tuition_fee = NULL,
    enrolment_fee = 225,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.curtincollege.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '087938G';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 68000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 225,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.curtincollege.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '087939G';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 63600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 225,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.curtincollege.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '087940C';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 72000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 225,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.curtincollege.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '087941B';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 73000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 225,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.curtincollege.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '087942A';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 69000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 225,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Academic entry requirements apply.',
    apply_form = 'https://www.curtincollege.edu.au/international',
    updated_at = NOW()
WHERE cricos_course_code = '087943M';
