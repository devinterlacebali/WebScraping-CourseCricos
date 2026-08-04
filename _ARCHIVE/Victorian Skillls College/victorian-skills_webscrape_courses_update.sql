-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '04354H';

-- Diploma of Building and Construction (Building)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Building and Construction (Building)</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 26000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3400,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117726A';

-- Certificate III in Carpentry
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Carpentry</p>',
    course_duration_per_week = 58,
    offshore_tuition_fee = 27400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3400,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117727M';

-- Certificate III in Cabinet Making and Timber Technology
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Cabinet Making and Timber Technology</p>',
    course_duration_per_week = 66,
    offshore_tuition_fee = 26500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3400,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117728K';

-- Certificate III in Individual Support
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate III in Individual Support</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 18900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1900,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117729J';

-- Certificate IV in Ageing Support
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Certificate IV in Ageing Support</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 18900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1900,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117730E';

-- Diploma of Community Services
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Community Services</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 28900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1900,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117731D';

-- Graduate Diploma of Management (Learning)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Graduate Diploma of Management (Learning)</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 16900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1900,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117732C';

-- General English
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>General English</p>',
    course_duration_per_week = 60,
    offshore_tuition_fee = 18400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 900,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117733B';

-- IELTS Preparation
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>IELTS Preparation</p>',
    course_duration_per_week = 36,
    offshore_tuition_fee = 11200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 700,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '117734A';

-- Diploma of Community Services
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Community Services</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 28900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1900,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '118868A';