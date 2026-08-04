-- Optimum Training Academy Pty Ltd (04432K) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='04432K';

UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 8000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '120036A';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 15000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '120037M';
UPDATE courses SET
    course_duration_per_week = 1,
    offshore_tuition_fee = 100,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '120038K';
UPDATE courses SET
    course_duration_per_week = 1,
    offshore_tuition_fee = 200,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '120039J';
UPDATE courses SET
    course_duration_per_week = 1,
    offshore_tuition_fee = 250,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '120040E';
