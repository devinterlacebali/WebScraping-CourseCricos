-- QLD Provider: Gold Coast Learning Centre (03268C)
-- Courses sourced from CRICOS register (36 courses)

UPDATE provider_institution SET
    intake_date = 'January, February, April, July, October',
    updated_at = NOW()
WHERE cricos_provider_code = '03268C';

UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Accounting</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> FNS60217</p>',
    course_duration_per_week = 30,
    offshore_tuition_fee = 5250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '0100042';
UPDATE courses SET
    course_description = '<h4>General English</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 10560,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '073772G';
UPDATE courses SET
    course_description = '<h4>IELTS Examination Preparation</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 10,
    offshore_tuition_fee = 3800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '073775D';
UPDATE courses SET
    course_description = '<h4>Diploma of Accounting</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> FNS50217</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 6300,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '097811G';
UPDATE courses SET
    course_description = '<h4>Diploma of TESOL (Teaching English to Speakers of Other Languages)</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> 10688NAT</p>',
    course_duration_per_week = 16,
    offshore_tuition_fee = 4900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '097813E';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Leadership and Management</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> BSB40520</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 4500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '103972B';
UPDATE courses SET
    course_description = '<h4>Diploma of Leadership and Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50420</p>',
    course_duration_per_week = 40,
    offshore_tuition_fee = 4550,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '104243E';
UPDATE courses SET
    course_description = '<h4>Certificate II in Workplace Skills</h4> <p><strong>Level:</strong> Certificate II</p> <p><strong>VET Code:</strong> BSB20120</p>',
    course_duration_per_week = 44,
    offshore_tuition_fee = 2810,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '108050D';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Marketing and Communication</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> BSB40820</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 5225,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '108051C';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Project Management Practice</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> BSB40920</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 5540,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '108052B';
UPDATE courses SET
    course_description = '<h4>Diploma of Business</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50120</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 6500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '108053A';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Human Resource Management</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> BSB60320</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 6540,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '108054M';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Leadership and Management</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> BSB60420</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 5885,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '108055K';
UPDATE courses SET
    course_description = '<h4>Diploma of Human Resource Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50320</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 5540,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '108056J';
UPDATE courses SET
    course_description = '<h4>Diploma of Marketing and Communication</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50620</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 6275,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '108057H';
UPDATE courses SET
    course_description = '<h4>Diploma of Project Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50820</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 6275,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '108058G';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Business</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> BSB60120</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 6695,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '108059F';
UPDATE courses SET
    course_description = '<h4>Certificate III in Business</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> BSB30120</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 4700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '108069D';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Business</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> BSB40120</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 5700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '108070M';
UPDATE courses SET
    course_description = '<h4>Certificate III in Entrepreneurship and New Business</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> BSB30220</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 4700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '108071K';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Entrepreneurship and New Business</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> BSB40320</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 5700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '108072J';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Human Resource Management</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> BSB40420</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 5000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 400,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '108271B';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Program Management</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> BSB60720</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 6000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '108273M';
UPDATE courses SET
    course_description = '<h4>Certificate III in Hairdressing</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> SHB30416</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 15500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '109052E';
UPDATE courses SET
    course_description = '<h4>Certificate III in Beauty Services</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> SHB30121</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 6000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '109231B';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Accounting and Bookkeeping</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> FNS40222</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 5300,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '109989M';
UPDATE courses SET
    course_description = '<h4>Certificate III in Accounts Administration</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> FNS30322</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 4700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '110037E';
UPDATE courses SET
    course_description = '<h4>Certificate IV in English Language Teaching (TESOL)</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> 11021NAT</p>',
    course_duration_per_week = 20,
    offshore_tuition_fee = 5000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 450,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '110169D';
UPDATE courses SET
    course_description = '<h4>Diploma of English Language Teaching (TESOL)</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> 11020NAT</p>',
    course_duration_per_week = 33,
    offshore_tuition_fee = 6000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 450,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '110170M';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Massage Therapy</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> HLT42015</p>',
    course_duration_per_week = 41,
    offshore_tuition_fee = 7000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '110373M';
UPDATE courses SET
    course_description = '<h4>Diploma of Remedial Massage</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> HLT52015</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 9000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '110374K';
UPDATE courses SET
    course_description = '<h4>Diploma of Accounting</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> FNS50222</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 6000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 200,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '112744F';
UPDATE courses SET
    course_description = '<h4>Diploma of Salon Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> SHB50216</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 7000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '112745E';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Accounting</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> FNS60222</p>',
    course_duration_per_week = 106,
    offshore_tuition_fee = 6500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 200,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '112746D';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Massage Therapy</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> HLT42021</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '114191G';
UPDATE courses SET
    course_description = '<h4>Diploma of Remedial Massage</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> HLT52021</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.goldcoaststudy.com',
    updated_at = NOW()
WHERE cricos_course_code = '114192F';