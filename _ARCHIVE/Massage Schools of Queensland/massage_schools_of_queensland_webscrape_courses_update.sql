-- QLD Provider: Massage Schools of Queensland (01854A)
-- Courses sourced from CRICOS register (11 courses)

UPDATE provider_institution SET
    intake_date = 'January, February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '01854A';

UPDATE courses SET
    course_description = '<h4>Diploma of Sport and Recreation Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> SIS50115</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 9500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.massageschools.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '0102048';
UPDATE courses SET
    course_description = '<h4>Diploma of Clinical Aromatherapy</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> HLT52315</p>',
    course_duration_per_week = 75,
    offshore_tuition_fee = 18500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.massageschools.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '094163C';
UPDATE courses SET
    course_description = '<h4>Diploma of Remedial Massage</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> HLT52015</p>',
    course_duration_per_week = 75,
    offshore_tuition_fee = 17300,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.massageschools.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '094164B';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Massage Therapy</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> HLT42015</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 7980,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.massageschools.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '094166M';
UPDATE courses SET
    course_description = '<h4>Diploma of Project Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50820</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 9400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.massageschools.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '104105D';
UPDATE courses SET
    course_description = '<h4>Diploma of Leadership and Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50420</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 9400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.massageschools.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '104137G';
UPDATE courses SET
    course_description = '<h4>Diploma of School Age Education and Care</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> CHC50221</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 7500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 400,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.massageschools.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '109053D';
UPDATE courses SET
    course_description = '<h4>Diploma of Event Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> SIT50322</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 9500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 400,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.massageschools.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '110356A';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Massage Therapy</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> HLT42021</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 7980,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.massageschools.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '113411H';
UPDATE courses SET
    course_description = '<h4>Diploma of Remedial Massage</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> HLT52021</p>',
    course_duration_per_week = 73,
    offshore_tuition_fee = 17500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.massageschools.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '113412G';
UPDATE courses SET
    course_description = '<h4>Diploma of Sport, Aquatics and Recreation Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> SIS50122</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 15000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 400,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.massageschools.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '113413F';