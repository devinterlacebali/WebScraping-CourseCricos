-- Update provider institution details
UPDATE provider_institution SET intake_date = 'February, July', updated_at = NOW() WHERE cricos_provider_code = '00144F';

UPDATE courses SET course_description = '<h4>Course Overview</h4><p>The Hamilton and Alexandra College - International Program for secondary students.</p>', course_duration_per_week = 312, offshore_tuition_fee = 199540, enrolment_fee = 32558, entry_requirements = 'Contact school for international student entry requirements. AEAS testing may apply.', apply_form = 'https://www.hamiltoncollege.vic.edu.au/enrolment/', updated_at = NOW() WHERE cricos_course_code = '015915M';

