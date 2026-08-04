-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '04305F';

-- Certificate III in Commercial Cookery
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Commercial Cookery</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 30800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2800,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117071B';

-- Certificate IV in Kitchen Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Kitchen Management</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 40500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 5500,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117072A';

-- Diploma of Hospitality Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Hospitality Management</p>',
    course_duration_per_week = 94,
    offshore_tuition_fee = 40500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 5500,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117073M';

-- Certificate III in Carpentry
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Carpentry</p>',
    course_duration_per_week = 60,
    offshore_tuition_fee = 32800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2800,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117103K';

-- Certificate III in Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 27800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2800,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117104J';

-- Diploma of Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 27800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2800,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117105H';

-- Graduate Diploma of Management (Learning)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Graduate Diploma of Management (Learning)</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 22300,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2300,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117106G';

-- Diploma of Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 27800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2800,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '118678G';

-- Certificate III in Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 27800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2800,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '119691B';