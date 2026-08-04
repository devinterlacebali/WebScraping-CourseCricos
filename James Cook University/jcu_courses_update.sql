-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, February, March, May, July, September, October, November',
    updated_at = NOW()
WHERE cricos_provider_code = '00117J';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study a Diploma of Business [Pathway], and you will graduate with an understanding of key business perspectives and approaches.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 30191,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>Successful completion of a course of study equivalent to an Australian Year 12 Certificate, or Successful completion of JCU Certificate of Higher Education</p><br/><p><strong>English language requirements</strong></p> <p>Band P</p> <p>If your native language is not English, you must meet the <a href="https://www.jcu.edu.au/policy/academic-governance/student-experience/admissions-policy-schedule-ii">minimum English language requirements</a> for this course.</p>',
    apply_form = 'https://www.jcu.edu.au/courses/diploma-of-business-pathway',
    updated_at = NOW()
WHERE cricos_course_code = '112845A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This Pathway Course Will Allow You to Take the 1st Steps into a Future Career in Engineering | Learn More & Apply Online with James Cook University Today!</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 32268,
    onshore_tuition_fee = 7520,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>Successful completion of a course of study equivalent to an Australian Year 12 Certificate</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/diploma-of-engineering-pathway',
    updated_at = NOW()
WHERE cricos_course_code = '098159M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study & Obtain a Diploma of Higher Education | Learn More & Apply Online with James Cook University Today!</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 34649,
    onshore_tuition_fee = 10980,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>Business major - English (Units 3/4,C); all other majors - nil</p><br/> <p><strong>English language requirements</strong></p><p>For the Business major: Applicants of non-English speaking background must meet the English language proficiency requirements of Band 1 – <a href="https://www.jcu.edu.au/policy/academic-governance/student-experience/admissions-policy-schedule-ii">Schedule II of the JCU Admissions Policy</a>.</p><p>For the Psychological Science major: Applicants of non-English speaking background must meet the English language proficiency requirements of Band 1 – <a href="https://www.jcu.edu.au/policy/academic-governance/student-experience/admissions-policy-schedule-ii">Schedule II of the JCU Admissions Policy</a>.</p><p>For all other majors: Applicants of non-English speaking background must meet the English language proficiency requirements of Band P – <a href="https://www.jcu.edu.au/policy/academic-governance/student-experience/admissions-policy-schedule-ii">Schedule II of the JCU Admissions Policy</a>.</p>',
    apply_form = 'https://www.jcu.edu.au/courses/diploma-of-higher-education',
    updated_at = NOW()
WHERE cricos_course_code = '082840C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn Programming, Data Science & Internet Fundamentals with JCU’s 1 Year Diploma of Information Technology (Pathway) | Apply Online Today with JCU!</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 29153,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>Successful completion of a course of study equivalent to an Australian Year 12 Certificate</p><br/><p><strong>English language requirements</strong></p> <p>Band P</p> <p>If your native language is not English, you must meet the <a href="https://www.jcu.edu.au/policy/academic-governance/student-experience/admissions-policy-schedule-ii">minimum English language requirements</a> for this course.</p>',
    apply_form = 'https://www.jcu.edu.au/courses/diploma-of-information-technology-pathway',
    updated_at = NOW()
WHERE cricos_course_code = '0100451';
UPDATE courses SET
    course_description = '',
    course_duration_per_week = 52,
    offshore_tuition_fee = 29153,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>Successful completion of a course of study equivalent to an Australian Year 12 Certificate or Successful completion of JCU Certificate of Higher Education</p><br/><p><strong>English language requirements</strong></p> <p>Band P</p> <p>If your native language is not English, you must meet the <a href="https://www.jcu.edu.au/policy/academic-governance/student-experience/admissions-policy-schedule-ii">minimum English language requirements</a> for this course.</p>',
    apply_form = 'https://www.jcu.edu.au/courses/diploma-of-tourism,-hospitality-and-events-pathway',
    updated_at = NOW()
WHERE cricos_course_code = '113866K';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Certificate of Advanced Practice and Prescribing for Pharmacists | https://www.jcu.edu.au/courses/graduate-certificate-of-advanced-practice-and-prescribing-for-pharmacists

-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Certificate of Prehospital and Retrieval Medicine | https://www.jcu.edu.au/courses/graduate-certificate-of-prehospital-and-retrieval-medicine

