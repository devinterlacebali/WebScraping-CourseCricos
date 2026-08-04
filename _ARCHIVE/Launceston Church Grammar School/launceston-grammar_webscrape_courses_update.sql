-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '00650K';

-- Secondary Senior Years 11-12
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Secondary Senior Years 11-12</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 103500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 43850,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '004200D';

-- Secondary Junior Years 7-10
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Secondary Junior Years 7-10</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 195800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 83400,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '017743K';

-- Primary School Grade 5-6
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Primary School Grade 5-6</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 95100,
    onshore_tuition_fee = NULL,
    enrolment_fee = 43850,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '051397G';