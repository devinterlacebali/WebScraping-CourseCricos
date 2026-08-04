-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '03611D';

-- Diploma of Leadership and Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Leadership and Management</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '108129H';

-- Advanced Diploma of Leadership and Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Leadership and Management</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 14000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '108130D';

-- Certificate III in Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '108574J';

-- Diploma of Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 13000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '108575H';

-- Certificate III in Commercial Cookery
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Commercial Cookery</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 16000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '110706F';

-- Certificate IV in Kitchen Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Kitchen Management</p>',
    course_duration_per_week = 96,
    offshore_tuition_fee = 24000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1500,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '110707E';

-- Diploma of Hospitality Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Hospitality Management</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 16000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '110708D';

-- Advanced Diploma of Information Technology
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Information Technology</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 28300,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2300,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '116774A';

-- Diploma of Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 13000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '118622A';

-- Certificate III in Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '119632B';