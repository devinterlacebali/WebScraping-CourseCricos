-- King's Christian College (00341A) - Web-scraped course data
-- Generated: from https://www.kingscollege.qld.edu.au

-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'May',
    updated_at = NOW()
WHERE cricos_provider_code = '00341A';

UPDATE courses SET
    course_duration_per_week = 364,
    offshore_tuition_fee = 196460,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = 'English Language Preparation: All international students are required to develop a solid foundation in English prior to commencing their enrolment at King’s. To support this, both primary and high school students may enrol in one of the many excellent language schools located on the Gold Coast. Primary-aged students are encouraged to attendYoung Learnersprograms.High school students should undertakeHigh School Preparationcourses. Once students acquire the necessary English proficiency (see our p',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '082924K';

UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 119680,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = 'English Language Preparation: All international students are required to develop a solid foundation in English prior to commencing their enrolment at King’s. To support this, both primary and high school students may enrol in one of the many excellent language schools located on the Gold Coast. Primary-aged students are encouraged to attendYoung Learnersprograms.High school students should undertakeHigh School Preparationcourses. Once students acquire the necessary English proficiency (see our p',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '082925J';

UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 55840,
    onshore_tuition_fee = NULL,
    enrolment_fee = 57872,
    materials_fee = NULL,
    entry_requirements = 'English Language Preparation: All international students are required to develop a solid foundation in English prior to commencing their enrolment at King’s. To support this, both primary and high school students may enrol in one of the many excellent language schools located on the Gold Coast. Primary-aged students are encouraged to attendYoung Learnersprograms.High school students should undertakeHigh School Preparationcourses. Once students acquire the necessary English proficiency (see our p',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '082926G';

