UPDATE provider_institution SET
    intake_date = 'January, April, July, October',
    updated_at = NOW()
WHERE cricos_provider_code = '00331C';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 165080,
    onshore_tuition_fee = NULL,
    enrolment_fee = 8350,
    materials_fee = NULL,
    entry_requirements = 'Secondary School Production Newsies tickets on sale now!Book HereMenuDiscover OxleyBack To TopParent CentreVisit OxleyToursSchool at Work ToursPrep ToursContact UsPhilosophyWho We ArePortrait of a GraduateVisionOur OriginsStrategic Education PlanJunior SchoolOur Junior SchoolEarly YearsUpper YearsPr',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '016943K';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 227691,
    onshore_tuition_fee = NULL,
    enrolment_fee = 10150,
    materials_fee = NULL,
    entry_requirements = 'Secondary School Production Newsies tickets on sale now!Book HereMenuDiscover OxleyBack To TopParent CentreVisit OxleyToursSchool at Work ToursPrep ToursContact UsPhilosophyWho We ArePortrait of a GraduateVisionOur OriginsStrategic Education PlanJunior SchoolOur Junior SchoolEarly YearsUpper YearsPr',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '016944J';

