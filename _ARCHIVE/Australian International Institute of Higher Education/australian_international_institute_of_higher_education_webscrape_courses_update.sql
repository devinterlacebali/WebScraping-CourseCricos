-- QLD Provider: Australian International Institute of Higher Education (04013G)
-- Courses sourced from CRICOS register (7 courses)

UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '04013G';

UPDATE courses SET
    course_description = '<h4>Bachelor of Business (Information Systems)</h4> <p><strong>Level:</strong> Bachelor Degree</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 48000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Australian Year 12 or equivalent, English language proficiency (IELTS 6.0+ or equivalent)</p>',
    apply_form = 'https://www.aiihe.edu.au/',
    updated_at = NOW()
WHERE cricos_course_code = '109374J';
UPDATE courses SET
    course_description = '<h4>Bachelor of Business (Marketing)</h4> <p><strong>Level:</strong> Bachelor Degree</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 48000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Australian Year 12 or equivalent, English language proficiency (IELTS 6.0+ or equivalent)</p>',
    apply_form = 'https://www.aiihe.edu.au/',
    updated_at = NOW()
WHERE cricos_course_code = '110052F';
UPDATE courses SET
    course_description = '<h4>Master of Information Technology</h4> <p><strong>Level:</strong> Masters Degree (Coursework)</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 48000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Australian Year 12 or equivalent, English language proficiency (IELTS 6.0+ or equivalent)</p>',
    apply_form = 'https://www.aiihe.edu.au/',
    updated_at = NOW()
WHERE cricos_course_code = '120466A';
UPDATE courses SET
    course_description = '<h4>Master of Information Technology (Cybersecurity)</h4> <p><strong>Level:</strong> Masters Degree (Coursework)</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 48000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Australian Year 12 or equivalent, English language proficiency (IELTS 6.0+ or equivalent)</p>',
    apply_form = 'https://www.aiihe.edu.au/',
    updated_at = NOW()
WHERE cricos_course_code = '120467M';
UPDATE courses SET
    course_description = '<h4>Master of Information Technology (Data Science)</h4> <p><strong>Level:</strong> Masters Degree (Coursework)</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 48000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 250,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Australian Year 12 or equivalent, English language proficiency (IELTS 6.0+ or equivalent)</p>',
    apply_form = 'https://www.aiihe.edu.au/',
    updated_at = NOW()
WHERE cricos_course_code = '120468K';
UPDATE courses SET
    course_description = '<h4>Graduate Diploma of Information Technology</h4> <p><strong>Level:</strong> Graduate Diploma</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 24000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.aiihe.edu.au/',
    updated_at = NOW()
WHERE cricos_course_code = '120469J';
UPDATE courses SET
    course_description = '<h4>Graduate Certificate of Information Technology</h4> <p><strong>Level:</strong> Graduate Certificate</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.aiihe.edu.au/',
    updated_at = NOW()
WHERE cricos_course_code = '120470E';