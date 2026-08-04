-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '03976H';

-- Diploma of Business
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Business</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 8200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '108611J';

-- Certificate IV in Ageing Support
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Ageing Support</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 10250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '110664M';

-- Advanced Diploma of Leadership and Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Leadership and Management</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 8250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '110666J';

-- Certificate III in Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 16250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '115134H';

-- Certificate III in Individual Support
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Individual Support</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 13250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '115135G';

-- Certificate IV in Disability Support
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Disability Support</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 16250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '115136F';

-- Diploma of Community Services
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Community Services</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 21250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '115137E';

-- Diploma of Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 16250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '115138D';

-- Diploma of Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 16250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '118654D';

-- Diploma of Community Services
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Community Services</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 21250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '118819K';

-- Certificate III in Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 16250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '119667B';