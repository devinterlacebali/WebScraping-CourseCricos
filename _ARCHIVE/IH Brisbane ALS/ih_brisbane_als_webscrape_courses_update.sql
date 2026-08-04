-- QLD Provider: IH Brisbane ALS (02885G)
-- Courses sourced from CRICOS register (22 courses)

UPDATE provider_institution SET
    intake_date = 'January, February, April, July, October',
    updated_at = NOW()
WHERE cricos_provider_code = '02885G';

UPDATE courses SET
    course_description = '<h4>General English (Beginner - Advanced)</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 72,
    offshore_tuition_fee = 29520,
    onshore_tuition_fee = NULL,
    enrolment_fee = 19998,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '062145C';
UPDATE courses SET
    course_description = '<h4>English for Academic Purposes</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 12,
    offshore_tuition_fee = 4920,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3453,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '062146B';
UPDATE courses SET
    course_description = '<h4>IELTS Preparation Course (Intermediate - Advanced)</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 36,
    offshore_tuition_fee = 14760,
    onshore_tuition_fee = NULL,
    enrolment_fee = 10359,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '062147A';
UPDATE courses SET
    course_description = '<h4>Cambridge Exam Preparation - Advanced</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 12,
    offshore_tuition_fee = 5000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3573,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '062148M';
UPDATE courses SET
    course_description = '<h4>Cambridge Exam Preparation - First Certificate</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 12,
    offshore_tuition_fee = 5000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3573,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '062149K';
UPDATE courses SET
    course_description = '<h4>Business English (Intermediate)</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 8,
    offshore_tuition_fee = 3280,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2302,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '076650D';
UPDATE courses SET
    course_description = '<h4>Certificate I in Retail Services</h4> <p><strong>Level:</strong> Certificate I</p> <p><strong>VET Code:</strong> SIR10116</p>',
    course_duration_per_week = 15,
    offshore_tuition_fee = 3750,
    onshore_tuition_fee = NULL,
    enrolment_fee = 4341,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '096424D';
UPDATE courses SET
    course_description = '<h4>Certificate II in Retail Services</h4> <p><strong>Level:</strong> Certificate II</p> <p><strong>VET Code:</strong> SIR20216</p>',
    course_duration_per_week = 35,
    offshore_tuition_fee = 8750,
    onshore_tuition_fee = NULL,
    enrolment_fee = 9796,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '096426B';
UPDATE courses SET
    course_description = '<h4>Certificate III in Retail</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> SIR30216</p>',
    course_duration_per_week = 47,
    offshore_tuition_fee = 11500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 13069,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '096428M';
UPDATE courses SET
    course_description = '<h4>Certificate II in Workplace Skills</h4> <p><strong>Level:</strong> Certificate II</p> <p><strong>VET Code:</strong> BSB20120</p>',
    course_duration_per_week = 55,
    offshore_tuition_fee = 11000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '103327J';
UPDATE courses SET
    course_description = '<h4>Certificate III in Business</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> BSB30120</p>',
    course_duration_per_week = 55,
    offshore_tuition_fee = 11000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '103328H';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Business</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> BSB40120</p>',
    course_duration_per_week = 63,
    offshore_tuition_fee = 12600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '103329G';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Human Resource Management</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> BSB40420</p>',
    course_duration_per_week = 63,
    offshore_tuition_fee = 12600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '103330C';
UPDATE courses SET
    course_description = '<h4>Diploma of Leadership and Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50420</p>',
    course_duration_per_week = 59,
    offshore_tuition_fee = 11800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '103331B';
UPDATE courses SET
    course_description = '<h4>Diploma of Business</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50120</p>',
    course_duration_per_week = 59,
    offshore_tuition_fee = 11800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '103332A';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Business</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> BSB60120</p>',
    course_duration_per_week = 59,
    offshore_tuition_fee = 11800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '103333M';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Leadership and Management</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> BSB60420</p>',
    course_duration_per_week = 59,
    offshore_tuition_fee = 11800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '103334K';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Horticulture</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> AHC40416</p>',
    course_duration_per_week = 59,
    offshore_tuition_fee = 11800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 400,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '107532E';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Horticulture</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> AHC40422</p>',
    course_duration_per_week = 59,
    offshore_tuition_fee = 14000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 600,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '113194A';
UPDATE courses SET
    course_description = '<h4>Certificate III in Individual Support</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> CHC33021</p>',
    course_duration_per_week = 55,
    offshore_tuition_fee = 11800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1200,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '115203M';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Ageing Support</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> CHC43015</p>',
    course_duration_per_week = 79,
    offshore_tuition_fee = 15800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '115204K';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Civil Construction Design</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> RII60520</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 30000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 3000,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.ihbrisbane.com.au; www.alscertificates.com',
    updated_at = NOW()
WHERE cricos_course_code = '116125A';