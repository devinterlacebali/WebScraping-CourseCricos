UPDATE provider_institution SET
    intake_date = 'January, April, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00324B';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 315000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 1200,
    materials_fee = NULL,
    entry_requirements = 'AEAS testing required: Years 7-8 (40+), Years 9-10 (60+), Year 11 (80+). School reports and interview.',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '011309K';

