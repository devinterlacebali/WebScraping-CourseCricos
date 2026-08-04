-- QLD Provider: ILSC Brisbane (02137M)
-- Courses sourced from CRICOS register (24 courses)

UPDATE provider_institution SET
    intake_date = 'January, February, April, July, October',
    updated_at = NOW()
WHERE cricos_provider_code = '02137M';

UPDATE courses SET
    course_description = '<h4>English for Academic Purposes Program</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 49,
    offshore_tuition_fee = 18720,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '0101685';
UPDATE courses SET
    course_description = '<h4>IELTS Mastery Program</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 25,
    offshore_tuition_fee = 9360,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '0101686';
UPDATE courses SET
    course_description = '<h4>Cambridge Mastery Program</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 37,
    offshore_tuition_fee = 14040,
    onshore_tuition_fee = NULL,
    enrolment_fee = 550,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '0101687';
UPDATE courses SET
    course_description = '<h4>General English Program</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 81,
    offshore_tuition_fee = 31200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 550,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '0101688';
UPDATE courses SET
    course_description = '<h4>English Language Programs for International Students (Beginner to Advanced) (4-56 weeks)</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 56,
    offshore_tuition_fee = 25840,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '060152J';
UPDATE courses SET
    course_description = '<h4>Diploma of Project Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50820</p>',
    course_duration_per_week = 66,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '104109M';
UPDATE courses SET
    course_description = '<h4>Diploma of Leadership and Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50420</p>',
    course_duration_per_week = 64,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '104145G';
UPDATE courses SET
    course_description = '<h4>Diploma of Business</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50120</p>',
    course_duration_per_week = 76,
    offshore_tuition_fee = 12500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '104773A';
UPDATE courses SET
    course_description = '<h4>Certificate III in Business</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> BSB30120</p>',
    course_duration_per_week = 76,
    offshore_tuition_fee = 12500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '104774M';
UPDATE courses SET
    course_description = '<h4>Diploma of Marketing and Communication</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50620</p>',
    course_duration_per_week = 328,
    offshore_tuition_fee = 12500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '104775K';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Leadership and Management</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> BSB60420</p>',
    course_duration_per_week = 97,
    offshore_tuition_fee = 22000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 480,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '104776J';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Marketing and Communication</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> BSB40820</p>',
    course_duration_per_week = 76,
    offshore_tuition_fee = 12500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '104777H';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Business</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> BSB40120</p>',
    course_duration_per_week = 76,
    offshore_tuition_fee = 12500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '104778G';
UPDATE courses SET
    course_description = '<h4>Certificate II in Workplace Skills</h4> <p><strong>Level:</strong> Certificate II</p> <p><strong>VET Code:</strong> BSB20120</p>',
    course_duration_per_week = 68,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '105113G';
UPDATE courses SET
    course_description = '<h4>Certificate III in Entrepreneurship and New Business</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> BSB30220</p>',
    course_duration_per_week = 56,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 480,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '107807E';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Marketing and Communication</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> BSB60520</p>',
    course_duration_per_week = 100,
    offshore_tuition_fee = 22000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 480,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '107808D';
UPDATE courses SET
    course_description = '<h4>English for Teaching Professionals</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 280,
    offshore_tuition_fee = 5600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '112864J';
UPDATE courses SET
    course_description = '<h4>Diploma of Digital Marketing</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> 10931NAT</p>',
    course_duration_per_week = 66,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 510,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '116737F';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Environmentally Sustainable Management</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> 11130NAT</p>',
    course_duration_per_week = 54,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 510,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '116738E';
UPDATE courses SET
    course_description = '<h4>Diploma of Artificial Intelligence (AI)</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> 11287NAT</p>',
    course_duration_per_week = 66,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 510,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '117286J';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Hospitality Management</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> SIT60322</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 16000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 800,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '120081G';
UPDATE courses SET
    course_description = '<h4>Diploma of Hospitality Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> SIT50422</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 8000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 800,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '120082F';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Digital Marketing</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> 11266NAT</p>',
    course_duration_per_week = 76,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '120083E';
UPDATE courses SET
    course_description = '<h4>Diploma of Digital Marketing</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> 11422NAT</p>',
    course_duration_per_week = 66,
    offshore_tuition_fee = 9000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ilsc.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '120460G';