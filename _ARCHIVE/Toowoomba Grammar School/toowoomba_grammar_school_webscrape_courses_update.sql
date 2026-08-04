-- QLD Provider: Toowoomba Grammar School (00525D)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00525D';

UPDATE courses SET
    course_description = '<h4>Secondary Senior Years 11-12  Boys Only</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 96920,
    onshore_tuition_fee = NULL,
    enrolment_fee = 81735,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.twgs.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '004981C';
UPDATE courses SET
    course_description = '<h4>Primary Years 5-6 Boys Only</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 94720,
    onshore_tuition_fee = NULL,
    enrolment_fee = 79945,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.twgs.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082952F';
UPDATE courses SET
    course_description = '<h4>Secondary Junior Years 7-10 Boys Only</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 193840,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150955,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.twgs.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '082953E';