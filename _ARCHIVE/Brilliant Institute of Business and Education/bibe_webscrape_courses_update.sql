-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '03961D';

-- Certificate III in Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 15500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '111053H';

-- Diploma of Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 15500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '111054G';

-- Graduate Diploma of Management (Learning)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Graduate Diploma of Management (Learning)</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 14000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '112911G';

-- Diploma of Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 15500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '118913A';

-- Certificate III in Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Early Childhood Education and Care</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 15500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '119665D';

-- Certificate III in Solid Plastering
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Solid Plastering</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 22000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '120679K';

-- Certificate III in Bricklaying and Blocklaying
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Bricklaying and Blocklaying</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 22000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '120680F';