-- QLD Provider: Englishwise Global (04311H)
-- Courses sourced from CRICOS register (3 courses)

UPDATE provider_institution SET
    intake_date = 'January, February, April, July, October',
    updated_at = NOW()
WHERE cricos_provider_code = '04311H';

UPDATE courses SET
    course_description = '<h4>PTE and IELTS Examination Preparation</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 30,
    offshore_tuition_fee = 11400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 800,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://englishwiseglobal.qld.edu.au/',
    updated_at = NOW()
WHERE cricos_course_code = '117142C';
UPDATE courses SET
    course_description = '<h4>General English</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 72,
    offshore_tuition_fee = 22800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1400,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://englishwiseglobal.qld.edu.au/',
    updated_at = NOW()
WHERE cricos_course_code = '117626E';
UPDATE courses SET
    course_description = '<h4>English for Academic Purposes</h4> <p><strong>Level:</strong> Non AQF Award</p>',
    course_duration_per_week = 48,
    offshore_tuition_fee = 15200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1000,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://englishwiseglobal.qld.edu.au/',
    updated_at = NOW()
WHERE cricos_course_code = '117627D';