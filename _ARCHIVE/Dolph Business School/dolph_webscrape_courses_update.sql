-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '03642G';

-- Diploma of Hospitality Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Hospitality Management</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 16000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '0101070';

-- Diploma of Leadership and Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Leadership and Management</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 13000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '104346J';

-- Certificate IV in Kitchen Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Kitchen Management</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 16000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '109548C';

-- Certificate III in Commercial Cookery
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Commercial Cookery</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 22000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '109873A';

-- Diploma of Business
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Business</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 13000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '110133E';

-- Graduate Diploma of Management (Learning)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Graduate Diploma of Management (Learning)</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 31000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '113168C';

-- Diploma of Community Services
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Community Services</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 24000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '114232C';

-- Diploma of Hospitality Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Hospitality Management</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 17600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1600,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '114305B';

-- Diploma of Community Services
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Community Services</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 32000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2000,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '118768E';

-- Advanced Diploma of Hospitality Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Hospitality Management</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 32000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2500,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '120817E';

-- Diploma of Interpreting
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Interpreting</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 10200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1200,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '120818D';