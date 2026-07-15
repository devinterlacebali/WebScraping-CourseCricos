-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, February, March, April, June, July, August, October, December',
    updated_at = NOW()
WHERE cricos_provider_code = '00116K';

-- Register-only (no study.unimelb match): Master of Education
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 104967,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '002127B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Bachelor of Commerce opens up careers in accounting, business, economics, finance, management, marketing and as an actuary, with some accreditations.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 189947,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5 (with no band less than 6.0)<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-commerce',
    updated_at = NOW()
WHERE cricos_course_code = '002143B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study at Australia''s #1 University and prepare yourself for a professional career in science</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 197008,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5 (with no band less than 6.0)<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-science',
    updated_at = NOW()
WHERE cricos_course_code = '002153M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study at Australia''s #1 University in 40 areas of specialisation, from languages and psychology, through to economics and media and communication</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 171690,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5 (with no band less than 6.0)<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-arts',
    updated_at = NOW()
WHERE cricos_course_code = '002167E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Explore course plans, entry requirements, careers & how to apply. Shape communities with an advanced understanding of urban policy & town planning</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 119684,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-planning',
    updated_at = NOW()
WHERE cricos_course_code = '002524M';
-- Register-only (no study.unimelb match): Bachelor of Engineering
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    updated_at = NOW()
WHERE cricos_course_code = '003626G';
-- Register-only (no study.unimelb match): Master of Commerce
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 76789,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '006654B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Find course plans, entry requirements & how to apply to the Master of Surgery. Undertake a research project at a leading hospital.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-surgery',
    updated_at = NOW()
WHERE cricos_course_code = '006666J';
-- Register-only (no study.unimelb match): Doctor of Philosophy (Medicine, Dentistry & Health Sciences)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 283064,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '006670B';
-- Register-only (no study.unimelb match): Master of Music
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 81475,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '006671A';
-- Register-only (no study.unimelb match): Master of Arts
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 67765,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '007306C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Find course plans, entry requirements & how to apply to the Master of Medicine. Undertake a research project at a leading hospital.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-medicine',
    updated_at = NOW()
