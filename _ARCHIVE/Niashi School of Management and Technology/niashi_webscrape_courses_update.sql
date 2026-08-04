-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '03737A';

-- Certificate IV in Leadership and Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Leadership and Management</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '104005H';

-- Diploma of Leadership and Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Leadership and Management</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 15500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '104381F';

-- Certificate IV in Business
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Business</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12750,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '105601B';

-- Diploma of Business
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Business</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 15750,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '105602A';

-- Certificate III in Carpentry
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Carpentry</p>',
    course_duration_per_week = 92,
    offshore_tuition_fee = 23050,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '107075C';

-- Certificate III in Painting and Decorating
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Painting and Decorating</p>',
    course_duration_per_week = 92,
    offshore_tuition_fee = 23050,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '107076B';

-- Certificate III in Commercial Cookery
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Commercial Cookery</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 13550,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1050,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '111428D';

-- Certificate IV in Kitchen Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Kitchen Management</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 19550,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1050,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '111429C';

-- Diploma of Hospitality Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Hospitality Management</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 19250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '111430K';

-- Advanced Diploma of Hospitality Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Hospitality Management</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 25250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '111710B';

-- Certificate III in Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 14000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1500,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '116052B';

-- Diploma of Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 16000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1500,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '116055K';

-- Diploma of Building and Construction (Building)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Building and Construction (Building)</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 23550,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1050,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '118187D';

-- Diploma of Building and Construction (Management)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Building and Construction (Management)</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 17250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '118188C';

-- Diploma of Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 16000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1500,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '118631M';

-- Certificate III in Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 14000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1500,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '119642M';