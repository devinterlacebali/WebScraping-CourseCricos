-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '02886G';

-- Diploma of Beauty Therapy
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Beauty Therapy</p>',
    course_duration_per_week = 90,
    offshore_tuition_fee = 22000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '089054F';

-- Certificate III in Beauty Services
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Beauty Services</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 8000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '089084M';

-- Certificate IV in Hairdressing
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Hairdressing</p>',
    course_duration_per_week = 42,
    offshore_tuition_fee = 8800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1200,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '091498D';

-- Certificate III in Hairdressing
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Hairdressing</p>',
    course_duration_per_week = 70,
    offshore_tuition_fee = 17200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1200,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '093650G';

-- Diploma of Salon Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Salon Management</p>',
    course_duration_per_week = 35,
    offshore_tuition_fee = 7350,
    onshore_tuition_fee = NULL,
    enrolment_fee = 550,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '093651F';

-- Diploma of Business
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Business</p>',
    course_duration_per_week = 44,
    offshore_tuition_fee = 6550,
    onshore_tuition_fee = NULL,
    enrolment_fee = 350,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '107527B';

-- Certificate III in Nail Technology
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Nail Technology</p>',
    course_duration_per_week = 36,
    offshore_tuition_fee = 9000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1200,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '108561C';

-- Certificate III in Beauty Services
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Beauty Services</p>',
    course_duration_per_week = 44,
    offshore_tuition_fee = 12200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1200,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '108562B';

-- Certificate IV in Beauty Therapy
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Beauty Therapy</p>',
    course_duration_per_week = 64,
    offshore_tuition_fee = 15200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1200,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '108563A';

-- Diploma of Beauty Therapy
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Beauty Therapy</p>',
    course_duration_per_week = 80,
    offshore_tuition_fee = 18600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1200,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '108564M';

-- Advanced Diploma of Skin Therapy
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Skin Therapy</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 16700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1200,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '108565K';

-- Diploma of Cosmetic Tattooing
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Cosmetic Tattooing</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 15000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1500,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '108566J';

-- Certificate IV in Massage Therapy
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Massage Therapy</p>',
    course_duration_per_week = 56,
    offshore_tuition_fee = 8150,
    onshore_tuition_fee = NULL,
    enrolment_fee = 550,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '108580M';

-- Diploma of Remedial Massage
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Remedial Massage</p>',
    course_duration_per_week = 95,
    offshore_tuition_fee = 16550,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '108581K';

-- Diploma of Clinical Aromatherapy
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Clinical Aromatherapy</p>',
    course_duration_per_week = 94,
    offshore_tuition_fee = 17600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1200,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '108582J';

-- Diploma of Leadership and Management
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Leadership and Management</p>',
    course_duration_per_week = 46,
    offshore_tuition_fee = 13950,
    onshore_tuition_fee = NULL,
    enrolment_fee = 350,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '108583H';

-- Advanced Diploma of Business
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Business</p>',
    course_duration_per_week = 44,
    offshore_tuition_fee = 8550,
    onshore_tuition_fee = NULL,
    enrolment_fee = 350,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '108584G';

-- Graduate Diploma of Management (Learning)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Graduate Diploma of Management (Learning)</p>',
    course_duration_per_week = 44,
    offshore_tuition_fee = 13950,
    onshore_tuition_fee = NULL,
    enrolment_fee = 350,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '108585F';

-- Certificate III in Barbering
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Barbering</p>',
    course_duration_per_week = 70,
    offshore_tuition_fee = 17200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1200,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '112787F';

-- Certificate III in Make-Up
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Make-Up</p>',
    course_duration_per_week = 44,
    offshore_tuition_fee = 9000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1200,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '112788E';

-- Certificate IV in Massage Therapy
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Massage Therapy</p>',
    course_duration_per_week = 62,
    offshore_tuition_fee = 14200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1200,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '112789D';

-- Diploma of Remedial Massage
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Remedial Massage</p>',
    course_duration_per_week = 120,
    offshore_tuition_fee = 17600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1200,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '112790M';

-- English for Academic Purposes I
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>English for Academic Purposes I</p>',
    course_duration_per_week = 20,
    offshore_tuition_fee = 6480,
    onshore_tuition_fee = NULL,
    enrolment_fee = 680,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '113519G';

-- General English I Beginner
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>General English I Beginner</p>',
    course_duration_per_week = 30,
    offshore_tuition_fee = 7730,
    onshore_tuition_fee = NULL,
    enrolment_fee = 680,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '113520C';

-- General English II Intermediate
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>General English II Intermediate</p>',
    course_duration_per_week = 20,
    offshore_tuition_fee = 5480,
    onshore_tuition_fee = NULL,
    enrolment_fee = 680,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '113521B';

-- General English III Advanced
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>General English III Advanced</p>',
    course_duration_per_week = 18,
    offshore_tuition_fee = 4180,
    onshore_tuition_fee = NULL,
    enrolment_fee = 680,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '113522A';

-- Certificate III in Individual Support
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Individual Support</p>',
    course_duration_per_week = 62,
    offshore_tuition_fee = 13200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 900,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '114211H';

-- Certificate IV in Ageing Support
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Ageing Support</p>',
    course_duration_per_week = 79,
    offshore_tuition_fee = 16100,
    onshore_tuition_fee = NULL,
    enrolment_fee = 900,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '114212G';

-- Certificate IV in Disability Support
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Disability Support</p>',
    course_duration_per_week = 56,
    offshore_tuition_fee = 8400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 900,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '114213F';

-- Certificate III in Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Early Childhood Education and Care</p>',
    course_duration_per_week = 79,
    offshore_tuition_fee = 14100,
    onshore_tuition_fee = NULL,
    enrolment_fee = 900,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '114214E';

-- Diploma of Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Early Childhood Education and Care</p>',
    course_duration_per_week = 79,
    offshore_tuition_fee = 16500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 900,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '114215D';

-- Diploma of Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Early Childhood Education and Care</p>',
    course_duration_per_week = 79,
    offshore_tuition_fee = 16500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 900,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '118586M';

-- Certificate III in Early Childhood Education and Care
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Early Childhood Education and Care</p>',
    course_duration_per_week = 79,
    offshore_tuition_fee = 14100,
    onshore_tuition_fee = NULL,
    enrolment_fee = 900,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '119590G';