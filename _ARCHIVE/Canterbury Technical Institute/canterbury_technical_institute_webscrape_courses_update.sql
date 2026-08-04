-- QLD Provider: Canterbury Technical Institute (02938M)
-- Courses sourced from CRICOS register (22 courses)

UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '02938M';

UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Hospitality Management</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> SIT60316</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 22000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '097969G';
UPDATE courses SET
    course_description = '<h4>Diploma of Project Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50820</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 16500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '104036A';
UPDATE courses SET
    course_description = '<h4>Diploma of Leadership and Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50420</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 16500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '104193K';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Program Management</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> BSB60720</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 22000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '104440M';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Leadership and Management</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> BSB60420</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 22000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '104760F';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Business</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> BSB60120</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 22000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '104761E';
UPDATE courses SET
    course_description = '<h4>Diploma of Business</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50120</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 16500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '104762D';
UPDATE courses SET
    course_description = '<h4>Diploma of Information Technology</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> ICT50220</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 16500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '105042F';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Information Technology</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> ICT60220</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 24000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '105045C';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Kitchen Management</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> SIT40521</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 22000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1400,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '109677E';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Ageing Support</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> CHC43015</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 450,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '111635H';
UPDATE courses SET
    course_description = '<h4>Diploma of Community Services</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> CHC52015</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 22000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 450,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '111636G';
UPDATE courses SET
    course_description = '<h4>Certificate III in Individual Support</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> CHC33021</p>',
    course_duration_per_week = 35,
    offshore_tuition_fee = 6000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 450,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112485J';
UPDATE courses SET
    course_description = '<h4>Diploma of Community Services</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> CHC52021</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 22000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '112486H';
UPDATE courses SET
    course_description = '<h4>Certificate III in Hospitality</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> SIT30622</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 8000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '113196K';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Hospitality</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> SIT40422</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 8000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '113197J';
UPDATE courses SET
    course_description = '<h4>Diploma of Hospitality Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> SIT50422</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 16500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '113198H';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Hospitality Management</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> SIT60322</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 22000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '113199G';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Civil Construction Design</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> RII60520</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 24000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 300,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '117367H';
UPDATE courses SET
    course_description = '<h4>Diploma of Civil Construction Design</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> RII50520</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 24000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '118001H';
UPDATE courses SET
    course_description = '<h4>Diploma of Community Services</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> CHC52025</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 22000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 500,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '118703M';
UPDATE courses SET
    course_description = '<h4>Certificate III in Carpentry</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> CPC30220</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 24000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 5000,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.cti.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '120634A';