WHERE cricos_course_code = '007317M';
-- Register-only (no study.unimelb match): Graduate Diploma in Clinical Dentistry
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 70976,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '007318K';
-- Register-only (no study.unimelb match): Bachelor of Arts (Degree with Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 57316,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '009645A';
-- Register-only (no study.unimelb match): Master of Psychology
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 132250,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '009681G';
-- Register-only (no study.unimelb match): Master of Psychology (Educational and Developmental)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 117600,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '009699J';
-- Register-only (no study.unimelb match): Master of Analytics Management
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 50160,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '0100137';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover this specialist course, which will equip you with comprehensive training and technical knowledge for a career in the finance industry.</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 102276,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-finance',
    updated_at = NOW()
WHERE cricos_course_code = '0100876';
-- Register-only (no study.unimelb match): Master of Finance (Enhanced)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 138567,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '0100877';
-- Register-only (no study.unimelb match): Graduate Diploma in Finance (exit award only)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '0100878';
-- Register-only (no study.unimelb match): Master of Actuarial Science (Enhanced)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '0100879';
-- Register-only (no study.unimelb match): Master of Actuarial Science (Extended)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '0100880';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Specialist computer science degree, with a major research project. Focus on AI, cybersecurity, programming, distributed computing and more.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 132250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-computer-science',
    updated_at = NOW()
WHERE cricos_course_code = '0100884';
-- Register-only (no study.unimelb match): Master of Theatre (Voice)
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 60609,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '0100967';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn to practice a form of psychotherapy utilising creative modalities. Discover course plans, entry requirements & how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 98650,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-creative-arts-therapy',
    updated_at = NOW()
WHERE cricos_course_code = '0100983';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements & how to apply to this specialist course, which will prepare you for the actuarial profession.</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 94538,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-actuarial-science',
    updated_at = NOW()
WHERE cricos_course_code = '0101265';
-- Register-only (no study.unimelb match): Master of Business Administration
UPDATE courses SET
    course_duration_per_week = 98,
    offshore_tuition_fee = 120384,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '0101669';
-- Register-only (no study.unimelb match): Bachelor of Science (Degree with Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 62208,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '014791D';
-- Register-only (no study.unimelb match): Bachelor of Commerce (Degree with Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 57856,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '014798G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Explore course structure, entry requirements & more for this dual-delivery public health course, uniting with a diverse cohort to improve healthcare</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 140650,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-public-health',
    updated_at = NOW()
WHERE cricos_course_code = '020358D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In this course you''ll learn skillsets to meet the demands of complex public policy-making. Discover course plans, entry requirements & how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-public-policy-and-management',
    updated_at = NOW()
WHERE cricos_course_code = '020385A';
-- Register-only (no study.unimelb match): Diploma in Music (Practical)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 34880,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '022054D';
-- Register-only (no study.unimelb match): Graduate Diploma in Arts (Advanced)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 48992,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '023185G';
-- Register-only (no study.unimelb match): Graduate Diploma in Science (Advanced)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '023188D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Understand the important issues & conceptual frameworks relating to your area of study. Discover course plans, entry requirements & learn how to apply</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 45984,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-arts',
    updated_at = NOW()
WHERE cricos_course_code = '023190K';
-- Register-only (no study.unimelb match): Master of Information Systems
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 68222,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '023203K';
-- Register-only (no study.unimelb match): Graduate Diploma in Information Systems
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 64000,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '024749A';
-- Register-only (no study.unimelb match): Graduate Diploma in Psychology (Advanced)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 60000,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '026666K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will equip you with the skillset to launch a career in the arts museum sector. Discover course plans, entry requirements & how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-art-curatorship',
    updated_at = NOW()
WHERE cricos_course_code = '027565G';
-- Register-only (no study.unimelb match): Master of Telecommunications Engineering
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 48320,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '027900G';
-- Register-only (no study.unimelb match): Bachelor of Fine Arts (Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 66912,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '029294J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will specialise you in your preferred area in the development field. Discover course plans, entry requirements & how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-development-studies',
    updated_at = NOW()
WHERE cricos_course_code = '031145D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course builds a solid foundation for your further studies and research. Discover course plans, entry requirements & how to apply.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 22992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-arts',
    updated_at = NOW()
WHERE cricos_course_code = '031944F';
-- Register-only (no study.unimelb match): Graduate Certificate in Arts (Advanced)
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 24496,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '031945E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements, and how to apply for the Master of International Tax.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-international-tax',
    updated_at = NOW()
WHERE cricos_course_code = '031950G';
-- Register-only (no study.unimelb match): Master of Environmental Engineering
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 62976,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '032293F';
-- Register-only (no study.unimelb match): Graduate Certificate in Information Systems (Advanced)
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 32000,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '035407K';
-- Register-only (no study.unimelb match): Bachelor of Dance (Degree with Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 24960,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '037218K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study at Australia''s #1 University and prepare yourself for a professional career in veterinary, agricultural and food sciences</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 170700,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5 (with no band less than 6.0)<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-agriculture',
    updated_at = NOW()
WHERE cricos_course_code = '037228G';
-- Register-only (no study.unimelb match): Bachelor of Agriculture (Degree with Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 52752,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '037229G';
-- Register-only (no study.unimelb match): Master of Psychology (Clinical Psychology)/Doctor of Philosophy
UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 341886,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '037232A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop specialised skills in environment, sustainability and leadership while working alongside industry partners in this 6-month course</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 28496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-environment',
    updated_at = NOW()
WHERE cricos_course_code = '040953G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study environmental fields such as climate change, public health or sustainability with opportunities to connect with industry and do research</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 56992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-environment',
    updated_at = NOW()
WHERE cricos_course_code = '040954G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Get ready for a unique and exciting career designing new and better ways to feed the world. The Graduate Diploma in Food Science combines a strong ...</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 54976,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-food-science',
    updated_at = NOW()
WHERE cricos_course_code = '041484B';
-- Register-only (no study.unimelb match): Exchange program (Postgraduate)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 31948,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '041630G';
-- Register-only (no study.unimelb match): Exchange Program (Undergraduate)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 28332,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '041631G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Get ready for a unique and exciting career designing new and better ways to feed the world. The Graduate Certificate in Food Science allows you to ...</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 27488,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-food-science',
    updated_at = NOW()
WHERE cricos_course_code = '042903B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will specialise you in media in an increasingly complex globalised context. Discover course plans, entry requirements & how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-global-media-communication',
    updated_at = NOW()
WHERE cricos_course_code = '045345C';
-- Register-only (no study.unimelb match): Study Abroad (Postgraduate 1)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 26000,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '045530B';
-- Register-only (no study.unimelb match): Study Abroad (Postgraduate 2)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 26000,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '045531A';
-- Register-only (no study.unimelb match): Study Abroad (Undergraduate)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 26000,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '045532M';
-- Register-only (no study.unimelb match): Master of Engineering Project Management
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44736,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '045957G';
-- Register-only (no study.unimelb match): Graduate Certificate in Engineering
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 31488,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '045960B';
-- Register-only (no study.unimelb match): Master of Primary Health Care
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '046262J';
-- Register-only (no study.unimelb match): Graduate Diploma in Urban Planning
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 57984,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '049410M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will enable you to navigate social policy through a global lens. Discover course plans, entry requirements & learn how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-social-policy',
    updated_at = NOW()
WHERE cricos_course_code = '049598E';
-- Register-only (no study.unimelb match): Bachelor of Film and Television (Degree with Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 48576,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '049961B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements and how to apply to the Master of Law and Development.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-law-and-development',
    updated_at = NOW()
WHERE cricos_course_code = '051271K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This program is a research doctorate for experienced professionals with educational responsibilities. Discover entry requirements and how to apply.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 241332,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/doctor-of-education',
    updated_at = NOW()
WHERE cricos_course_code = '051658B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements, careers paths & how to apply. Enhance your qualifications in property valuation in this 1-year course.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 57984,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-property-valuation',
    updated_at = NOW()
WHERE cricos_course_code = '052669B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop scientific, theoretical and clinical skills to practice as an oral health therapist or hygienist. Find course plans, entry requirements & how</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 270224,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7 (with no bands less than 7)<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-oral-health',
    updated_at = NOW()
WHERE cricos_course_code = '053176D';
-- Register-only (no study.unimelb match): Bachelor of Science (Honours) Psychology
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 45120,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '053177C';
-- Register-only (no study.unimelb match): Bachelor of Arts (Honours) Psychology
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 45120,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '053178B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Designed for qualified engineers looking to change their field of work. Learn to design, plan and construct sustainable, resilient structures.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 62976,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-structures',
    updated_at = NOW()
WHERE cricos_course_code = '053355A';
-- Register-only (no study.unimelb match): Master of Psychology (Clinical)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 102729,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '053838D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Fast-track your career in management, gain expertise in navigating organisational change and leading projects in this master of engineering degree.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 62976,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-engineering-management',
    updated_at = NOW()
WHERE cricos_course_code = '054325K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will expose you to the latest theoretical & practical advances in criminology. Discover course plans, entry requirements & how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-criminology',
    updated_at = NOW()
WHERE cricos_course_code = '055074E';
-- Register-only (no study.unimelb match): Master of Marketing
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 0,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '055075D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn the skillset needed to become a successful music therapist. Discover course plans, entry requirements & how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 98650,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-music-therapy',
    updated_at = NOW()
WHERE cricos_course_code = '055550D';
-- Register-only (no study.unimelb match): Master of Information Systems
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44736,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '055846K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Blend business and IT to drive organisational and technological change. Suited for students who want the skillset to be digital thinkers and business</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 134400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-information-systems',
    updated_at = NOW()
WHERE cricos_course_code = '055847J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Find course plans, entry requirements & how to apply to the course. Gain advanced skills & training to lead the future of clinical research.</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 68200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 7.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-research',
    updated_at = NOW()
WHERE cricos_course_code = '055848G';
-- Register-only (no study.unimelb match): Graduate Diploma in Clinical Research
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44000,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '055856G';
-- Register-only (no study.unimelb match): Graduate Certificate in Music
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 23488,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '056280B';
-- Register-only (no study.unimelb match): Graduate Diploma in Music
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 46976,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '056297D';
-- Register-only (no study.unimelb match): Master of Agribusiness
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 69930,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '056410G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In this course you''ll write a thesis of independent research to earn your PhD. Discover course plans, entry requirements & learn how to apply.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 236580,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/doctor-of-philosophy-arts',
    updated_at = NOW()
WHERE cricos_course_code = '056954J';
-- Register-only (no study.unimelb match): Doctor of Philosophy - Business and Economics
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 283064,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '056955G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements & how to apply to the Doctor of Philosophy (PhD) in Law, an exceptional research degree.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 236580,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/doctor-of-philosophy-law',
    updated_at = NOW()
WHERE cricos_course_code = '056956G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Designed for graduates to demonstrate academic leadership, independence, creativity and innovation in their research work.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 297024,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/doctor-of-philosophy-engineering-and-it',
    updated_at = NOW()
WHERE cricos_course_code = '056957F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Complete your PhD in Science with an independent research project to produce an original thesis and contribution to knowledge.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 255144,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/doctor-of-philosophy-science',
    updated_at = NOW()
WHERE cricos_course_code = '056958E';
-- Register-only (no study.unimelb match): Doctor of Philosophy - Medicine, Health Sciences
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 275787,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '056959D';
-- Register-only (no study.unimelb match): Doctor of Philosophy - Music
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 218016,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '056960M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn how to apply for PhD opportunities. Deepen your research and expertise in your chosen built environment field, guided by experienced supervisors</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 264500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/doctor-of-philosophy-architecture-building-and-planning',
    updated_at = NOW()
WHERE cricos_course_code = '056961K';
-- Register-only (no study.unimelb match): Master of Psychology (Educational and Developmental)/Doctor of Philosophy
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 241332,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '056962J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>A Doctor of Philosophy (PhD) in Agricultural Science helps you demonstrate academic leadership, increasing independence, creativity and innovation ...</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 273708,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/doctor-of-philosophy-agricultural-sciences',
    updated_at = NOW()
WHERE cricos_course_code = '056964G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>A Doctor of Philosophy (PhD) in Veterinary Science helps you demonstrate academic leadership, increasing independence, creativity and innovation in...</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 273708,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/doctor-of-philosophy-veterinary-science',
    updated_at = NOW()
WHERE cricos_course_code = '056965F';
-- Register-only (no study.unimelb match): Doctor of Philosophy - Melbourne Business School
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 182473,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '056966E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Make a distinct contribution and become a thought leader in the education field. Discover entry requirements and how to apply.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 241332,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/doctor-of-philosophy-education',
    updated_at = NOW()
WHERE cricos_course_code = '056968C';
-- Register-only (no study.unimelb match): Master of Law (Juris Doctor)/Master of Business Administration
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 209885,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '057850J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will develop your skillset in a broad spectrum of writing, publishing & editing. Discover course plans, entry requirements & how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with writing 7.0 and no other band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-creative-writing-publishing-and-editing',
    updated_at = NOW()
WHERE cricos_course_code = '058718E';
-- Register-only (no study.unimelb match): Bachelor of Music
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 133691,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '058837J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study the biomedical science of life, disease, and health systems right in the heart of the Melbourne Biomedical Precinct.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 212384,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5 (with no band less than 6.0)<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-biomedicine',
    updated_at = NOW()
WHERE cricos_course_code = '058838G';
-- Register-only (no study.unimelb match): Bachelor of Environments
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 179099,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '058839G';
-- Register-only (no study.unimelb match): Graduate Diploma in Nursing Practice
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44000,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '059231J';
-- Register-only (no study.unimelb match): Doctor of Philosophy - Victorian College of the Arts
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 218016,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '059249K';
-- Register-only (no study.unimelb match): Graduate Diploma in Performance Creation
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 31136,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '059250F';
-- Register-only (no study.unimelb match): Bachelor of Music (Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 39936,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '060219F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study arboriculture, garden design, tree management and more. Green up our urban spaces!</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 123850,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-horticulture',
    updated_at = NOW()
WHERE cricos_course_code = '061121G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Explore the foundations of designing, creating, managing and advocating for urban green spaces.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 58976,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-urban-horticulture',
    updated_at = NOW()
WHERE cricos_course_code = '061122G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Explore course plans, entry requirements, careers & how to apply. Specialise in property and real estate management in this industry-aligned degree</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 188644,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-property',
    updated_at = NOW()
WHERE cricos_course_code = '061195A';
-- Register-only (no study.unimelb match): Master of Property
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 84269,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '061196M';
-- Register-only (no study.unimelb match): Master of Architecture
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 91249,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '061197K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Explore the Master of Construction Management and construction management courses, with course plans, entry requirements, career paths & how to apply.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 188644,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-construction-management',
    updated_at = NOW()
WHERE cricos_course_code = '061198J';
-- Register-only (no study.unimelb match): Master of Landscape Architecture
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 81016,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '061208A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Explore course plans, entry requirements, career paths & how to apply. Develop contemporary landscape architecture skills in ecology & design</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 188644,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-landscape-architecture',
    updated_at = NOW()
WHERE cricos_course_code = '061209M';
-- Register-only (no study.unimelb match): Master of Construction Management
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 87707,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '061210G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements & how to apply to master of nursing science. Gain a qualification recognised nationally and globally.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 92400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0 with no band less than 7.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-nursing-science',
    updated_at = NOW()
WHERE cricos_course_code = '061211F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Find course plans, entry requirements & how to apply to master of social work (MSW). Make a difference in policy, mental health, aged care & more.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 115132,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 7.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-social-work',
    updated_at = NOW()
WHERE cricos_course_code = '061212E';
-- Register-only (no study.unimelb match): Master of Social Work
UPDATE courses SET
    course_duration_per_week = 130,
    offshore_tuition_fee = 82211,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '061213D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements, careers & how to apply to M Arch. Develop skills in architectural practice in this accredited degree.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 188644,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-architecture',
    updated_at = NOW()
WHERE cricos_course_code = '061224A';
-- Register-only (no study.unimelb match): Graduate Diploma in Teaching
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 34528,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '061225M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will enable you to launch your career in publishing & communications. Discover course plans, entry requirements & learn how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with writing 7.0 and no other band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-publishing-and-communications',
    updated_at = NOW()
WHERE cricos_course_code = '061634E';
-- Register-only (no study.unimelb match): Master of Cultural Material Conservation
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '061638A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Find course structure, entry requirements & how to apply to this psychology course, delving into human behaviour complexities for mental health impact</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 57240,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-psychology',
    updated_at = NOW()
WHERE cricos_course_code = '061720G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn how to apply for graduate research opportunities. Grow your expertise in your chosen-built environment field, guided by experienced supervisors</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 119684,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-architecture-building-and-planning',
    updated_at = NOW()
WHERE cricos_course_code = '061947K';
-- Register-only (no study.unimelb match): Master of Philosophy - Economics and Commerce
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '061949G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course teaches advanced skills in carrying out independent research through a critical application of specialist knowledge. Learn more.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 109200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-education',
    updated_at = NOW()
WHERE cricos_course_code = '061950D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Build your expertise in a specialist area and be supported by experienced supervisors and advisory committees to create significant change in society.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 134400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-engineering-and-it',
    updated_at = NOW()
WHERE cricos_course_code = '061951C';
-- Register-only (no study.unimelb match): Master of Philosophy - Psychological Sciences
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '061954M';
-- Register-only (no study.unimelb match): Master of Philosophy - Dental Science
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '061955K';
-- Register-only (no study.unimelb match): Master of Philosophy - Medicine
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '061956J';
-- Register-only (no study.unimelb match): Master of Philosophy - Music
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 81475,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '061957G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Complete a major piece of independent research as a path to an academic career, PhD or in industry as you work with leading academics.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 115450,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-science',
    updated_at = NOW()
WHERE cricos_course_code = '061958G';
-- Register-only (no study.unimelb match): Master of Philosophy - Arts
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 107050,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '061961A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Master of Philosophy (Agricultural Sciences) is an internationally recognised masters (by research) degree. It is designed help develop advance...</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 123850,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-agricultural-sciences',
    updated_at = NOW()
WHERE cricos_course_code = '061966G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements, and how to apply for the Master of Philosophy (Law).</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 107050,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-law',
    updated_at = NOW()
WHERE cricos_course_code = '061967F';
-- Register-only (no study.unimelb match): Master of Philosophy - Victorian College of Arts
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 36832,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '061968E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Find course plans, entry requirements & how to apply to the course. Gain an accredited certification & international opportunities.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 151200,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0 with written 7.0 and no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-genetic-counselling',
    updated_at = NOW()
WHERE cricos_course_code = '061969D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements, how to apply to this course, and discover how to contribute to a healthier world.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 115450,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-food-science',
    updated_at = NOW()
WHERE cricos_course_code = '061970M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements & how to apply to this course, which offers comprehensive training in all aspects of clinical audiology.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 144884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 7.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-audiology',
    updated_at = NOW()
WHERE cricos_course_code = '062905A';
-- Register-only (no study.unimelb match): Graduate Diploma in Management
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 94538,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '064484A';
-- Register-only (no study.unimelb match): Graduate Certificate in Management
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 60992,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '064486K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Melbourne Business School''s Master of Management will equip you with foundational business training and specialist organisational management training.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-management',
    updated_at = NOW()
WHERE cricos_course_code = '064496G';
-- Register-only (no study.unimelb match): Master of Management (Accounting)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '064499E';
-- Register-only (no study.unimelb match): Master of Management (Finance)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '064502D';
-- Register-only (no study.unimelb match): Master of Management (Marketing)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '064503C';
-- Register-only (no study.unimelb match): Master of Advanced Social Work (Research)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '064990E';
-- Register-only (no study.unimelb match): Master of Engineering
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 73309,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '065142D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Broaden your career options in with a language qualification. No previous experience is required and you can study alongside your bachelors degree</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 44832,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5 (with no band less than 6.0)<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/undergraduate/diploma-in-languages',
    updated_at = NOW()
WHERE cricos_course_code = '065143C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements & how to apply to this course, where you''ll learn advanced knowledge in economics and econometrics.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-economics',
    updated_at = NOW()
WHERE cricos_course_code = '065396D';
-- Register-only (no study.unimelb match): Master of Philosophy - Health Sciences
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '065917F';
-- Register-only (no study.unimelb match): Master of Philosophy - Population and Global Health
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '065918E';
-- Register-only (no study.unimelb match): Doctor of Medical Science
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 283064,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '066156A';
-- Register-only (no study.unimelb match): Doctor of Medical Science (Thesis by Compilation)
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 38528,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '066157M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Master of Philosophy (Veterinary Science) is an internationally recognised masters (by research) degree. It is designed to help develop advance...</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 123850,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-philosophy-veterinary-science',
    updated_at = NOW()
WHERE cricos_course_code = '067211B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will specialise you in nuanced international politics, laws & government. Discover course plans, entry requirements & learn how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-international-relations',
    updated_at = NOW()
WHERE cricos_course_code = '068096C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will prepare you to tackle contemporary leadership challenges. Discover course plans, entry requirements & learn how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/executive-master-of-arts',
    updated_at = NOW()
WHERE cricos_course_code = '068099M';
-- Register-only (no study.unimelb match): Master of Engineering
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 208451,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '069275C';
-- Register-only (no study.unimelb match): Graduate Diploma in Commerce (Management)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 0,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '069663B';
-- Register-only (no study.unimelb match): Master of Commerce (Marketing)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 0,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '069664A';
-- Register-only (no study.unimelb match): Graduate Diploma in Commerce (Marketing)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 0,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '069665M';
-- Register-only (no study.unimelb match): Diploma in Mathematical Sciences
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 33824,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '069829G';
-- Register-only (no study.unimelb match): Diploma in Informatics
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44736,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '069831B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course is a pathway into a research degree for those with a coursework masters. Discover course plans, entry requirements and how to apply.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 24928,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with writing 7.0 and no other band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-educational-research',
    updated_at = NOW()
WHERE cricos_course_code = '070381B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements & how to apply to this physiotherapy course, combining your passion for health with a rewarding career.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 231648,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0 with written 7.0 and no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/doctor-of-physiotherapy',
    updated_at = NOW()
WHERE cricos_course_code = '071302J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Find course plans, entry requirements & how to apply to this dental surgery course, embracing a forward-thinking approach in the Asia Pacific region.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 519793,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0 with written 7.0 and no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/doctor-of-dental-surgery',
    updated_at = NOW()
WHERE cricos_course_code = '071303G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements & how to apply to doctor of medicine, offering you a fresh approach to medical training.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 570732,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0 with written 7.0 and no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/doctor-of-medicine',
    updated_at = NOW()
WHERE cricos_course_code = '071304G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Apply for the Doctor of Veterinary Medicine (DVM) course and become a veterinarian or start a career in animal health and welfare.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 399052,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with writing 7.0 and no other band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/doctor-of-veterinary-medicine',
    updated_at = NOW()
WHERE cricos_course_code = '071999D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This professional masters course will develop your biotechnology and professional skills with an industry project in health, agribusiness or tech.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 117600,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-biotechnology',
    updated_at = NOW()
WHERE cricos_course_code = '072809G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements & how to apply to doctor of optometry, pursuing the first OD program in the Southern Hemisphere.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 320192,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5 with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/doctor-of-optometry',
    updated_at = NOW()
WHERE cricos_course_code = '072811B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Explore course plans, entry requirements, careers & how to apply. Design public spaces that address urban challenges in this industry-aligned degree</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 119684,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-design',
    updated_at = NOW()
WHERE cricos_course_code = '072812A';
-- Register-only (no study.unimelb match): Bachelor of Environments (Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 62208,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '073112K';
-- Register-only (no study.unimelb match): Bachelor of Biomedicine (Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 62208,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '073113J';
-- Register-only (no study.unimelb match): Graduate Certificate in Bushfire Planning and Management
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 23664,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '073114G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements & how to apply to this speech pathology course, expanding career horizons with opportunities worldwide.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 146967,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0 with no band less than 7.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-speech-pathology',
    updated_at = NOW()
WHERE cricos_course_code = '073115G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements & how to apply to the Juris Doctor (JD), which leads to admission to the legal profession.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 191928,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.5: with no band less than 7.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/juris-doctor',
    updated_at = NOW()
WHERE cricos_course_code = '073303C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will prepare you for management in the arts, entertainment & cultural industries. Discover course plans, entry requirements & how to apply</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-arts-and-cultural-management',
    updated_at = NOW()
WHERE cricos_course_code = '073305A';
-- Register-only (no study.unimelb match): Master of Evaluation
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 36128,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '073589F';
-- Register-only (no study.unimelb match): Master of Evaluation
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 89675,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '073590B';
-- Register-only (no study.unimelb match): Graduate Certificate in Evaluation
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 18064,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '073591A';
-- Register-only (no study.unimelb match): Master of Design
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 37984,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '074683M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements and how to apply for the Master of Employment and Labour Relations Law.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-employment-and-labour-relations-law',
    updated_at = NOW()
WHERE cricos_course_code = '074995F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn more about the Master of Laws (LLM), which is for law graduates looking to upskill, with a choice of 150+ subjects in 27 legal areas.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-laws',
    updated_at = NOW()
WHERE cricos_course_code = '074996E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain sought-after commercial law expertise with the Master of Commercial Law, part of the world-renowned Melbourne Law Masters (MLM).</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-commercial-law',
    updated_at = NOW()
WHERE cricos_course_code = '074997D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements, and how to apply for the Master of Construction Law.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-construction-law',
    updated_at = NOW()
WHERE cricos_course_code = '074998C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements, and how to apply for the Master of Health and Medical Law.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-health-and-medical-law',
    updated_at = NOW()
WHERE cricos_course_code = '074999B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements, and how to apply to the Master of Intellectual Property Law to become a patent or trademark attorney.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-intellectual-property-law',
    updated_at = NOW()
WHERE cricos_course_code = '075000B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements, and how to apply for the Master of Public and International Law.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-public-and-international-law',
    updated_at = NOW()
WHERE cricos_course_code = '075001A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements & how to apply for the Master of Tax, which focuses on trends and current developments in tax practice.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-tax',
    updated_at = NOW()
WHERE cricos_course_code = '075002M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements & how to apply for the Master of Banking and Finance Law.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-banking-and-finance-law',
    updated_at = NOW()
WHERE cricos_course_code = '075003K';
-- Register-only (no study.unimelb match): Master of Commerce
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 64562,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '075103F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>You will learn from specialists in renewable, thermal and nuclear energy and transport. Analyse energy systems from a technical, commercial and polic</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 97613,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-energy-systems',
    updated_at = NOW()
WHERE cricos_course_code = '075124A';
-- Register-only (no study.unimelb match): Graduate Diploma in Arts and Cultural Management (Advanced)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 48992,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '075125M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements and how to apply for the Graduate Diploma in Employment and Labour Relations Law.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-employment-and-labour-relations-law',
    updated_at = NOW()
WHERE cricos_course_code = '075252D';
-- Register-only (no study.unimelb match): Graduate Certificate in Education
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 24928,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '075300A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements and how to apply to the Graduate Diploma in Human Rights Law.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-human-rights-law',
    updated_at = NOW()
WHERE cricos_course_code = '075314F';
-- Register-only (no study.unimelb match): Graduate Diploma in Communications Law
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 25664,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '075316D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements and how to apply to the Graduate Diploma in International Economic Law.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-international-economic-law',
    updated_at = NOW()
WHERE cricos_course_code = '075317C';
-- Register-only (no study.unimelb match): Graduate Diploma in Sports Law
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '075318B';
-- Register-only (no study.unimelb match): Graduate Diploma in Legal Studies
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '075319A';
-- Register-only (no study.unimelb match): Master of Fine Arts
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 81475,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '075321G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements and how to apply to the Graduate Diploma in Tax.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-tax',
    updated_at = NOW()
WHERE cricos_course_code = '075324D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements and how to apply to the Graduate Diploma in International Tax.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-international-tax',
    updated_at = NOW()
WHERE cricos_course_code = '075325C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements and how to apply to the Graduate Diploma in International Law.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-international-law',
    updated_at = NOW()
WHERE cricos_course_code = '075326B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements and how to apply to the Graduate Diploma in Intellectual Property Law.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-intellectual-property-law',
    updated_at = NOW()
WHERE cricos_course_code = '075327A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements and how to apply to the Graduate Diploma in Health and Medical Law.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-health-and-medical-law',
    updated_at = NOW()
WHERE cricos_course_code = '075329K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements and how to apply to the Graduate Diploma in Government Law.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-government-law',
    updated_at = NOW()
WHERE cricos_course_code = '075330F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements and how to apply to the Graduate Diploma in Dispute Resolution.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-dispute-resolution',
    updated_at = NOW()
WHERE cricos_course_code = '075331E';
-- Register-only (no study.unimelb match): Graduate Diploma in Corporations and Securities Law
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '075332D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements and how to apply for the Graduate Diploma in Construction Law.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-construction-law',
    updated_at = NOW()
WHERE cricos_course_code = '075333C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements and how to apply for the Graduate Diploma in Banking and Finance Law.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-banking-and-finance-law',
    updated_at = NOW()
WHERE cricos_course_code = '075334B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements & how to apply to the Graduate Diploma in Asian Law, covering a range of Asian legal systems & societies</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-asian-law',
    updated_at = NOW()
WHERE cricos_course_code = '075335A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will enable you to launch a successful career in journalism. Discover course plans, entry requirements & learn how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with writing 7.0 and no other band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-journalism',
    updated_at = NOW()
WHERE cricos_course_code = '075464C';
-- Register-only (no study.unimelb match): Bachelor of Fine Arts
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 128724,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '075490A';
-- Register-only (no study.unimelb match): Graduate Diploma in Arts and Community Practice
UPDATE courses SET
    course_duration_per_week = 54,
    offshore_tuition_fee = 31136,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '075491M';
-- Register-only (no study.unimelb match): Graduate Diploma in Film and Television
UPDATE courses SET
    course_duration_per_week = 54,
    offshore_tuition_fee = 46976,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '075492K';
-- Register-only (no study.unimelb match): Master of Arts and Community Practice
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 69076,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '075493J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your individual, professional art practice. Discover course plans, entry requirements & how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 98650,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-contemporary-art',
    updated_at = NOW()
WHERE cricos_course_code = '075494G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop the skills to write, direct and edit your own films and media. Discover course plans, entry requirements & how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 98650,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-film-and-television',
    updated_at = NOW()
WHERE cricos_course_code = '075498D';
-- Register-only (no study.unimelb match): Master of Producing
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 60609,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '075500D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn industry-ready writing skills to tell stories through visual media. Discover course plans, entry requirements & how to apply.</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 72813,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-screenwriting',
    updated_at = NOW()
WHERE cricos_course_code = '075501C';
-- Register-only (no study.unimelb match): Master of Theatre (Writing)
UPDATE courses SET
    course_duration_per_week = 54,
    offshore_tuition_fee = 46976,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '075502B';
-- Register-only (no study.unimelb match): Graduate Diploma in Contemporary Art
UPDATE courses SET
    course_duration_per_week = 54,
    offshore_tuition_fee = 46976,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '075503A';
-- Register-only (no study.unimelb match): Graduate Diploma in Transnational Arts
UPDATE courses SET
    course_duration_per_week = 54,
    offshore_tuition_fee = 0,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '075504M';
-- Register-only (no study.unimelb match): Master of Transnational Arts
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 63829,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '075506J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Find course plans, entry requirements & how to apply to the course. Specialise in dentistry with expert training in various fields.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 294564,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 7.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/doctor-of-clinical-dentistry',
    updated_at = NOW()
WHERE cricos_course_code = '076196K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Specialise in one of 12 streams for knowledge and technical skills with practical knowledge to create positive change in the environment.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 119684,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-environment',
    updated_at = NOW()
WHERE cricos_course_code = '076197J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements & how to apply to the Master of Private Law, which focuses on commercial litigation and transactions.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-private-law',
    updated_at = NOW()
WHERE cricos_course_code = '076224M';
-- Register-only (no study.unimelb match): Master of Music (Opera Performance)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 98650,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '076225K';
-- Register-only (no study.unimelb match): Master of Music (Performance Teaching)
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 72813,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '076226J';
-- Register-only (no study.unimelb match): Master of English in a Global Context
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 56900,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '077472J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course caters equally to those with a limited IT background looking for in-depth technical education and those with strong IT experience.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 134400,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-information-technology',
    updated_at = NOW()
WHERE cricos_course_code = '077475F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements & how to apply to the Graduate Diploma in Environmental Law, covering water law, climate change law etc.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-environmental-law',
    updated_at = NOW()
WHERE cricos_course_code = '077726C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements and how to apply for the Graduate Diploma in Energy and Resources Law.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-energy-and-resources-law',
    updated_at = NOW()
WHERE cricos_course_code = '077727B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements, & how to apply to the Master of Environmental Law, which covers water law, climate change law and more.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-law',
    updated_at = NOW()
WHERE cricos_course_code = '077728A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements and how to apply for the Master of Energy and Resources Law.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-energy-and-resources-law',
    updated_at = NOW()
WHERE cricos_course_code = '077729M';
-- Register-only (no study.unimelb match): Master of Information Technology
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 41344,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '077764G';
-- Register-only (no study.unimelb match): Master of Information Technology
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 68222,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '077766F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course gives you a theoretical and practical foundation to launch your career. Discover course plans, entry requirements & how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-linguistics',
    updated_at = NOW()
WHERE cricos_course_code = '077928D';
-- Register-only (no study.unimelb match): Graduate Certificate in Information Systems
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 32000,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '078389G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will equip you to apply positive psychology principles in your professional & personal life. Learn more and discover how to apply.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 72000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with writing 7.0 and no other band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-positive-psychology',
    updated_at = NOW()
WHERE cricos_course_code = '079279E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Find course structure, entry requirements & how to apply to this biomedical science course, collaborating with experts in transformative research.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 119684,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-biomedical-science',
    updated_at = NOW()
WHERE cricos_course_code = '079405D';
-- Register-only (no study.unimelb match): Master of Psychiatry
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 112540,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '079406C';
-- Register-only (no study.unimelb match): Master of Research (Dental Science)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 83750,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '079645K';
-- Register-only (no study.unimelb match): Master of Research (MDHS)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 65050,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '079646J';
-- Register-only (no study.unimelb match): Master of Research (Psychological Sciences)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 83750,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '079647G';
-- Register-only (no study.unimelb match): Master of Research (Population and Global Health)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 83750,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '079649F';
-- Register-only (no study.unimelb match): Master of Research (Health Sciences)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 83750,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '079650B';
-- Register-only (no study.unimelb match): Master of Research (Medicine)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 83750,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '079651A';
-- Register-only (no study.unimelb match): Master of Enterprise
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 72760,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '080338M';
-- Register-only (no study.unimelb match): Master of Arts (Thesis)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 107050,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '080604J';
-- Register-only (no study.unimelb match): Master of Arts (Advanced Seminar and Shorter Thesis)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 107050,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '080605G';
-- Register-only (no study.unimelb match): Master of Commerce (Accounting)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 0,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '080606G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover this specialist course, which will equip you with effective management skills for the global business sector.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-international-business',
    updated_at = NOW()
WHERE cricos_course_code = '080608E';
-- Register-only (no study.unimelb match): Graduate Diploma in Built Environments (Advanced)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 57984,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '080610M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements, careers & how to apply. Earn qualifications or create a path to future study in this flexible 1-year degree</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 57984,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-built-environments',
    updated_at = NOW()
WHERE cricos_course_code = '080611K';
-- Register-only (no study.unimelb match): Master of Production Design for Screen
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 71176,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '081322M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements & how to apply to this course, to advance your actuarial, mathematics and modelling knowledge skills.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-actuarial-science',
    updated_at = NOW()
WHERE cricos_course_code = '081745K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Explore course plans, entry requirements, careers & how to apply. Specialise in heritage policy & conservation in this 1-year industry-aligned degree</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 56992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-and-cultural-heritage',
    updated_at = NOW()
WHERE cricos_course_code = '082253M';
-- Register-only (no study.unimelb match): Graduate Certificate in Urban and Cultural Heritage
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 28992,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '082254K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Master of Food and Packaging Innovation is an advanced interdisciplinary degree that combines food science, entrepreneurship and innovation in ...</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 121767,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-food-and-packaging-innovation',
    updated_at = NOW()
WHERE cricos_course_code = '083118K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements & how to apply to this course, a flexible, shorter graduate qualification in economics.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-economics',
    updated_at = NOW()
WHERE cricos_course_code = '083552C';
-- Register-only (no study.unimelb match): Master of Business Analytics
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 91488,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '084058J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course focuses on the impact of evidence-based approaches to the leadership of teaching and learning. Learn more and discover how to apply.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 52000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with writing 7.0 and no other band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-instructional-leadership',
    updated_at = NOW()
WHERE cricos_course_code = '084959E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In the Master of Ag Sciences, you''ll develop your knowledge of the fundamental and applied science of agriculture to contribute to a healthier world.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 115450,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-agricultural-sciences',
    updated_at = NOW()
WHERE cricos_course_code = '085097E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover the science of sustainable and profitable food and fibre production with this graduate diploma from Australia''s number 2 university for ag...</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 54976,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-agricultural-sciences',
    updated_at = NOW()
WHERE cricos_course_code = '085100D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover the science of sustainable and profitable food and fibre production with this graduate certificate from Australia''s number 2 university fo...</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 27488,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-agricultural-sciences',
    updated_at = NOW()
WHERE cricos_course_code = '085101C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will qualify you in the merging sectors of marketing and communications. Discover course plans, entry requirements & learn how to apply</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-marketing-communications',
    updated_at = NOW()
WHERE cricos_course_code = '085102B';
-- Register-only (no study.unimelb match): Master of Management (Accounting and Finance)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '085103A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will help you build the skills required to support specialist learning needs. Discover course plans, entry requirements and how to apply.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 48992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with writing 7.0 and no other band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-learning-intervention',
    updated_at = NOW()
WHERE cricos_course_code = '085104M';
-- Register-only (no study.unimelb match): Graduate Certificate in Learning Intervention
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 16688,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '085105K';
-- Register-only (no study.unimelb match): Graduate Certificate in Science
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 23700,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '085109F';
-- Register-only (no study.unimelb match): Master of Advanced Nursing
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 68200,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '085339C';
-- Register-only (no study.unimelb match): Master of Design for Performance
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 71176,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '085429A';
-- Register-only (no study.unimelb match): Master of Dance
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 52948,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '085430G';
-- Register-only (no study.unimelb match): Master of Theatre (Dramaturgy)
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 72813,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '085431G';
-- Register-only (no study.unimelb match): Master of Theatre (Directing)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 98650,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '085432F';
-- Register-only (no study.unimelb match): Study Abroad (Postgraduate 3)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 26000,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '085608J';
-- Register-only (no study.unimelb match): Graduate Diploma in Science
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 47874,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '085609G';
-- Register-only (no study.unimelb match): Graduate Certificate in Journalism (Advanced)
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 24496,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '085948M';
-- Register-only (no study.unimelb match): Graduate Certificate in Publishing and Communications (Advanced)
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 24496,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '085949K';
-- Register-only (no study.unimelb match): Graduate Certificate in Science (Advanced)
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '085950F';
-- Register-only (no study.unimelb match): Graduate Diploma in Journalism (Advanced)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 48992,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '085951E';
-- Register-only (no study.unimelb match): Graduate Diploma in Publishing and Communication (Advanced)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 48992,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '085952D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements, and how to apply to the Master of Human Rights Law.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-human-rights-law',
    updated_at = NOW()
WHERE cricos_course_code = '088072A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Explore course plans, entry requirements & how to apply to this Biostatistics course, enabling you to lead data-driven policies for population health.</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 97613,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-biostatistics',
    updated_at = NOW()
WHERE cricos_course_code = '088478A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Find course plans, entry requirements & how to apply to the Graduate Diploma in Biostatistics.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 62976,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-biostatistics',
    updated_at = NOW()
WHERE cricos_course_code = '088479M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Graduate Diploma in Veterinary Professional Leadership and Management will help advance veterinarian or a veterinary students in specialist tra...</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60640,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-veterinary-professional-leadership-and-management',
    updated_at = NOW()
WHERE cricos_course_code = '088481F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Take intensive subjects and specialise in economic geology, mining and resources, energy, the geotechnical industry or environmental geoscience.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-geoscience',
    updated_at = NOW()
WHERE cricos_course_code = '089358A';
-- Register-only (no study.unimelb match): Master of Business Administration/Master of Marketing
UPDATE courses SET
    course_duration_per_week = 102,
    offshore_tuition_fee = 101470,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '089359M';
-- Register-only (no study.unimelb match): Master of Entrepreneurship
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 52512,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '089646D';
-- Register-only (no study.unimelb match): Graduate Certificate in Entrepreneurship
UPDATE courses SET
    course_duration_per_week = 16,
    offshore_tuition_fee = 16752,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '089647C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Explore course plans, entry requirements, career paths & how to apply. Gain in-demand skills in architecture and engineering in this accredited degree</p>',
    course_duration_per_week = 182,
    offshore_tuition_fee = 306221,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-architectural-engineering',
    updated_at = NOW()
WHERE cricos_course_code = '089660F';
-- Register-only (no study.unimelb match): Master of Commerce (Actuarial Science)
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 94538,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '089805E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Bachelor of Design will teach you to be creative and innovative through studios, site visits, field trips and interactions with industry.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 189352,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5 (with no band less than 6.0)<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-design',
    updated_at = NOW()
WHERE cricos_course_code = '090744C';
-- Register-only (no study.unimelb match): Master of Philosophy (Biomedical Science)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '091556K';
-- Register-only (no study.unimelb match): Master of Management (Human Resources)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '092726M';
-- Register-only (no study.unimelb match): Master of Applied Econometrics
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '092759B';
-- Register-only (no study.unimelb match): Graduate Diploma in Applied Econometrics
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '092760J';
-- Register-only (no study.unimelb match): Master of Commerce (Decision, Risk and Financial Sciences)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '092761G';
-- Register-only (no study.unimelb match): Master of Commerce (Finance)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '092762G';
-- Register-only (no study.unimelb match): Master of Commerce (Accounting)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '092763F';
-- Register-only (no study.unimelb match): Graduate Diploma in Commerce (Accounting)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '092764E';
-- Register-only (no study.unimelb match): Graduate Diploma in Commerce (Finance)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '092765D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements, how to apply to this course, and gain technical and analytical skills to manage complex data collections.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 121767,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-data-science',
    updated_at = NOW()
WHERE cricos_course_code = '092791B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Specialise in physical, human or integrated geography with the opportunity for research and field experience in Australia and overseas.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-geography',
    updated_at = NOW()
WHERE cricos_course_code = '092792A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Solve environmental challenges as you learn technical skills and work with industry. Learn about air, water and land contamination and climate change.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 126000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-science',
    updated_at = NOW()
WHERE cricos_course_code = '092793M';
-- Register-only (no study.unimelb match): Master of Teaching (Early Childhood and Primary)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 137150,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093002F';
-- Register-only (no study.unimelb match): Graduate Diploma in Pedagogy
UPDATE courses SET
    course_duration_per_week = 14,
    offshore_tuition_fee = 43133,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '093003E';
-- Register-only (no study.unimelb match): Master of Teaching (Secondary)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 109200,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093406G';
-- Register-only (no study.unimelb match): Master of Teaching (Early Childhood)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 109200,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093410A';
-- Register-only (no study.unimelb match): Master of Teaching (Primary)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 109200,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093411M';
-- Register-only (no study.unimelb match): Graduate Diploma in Educational Studies
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 49856,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093417E';
-- Register-only (no study.unimelb match): Master of Fine Arts (Dance)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 77801,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093574C';
-- Register-only (no study.unimelb match): Master of Fine Arts (Film and Television)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 77801,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093575B';
-- Register-only (no study.unimelb match): Master of Fine Arts (Indigenous Arts and Culture)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 77801,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093576A';
-- Register-only (no study.unimelb match): Master of Fine Arts (Music Theatre)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 77801,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093577M';
-- Register-only (no study.unimelb match): Master of Fine Arts (Interdisciplinary Arts Practice)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 98650,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093578K';
-- Register-only (no study.unimelb match): Master of Fine Arts (Production)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 98650,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093579J';
-- Register-only (no study.unimelb match): Master of Fine Arts (Theatre)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 81475,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093580E';
-- Register-only (no study.unimelb match): Master of Fine Arts (Visual Art)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 77801,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093581D';
-- Register-only (no study.unimelb match): Bachelor of Fine Arts (Animation)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 128352,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093582C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Bachelor of Fine Arts Dance leads to jobs such as dancer, artistic director, choreographer, community dance artist, contemporary dancer</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 128352,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5 (with no band less than 6.0)<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/undergraduate/bachelor-of-fine-arts-dance',
    updated_at = NOW()
WHERE cricos_course_code = '093583B';
-- Register-only (no study.unimelb match): Bachelor of Fine Arts (Film and Television)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 128984,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093584A';
-- Register-only (no study.unimelb match): Bachelor of Fine Arts (Music Theatre)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 110016,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093585M';
-- Register-only (no study.unimelb match): Bachelor of Fine Arts (Production)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 128724,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093586K';
-- Register-only (no study.unimelb match): Bachelor of Fine Arts (Screenwriting)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 128724,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093587J';
-- Register-only (no study.unimelb match): Bachelor of Fine Arts (Theatre Practice)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 110016,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093588G';
-- Register-only (no study.unimelb match): Bachelor of Fine Arts (Visual Art)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 131432,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093589G';
-- Register-only (no study.unimelb match): Graduate Certificate in Professional Skills for Scientists
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 29696,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '093590C';
-- Register-only (no study.unimelb match): Study Abroad - Research (Fee Band 1)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 34556,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '094124K';
-- Register-only (no study.unimelb match): Study Abroad - Research (Fee Band 2)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 42916,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '094125J';
-- Register-only (no study.unimelb match): Study Abroad - Research (Fee Band 3)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 48510,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '094126G';
-- Register-only (no study.unimelb match): Exchange - Research
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 0,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '094127G';
-- Register-only (no study.unimelb match): Master of Science (Bioinformatics)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '094592D';
-- Register-only (no study.unimelb match): Master of Science (Biosciences)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '094593C';
-- Register-only (no study.unimelb match): Master of Science (Chemistry)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '094594B';
-- Register-only (no study.unimelb match): Master of Science (Computer Science)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 134400,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '094595A';
-- Register-only (no study.unimelb match): Master of Science (Earth Sciences)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '094596M';
-- Register-only (no study.unimelb match): Master of Science (Ecosystem Science)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 104632,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '094597K';
-- Register-only (no study.unimelb match): Master of Science (Epidemiology)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '094598J';
-- Register-only (no study.unimelb match): Master of Science (Mathematics and Statistics)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '094599G';
-- Register-only (no study.unimelb match): Master of Science (Physics)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '094600J';
-- Register-only (no study.unimelb match): Master of Music (Orchestral Performance)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 98650,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '094859D';
-- Register-only (no study.unimelb match): Bachelor of Fine Arts (Theatre)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 130636,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '094860M';
-- Register-only (no study.unimelb match): Bachelor of Fine Arts (Acting)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 128908,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '094861K';
-- Register-only (no study.unimelb match): Graduate Diploma in Orchestral Studies
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 46976,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '094862J';
-- Register-only (no study.unimelb match): Master of Commerce (Marketing)
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 69881,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '094863G';
-- Register-only (no study.unimelb match): Master of Commerce (Management)
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 69881,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '094864G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course offers relevant professional learning for educators in a broad range of fields related to education. Learn more & discover how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 104967,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-education',
    updated_at = NOW()
WHERE cricos_course_code = '095802B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will allow you to become a language teacher in schools, language centres and universities around the world. Learn more and discover how to</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with writing 7.0 and no other band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-modern-languages-education',
    updated_at = NOW()
WHERE cricos_course_code = '095990D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course provides recognition as an accredited language teacher for students eligible for VIT registration. Learn more and discover how to apply.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 24928,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with writing 7.0 and no other band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-modern-languages-education',
    updated_at = NOW()
WHERE cricos_course_code = '095991C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will instruct you in teaching English as an additional language. Discover course plans, entry requirements and how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-tesol',
    updated_at = NOW()
WHERE cricos_course_code = '095992B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This TESOL course will qualify you to teach English as an additional language. Discover course plans, entry requirements and how to apply.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 24496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with writing 7.0 and no other band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-tesol',
    updated_at = NOW()
WHERE cricos_course_code = '095993A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop skills in computer science and statistics to solve real-world problems. Build analytic and technical skills to manage large data collections</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 61984,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-foundational-data-science',
    updated_at = NOW()
WHERE cricos_course_code = '095994M';
-- Register-only (no study.unimelb match): Master of Commerce (Economics)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '096133D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will enable you to launch a career in international journalism. Discover course plans, entry requirements & how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with writing 6.5 and no other band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-international-journalism',
    updated_at = NOW()
WHERE cricos_course_code = '096334F';
-- Register-only (no study.unimelb match): Graduate Certificate in Port Engineering
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 24160,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '096346B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Find course plans, entry requirements & how to apply to the Graduate Certificate in Genomics and Health.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 34000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-genomics-and-health',
    updated_at = NOW()
WHERE cricos_course_code = '096347A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Find course plans, entry requirements & how to apply to the Graduate Diploma in Genomics and Health.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 68000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-genomics-and-health',
    updated_at = NOW()
WHERE cricos_course_code = '096348M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Find course plans, entry requirements & how to apply to Master of Genomics and Health, the first course of its kind to be offered in Australia.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 142800,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0 with written 7.0 and no band less than 6.5<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-genomics-and-health',
    updated_at = NOW()
WHERE cricos_course_code = '096349K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Find course plans, entry requirements & how to apply to the course. Master applied psychology skills and knowledge for diverse career paths.</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 97613,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-applied-psychology',
    updated_at = NOW()
WHERE cricos_course_code = '096378E';
-- Register-only (no study.unimelb match): Bachelor of Oral Health (Degree with Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 54368,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '097031B';
-- Register-only (no study.unimelb match): Graduate Diploma in Enterprise (Exit Award)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 45824,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '098270A';
-- Register-only (no study.unimelb match): Graduate Certificate in Supply Chain Management (Exit Award)
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 22016,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '098271M';
-- Register-only (no study.unimelb match): Graduate Diploma in Supply Chain Management (Exit Award)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 45824,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '098272K';
-- Register-only (no study.unimelb match): Master of Industrial Research (Chemistry)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 123850,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '098316C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Prepare for a career in forest, landscape, ecosystem, conservation and resource management to build practical and professional skills</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-ecosystem-management-and-conservation',
    updated_at = NOW()
WHERE cricos_course_code = '098317B';
-- Register-only (no study.unimelb match): Master of Commerce (Management)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '098522G';
-- Register-only (no study.unimelb match): Master of Commerce (Marketing)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '098523G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>A Doctor of Philosophy (PhD) award for original research undertaken in the area of fine arts or music. Discover entry requirements & how to apply.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 218016,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/doctor-of-philosophy-fine-arts-and-music',
    updated_at = NOW()
WHERE cricos_course_code = '099323G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your research skills and contribute to understandings of contemporary artistic practice and theories of arts and culture.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 98650,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-fine-arts',
    updated_at = NOW()
WHERE cricos_course_code = '099324F';
-- Register-only (no study.unimelb match): Master of Music (Research)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 98650,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '099325E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Acquire technical expertise in computer science, including: programming paradigms; and an understanding of the software development lifecycle.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 64000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-computer-science',
    updated_at = NOW()
WHERE cricos_course_code = '099421E';
-- Register-only (no study.unimelb match): Graduate Certificate in Computer Science
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 32000,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '099422D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Industrial engineers ensure a company’s competitiveness from design and production to business strategy by maximising efficiency and effectiveness in</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 132250,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-industrial-engineering',
    updated_at = NOW()
WHERE cricos_course_code = '102808M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover this specialist course, designed to provide a leading-edge theoretical and practical foundation in the domain of Digital Marketing.</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 94538,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-digital-marketing',
    updated_at = NOW()
WHERE cricos_course_code = '103161D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will enable you to launch a career as a professional translator or interpreter. Discover course plans, entry requirements & how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-translation-and-interpreting',
    updated_at = NOW()
WHERE cricos_course_code = '103338F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your design skills and gain the practical experience to pursue a career in stage or screen production design, including film, television, thea</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 98650,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-design-and-production',
    updated_at = NOW()
WHERE cricos_course_code = '103430K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Designed for graduates interested in gaining a short qualification in languages. Discover course plans, entry requirements & how to apply.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 23168,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-language-and-cultural-literacy',
    updated_at = NOW()
WHERE cricos_course_code = '104600M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements, careers & how to apply. Future-proof your expertise in the built environment industry with a double degree</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 264500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-architecture-master-of-construction-management',
    updated_at = NOW()
WHERE cricos_course_code = '105512C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements, careers & how to apply. Future-proof your expertise in the built environment industry with a double degree.</p>',
    course_duration_per_week = 182,
    offshore_tuition_fee = 226572,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-architecture-master-of-urban-cultural-heritage',
    updated_at = NOW()
WHERE cricos_course_code = '105513B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements, careers & how to apply. Future-proof your expertise in the built environment industry with a double degree.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 264500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-architecture-master-of-property',
    updated_at = NOW()
WHERE cricos_course_code = '105514A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements, careers & how to apply. Future-proof your expertise in the built environment industry with a double degree.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 264500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-architecture-master-of-urban-design',
    updated_at = NOW()
WHERE cricos_course_code = '105515M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements, careers & how to apply. Future-proof your expertise in the built environment industry with a double degree.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 264500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-architecture-master-of-urban-planning',
    updated_at = NOW()
WHERE cricos_course_code = '105516K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements, careers & how to apply. Future-proof your expertise in the built environment industry with a double degree.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 264500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-construction-management-master-of-property',
    updated_at = NOW()
WHERE cricos_course_code = '105517J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements, careers & how to apply. Future-proof your expertise in the built environment industry with a double degree.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 264500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-property-master-of-urban-planning',
    updated_at = NOW()
WHERE cricos_course_code = '105518H';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements, careers & how to apply. Future-proof your expertise in the built environment industry with a double degree.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 188644,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-urban-planning-master-of-urban-design',
    updated_at = NOW()
WHERE cricos_course_code = '105519G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements, careers & how to apply. Future-proof your expertise in the built environment industry with a double degree.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 264500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-architecture-master-of-landscape-architecture',
    updated_at = NOW()
WHERE cricos_course_code = '105520C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements, careers & how to apply. Future-proof your expertise in the built environment industry with a double degree.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 264500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-landscape-architecture-master-of-urban-design',
    updated_at = NOW()
WHERE cricos_course_code = '105521B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements, careers & how to apply. Future-proof your expertise in the built environment industry with a double degree.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 264500,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-landscape-architecture-master-of-urban-planning',
    updated_at = NOW()
WHERE cricos_course_code = '105522A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Engage in practice-based research, dance theory and creative technologies. Discover course plans, entry requirements & how to apply.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 98650,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-dance',
    updated_at = NOW()
WHERE cricos_course_code = '105697M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Apply biomedical engineering skills to medical treatments, instruments and machines, focusing on the design and operation of devices and processes.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 208451,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-biomedical-engineering',
    updated_at = NOW()
WHERE cricos_course_code = '106103A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn unique chemical and engineering skills to help design and implement industrial-scale processes to convert raw and waste materials into products.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 208451,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-chemical-engineering',
    updated_at = NOW()
WHERE cricos_course_code = '106104M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain advanced civil engineering skills, guided by experts in infrastructure design, water resource management and transport engineering.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 208451,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-civil-engineering',
    updated_at = NOW()
WHERE cricos_course_code = '106105K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Build and improve our power and telecommunications systems and develop future electronic devices.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 208451,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-electrical-engineering',
    updated_at = NOW()
WHERE cricos_course_code = '106106J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Engineer solutions to the challenges facing our world in climate change, water resources, energy and bushfire management.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 208451,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-engineering',
    updated_at = NOW()
WHERE cricos_course_code = '106107H';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Mechanical engineers work in a range of fields: infrastructure and construction, aerostructures, biotechnology, manufacturing, or mining and resources</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 208451,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-mechanical-engineering',
    updated_at = NOW()
WHERE cricos_course_code = '106108G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop automation and advanced manufacturing technologies. Harness computer controls in areas such as robotics, vehicles and CNC machines.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 208451,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-mechatronics-engineering',
    updated_at = NOW()
WHERE cricos_course_code = '106109F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn best practice for every stage of the software development cycle from design and engineering to deployment.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 208451,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-software-engineering',
    updated_at = NOW()
WHERE cricos_course_code = '106110B';
-- Register-only (no study.unimelb match): Master of Spatial Engineering
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 191928,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '106111A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Designed for qualified engineers who are looking to change their field of work or advance in their careers.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 62976,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-environmental-systems-engineering',
    updated_at = NOW()
WHERE cricos_course_code = '106187C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements & how to apply to this course, and build the skillset needed to work on solutions to climate change.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 126000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-climate-science',
    updated_at = NOW()
WHERE cricos_course_code = '106786B';
-- Register-only (no study.unimelb match): Graduate Diploma in Applied Econometrics
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 46752,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '107110E';
-- Register-only (no study.unimelb match): Master of Applied Econometrics
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 94538,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '107111D';
-- Register-only (no study.unimelb match): Master of Applied Econometrics (Enhanced)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '107112C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover how the Graduate Certificate in Entrepreneurship can empower you to drive impactful change, both in organisations or with your own business.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 30496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-entrepreneurship',
    updated_at = NOW()
WHERE cricos_course_code = '107113B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course plans, entry requirements & how to apply to this course, providing you with the skillset needed to become a successful entrepreneur.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 60992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-entrepreneurship',
    updated_at = NOW()
WHERE cricos_course_code = '107114A';
-- Register-only (no study.unimelb match): Master of Entrepreneurship (Enhanced)
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 94538,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '107115M';
-- Register-only (no study.unimelb match): Bachelor of Design (Degree with Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 56704,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '107132K';
-- Register-only (no study.unimelb match): Master of Teaching (Early Childhood and Primary)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 122850,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '107556H';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop skills to connect the physical and digital worlds combining skills in architecture, design, construction and engineering.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 208451,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-digital-infrastructure-engineering',
    updated_at = NOW()
WHERE cricos_course_code = '108720D';
-- Register-only (no study.unimelb match): Master of Screen Producing
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 90250,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '110761K';
-- Register-only (no study.unimelb match): Master of Biostatistics (Enhanced)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 132250,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '111031C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This program is designed to recognise and activate Indigenous knowledge and deepen engagement and reciprocal learning with Indigenous communities.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 273708,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/doctor-of-philosophy-indigenous-knowledge',
    updated_at = NOW()
WHERE cricos_course_code = '111523E';
-- Register-only (no study.unimelb match): Bachelor of Science Advanced (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 142979,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '112780B';
-- Register-only (no study.unimelb match): Exchange CASA
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 26000,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '112851C';
-- Register-only (no study.unimelb match): Study Abroad CASA
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 26000,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '112852B';
-- Register-only (no study.unimelb match): Bachelor of Medical Science (Degree with Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 64032,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '113001D';
-- Register-only (no study.unimelb match): Master of Social Change Leadership
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 36000,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '113015J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Engage with the political, economic, social and cultural landscape of contemporary China.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 102884,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-contemporary-chinese-studies',
    updated_at = NOW()
WHERE cricos_course_code = '114286M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements & how to apply to this clinical dentistry course. Stay ahead with prosthodontics advancements.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 88992,
    onshore_tuition_fee = NULL,
    enrolment_fee = 5150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 7.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-clinical-dentistry',
    updated_at = NOW()
WHERE cricos_course_code = '114365A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Want to bridge diverse cultures and open doors to international cooperation? Our Graduate Certificate in Translation can prepare you for an excitin...</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 24496,
    onshore_tuition_fee = NULL,
    enrolment_fee = 150,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-translation',
    updated_at = NOW()
WHERE cricos_course_code = '114388E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover course structure, entry requirements & how to apply to this course, unlocking leadership roles in advanced nursing practice & public health.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 74189,
    onshore_tuition_fee = NULL,
    enrolment_fee = 280,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-advanced-nursing-practice-master-of-public-health',
    updated_at = NOW()
WHERE cricos_course_code = '114963A';
-- Register-only (no study.unimelb match): Diploma in Computing
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 53248,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '115435F';
-- Register-only (no study.unimelb match): Master of Management (Entrepreneurship and Innovation)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '116966D';
-- Register-only (no study.unimelb match): Master of Management (Supply Chain Management)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 128084,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '116967C';
-- Register-only (no study.unimelb match): Master of Psychology (Clinical Neuropsychology)/Doctor of Philosophy
UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 341886,
    enrolment_fee = 0,
    updated_at = NOW()
WHERE cricos_course_code = '118471M';
-- Register-only (no study.unimelb match): Graduate Diploma in Medical Studies
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 129948,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '119129F';
-- Register-only (no study.unimelb match): Master of Medical Studies (Exit Only)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 259896,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '119130B';
-- Register-only (no study.unimelb match): Master of Medical Studies (Enhanced)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 389844,
    enrolment_fee = 150,
    updated_at = NOW()
WHERE cricos_course_code = '119131A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Find course plans, entry requirements & more for the dual-delivery Graduate Certificate in Public Health. Meet a diverse cohort to improve healthcare</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 35488,
    onshore_tuition_fee = NULL,
    enrolment_fee = 154,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 6.5: with no band less than 6.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-certificate-in-public-health',
    updated_at = NOW()
WHERE cricos_course_code = '120129G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study to build your career in early childhood educationBecome a highly qualified early childhood teacher with the University of Melbourne''s Graduat...</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 52000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 154,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><h5>English language requirements</h5>IELTS 7.0: with no band less than 7.0<br/>',
    apply_form = 'https://study.unimelb.edu.au/find/courses/graduate/graduate-diploma-in-early-childhood-teaching',
    updated_at = NOW()
WHERE cricos_course_code = '120163E';
-- Register-only (no study.unimelb match): Master of Theatre
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 106512,
    enrolment_fee = 154,
    updated_at = NOW()
WHERE cricos_course_code = '120886C';
