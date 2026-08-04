-- Boston International Pty Ltd (04032D) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='04032D';

UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 18000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1250,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '110589F';
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 6000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '110590B';
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 6000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '110592M';
UPDATE courses SET
    course_duration_per_week = 60,
    offshore_tuition_fee = 12000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '110593K';
UPDATE courses SET
    course_duration_per_week = 80,
    offshore_tuition_fee = 18000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '110594J';
UPDATE courses SET
    course_duration_per_week = 94,
    offshore_tuition_fee = 22000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 4000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '114308K';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 24000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 4000,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '114309J';
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 6000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 750,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '120339H';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 20000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 2500,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = '',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '120657E';
