-- QLD Provider: Sunshine Coast Grammar School (02537F)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, July',
    updated_at = NOW()
WHERE cricos_provider_code = '02537F';

UPDATE courses SET
    course_description = '<h4>Primary Years 1-6 Boys & Girls</h4> <p><strong>Level:</strong> Primary School Studies</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 192100,
    onshore_tuition_fee = NULL,
    enrolment_fee = 12400,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.scgs.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '086205J';
UPDATE courses SET
    course_description = '<h4>Junior Secondary Years 7-10 Boys & Girls</h4> <p><strong>Level:</strong> Junior Secondary Studies</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 173700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 9900,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic transcripts, English language proficiency assessment, school interview</p>',
    apply_form = 'https://www.scgs.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '086206G';
UPDATE courses SET
    course_description = '<h4>Senior Secondary Years 11-12 Boys & Girls</h4> <p><strong>Level:</strong> Senior Secondary Certificate of Education</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 86900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 6800,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>Academic records, English language proficiency (IELTS 5.5+ or equivalent), relevant prior study or work experience</p>',
    apply_form = 'https://www.scgs.qld.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '086207G';