-- QLD Provider: Townsville Grammar School (00564G)
-- Courses sourced from CRICOS register (4 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00564G';

UPDATE courses SET
    course_description = '<h4>Secondary Senior Yrs 11-12 Boys & Girls</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 79600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 55580,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.tgs.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004985K';
UPDATE courses SET
    course_description = '<h4>International Baccalaureate Diploma Program (Years 11-12)</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 100,
    offshore_tuition_fee = 79600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 55580,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.tgs.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '069022B';
UPDATE courses SET
    course_description = '<h4>Primary School Studies Year 1-6 Boys and Girls</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 188400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6700,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.tgs.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '086199B';
UPDATE courses SET
    course_description = '<h4>Secondary Junior Yrs 7-10 Boys and Girls</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 159200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 109260,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.tgs.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '086200C';