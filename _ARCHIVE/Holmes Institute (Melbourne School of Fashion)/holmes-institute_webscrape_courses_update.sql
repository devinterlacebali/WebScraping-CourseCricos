-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '00898G';

-- Advanced Diploma of Applied Fashion Design and Merchandising
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advanced Diploma of Applied Fashion Design and Merchandising</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 54000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '0100766';

-- Diploma of Applied Fashion Design and Merchandising
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diploma of Applied Fashion Design and Merchandising</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 36000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '0100776';

-- Secondary Years 11 - 12 (VCE)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Secondary Years 11 - 12 (VCE)</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 33800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '050632J';

-- Secondary Years 11 - 12 (VCAL)
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Secondary Years 11 - 12 (VCAL)</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 33800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '',
    updated_at = NOW()
WHERE cricos_course_code = '054541B';