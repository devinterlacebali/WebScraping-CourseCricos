-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'term_string}"},"query-input":{"@type":"PropertyValueSpecification","valueRequired":true,"valueName":"search_term_string"}}],"inLanguage":"en-AU"},{"@type":"Organization","@id":"https://www.',
    updated_at = NOW()
WHERE cricos_provider_code = '03803G';

-- Primary (Kindergarten to Year 6)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Primary (Kindergarten to Year 6)</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 207011,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7556,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '0100867';

-- Junior Secondary (Years 7 to 10)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Junior Secondary (Years 7 to 10)</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 137669,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6660,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '0100868';

-- Senior Secondary (Years 11 and 12)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Senior Secondary (Years 11 and 12)</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 74412,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3080,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '0100869';

-- Primary (Kindergarten to Year 6)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Primary (Kindergarten to Year 6)</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 207011,
    onshore_tuition_fee = NULL,
    enrolment_fee = 7556,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '0100870';