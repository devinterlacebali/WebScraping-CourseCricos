-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'term:'''',current_page:''https://www.',
    updated_at = NOW()
WHERE cricos_provider_code = '02506B';

-- Certificate III in Hospitality
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Hospitality</p>',
    course_duration_per_week = 36,
    offshore_tuition_fee = 9000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '0101982';

-- Certificate III in Individual Support
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Individual Support</p>',
    course_duration_per_week = 62,
    offshore_tuition_fee = 12500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '0102057';

-- Certificate IV in Ageing Support
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Ageing Support</p>',
    course_duration_per_week = 76,
    offshore_tuition_fee = 15000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '0102058';

-- Diploma of Community Services
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Community Services</p>',
    course_duration_per_week = 100,
    offshore_tuition_fee = 20000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '0102059';

-- Diploma of Hospitality Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Hospitality Management</p>',
    course_duration_per_week = 62,
    offshore_tuition_fee = 19950,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '091009D';

-- Advanced Diploma of Hospitality Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Hospitality Management</p>',
    course_duration_per_week = 86,
    offshore_tuition_fee = 21900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '091102G';

-- Certificate IV in TESOL (Teaching English to Speakers of Other Languages)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in TESOL (Teaching English to Speakers of Other Languages)</p>',
    course_duration_per_week = 27,
    offshore_tuition_fee = 4000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '099138G';

-- Diploma of TESOL (Teaching English to Speakers of Other Languages)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of TESOL (Teaching English to Speakers of Other Languages)</p>',
    course_duration_per_week = 72,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '099139G';

-- Certificate IV in Entrepreneurship and New Business
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Entrepreneurship and New Business</p>',
    course_duration_per_week = 24,
    offshore_tuition_fee = 6000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '104025D';

-- Diploma of Project Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Project Management</p>',
    course_duration_per_week = 48,
    offshore_tuition_fee = 10000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '104114C';

-- Diploma of Leadership and Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Leadership and Management</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 13000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '104153G';

-- Graduate Diploma of Management (Learning)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Graduate Diploma of Management (Learning)</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 400,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '106548E';

-- Advanced Diploma of Leadership and Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Leadership and Management</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 10400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 400,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '106550M';

-- Certificate IV in Patisserie
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Patisserie</p>',
    course_duration_per_week = 68,
    offshore_tuition_fee = 13500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '109465F';

-- Certificate IV in Kitchen Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Kitchen Management</p>',
    course_duration_per_week = 68,
    offshore_tuition_fee = 13500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '109653B';

-- Certificate III in Patisserie
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Patisserie</p>',
    course_duration_per_week = 46,
    offshore_tuition_fee = 9500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '109729J';

-- Certificate III in Commercial Cookery
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Commercial Cookery</p>',
    course_duration_per_week = 56,
    offshore_tuition_fee = 9500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '109785A';

-- Certificate III in Individual Support
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Individual Support</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 9400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 400,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '115148B';

-- Diploma of Community Services
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Community Services</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 26400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2400,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '115149A';

-- Diploma of Hospitality Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Hospitality Management</p>',
    course_duration_per_week = 96,
    offshore_tuition_fee = 21500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '115488D';

-- Advanced Diploma of Hospitality Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Hospitality Management</p>',
    course_duration_per_week = 120,
    offshore_tuition_fee = 26800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1800,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '115489C';

-- Diploma of Community Services
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Community Services</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 26400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2400,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English and IELTS prep to our TESOL Teacher Mentor Program, ANCE provides the communication tools students need for study, work, and life in Australia.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '118691K';