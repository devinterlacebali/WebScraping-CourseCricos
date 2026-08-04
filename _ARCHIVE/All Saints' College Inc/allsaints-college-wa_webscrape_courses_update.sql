-- All Saints' College Inc. (02029D) - Webscrape Update
UPDATE provider_institution SET intake_date='February, July', updated_at=NOW() WHERE cricos_provider_code='02029D';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 158360,
    onshore_tuition_fee = NULL,
    enrolment_fee = 15265,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.allsaints.wa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '034858B';
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 144900,
    onshore_tuition_fee = NULL,
    enrolment_fee = 15265,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.allsaints.wa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '095514K';
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 78750,
    onshore_tuition_fee = NULL,
    enrolment_fee = 13265,
    materials_fee = NULL,
    course_description = '',
    entry_requirements = 'Contact school for entry requirements. AEAS test and/or interview may be required.',
    apply_form = 'https://www.allsaints.wa.edu.au',
    updated_at = NOW()
WHERE cricos_course_code = '095517G';
