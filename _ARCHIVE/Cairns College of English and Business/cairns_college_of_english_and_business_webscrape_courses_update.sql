-- QLD Provider: Cairns College of English and Business (03251A)
-- Courses sourced from CRICOS register (28 courses)

UPDATE provider_institution SET
    intake_date = 'January, February, April, July, October',
    updated_at = NOW()
WHERE cricos_provider_code = '03251A';

UPDATE courses SET
    course_description = '<h4>General English (1-50 weeks)</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 58,
    offshore_tuition_fee = 16000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '072892G';
UPDATE courses SET
    course_description = '<h4>Cambridge First Certificate Preparation Course</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 16,
    offshore_tuition_fee = 3995,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '073934E';
UPDATE courses SET
    course_description = '<h4>Cambridge Advanced Certificate Preparation</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 16,
    offshore_tuition_fee = 3995,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '073935D';
UPDATE courses SET
    course_description = '<h4>IELTS Preparation</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 38,
    offshore_tuition_fee = 9350,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '073937B';
UPDATE courses SET
    course_description = '<h4>Diploma of Hospitality Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> SIT50416</p>',
    course_duration_per_week = 72,
    offshore_tuition_fee = 13630,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '093029F';
UPDATE courses SET
    course_description = '<h4>English for Academic Purposes (EAP)</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 12,
    offshore_tuition_fee = 3750,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '093030B';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Ageing Support</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> CHC43015</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 8000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '104832F';
UPDATE courses SET
    course_description = '<h4>Diploma of Leadership and Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50420</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 8500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '105437J';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Leadership and Management</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> BSB60420</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 8500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '105721E';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Business</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> BSB40120</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 8500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '105723C';
UPDATE courses SET
    course_description = '<h4>Certificate III in Early Childhood Education and Care</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> CHC30121</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 8500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '108263B';
UPDATE courses SET
    course_description = '<h4>Diploma of Early Childhood Education and Care</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> CHC50121</p>',
    course_duration_per_week = 72,
    offshore_tuition_fee = 12750,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '108264A';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Kitchen Management</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> SIT40521</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 11000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '109707D';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Guiding</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> SIT40222</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 8500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '109723D';
UPDATE courses SET
    course_description = '<h4>Certificate III in Commercial Cookery</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> SIT30821</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 11000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '109826H';
UPDATE courses SET
    course_description = '<h4>Certificate III in Guiding</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> SIT30322</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 8500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '109924F';
UPDATE courses SET
    course_description = '<h4>Diploma of Hospitality Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> SIT50422</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 12740,
    onshore_tuition_fee = NULL,
    enrolment_fee = 350,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112205M';
UPDATE courses SET
    course_description = '<h4>Certificate III in Hospitality</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> SIT30622</p>',
    course_duration_per_week = 44,
    offshore_tuition_fee = 8500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 350,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112206K';
UPDATE courses SET
    course_description = '<h4>Diploma of Travel and Tourism Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> SIT50122</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 12740,
    onshore_tuition_fee = NULL,
    enrolment_fee = 350,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112207J';
UPDATE courses SET
    course_description = '<h4>Certificate III in Tourism</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> SIT30122</p>',
    course_duration_per_week = 44,
    offshore_tuition_fee = 8500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 350,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112209G';
UPDATE courses SET
    course_description = '<h4>Certificate III in Individual Support</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> CHC33021</p>',
    course_duration_per_week = 56,
    offshore_tuition_fee = 8000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '113127A';
UPDATE courses SET
    course_description = '<h4>Diploma of Community Services</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> CHC52021</p>',
    course_duration_per_week = 84,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 600,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '113128M';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Hospitality</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> SIT40422</p>',
    course_duration_per_week = 84,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 600,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '113181F';
UPDATE courses SET
    course_description = '<h4>Diploma of Community Services</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> CHC52025</p>',
    course_duration_per_week = 84,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 600,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '118722H';
UPDATE courses SET
    course_description = '<h4>Diploma of Early Childhood Education and Care</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> CHC50125</p>',
    course_duration_per_week = 72,
    offshore_tuition_fee = 12750,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '118924J';
UPDATE courses SET
    course_description = '<h4>High School Preparation (HSP) Course</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 48,
    offshore_tuition_fee = 6000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '119454D';
UPDATE courses SET
    course_description = '<h4>Certificate III in Early Childhood Education and Care</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> CHC30125</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 8500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '119607C';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Community Sector Management</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> CHC62015</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 14900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 900,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cceb.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '120080H';