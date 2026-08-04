-- QLD Provider: Education Queensland International (00608A)
-- Courses sourced from CRICOS register (5 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00608A';

UPDATE courses SET
    course_description = '<h4>International Baccalaureate Diploma Program (Years 11-12)</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 51398,
    onshore_tuition_fee = NULL,
    enrolment_fee = 36872,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.eqi.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '079324E';
UPDATE courses SET
    course_description = '<h4>Primary School (Years P-6)</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 364,
    offshore_tuition_fee = 102732,
    onshore_tuition_fee = NULL,
    enrolment_fee = 5975,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.eqi.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '082519A';
UPDATE courses SET
    course_description = '<h4>Junior High School (Years 7-10)</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 64256,
    onshore_tuition_fee = NULL,
    enrolment_fee = 73767,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.eqi.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '082520G';
UPDATE courses SET
    course_description = '<h4>Senior High School (Years 11-12)</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 36320,
    onshore_tuition_fee = NULL,
    enrolment_fee = 36872,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.eqi.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '082521G';
UPDATE courses SET
    course_description = '<h4>High School Preparation</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 25480,
    onshore_tuition_fee = NULL,
    enrolment_fee = 18488,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://www.eqi.com.au',
    updated_at = NOW()
WHERE cricos_course_code = '087993A';