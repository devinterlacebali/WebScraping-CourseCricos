-- QLD Provider: Queensland International Institute (02763G)
-- Courses sourced from CRICOS register (13 courses)

UPDATE provider_institution SET
    intake_date = 'January, February, April, July, October',
    updated_at = NOW()
WHERE cricos_provider_code = '02763G';

UPDATE courses SET
    course_description = '<h4>Certificate IV in Ageing Support</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> CHC43015</p>',
    course_duration_per_week = 98,
    offshore_tuition_fee = 19650,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.qii.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '091948E';
UPDATE courses SET
    course_description = '<h4>General English-Starter to Elementary</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 24,
    offshore_tuition_fee = 6600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 650,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.qii.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '095477K';
UPDATE courses SET
    course_description = '<h4>Cambridge English Preliminary (PET) Preparation</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 12,
    offshore_tuition_fee = 4800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 700,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.qii.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '095478J';
UPDATE courses SET
    course_description = '<h4>Cambridge English First (FCE) Preparation</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 12,
    offshore_tuition_fee = 4800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 700,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.qii.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '095479G';
UPDATE courses SET
    course_description = '<h4>Cambridge English Advanced (CAE) Preparation</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 12,
    offshore_tuition_fee = 4800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 700,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.qii.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '095480D';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Leadership and Management</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> BSB40520</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12650,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.qii.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '103952F';
UPDATE courses SET
    course_description = '<h4>Diploma of Leadership and Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50420</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12650,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.qii.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '104174B';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Leadership and Management</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> BSB60420</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 650,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.qii.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '108953J';
UPDATE courses SET
    course_description = '<h4>Certificate III in Early Childhood Education and Care</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> CHC30121</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11000,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.qii.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '108955G';
UPDATE courses SET
    course_description = '<h4>Diploma of Early Childhood Education and Care</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> CHC50121</p>',
    course_duration_per_week = 60,
    offshore_tuition_fee = 12650,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.qii.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '108956F';
UPDATE courses SET
    course_description = '<h4>Certificate II in Hospitality</h4> <p><strong>Level:</strong> Certificate II</p> <p><strong>VET Code:</strong> SIT20322</p>',
    course_duration_per_week = 31,
    offshore_tuition_fee = 8000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.qii.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '109935C';
UPDATE courses SET
    course_description = '<h4>Diploma of Early Childhood Education and Care</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> CHC50125</p>',
    course_duration_per_week = 60,
    offshore_tuition_fee = 12650,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.qii.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '118921A';
UPDATE courses SET
    course_description = '<h4>Certificate III in Early Childhood Education and Care</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> CHC30125</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 11000,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.qii.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '119769G';