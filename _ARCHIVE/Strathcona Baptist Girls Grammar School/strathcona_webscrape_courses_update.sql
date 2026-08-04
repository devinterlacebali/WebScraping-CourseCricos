-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'Term Dates"},{"@type":"BreadcrumbList","@id":"https:\/\/www.',
    updated_at = NOW()
WHERE cricos_provider_code = '00577C';

-- Secondary Years 7 - 12 Girls Only
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Secondary Years 7 - 12 Girls Only</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 6000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 12716,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '005486K';

-- Primary Years P-6 (Girls only)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Primary Years P-6 (Girls only)</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 7000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 22253,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '119176K';