-- ⚠️ Skipped (no CRICOS in JSON-LD): JCU Prep | https://www.jcu.edu.au/courses/jcu-prep

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Become a leader in science and research with JCU’s Advanced Science degree. Discover innovative solutions for complex real-world challenges.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 130941,
    onshore_tuition_fee = 24840,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 90</strong></p> <p>Mathematical Methods (Units 3/4,C)</p><br/><p><strong>Recommended Knowledge</strong></p> <p>English (Units 3/4,C), Chemistry (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-advanced-science',
    updated_at = NOW()
WHERE cricos_course_code = '092515M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Harmonise your critical thinking, analytical and communication skills with in-depth knowledge and expertise in a range of social and cultural contexts.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 103947,
    onshore_tuition_fee = 35001,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 59</strong></p> <p>English (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-arts',
    updated_at = NOW()
WHERE cricos_course_code = '010346B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Broaden your understanding of different sociocultural contexts and explore opportunities for sustainable, human-focused business practices in a double degree.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 147596,
    onshore_tuition_fee = 54760,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 59</strong></p> <p>English (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-arts-bachelor-of-business',
    updated_at = NOW()
WHERE cricos_course_code = '036644M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Become a legal professional with versatile skills. Understanding the role and relevance of law in social, economic, environmental and political contexts.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 184495,
    onshore_tuition_fee = 79250,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 66.5</strong></p> <p>English (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-arts-bachelor-of-laws',
    updated_at = NOW()
WHERE cricos_course_code = '013247C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Combine your knowledge of society and cultures with scientific principles to better understand the connections between people and their environments.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 169908,
    onshore_tuition_fee = 46600,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 66.5</strong></p> <p><strong>Recommended Knowledge</strong></p> <p>English (Units 3/4,C), Mathematical Methods (Units 3/4,C),Chemistry, General Maths or Mathematical Methods (Units 3/4,C) – Mathematical Methods recommended for the Majors in Maths, Physics, and Data Science.</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-arts-bachelor-of-science',
    updated_at = NOW()
WHERE cricos_course_code = '028993A';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Bachelor of Biomedical Sciences - Bachelor of Laboratory Medicine | https://www.jcu.edu.au/courses/bachelor-of-biomedical-sciences

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Elevate your skills to excel in business with real-world industry experience. Use your insight build sustainable, competitive business strategies.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 106938,
    onshore_tuition_fee = 47730,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 59</strong></p> <p><strong>Recommended Knowledge</strong></p> <p>English (Units 3/4,C), Mathematical Methods (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-business',
    updated_at = NOW()
WHERE cricos_course_code = '026830C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Pair your business insight and hands-on experience with a strong understanding of legal principles to bring unparalleled expertise to future roles.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 147596,
    onshore_tuition_fee = 64440,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 66.5</strong></p> <p>English (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-business-bachelor-of-laws',
    updated_at = NOW()
WHERE cricos_course_code = '031833B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Understand the social and physiological drivers of human behaviour and the implications for human resources, marketing and business management.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 117444,
    onshore_tuition_fee = 35580,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 64</strong></p> <p>English (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-business-bachelor-of-psychological-science',
    updated_at = NOW()
WHERE cricos_course_code = '085453A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Launch yourself into the dynamic world of commerce, specialising in fields like accounting, economics, financial markets, money management and trade.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 110697,
    onshore_tuition_fee = 46950,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 59</strong></p> <p><strong>Recommended Knowledge</strong></p> <p>English (Units 3/4,C), Mathematical Methods (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-commerce',
    updated_at = NOW()
WHERE cricos_course_code = '0101385';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Diagnose, treat and manage oral health issues, improve speech function and alleviate pain caused by dental disease. Apply today.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 394945,
    onshore_tuition_fee = 57300,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>English (Units 3/4,C), Mathematical Methods (Units 3/4,C), Chemistry (Units 3/4,C)</p><br/><p><strong>Recommended Knowledge</strong></p> <p>Biology (Units 3/4,C)</p><br/> <p><a href="#how-to-apply">Special entry requirements</a> apply</p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-dental-surgery',
    updated_at = NOW()
WHERE cricos_course_code = '073997A';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Bachelor of Education (Early Childhood Education) | https://www.jcu.edu.au/courses/bachelor-of-education-early-childhood-education

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Connect with young learners and encourage positive development. Prepare to teach Prep to Year 6 through hands-on learning in diverse classroom settings.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 138596,
    onshore_tuition_fee = 19644,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 65</strong></p> <p>English (Units 3/4,C), General Mathematics or Mathematical Methods or Specialist Mathematics (Units 3/4,C); or equivalent.</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-education-primary',
    updated_at = NOW()
WHERE cricos_course_code = '081941F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Create positive learning environments for secondary school students. Strengthen your skills through practical classroom experiences.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 138596,
    onshore_tuition_fee = 24320,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 65</strong></p> <p>English (Units 3/4,C), General Mathematics or Mathematical Methods or Specialist Mathematics (Units 3/4,C); or equivalent.</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-education-secondary',
    updated_at = NOW()
WHERE cricos_course_code = '081942E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Combine advanced knowledge in mathematics, physics and science with analytical problem-solving skills to develop creative ideas and solutions.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 169908,
    onshore_tuition_fee = 33280,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 70</strong></p> <p><strong>Recommended Knowledge</strong></p> <p>English (Units 3/4,C) and Mathematical Methods (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-engineering-honours',
    updated_at = NOW()
WHERE cricos_course_code = '085458G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Become a world-class engineer and information technology professional. Develop hands-on skills in laboratory classes, practical workshops and projects.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 212385,
    onshore_tuition_fee = 43300,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 70</strong></p> <p><strong>Recommended Knowledge</strong></p> <p>English (Units 3/4,C) and Mathematical Methods (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-engineering-honours-bachelor-of-information-technology',
    updated_at = NOW()
WHERE cricos_course_code = '085411M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop skills for real-world research and innovation in engineering and science. Examine engineering principles, scientific methods and research practices.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 212385,
    onshore_tuition_fee = 42450,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 70</strong></p> <p><strong>Recommended Knowledge</strong></p> <p>English (Units 3/4,C) and Mathematical Methods (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-engineering-honours-bachelor-of-science',
    updated_at = NOW()
WHERE cricos_course_code = '085380B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Find innovative solutions to complex environmental problems. Pursue careers in environmental conservation, research, communication or management.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 117444,
    onshore_tuition_fee = 31290,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 63</strong></p> <p><strong>Recommended Knowledge</strong></p> <p>English (Units 3/4,C), Chemistry (Units 3/4,C), and General Maths or Mathematical Methods (Units 3/4, C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-environmental-science-and-management',
    updated_at = NOW()
WHERE cricos_course_code = '108976B';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Bachelor of Exercise Science-Bachelor of Exercise Physiology | https://www.jcu.edu.au/courses/bachelor-of-exercise-science-bachelor-of-exercise-physiology

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Build your skills in software development, web design, internet systems and databases. Gain practical experience through internships, workshops and projects.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 110697,
    onshore_tuition_fee = 28290,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 63</strong></p> <p><strong>Recommended Knowledge</strong></p> <p>English (Units 3/4,C), General Maths or Mathematical Methods (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-information-technology',
    updated_at = NOW()
WHERE cricos_course_code = '010438J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Prepare for a contemporary legal career as you develop skills in contracts, property, criminal, commercial, constitutional and administrative law. Apply now.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 110697,
    onshore_tuition_fee = 52197,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 75</strong></p> <p>English (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-laws',
    updated_at = NOW()
WHERE cricos_course_code = '0102134';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Immerse yourself in marine biology and coastal systems with JCU''s Bachelor of Marine Science. Build expertise in seabed mapping, sonar tracking and more.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 142065,
    onshore_tuition_fee = 26400,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 75</strong></p> <p><strong>Recommended Knowledge</strong></p> <p>English (Units 3/4,C), Chemistry (Units 3/4,C), and General Maths or Mathematical Methods (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-marine-science',
    updated_at = NOW()
WHERE cricos_course_code = '056552E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study a Bachelor of Medicine, Bachelor of Surgery at JCU and build a dynamic medical career. Benefit from small classes and hands-on clinical placements.</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 428298,
    onshore_tuition_fee = 81348,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>English (3/4,C), Mathematical Methods (Units 3/4,C), Chemistry (Units 3/4,C)</p><br/> <p><a href="#how-to-apply">Special entry requirements</a> apply</p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-medicine-bachelor-of-surgery',
    updated_at = NOW()
WHERE cricos_course_code = '043052K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Contribute to patient care with a Bachelor of Nursing Science. Successful completion can lead to eligibility for professional registration.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 115095,
    onshore_tuition_fee = 17760,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 66</strong></p> <p><strong>Recommended Knowledge</strong></p> <p>English (Units 3/4,C), Biology, Chemistry and one of General Maths, Mathematical Methods, or Specialist Maths (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-nursing-science',
    updated_at = NOW()
WHERE cricos_course_code = '010441C';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Bachelor of Nursing Science [Pre-Registration] [Mixed] | https://www.jcu.edu.au/courses/bachelor-of-nursing-science-ext

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Support people with injuries or disabilities to participate in the activities that matter to them. Accredited by the Occupational Therapy Council of Australia.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 169908,
    onshore_tuition_fee = 35480,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 70</strong></p> <p>English (Units 3/4,C); One of Biology, Chemistry, Physics, Health, Psychology or Physical Education (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-occupational-therapy-honours',
    updated_at = NOW()
WHERE cricos_course_code = '094677K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn about the practical use of medicines and preventative healthcare strategies. Develop your knowledge of human anatomy, chemistry and pharmacology.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 127431,
    onshore_tuition_fee = 28611,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 76</strong></p> <p>English (Units 3/4,C), General Mathematics (Units 3/4,C)</p><br/><p><strong>Recommended Knowledge</strong></p> <p>Chemistry (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-pharmacy-honours',
    updated_at = NOW()
WHERE cricos_course_code = '113584J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Address musculoskeletal and neurological health conditions caused by illness, ageing, or injury. Help people to manage pain and improve mobility.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 138333,
    onshore_tuition_fee = 26760,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 89</strong></p> <p><strong>Recommended Knowledge</strong></p> <p>English (Units 3/4,C), Mathematical Methods (Units 3/4,C), plus one of Chemistry, Biology, Physics, Physical Education, Psychology or Health (Units 3/4,C); or equivalent</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-physiotherapy',
    updated_at = NOW()
WHERE cricos_course_code = '053801F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Examine psychological theory, interpretation and application. Pursue clinical or professional psychology practice with Honours and Master-level progressions.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 117444,
    onshore_tuition_fee = 31740,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 64</strong></p> <p>English (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-psychological-science',
    updated_at = NOW()
WHERE cricos_course_code = '085452B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Examine human behaviour and build valuable research skills in this fourth-year training program. Take the next step in becoming a registered Psychologist.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 39148,
    onshore_tuition_fee = 9537,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree that includes an APAC-approved three-year sequence in psychology, completed in the past 10 years with a 5.5 GPA; or an APAC-approved bridging degree that includes foundational competencies, completed in the past 10 years with a 5.5 GPA; or equivalent.</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-psychological-science-honours',
    updated_at = NOW()
WHERE cricos_course_code = '086285D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Kickstart your career in science with real-world projects in unique environments. Gain knowledge and practical skills with a JCU Bachelor of Science.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 127431,
    onshore_tuition_fee = 26880,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 66.5</strong></p> <p><strong>Recommended Knowledge</strong></p> <p>English (Units 3/4,C), Chemistry, General Maths or Mathematical Methods (Units 3/4,C) – Mathematical Methods recommended for the Majors in Maths, Physics, and Data Science.</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-science',
    updated_at = NOW()
WHERE cricos_course_code = '076290A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Use your scientific expertise and in-depth legal knowledge to influence policy outcomes in fields like environmental law, bioethics and sustainability.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 212385,
    onshore_tuition_fee = 68800,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 66.5</strong></p> <p>English (Units 3/4,C),</p><br/><p><strong>Recommended Knowledge</strong></p> <p>Chemistry, General Maths or Mathematical Methods (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-science-bachelor-of-laws',
    updated_at = NOW()
WHERE cricos_course_code = '017881M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Promote the social welfare of individuals and communities. Build your knowledge of cross-cultural practices, eco-social justice and human psychology.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 138596,
    onshore_tuition_fee = 38148,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 62</strong></p> <p>English (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-social-work',
    updated_at = NOW()
WHERE cricos_course_code = '010351E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Apply your health expertise in anatomy, linguistics, psychology and education to help people manage communication and swallowing difficulties.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 184444,
    onshore_tuition_fee = 39760,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>ATAR 70</strong></p> <p>English (Units 3/4,C) plus one of Biology, Chemistry, Physics, Psychology or Health (Units 3/4,C)</p><br/> <p><a href="#accordion_pathways">Alternate Pathways</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-speech-pathology-honours',
    updated_at = NOW()
WHERE cricos_course_code = '094679G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Design customer-informed tourism, hospitality and events experiences through real-world practical placements and JCU''s five-star tourism industry connections.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 110697,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><strong>Recommended Knowledge</strong></p> <p>English (Units 3/4,C); Mathematical Methods (Units 3/4, C)</p><br/><p><strong>English language requirements</strong></p> <p>Band 1</p> <p>If your native language is not English, you must meet the <a href="https://www.jcu.edu.au/policy/academic-governance/student-experience/admissions-policy-schedule-ii">minimum English language requirements</a> for this course.</p> <p>View the <a href="https://www.jcu.edu.au/entry-options/entry-requirements/academic-and-english-language-entry-requirements/country-specific-academic-levels">international entry requirements</a> for this course</p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-tourism-hospitality-and-events',
    updated_at = NOW()
WHERE cricos_course_code = '0101080';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Deliver safe and effective health care for all types of animals and help meet tomorrow''s demands in sustainable farming. Apply today.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 369195,
    onshore_tuition_fee = 61350,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>English, Mathematical Methods, Chemistry (Units 3/4,C)</p><br/><p><strong>Recommended Knowledge</strong></p> <p>Biology (Units 3/4,C)</p><br/> <p><a href="#how-to-apply">Special entry requirements</a> apply</p>',
    apply_form = 'https://www.jcu.edu.au/courses/bachelor-of-veterinary-science-honours',
    updated_at = NOW()
WHERE cricos_course_code = '105718M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Elevate your business career with essential skills in finance and accounting, human relations, marketing, investment and international business. Apply today.</p>',
    course_duration_per_week = 35,
    offshore_tuition_fee = 13049,
    onshore_tuition_fee = 5800,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree in any discipline; or 5 years business experience; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/graduate-certificate-of-business-administration',
    updated_at = NOW()
WHERE cricos_course_code = '118036H';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Certificate of Career Development | https://www.jcu.edu.au/courses/graduate-certificate-of-career-development

-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Certificate of Diabetes Education | https://www.jcu.edu.au/courses/graduate-certificate-of-diabetes-education

-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Certificate of Disaster Health and Humanitarian Assistance | https://www.jcu.edu.au/courses/graduate-certificate-of-disaster-health-and-humanitarian-assistance

-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Certificate of Education | https://www.jcu.edu.au/courses/graduate-certificate-of-education

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Be inspired to improve the lives of others throughout the Tropics. Examine complex global development challenges through real-world scenarios and projects.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 18450,
    onshore_tuition_fee = 6330,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/graduate-certificate-of-global-development',
    updated_at = NOW()
WHERE cricos_course_code = '098476J';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Certificate of Health Professional Education | https://www.jcu.edu.au/courses/graduate-certificate-of-health-professional-education

-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Certificate of Indigenous Studies | https://www.jcu.edu.au/courses/graduate-certificate-of-indigenous-studies

-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Certificate of Infection Control | https://www.jcu.edu.au/courses/graduate-certificate-of-infection-control

-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Certificate of Information Technology | https://www.jcu.edu.au/courses/graduate-certificate-of-information-technology

-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Certificate of Lifestyle Medicine | https://www.jcu.edu.au/courses/graduate-certificate-of-lifestyle-medicine

-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Certificate of Nursing | https://online.jcu.edu.au/online-courses/graduate-certificate-nursing

-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Certificate of Project Management | https://www.jcu.edu.au/courses/graduate-certificate-of-project-management

-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Certificate of Psychology | https://online.jcu.edu.au/online-courses/graduate-certificate-psychology

-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Certificate of Public Health | https://www.jcu.edu.au/courses/graduate-certificate-of-public-health

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Understand the methodology required to develop a research proposal. Gain the experience required for entry to higher research degrees at JCU.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 18450,
    onshore_tuition_fee = 2370,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>A 4-year AQF level 7 bachelor degree or an AQF level 8 qualification in a relevant discipline, with a 5.0 GPA and grade of 65% or better in one research methods subject; or equivalent.</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/graduate-certificate-of-research-methods',
    updated_at = NOW()
WHERE cricos_course_code = '086003G';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Certificate of Travel Medicine | https://www.jcu.edu.au/courses/graduate-certificate-of-travel-medicine

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Understand the urgent social and environmental issues facing vulnerable communities. Help find solutions to support sustainable local and global development.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 36899,
    onshore_tuition_fee = 33133,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/graduate-diploma-of-global-development',
    updated_at = NOW()
WHERE cricos_course_code = '098477G';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Diploma of Health Professional Education | https://www.jcu.edu.au/courses/graduate-diploma-of-health-professional-education

-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Diploma of Lifestyle Medicine | https://www.jcu.edu.au/courses/graduate-diploma-of-lifestyle-medicine

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Build on your existing medical, biomedical or clinical knowledge. Expand your theoretical and communication skills through specialist laboratory placements.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 46111,
    onshore_tuition_fee = 11550,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree in biomedical sciences or cognate degree; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/graduate-diploma-of-medical-science',
    updated_at = NOW()
WHERE cricos_course_code = '092516K';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Diploma of Midwifery | https://www.jcu.edu.au/courses/graduate-diploma-of-midwifery

-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Diploma of Nursing | https://online.jcu.edu.au/online-courses/graduate-diploma-nursing

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn from JCU''s network of national and international experts in the field of psychological science. Develop valuable skills in research analysis and design.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 39148,
    onshore_tuition_fee = 17399,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>Completion of an AQF Level 7 bachelor degree that includes an Australian Psychology Accreditation Council approved three-year sequence in Psychology completed within the past 10 years; and a minimum program GPA of 5.0; or Completion of an Australian Psychology Accreditation Council approved bridging degree that achieves foundational competencies within the past 10 years; and a minimum program GPA of 5.0; or Other qualifications recognised by the Deputy Vice-Chancellor of the Academy as equivalent to the above.</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/graduate-diploma-of-psychology',
    updated_at = NOW()
WHERE cricos_course_code = '040166B';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Diploma of Psychology (Bridging) | https://online.jcu.edu.au/online-courses/graduate-diploma-psychology

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Build your public health expertise in epidemiology, pathogenesis, clinical presentation, differential diagnosis and tropical disease management.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 42477,
    onshore_tuition_fee = 33070,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree in a relative health discipline; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/graduate-diploma-of-public-health-and-tropical-medicine',
    updated_at = NOW()
WHERE cricos_course_code = '026853G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain the foundational research skills required to complete your own independent small-scale research project and communicate your findings.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 36899,
    onshore_tuition_fee = 7160,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree in a relevant discipline; with a minimum grade point average of 5.0 (credit average) in the final year; or other qualifications recognised by the University as equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/graduate-diploma-of-research-methods',
    updated_at = NOW()
WHERE cricos_course_code = '086005F';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Diploma of Rural Generalist Practice | https://www.jcu.edu.au/courses/graduate-diploma-of-rural-generalist-practice

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain advanced knowledge and academic experience in your chosen field of science. Learn through practical workshops, projects and directed study.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 46111,
    onshore_tuition_fee = 10150,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree in science; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/graduate-diploma-of-science',
    updated_at = NOW()
WHERE cricos_course_code = '076291M';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Graduate Diploma of Surgical Anatomy | https://www.jcu.edu.au/courses/graduate-diploma-of-surgical-anatomy

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Become an expert in preventing and controlling communicable diseases. Learn strategies for addressing health challenges in tropical communities.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 42477,
    onshore_tuition_fee = 32550,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree in a relevant health discipline; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/graduate-diploma-of-tropical-medicine-and-hygiene',
    updated_at = NOW()
WHERE cricos_course_code = '027615B';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Master of Business Administration | https://www.jcu.edu.au/courses/master-of-business-administration

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>JCU’s leadership-oriented MBA prepares you apply smart business thinking to corporate strategy, project management, innovation and entrepreneurship.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 78296,
    onshore_tuition_fee = 66266,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>Completion of an AQF level 7 bachelor degree; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-business-administration-2-year',
    updated_at = NOW()
WHERE cricos_course_code = '107829K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Tackle modern challenges in big-data with JCU''s Master of Data Science. Become an expert in machine learning, data mining and advanced modelling.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 76730,
    onshore_tuition_fee = 72982,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree; or minimum five years relevant industry experience in IT or Data Science/Data Analytics; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-data-science-professional',
    updated_at = NOW()
WHERE cricos_course_code = '102256E';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Master of Education | https://www.jcu.edu.au/courses/master-of-education

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Examine the interconnections of management, marketing, finance, sustainability and education. Be equipped to lead in educational and professional spheres.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 78296,
    onshore_tuition_fee = 59140,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>Completion of an AQF level 7 bachelor degree</p><br/><p><strong>English language requirements</strong></p> <p>Band 2</p> <p>If your native language is not English, you must meet the <a href="https://www.jcu.edu.au/policy/academic-governance/student-experience/admissions-policy-schedule-ii">minimum English language requirements</a> for this course.</p>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-education-master-of-business-administration',
    updated_at = NOW()
WHERE cricos_course_code = '096264D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Step into leadership and engineering project management roles with JCU''s Master of Engineering Management. Apply now.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 78560,
    onshore_tuition_fee = 68340,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 8 bachelor degree in engineering or allied discipline; or an AQF level 7 bachelor degree in engineering or allied discipline, plus at least two years relevant work experience; or equivalent.</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-engineering-management',
    updated_at = NOW()
WHERE cricos_course_code = '109381K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advance your engineering career with JCU''s Master of Engineering. Specialise in Renewable Energy, Internet of Things (IoT), Technology or Water Management.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 84954,
    onshore_tuition_fee = 72982,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>Completion of a four-year Bachelor of Engineering at AQF Level 7 (or equivalent) in any discipline; or Completion of three years of the Bachelor of Engineering at Xi’an University of Technology (XUT) approved under the JCU-XUT Articulation Schedule only. Note: Entry for Master of Engineering (Professional) in Water Resource Management; Internet of Things and Data Engineering; and Electrical and Renewable Energy majors require completion of a four-year Bachelor of Engineering at AQF Level 7 (or equivalent) in a discipline cognate to the major.</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-engineering-professional',
    updated_at = NOW()
WHERE cricos_course_code = '098486G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>JCU''s Master of Global Development prepares you to address issues with poverty, planning, social justice, climate change, resource management and global health.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 73798,
    onshore_tuition_fee = 25300,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-global-development',
    updated_at = NOW()
WHERE cricos_course_code = '098478G';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Master of Guidance and Counselling | https://www.jcu.edu.au/courses/master-of-guidance-and-counselling

-- ⚠️ Skipped (no CRICOS in JSON-LD): Master of Health Professional Education | https://www.jcu.edu.au/courses/master-of-health-professional-education

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Expand your IT skills in programming, data analysis and multimedia with JCU''s Master of Information Technology, accredited by the Australian Computer Society.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 76016,
    onshore_tuition_fee = 29260,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree; or equivalent.</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-information-technology',
    updated_at = NOW()
WHERE cricos_course_code = '084823K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Expand your career and enhance your employability by gaining expert skills in Information Technology (IT) and Business Administration.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 76016,
    onshore_tuition_fee = 66266,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree in Information Technology</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-information-technology-master-of-business-administration',
    updated_at = NOW()
WHERE cricos_course_code = '053817J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Fly high in tourism and hospitality with this specialist JCU postgraduate course. Gain expert knowledge and experience in business operations and management.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 78296,
    onshore_tuition_fee = 66266,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree in any discipline; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-international-tourism-and-hospitality-management',
    updated_at = NOW()
WHERE cricos_course_code = '081132F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain the Skills Essential to becoming a Leader in the Hospitality & Tourism Sector with This Joint Master’s Degree. | Apply Online at James Cook University Today!</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 78296,
    onshore_tuition_fee = 66266,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree in a business or tourism-related discipline; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-international-tourism-and-hospitality-management-master-of-business-administration',
    updated_at = NOW()
WHERE cricos_course_code = '063678K';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Master of Lifestyle Medicine | https://www.jcu.edu.au/courses/master-of-lifestyle-medicine

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advance your skills with JCU’s Master of Marine Biology. Gain hands-on tropical marine experience at Orpheus Island Research Station on the Great Barrier Reef.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 96984,
    onshore_tuition_fee = 17900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree in science with a minimum GPA of 5.0, or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-marine-biology',
    updated_at = NOW()
WHERE cricos_course_code = '107243C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Grow your existing biomedical, medical laboratory and clinical measurement science expertise with JCU’s Master of Medical Science. Apply today.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 92222,
    onshore_tuition_fee = 62380,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 Biomedical Science or Medical Laboratory Science degree; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-medical-science',
    updated_at = NOW()
WHERE cricos_course_code = '096262F';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Master of Nursing | https://online.jcu.edu.au/online-courses/master-nursing

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>JCU''s fully-accredited Master of Professional Accounting gives you the postgraduate qualifications and knowledge to start your career in accounting.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 78296,
    onshore_tuition_fee = 66266,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree in non-accounting discipline; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-professional-accounting',
    updated_at = NOW()
WHERE cricos_course_code = '081135C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Obtain a Joint Master of Professional Accounting - Master of Business Administration at James Cook University. Study in Townsville or Singapore. Apply Online!</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 78296,
    onshore_tuition_fee = 66266,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>Completion of an AQF level 7 bachelor degree in a business discipline other than accounting from this or another University; or Other qualifications and/or experience recognised by the Deputy Vice-Chancellor of the Academy as equivalent to the above *Business disciplines: marketing, management, commerce, human resource management, economics, tourism and hospitality, or other disciplines where students will have completed study relating to organisational behaviour, business, strategy, marketing, economics, communication and people management.</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-professional-accounting-master-of-business-administration',
    updated_at = NOW()
WHERE cricos_course_code = '055156C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop professional psychology skills across diagnostics, intervention and psychological assessment and emerge ready to begin your career.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 46111,
    onshore_tuition_fee = 17399,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>Provisional registration as a psychologist in Australia. AQF level 8 bachelor honours degree accredited by the Australian Psychology Accreditation Council with GPA of 5.0 or above; or AQF level 8 graduate diploma accredited by the Australian Psychology Accreditation Council with GPA of 5.0 or above.</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-professional-psychology',
    updated_at = NOW()
WHERE cricos_course_code = '111728C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>JCU''s Master of Clinical Psychology prepares you to practise as a psychologist. Graduates are eligible for Psychology Board of Australia registration.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 92222,
    onshore_tuition_fee = 9476,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>Class 1 or 2A honours from AQF Level 8 bachelor honours degree accredited by the Australian Psychological Society; or equivalent. Must hold Provisional registration as a psychologist in Australia.</p><br/><p><strong>English language requirements</strong></p> <p>Band 3c</p> <p>If your native language is not English, you must meet the <a href="https://www.jcu.edu.au/policy/academic-governance/student-experience/admissions-policy-schedule-ii">minimum English language requirements</a> for this course.</p>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-psychology-clinical',
    updated_at = NOW()
WHERE cricos_course_code = '019793F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Step into leadership roles in the health sector with JCU''s Master of Public Health. Enjoy the option to specialise in Aeromedical Retrieval. Apply now.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 42477,
    onshore_tuition_fee = 10430,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree in a relevant health discipline; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-public-health',
    updated_at = NOW()
WHERE cricos_course_code = '040170F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Extend your impact in public health and tropical medicine with this postgraduate degree. Learn how to influence health policies and stop the spread of disease.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 42477,
    onshore_tuition_fee = 11100,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree in a relevant discipline; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-public-health-and-tropical-medicine',
    updated_at = NOW()
WHERE cricos_course_code = '026849C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Understand the urgent health problems facing vulnerable communities and businesses. Be ready to take on senior roles in public health, planning and policy.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 84954,
    onshore_tuition_fee = 63580,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree in a Health Sciences discipline; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-public-health-master-of-business-administration',
    updated_at = NOW()
WHERE cricos_course_code = '040171E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop the interdisciplinary skills and expertise to address urgent issues facing vulnerable communities in public health and global development.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 84954,
    onshore_tuition_fee = 21960,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>Completion of an AQF level 7 bachelor degree in a relevant health discipline; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-public-health-master-of-global-development',
    updated_at = NOW()
WHERE cricos_course_code = '107244B';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Master of Rural Generalist Practice | https://www.jcu.edu.au/courses/master-of-rural-generalist-practice

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Magnify your expertise in Aquaculture, Earth Science, Environment, Fisheries, Geology, Global Change or Tropical Biology with JCU''s Master of Science.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 43949,
    onshore_tuition_fee = 9870,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF Level 7 bachelor degree in science with minimum GPA of 5.0; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-science',
    updated_at = NOW()
WHERE cricos_course_code = '074894M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Address global environmental challenges as you advance your professional career in Science. Benefit from hands-on experience in research or an internship.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 87904,
    onshore_tuition_fee = 16220,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF Level 7 bachelor degree in science with minimum GPA of 5.0; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-science-professional',
    updated_at = NOW()
WHERE cricos_course_code = '095865J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Make a difference with a master''s degree in social work. This accredited course is recognised by the Australian Association of Social Workers. Apply today.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 69298,
    onshore_tuition_fee = 19074,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree in a relevant discipline other than Social Work that includes a minimum of 1 year full-time study in social and behavioural sciences; or equivalent</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-social-work-professional-qualifying',
    updated_at = NOW()
WHERE cricos_course_code = '070091A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn to create supportive secondary learning environments with JCU''s Master of Teaching and Learning (Secondary) and be ready to teach students in Years 7-12.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 69298,
    onshore_tuition_fee = 9476,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF Level 7 bachelor degree which includes subjects in two teaching areas appropriate to curriculum in Australian secondary schools</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-teaching-and-learning-secondary',
    updated_at = NOW()
WHERE cricos_course_code = '095676C';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Master of Philosophy | https://www.jcu.edu.au/courses/master-of-philosophy

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Make a Meaningful Contribution to the Future of Indigenous Research & Affairs with James Cook University''s Master of Philosophy (Indigenous). Apply Online Today!</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 73798,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p>AQF level 7 bachelor degree with conditions</p><br/>',
    apply_form = 'https://www.jcu.edu.au/courses/master-of-philosophy-indigenous',
    updated_at = NOW()
WHERE cricos_course_code = '0100968';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study & Obtain a Doctor of Education [Research] in Townsville or Cairns | Learn More & Apply Online Today with James Cook University!</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 147596,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4> <p><a href="https://www.jcu.edu.au/policy/academic-governance/research-education/higher-degree-by-research-requirements">Higher degree by research requirements</a></p>',
    apply_form = 'https://www.jcu.edu.au/courses/doctor-of-education-research',
    updated_at = NOW()
WHERE cricos_course_code = '081375J';
-- ⚠️ Skipped (no CRICOS in JSON-LD): Doctor of Philosophy | https://www.jcu.edu.au/courses/doctor-of-philosophy

-- ⚠️ Skipped (no CRICOS in JSON-LD): Doctor of Philosophy (Indigenous) | https://www.jcu.edu.au/courses/doctor-of-philosophy-indigenous

-- Register-only (not on site scrape): Master of Laws
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 75273,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '013245E';
-- Register-only (not on site scrape): Bachelor of Biomedical Sciences
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 132596,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '013347K';
-- Register-only (not on site scrape): James Cook University Study Abroad Program (Half Year)
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 12772,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '044939G';
-- Register-only (not on site scrape): James Cook University Study Abroad Program (Full Year)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 25544,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '044940C';
-- Register-only (not on site scrape): James Cook University Exchange Program
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '046079G';
-- Register-only (not on site scrape): Tropical Australian Health Internship (1 semester) [Faculty of Medicine, Health and Molecular Sciences]
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 19574,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '047821G';
-- Register-only (not on site scrape): Postgraduate Qualifying Program - Business
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 18268,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '060146G';
-- Register-only (not on site scrape): Master of Business Administration - Master of Conflict Management and Resolution
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 79862,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '069811F';
-- Register-only (not on site scrape): Bachelor of Physiotherapy (Honours) [End-on]
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 46111,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '070074B';
-- Register-only (not on site scrape): Master of Philosophy (Creative Arts)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 75273,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '075190B';
-- Register-only (not on site scrape): Introductory Academic Program
UPDATE courses SET
    course_duration_per_week = 4,
    offshore_tuition_fee = 2000,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '075191A';
-- Register-only (not on site scrape): Master of Philosophy (Education)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 75273,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081339B';
-- Register-only (not on site scrape): Master of Philosophy (Society and Culture)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 75273,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081345D';
-- Register-only (not on site scrape): Master of Philosophy (Information Technology)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 75273,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081358K';
-- Register-only (not on site scrape): Master of Philosophy (Management and Commerce)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 75273,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081362C';
-- Register-only (not on site scrape): Master of Philosophy (Agriculture, Environmental and Related Studies)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 94066,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081368G';
-- Register-only (not on site scrape): Master of Philosophy (Architecture and Building)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 86653,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081369G';
-- Register-only (not on site scrape): Master of Philosophy (Engineering and Related Technologies)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 94066,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081370C';
-- Register-only (not on site scrape): Master of Philosophy (Natural and Physical Sciences)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 94066,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081373M';
-- Register-only (not on site scrape): Doctor of Philosophy (Education)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 156689,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081377G';
-- Register-only (not on site scrape): Doctor of Philosophy (Society and Culture)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 156689,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081379E';
-- Register-only (not on site scrape): Doctor of Philosophy (Creative Arts)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 156689,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081381M';
-- Register-only (not on site scrape): Doctor of Philosophy (Information Technology)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 156689,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081384G';
-- Register-only (not on site scrape): Doctor of Philosophy (Management and Commerce)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 156689,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081385G';
-- Register-only (not on site scrape): Doctor of Philosophy (Agriculture, Environmental and Related Studies)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 195808,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081386F';
-- Register-only (not on site scrape): Doctor of Philosophy (Architecture and Building)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 180377,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081387E';
-- Register-only (not on site scrape): Doctor of Philosophy (Engineering and Related Technologies)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 195808,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081388D';
-- Register-only (not on site scrape): Doctor of Philosophy (Natural and Physical Sciences)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 195808,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081389C';
-- Register-only (not on site scrape): Doctor of Philosophy (Health)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 180377,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081922J';
-- Register-only (not on site scrape): Master of Philosophy (Health)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 86653,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '081931G';
-- Register-only (not on site scrape): Bachelor of Biomedical Sciences (Honours) [End-on]
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 42477,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '085381A';
-- Register-only (not on site scrape): Bachelor of Information Technology (Honours) [End-on]
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 36898,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '085385G';
-- Register-only (not on site scrape): Bachelor of Science (Honours) [End-on]
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 42477,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '085388E';
-- Register-only (not on site scrape): Bachelor of Arts (Honours) [End-on]
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 34649,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '085456J';
-- Register-only (not on site scrape): Bachelor of Business (Honours) [End-on]
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 35646,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '086053J';
-- Register-only (not on site scrape): Bachelor of Medicine, Bachelor of Surgery (Honours) [End-on]
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 71383,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '086054G';
-- Register-only (not on site scrape): Bachelor of Sport and Exercise Science (Honours) [End-on]
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 39148,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '086055G';
-- Register-only (not on site scrape): Bachelor of Veterinary Science (Honours) [End-on]
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 73844,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '086056F';
-- Register-only (not on site scrape): Bachelor of Social Work (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 147136,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '093296J';
-- Register-only (not on site scrape): Bachelor of Medicine, Bachelor of Surgery (Honours)
UPDATE courses SET
    course_duration_per_week = 312,
    offshore_tuition_fee = 473482,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '094676M';
-- Register-only (not on site scrape): Bachelor of Medical Science (Honours) [End-on]
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 42477,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '095901K';
-- Register-only (not on site scrape): Bachelor of Laws (Honours) [End-on]
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 36898,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '102721G';
-- Register-only (not on site scrape): Bachelor of Commerce (Honours) [End-on]
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 36898,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '103175J';
-- Register-only (not on site scrape): Bachelor of Physiotherapy (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 195808,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '105717A';
-- Register-only (not on site scrape): Master of Philosophy (Medical, Molecular and Veterinary Sciences)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 94066,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '106731F';
-- Register-only (not on site scrape): Doctor of Philosophy (Medical, Molecular and Veterinary Sciences)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 195808,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '106732E';
-- Register-only (not on site scrape): Doctor of Philosophy (Indigenous)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 156689,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '106733D';
-- Register-only (not on site scrape): Bachelor of Science (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 180377,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '113432C';
-- Register-only (not on site scrape): Bachelor of Exercise Science - Bachelor of Physiology
UPDATE courses SET
    course_duration_per_week = 189,
    offshore_tuition_fee = 229096,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '117517K';
-- Register-only (not on site scrape): Bachelor of Midwifery
UPDATE courses SET
    course_duration_per_week = 154,
    offshore_tuition_fee = 119782,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '119970F';
-- Register-only (not on site scrape): Bachelor of Human Services
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 108160,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '120792J';
