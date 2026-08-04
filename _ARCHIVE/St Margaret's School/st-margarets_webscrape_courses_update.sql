-- St Margaret's School (00344J) - Web-scraped course data
-- Generated: from https://www.stmargarets.vic.edu.au

-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'May',
    updated_at = NOW()
WHERE cricos_provider_code = '00344J';

UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 251865,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = 'Admissions Overview: St Margaret’s Berwick Grammar offers a unique learning environment designed to honour everything we know about providing a great education.The school, set over two campuses, offers Early Learning (3 and 4 year olds), Junior School (Prep – Year 6), and Senior Girls (Years 7 – 12) in defined areas on our 30-acre Berwick Campus and our dedicated 20-acre senior boys campus at Officer.Admission to the school is based on how we can best help a student achieve academically by helpi',
    apply_form = '',
    updated_at = NOW()
WHERE cricos_course_code = '019219C';

