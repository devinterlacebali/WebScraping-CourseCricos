-- QLD Provider: Academique (03322B)
-- Courses sourced from CRICOS register (13 courses)

UPDATE provider_institution SET
    intake_date = 'January, February, April, July, October',
    updated_at = NOW()
WHERE cricos_provider_code = '03322B';

UPDATE courses SET
    course_description = '<h4>General English - Elementary to Advanced</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 72,
    offshore_tuition_fee = 18000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 200,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'http://www.academique.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '097218B';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Business</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> BSB40120</p>',
    course_duration_per_week = 42,
    offshore_tuition_fee = 8400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'http://www.academique.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '103574E';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Leadership and Management</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> BSB60420</p>',
    course_duration_per_week = 64,
    offshore_tuition_fee = 8250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'http://www.academique.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '103575D';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Human Resource Management</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> BSB60320</p>',
    course_duration_per_week = 64,
    offshore_tuition_fee = 8250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'http://www.academique.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '103576C';
UPDATE courses SET
    course_description = '<h4>Advanced Diploma of Business</h4> <p><strong>Level:</strong> Advanced Diploma</p> <p><strong>VET Code:</strong> BSB60120</p>',
    course_duration_per_week = 64,
    offshore_tuition_fee = 8250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'http://www.academique.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '103601G';
UPDATE courses SET
    course_description = '<h4>Diploma of Leadership and Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50420</p>',
    course_duration_per_week = 74,
    offshore_tuition_fee = 9900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'http://www.academique.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '103679G';
UPDATE courses SET
    course_description = '<h4>Diploma of Human Resource Management</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50320</p>',
    course_duration_per_week = 74,
    offshore_tuition_fee = 9900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'http://www.academique.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '103681B';
UPDATE courses SET
    course_description = '<h4>Diploma of Business</h4> <p><strong>Level:</strong> Diploma</p> <p><strong>VET Code:</strong> BSB50120</p>',
    course_duration_per_week = 74,
    offshore_tuition_fee = 9900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'http://www.academique.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '103682A';
UPDATE courses SET
    course_description = '<h4>Certificate III in Painting and Decorating</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> CPC30620</p>',
    course_duration_per_week = 94,
    offshore_tuition_fee = 20000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'http://www.academique.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '103824C';
UPDATE courses SET
    course_description = '<h4>Certificate III in Carpentry</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> CPC30220</p>',
    course_duration_per_week = 94,
    offshore_tuition_fee = 30000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'http://www.academique.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '104556K';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Building and Construction</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> CPC40120</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 10000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 10,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'http://www.academique.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '107077A';
UPDATE courses SET
    course_description = '<h4>Certificate III in Individual Support</h4> <p><strong>Level:</strong> Certificate III</p> <p><strong>VET Code:</strong> CHC33021</p>',
    course_duration_per_week = 64,
    offshore_tuition_fee = 10000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'http://www.academique.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '114756H';
UPDATE courses SET
    course_description = '<h4>Certificate IV in Ageing Support</h4> <p><strong>Level:</strong> Certificate IV</p> <p><strong>VET Code:</strong> CHC43015</p>',
    course_duration_per_week = 100,
    offshore_tuition_fee = 10000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'http://www.academique.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '115518C';