-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '02868J';

-- Certificate IV in Automotive Mechanical Diagnosis
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Automotive Mechanical Diagnosis</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 6950,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '091662G';

-- Diploma of Automotive Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Automotive Management</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 7500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '091689G';

-- Certificate III in Light Vehicle Mechanical Technology
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Light Vehicle Mechanical Technology</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 16500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 600,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '103673B';

-- Certificate IV in Kitchen Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Kitchen Management</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 20000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '109669E';

-- Certificate III in Commercial Cookery
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Commercial Cookery</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 15000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '109798G';

-- Diploma of Hospitality Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Hospitality Management</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 24000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '112934M';

-- Advanced Diploma of Hospitality Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Hospitality Management</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 24000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '112935K';

-- Diploma of Community Services
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Community Services</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 17990,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '115245A';