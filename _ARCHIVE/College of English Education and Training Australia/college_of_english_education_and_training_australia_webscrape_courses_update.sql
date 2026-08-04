-- QLD Provider: College of English Education and Training Australia (03605B)
-- Courses sourced from CRICOS register (14 courses)

UPDATE provider_institution SET
    intake_date = 'January, February, April, July, October',
    updated_at = NOW()
WHERE cricos_provider_code = '03605B';

UPDATE courses SET
    course_description = '<h4>General English</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 72,
    offshore_tuition_fee = 22480,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1020,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.ceetacollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '0101532';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Kitchen Management</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> SIT40521</p>',
    course_duration_per_week = 70,
    offshore_tuition_fee = 19220,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ceetacollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '109538E';
UPDATE courses SET
    course_description = '<h4>Diploma of Hospitality Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> SIT50422</p>',
    course_duration_per_week = 60,
    offshore_tuition_fee = 13250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ceetacollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112454E';
UPDATE courses SET
    course_description = '<h4>Certificate III in Individual Support</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> CHC33021</p>',
    course_duration_per_week = 32,
    offshore_tuition_fee = 6000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ceetacollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112455D';
UPDATE courses SET
    course_description = '<h4>Diploma of Community Services</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> CHC52021</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 24500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 900,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ceetacollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112456C';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Ageing Support</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> CHC43015</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 9250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ceetacollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112457B';
UPDATE courses SET
    course_description = '<h4>Diploma of Early Childhood Education and Care</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> CHC50121</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 15250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ceetacollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112458A';
UPDATE courses SET
    course_description = '<h4>Certificate III in Early Childhood Education and Care</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> CHC30121</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 9000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ceetacollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112459M';
UPDATE courses SET
    course_description = '<h4>Diploma of Leadership and Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50420</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 10000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ceetacollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112519D';
UPDATE courses SET
    course_description = '<h4>Graduate Diploma of Management (Learning)</h4> <p><strong>Level:</strong> Graduate Diploma</p> <p><strong>VET Code:</strong> BSB80120</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ceetacollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112520M';
UPDATE courses SET
    course_description = '<h4>Diploma of Business</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50120</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 10000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ceetacollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112521K';
UPDATE courses SET
    course_description = '<h4>Diploma of Community Services</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> CHC52025</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 24500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 900,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ceetacollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '118758G';
UPDATE courses SET
    course_description = '<h4>Diploma of Early Childhood Education and Care</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> CHC50125</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 15250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ceetacollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '118903C';
UPDATE courses SET
    course_description = '<h4>Certificate III in Early Childhood Education and Care</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> CHC30125</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 9000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ceetacollege.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '119631C';