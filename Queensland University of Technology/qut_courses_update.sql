-- UPDATE provider institution
UPDATE provider_institution SET
    intake_date = 'January, February, March, April, May, June, July, August, September, October, November, December',
    updated_at = NOW()
WHERE cricos_provider_code = '00213J';

-- ⏭️ Skipped (no CRICOS): Graduate Certificate in Smart Transport and Mobility | https://www.qut.edu.au/courses/graduate-certificate-in-smart-transport-and-mobility
-- ⏭️ Skipped (no CRICOS): Graduate Certificate in Renewable Energy Systems | https://www.qut.edu.au/courses/graduate-certificate-in-renewable-energy-systems
-- ⏭️ Skipped (no CRICOS): Diploma in Esports/Bachelor of Business | https://www.qut.edu.au/courses/diploma-in-esports-bachelor-of-business
-- ⏭️ Skipped (no CRICOS): Diploma in Esports/Bachelor of Information Technology | https://www.qut.edu.au/courses/diploma-in-esports-bachelor-of-information-technology
-- ⏭️ Skipped (no CRICOS): Graduate Certificate in Education (Indigenous Australian Education for Teachers) | https://www.qut.edu.au/courses/graduate-certificate-in-education-indigenous-australian-education-for-teachers
-- ⏭️ Skipped (no CRICOS): Graduate Certificate in Education (Leading Early Childhood Education) | https://www.qut.edu.au/courses/graduate-certificate-in-education-leading-early-childhood-education
-- ⏭️ Skipped (no CRICOS): Graduate Certificate in Education (Teaching English to Speakers of Other Languages) | https://www.qut.edu.au/courses/graduate-certificate-in-education-tesol
-- ⏭️ Skipped (no CRICOS): Graduate Certificate in Education - Choice of Units | https://www.qut.edu.au/courses/graduate-certificate-in-education-choice-of-units
-- ⏭️ Skipped (no CRICOS): Master of Education (School Guidance and Counselling) | https://www.qut.edu.au/courses/master-of-education-school-guidance-and-counselling
-- ⏭️ Skipped (no CRICOS): Undergraduate Certificate (Nursing) | https://www.qut.edu.au/courses/undergraduate-certificate-nursing
-- ⏭️ Skipped (no CRICOS): Diploma in Creative Industries/Bachelor of Design - International | https://www.qut.edu.au/courses/diploma-in-creative-industries-bachelor-of-design-international
-- ⏭️ Skipped (no CRICOS): Master of Diagnostic Genomics | https://www.qut.edu.au/courses/master-of-diagnostic-genomics
-- ⏭️ Skipped (no CRICOS): Master of Nurse Practitioner | https://www.qut.edu.au/courses/master-of-nurse-practitioner
-- ⏭️ Skipped (no CRICOS): University Preparation Program | https://www.qut.edu.au/courses/university-preparation-program
-- ⏭️ Skipped (no CRICOS): Bachelor of Radiation Therapy | https://www.qut.edu.au/courses/bachelor-of-radiation-therapy

UPDATE courses SET
    course_description = '<p>If you’re an outstanding graduate and aspiring researcher, you may be eligible to apply for a scholarship in one of our scholarship rounds.</p><p> <a href="https://www.qut.edu.au/research/study-with-us/scholarships/applying-for-scholarships"> Applying for a research scholarship </a> </p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 112800,
    onshore_tuition_fee = 105600,
    entry_requirements = '<p>International applicants are encouraged to contact the course coordinator before submitting their application.</p><p>International applicants are encouraged to contact the course coordinator before submitting their application.</p>',
    apply_form = 'https://www.qut.edu.au/courses/doctor-of-education',
    updated_at = NOW()
WHERE cricos_course_code = '015023C';
-- 5 course pages share CRICOS 113182E
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Launch your career in the exciting fields of construction, quantity surveying, urban planning, interior design, and landscape architecture with Queensland’s most in-demand built environment degree. Gain hands-on experience with leaders in the industry, build an impressive portfolio, and make connections through real-world work placements.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 173200,
    onshore_tuition_fee = 41600,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-built-environment-honours-interior-design',
    updated_at = NOW()
WHERE cricos_course_code = '113182E';
-- 3 course pages share CRICOS 116308E
--   conflicting onshore_tuition_fee: [12700, 38100, 50800] -> kept 50800
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Develop strong foundational architectural skills and knowledge to help you make a successful transition to QUT’s undergraduate degrees in architectural studies and built environment with majors in interior design and landscape architecture. </p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 40700,
    onshore_tuition_fee = 50800,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/diploma-in-architectural-studies-bachelor-of-built-environment-honours',
    updated_at = NOW()
WHERE cricos_course_code = '116308E';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Accelerate your study and position yourself for future leadership roles across the built environment and project management sectors.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 215000,
    onshore_tuition_fee = 52500,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-built-environment-honours-master-of-project-management',
    updated_at = NOW()
WHERE cricos_course_code = '116499D';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Gain management qualifications with advanced engineering skills and knowledge. Study quality control, organisational infrastructure management, and development of decision support systems.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 48000,
    onshore_tuition_fee = 33600,
    apply_form = 'https://www.qut.edu.au/courses/master-of-engineering-management',
    updated_at = NOW()
WHERE cricos_course_code = '006368G';
-- 2 course pages share CRICOS 120798C
--   conflicting offshore_tuition_fee: [103000, 200000] -> kept 200000
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Excel in your accounting career, from senior leadership roles to launching your own professional services firm, with the QUT Master of Professional Accounting. </p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 200000,
    entry_requirements = '<p>As this is a new course, the threshold will be available mid-January 2027.</p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-nutrition-science-master-of-nutrition-and-dietetics',
    updated_at = NOW()
WHERE cricos_course_code = '120798C';
-- 2 course pages share CRICOS 081618F
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Learn the foundational business skills from real-world teaching staff to enter into the second year of a QUT Bachelor of Business degree.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 27000,
    onshore_tuition_fee = 17400,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/diploma-in-business',
    updated_at = NOW()
WHERE cricos_course_code = '081618F';
-- 10 course pages share CRICOS 009038B
UPDATE courses SET
    course_description = '<p>''''The best aspect of undertaking honours in accountancy is the extensive range of knowledge that you gain... Also it’s nice to know that you’ve made a contribution to the accountancy arena.''''</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 49400,
    onshore_tuition_fee = 17400,
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-business-honours-entrepreneurship-and-innovation',
    updated_at = NOW()
WHERE cricos_course_code = '009038B';
-- 11 course pages share CRICOS 0101552
--   conflicting offshore_tuition_fee: [12450, 12600, 18900, 20200, 22200, 24900] -> kept 24900
--   conflicting onshore_tuition_fee: [2184, 2400, 2500, 4000, 4800, 13900, 16200] -> kept 4800
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Unique to QUT. Gain advanced knowledge of using and prescribing medicines to treat podiatric conditions. One-year, part-time study.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 24900,
    onshore_tuition_fee = 4800,
    entry_requirements = '<p>Semester 1 entry can only be studied part-time. Semester 2 entry is full-time only.</p>',
    apply_form = 'https://www.qut.edu.au/courses/graduate-certificate-in-water-modelling',
    updated_at = NOW()
WHERE cricos_course_code = '0101552';
-- 2 course pages share CRICOS 0101676
--   conflicting offshore_tuition_fee: [89000, 133500] -> kept 133500
--   conflicting onshore_tuition_fee: [19000, 28500] -> kept 28500
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>If you have a completed degree in health or medical science, we’ll recognise your prior learning so you can complete your paramedic science degree sooner.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 133500,
    onshore_tuition_fee = 28500,
    entry_requirements = '<p>Note: Admission to course is based on prior study in addition to a rank. Please refer to Entry Requirements.</p><p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-paramedic-science',
    updated_at = NOW()
WHERE cricos_course_code = '0101676';
-- 4 course pages share CRICOS 009034F
--   conflicting offshore_tuition_fee: [31300, 42200, 44500] -> kept 44500
--   conflicting onshore_tuition_fee: [10600, 16500, 31200, 32300] -> kept 32300
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Learn from experts in the field of medical sonography. Develop your skills using ultrasound simulators, interactive resources, and within intensive learning blocks.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 44500,
    onshore_tuition_fee = 32300,
    entry_requirements = '<p>This program is not available to Australian government student visa holders.</p><p>This program is not available to Australian government student visa holders.</p>',
    apply_form = 'https://www.qut.edu.au/courses/graduate-diploma-in-diagnostic-genomics',
    updated_at = NOW()
WHERE cricos_course_code = '009034F';
-- 12 course pages share CRICOS 096565B
--   conflicting offshore_tuition_fee: [124200, 128400, 131100] -> kept 131100
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Our fashion degree is the longest running fashion degree in Queensland and provides industry-standard facilities. Graduates have launched internationally successful careers.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 131100,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-design-fashion-design-master-of-design-strategic-design',
    updated_at = NOW()
WHERE cricos_course_code = '096565B';
-- 7 course pages share CRICOS 096566A
--   conflicting offshore_tuition_fee: [163200, 171600] -> kept 171600
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Shape our experience with technology, devices, apps and websites. Be prepared for your career with design studio units, work experience and international study tours.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 171600,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-design-international-experience-design',
    updated_at = NOW()
WHERE cricos_course_code = '096566A';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Gain a design qualification in as little as one semester. Rapidly advance your design career and elevate your leadership skills with a Graduate Certificate in Strategic Design. </p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 10400,
    onshore_tuition_fee = 6950,
    apply_form = 'https://www.qut.edu.au/courses/graduate-certificate-in-strategic-design',
    updated_at = NOW()
WHERE cricos_course_code = '115461D';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Gain a design qualification in as little as one year. Rapidly advance your design career and elevate your leadership skills with a Graduate Diploma in Strategic Design.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 43600,
    onshore_tuition_fee = 30000,
    apply_form = 'https://www.qut.edu.au/courses/graduate-diploma-in-strategic-design',
    updated_at = NOW()
WHERE cricos_course_code = '115460E';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Rapidly advance your design career and elevate your leadership skills with the Master of Design (Strategic Design), a career-focused course mirroring real-world projects.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 85200,
    onshore_tuition_fee = 57600,
    apply_form = 'https://www.qut.edu.au/courses/master-of-design-strategic-design',
    updated_at = NOW()
WHERE cricos_course_code = '115459J';
-- 2 course pages share CRICOS 116650B
--   conflicting offshore_tuition_fee: [79000, 118500] -> kept 118500
--   conflicting onshore_tuition_fee: [11200, 16800] -> kept 16800
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>This degree offers you the chance to make a meaningful impact by laying the foundations for lifelong learning with children from birth to five years, before they start their schooling journey.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 118500,
    onshore_tuition_fee = 16800,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>2026 is the first year this course will be offered to all international students. 2025 the course will only be offered to international students who completed a relevant diploma.</p><p>2026 is the first year this course will be offered to all international students. 2025 the course will only be offered to international students who completed a relevant diploma.</p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-early-childhood-education-birth-to-five',
    updated_at = NOW()
WHERE cricos_course_code = '116650B';
-- 2 course pages share CRICOS 080481D
--   conflicting offshore_tuition_fee: [118500, 158000] -> kept 158000
--   conflicting onshore_tuition_fee: [18600, 24800] -> kept 24800
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Build upon your existing experience within early childhood education and further impact the development of children in prior-to-school settings and the lower years of primary school (Prep-Year 3).</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 158000,
    onshore_tuition_fee = 24800,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>The 2.5 year accelerated program is only available to full-time students commencing in the February intake. Part-time on-campus students should note that daytime attendance is required. Some lectures and tutorials may have evening sessions.</p><p>The 2.5 year accelerated program is only available to full-time students commencing in the February intake. Part-time on-campus students should note that daytime attendance is required. Some lectures and tutorials may have evening sessions.</p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-education-early-childhood',
    updated_at = NOW()
WHERE cricos_course_code = '080481D';
-- 12 course pages share CRICOS 084921G
--   conflicting offshore_tuition_fee: [194400, 200800, 243000] -> kept 243000
--   conflicting onshore_tuition_fee: [33600, 42000] -> kept 42000
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Streamline your path to a successful engineering management career with our combined undergraduate and postgraduate study package. </p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 243000,
    onshore_tuition_fee = 42000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-master-of-engineering-management',
    updated_at = NOW()
WHERE cricos_course_code = '084921G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Make our infrastructure safe and sustainable for the next generation with Queensland’s only Master of Sustainable Infrastructure. </p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 75600,
    onshore_tuition_fee = 14250,
    apply_form = 'https://www.qut.edu.au/courses/master-of-sustainable-infrastructure',
    updated_at = NOW()
WHERE cricos_course_code = '113911K';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Study a Master of Robotics and Artificial Intelligence to design and develop robotics and automation systems that bring modern industry into the future.</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 75000,
    onshore_tuition_fee = 14250,
    apply_form = 'https://www.qut.edu.au/courses/master-of-robotics-and-artificial-intelligence',
    updated_at = NOW()
WHERE cricos_course_code = '111159J';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Learn advanced engineering skills to lead the future of sustainable energy with Queensland’s only masters degree in renewable engineering. </p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 76650,
    onshore_tuition_fee = 14250,
    apply_form = 'https://www.qut.edu.au/courses/master-of-renewable-energy',
    updated_at = NOW()
WHERE cricos_course_code = '113912J';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Learn the skills to become an innovative engineer to design, optimise and improve manufacturing. Major in Digital and Robotics Manufacturing or Bioprocess Engineering.</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 74550,
    onshore_tuition_fee = 14250,
    apply_form = 'https://www.qut.edu.au/courses/master-of-advanced-manufacturing',
    updated_at = NOW()
WHERE cricos_course_code = '113913H';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Study a Master of Biomedical Systems and Technology and develop the entrepreneurial and technical skills to lead responsible healthcare innovation. </p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 72900,
    onshore_tuition_fee = 54450,
    apply_form = 'https://www.qut.edu.au/courses/master-of-biomedical-systems-and-technology',
    updated_at = NOW()
WHERE cricos_course_code = '118487C';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Learn to provide smart, cost-effective and environmentally responsible infrastructure solutions for a sustainable society and gain skills to lead complex engineering projects.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 96400,
    onshore_tuition_fee = 21000,
    apply_form = 'https://www.qut.edu.au/courses/master-of-sustainable-infrastructure-with-project-management',
    updated_at = NOW()
WHERE cricos_course_code = '114879H';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Gain advanced knowledge in this 2-year engineering degree in robotics and artificial intelligence, including data analytics and specialist AI skills to help you get ahead in your career.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 99000,
    onshore_tuition_fee = 19000,
    apply_form = 'https://www.qut.edu.au/courses/master-of-advanced-robotics-and-artificial-intelligence',
    updated_at = NOW()
WHERE cricos_course_code = '114880D';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Upskill in renewable and sustainable energy systems and gain fundamental knowledge and skills in managing engineering projects.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 101800,
    onshore_tuition_fee = 20800,
    apply_form = 'https://www.qut.edu.au/courses/master-of-renewable-energy-with-project-management',
    updated_at = NOW()
WHERE cricos_course_code = '114881C';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Specialise in digital and robotic manufacturing or bioprocess engineering and develop project management skills to lead sustainable manufacturing projects.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 97400,
    onshore_tuition_fee = 23000,
    apply_form = 'https://www.qut.edu.au/courses/master-of-advanced-manufacturing-with-project-management',
    updated_at = NOW()
WHERE cricos_course_code = '114882B';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Develop smart, cost-effective and environmentally responsible infrastructure solutions for a sustainable society coupled with key data analytics skills to drive decisions.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 96000,
    onshore_tuition_fee = 19000,
    apply_form = 'https://www.qut.edu.au/courses/master-of-sustainable-infrastructure-with-data-analytics',
    updated_at = NOW()
WHERE cricos_course_code = '114974J';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Upskill in renewable and sustainable energy systems and gain fundamental data analysis knowledge and skills with the Master of Renewable Energy with Data Analytics.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 100800,
    onshore_tuition_fee = 18200,
    apply_form = 'https://www.qut.edu.au/courses/master-of-renewable-energy-with-data-analytics',
    updated_at = NOW()
WHERE cricos_course_code = '114975H';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Specialise in digital and robotic manufacturing or bioprocess engineering and develop important data analytics skills to design sustainable manufacturing systems.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 98800,
    onshore_tuition_fee = 18400,
    apply_form = 'https://www.qut.edu.au/courses/master-of-advanced-manufacturing-with-data-analytics',
    updated_at = NOW()
WHERE cricos_course_code = '114976G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Gain cutting-edge engineering management knowledge and skills, while specialising in artificial intelligence in medical technology, bioprocess engineering, digital and robotic manufacturing, renewable energy systems, renewable power, smart transport and mobility, or water engineering.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 95400,
    onshore_tuition_fee = 66400,
    apply_form = 'https://www.qut.edu.au/courses/master-of-engineering-management-master-of-engineering-technology',
    updated_at = NOW()
WHERE cricos_course_code = '114957K';
-- 3 course pages share CRICOS 086329G
--   conflicting offshore_tuition_fee: [37400, 44100] -> kept 44100
--   conflicting onshore_tuition_fee: [9500, 13500, 38000] -> kept 13500
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Learn the business, technology, and strategy behind the global esports industry.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 44100,
    onshore_tuition_fee = 13500,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/diploma-in-esports',
    updated_at = NOW()
WHERE cricos_course_code = '086329G';
-- 5 course pages share CRICOS 092648J
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>This unique pathway program is designed for dedicated gamers who are curious about experiencing the whole game and interactive media development process.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 132900,
    onshore_tuition_fee = 29700,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-games-and-interactive-environments-animation',
    updated_at = NOW()
WHERE cricos_course_code = '092648J';
UPDATE courses SET
    course_description = '<p>Admission to the course is based on prior study in addition to a selection rank.</p><p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 75800,
    onshore_tuition_fee = 9400,
    entry_requirements = '<p>Admission to the course is based on prior study in addition to a selection rank.</p><p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can''''t defer your offer in this course. You must start in the semester you apply for.</p>',
    apply_form = 'https://www.qut.edu.au/courses/master-of-teaching-early-childhood',
    updated_at = NOW()
WHERE cricos_course_code = '084581A';
UPDATE courses SET
    course_description = '<p>Admission to the course is based on prior study in addition to a selection rank.</p><p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 75800,
    onshore_tuition_fee = 9400,
    entry_requirements = '<p>Admission to the course is based on prior study in addition to a selection rank.</p><p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can''''t defer your offer in this course. You must start in the semester you apply for.</p>',
    apply_form = 'https://www.qut.edu.au/courses/master-of-teaching-primary',
    updated_at = NOW()
WHERE cricos_course_code = '084582M';
UPDATE courses SET
    course_description = '<p>Admission to the course is based on prior study in addition to a selection rank.</p><p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 75800,
    onshore_tuition_fee = 9400,
    entry_requirements = '<p>Admission to the course is based on prior study in addition to a selection rank.</p><p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can''''t defer your offer in this course. You must start in the semester you apply for.</p>',
    apply_form = 'https://www.qut.edu.au/courses/master-of-teaching-secondary',
    updated_at = NOW()
WHERE cricos_course_code = '084583K';
-- 3 course pages share CRICOS 094024C
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Make an even bigger impact by studying a course that aligns with your career path, whether you''''re leading from the front of a classroom or driving change beyond it. </p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 18900,
    onshore_tuition_fee = 2400,
    apply_form = 'https://www.qut.edu.au/courses/graduate-certificate-in-education-educational-leadership',
    updated_at = NOW()
WHERE cricos_course_code = '094024C';
-- 8 course pages share CRICOS 081798G
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Make an even bigger impact by studying a course that aligns with your career path, whether you''''re leading from the front of a classroom or driving change beyond it. </p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 56850,
    onshore_tuition_fee = 7050,
    apply_form = 'https://www.qut.edu.au/courses/master-of-education-educational-leadership',
    updated_at = NOW()
WHERE cricos_course_code = '081798G';
-- 2 course pages share CRICOS 093729M
--   conflicting onshore_tuition_fee: [4096, 4900] -> kept 4900
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Enhance your leadership skills with the Public Sector Management Program (PSMP), a nationally recognised study option for mid-level managers in the Australian public service.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 11300,
    onshore_tuition_fee = 4900,
    apply_form = 'https://www.qut.edu.au/courses/graduate-certificate-in-business-process-management',
    updated_at = NOW()
WHERE cricos_course_code = '093729M';
UPDATE courses SET
    course_duration_per_week = 104,
    onshore_tuition_fee = 2100,
    apply_form = 'https://www.qut.edu.au/courses/graduate-diploma-in-business-enterprise-leadership',
    updated_at = NOW()
WHERE cricos_course_code = '069962B';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>This diploma helps you meet the academic and English language requirements to enter your QUT bachelor degree with up to seven units of credit.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 35300,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>Select the country where you completed your studies to see a guide to the grades you need to apply for this course.</p><p>If your country or qualification is not listed, you can still apply for this course and we will assess your eligibility.</p>',
    apply_form = 'https://www.qut.edu.au/courses/diploma-in-health-science-nursing',
    updated_at = NOW()
WHERE cricos_course_code = '118489A';
-- 3 course pages share CRICOS 096570E
--   conflicting offshore_tuition_fee: [169200, 175600] -> kept 175600
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine creativity and technology to design and build human-centred digital experiences.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 175600,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-design-experience-design-bachelor-of-information-technology',
    updated_at = NOW()
WHERE cricos_course_code = '096570E';
-- 5 course pages share CRICOS 096578G
UPDATE courses SET
    course_description = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p>',
    course_duration_per_week = 286,
    offshore_tuition_fee = 233750,
    onshore_tuition_fee = 95700,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-communication-journalism-bachelor-of-laws-honours',
    updated_at = NOW()
WHERE cricos_course_code = '096578G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Develop a unique set of skills to enhance your employment options whether you choose to work in the legal fraternity or within the property industry.</p>',
    course_duration_per_week = 286,
    offshore_tuition_fee = 246950,
    onshore_tuition_fee = 95700,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-property-economics-bachelor-of-laws-honours',
    updated_at = NOW()
WHERE cricos_course_code = '099273A';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combining a law and justice degree gives you a powerful blend of legal expertise and a deep understanding of the justice system, opening doors to diverse careers in law, policy, and social reform. </p>',
    course_duration_per_week = 286,
    offshore_tuition_fee = 235400,
    onshore_tuition_fee = 95700,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-justice-bachelor-of-laws-honours',
    updated_at = NOW()
WHERE cricos_course_code = '083027B';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Develop highly sought after skills in urban planning and property economics to make informed and impactful decisions on sustainable development, community planning, and investment strategies. </p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 216000,
    onshore_tuition_fee = 63000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-built-environment-honours-urban-and-regional-planning-bachelor-of-property-economics',
    updated_at = NOW()
WHERE cricos_course_code = '116651A';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine an understanding of human behaviour with design thinking and creativity to develop user-centric solutions and processes across a range of industries. </p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 158000,
    onshore_tuition_fee = 39200,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-behavioural-science-psychology-bachelor-of-design-visual-communication',
    updated_at = NOW()
WHERE cricos_course_code = '116309D';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Gain a competitive advantage in the building and property industries by leading design projects that effectively balance economic profitability with ecological sustainability. </p>',
    course_duration_per_week = 286,
    offshore_tuition_fee = 242550,
    onshore_tuition_fee = 68200,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-built-environment-honours-interior-design-bachelor-of-property-economics',
    updated_at = NOW()
WHERE cricos_course_code = '116653K';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Learn how to drive growth and make strong commercial decisions, understand regulations and manage construction projects at any scale. </p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 220500,
    onshore_tuition_fee = 65000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-built-environment-honours-construction-management-and-quantity-surveying-bachelor-of-property-economics',
    updated_at = NOW()
WHERE cricos_course_code = '116654J';
-- 4 course pages share CRICOS 081617G
--   conflicting onshore_tuition_fee: [13400, 40200] -> kept 40200
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>The course is designed as a pathway to undergraduate creative industries courses allowing you to enter your QUT Bachelor degree with up to one year of credit.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 27000,
    onshore_tuition_fee = 40200,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/diploma-in-creative-industries-bachelor-of-communication',
    updated_at = NOW()
WHERE cricos_course_code = '081617G';
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 150400,
    onshore_tuition_fee = 140800,
    entry_requirements = '<p>The part-time study options may be subject to QUT approval.</p><p>The part-time study options may be subject to QUT approval.</p>',
    apply_form = 'https://www.qut.edu.au/courses/doctor-of-philosophy',
    updated_at = NOW()
WHERE cricos_course_code = '006367J';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Kickstart your IT career with the QUT Graduate Certificate in Information Technology. Gain hands-on skills in programming, web development, and systems design—ready for the jobs of tomorrow.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 11250,
    onshore_tuition_fee = 4800,
    apply_form = 'https://www.qut.edu.au/courses/graduate-certificate-in-information-technology',
    updated_at = NOW()
WHERE cricos_course_code = '0101555';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Advance your IT career with a postgraduate qualification designed to upgrade, specialise, or completely reshape your tech skillset in just one year.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 44900,
    onshore_tuition_fee = 9500,
    apply_form = 'https://www.qut.edu.au/courses/graduate-diploma-in-information-technology',
    updated_at = NOW()
WHERE cricos_course_code = '0101556';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Advance your career with the QUT Master of Artificial Intelligence. Gain specialised AI and machine learning skills, complete industry projects, and learn from top experts. Address the rising demand for AI professionals and prepare for roles like AI Engineer, Machine Learning Specialist, Data Scientist, and more.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 89800,
    onshore_tuition_fee = 19000,
    apply_form = 'https://www.qut.edu.au/courses/master-of-artificial-intelligence',
    updated_at = NOW()
WHERE cricos_course_code = '117578H';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Develop the skills to analyse data, create visualisations, and apply statistical and machine learning models. Prepare for a career in data science and analytics, or specialise further in the Master of Data Science program. </p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 11050,
    onshore_tuition_fee = 2150,
    apply_form = 'https://www.qut.edu.au/courses/graduate-certificate-in-data-science',
    updated_at = NOW()
WHERE cricos_course_code = '116755D';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Advance your career with a postgraduate degree that provides theoretical foundations and practical skills in the growing field of data science that turns data into valuable insights and intelligence. </p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 88400,
    onshore_tuition_fee = 17000,
    apply_form = 'https://www.qut.edu.au/courses/master-of-data-science',
    updated_at = NOW()
WHERE cricos_course_code = '116754E';
-- 3 course pages share CRICOS 081616G
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>The Diploma in Information Technology is a pathway program designed to help you successfully progress to QUT''''s Bachelor of Information Technology.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 27000,
    onshore_tuition_fee = 11500,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/diploma-in-information-technology',
    updated_at = NOW()
WHERE cricos_course_code = '081616G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>This vertical double degree bridges the gap between IT proficiency and data science expertise. Graduate with a bachelor degree and master degree within four years and fast-track your ability to join the workforce as one of the most sought-after professionals. </p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 180000,
    onshore_tuition_fee = 38400,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-information-technology-master-of-data-science',
    updated_at = NOW()
WHERE cricos_course_code = '116996J';
-- 4 course pages share CRICOS 006117E
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Understand criminology and help communities feel safe. You’ll gain insights from leading experts into trauma informed practice, child protection, youth crime and research methods.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 120900,
    onshore_tuition_fee = 52200,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-justice-criminology-and-violence-prevention',
    updated_at = NOW()
WHERE cricos_course_code = '006117E';
-- 5 course pages share CRICOS 096577J
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Study media, digital platforms, and communication strategy at QUT. Graduate ready for careers in media analysis, content creation, and communication management.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 120000,
    onshore_tuition_fee = 51600,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-communication-media-and-communication-industries',
    updated_at = NOW()
WHERE cricos_course_code = '096577J';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Develop new skills in social media, data analytics, artificial intelligence and visualisation, all the while investigating how constantly-evolving technologies disrupt various industries. Learn about what can be done to minimise this disruption and how best to harness the potential of emerging communication technologies.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 10400,
    onshore_tuition_fee = 6950,
    apply_form = 'https://www.qut.edu.au/courses/graduate-certificate-in-digital-communication',
    updated_at = NOW()
WHERE cricos_course_code = '099300C';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Build upon a working knowledge of modern technology and master the emerging digital communication technologies of the future. You''''ll graduate with a practical skills toolkit that will guide you through periods of technological change and industry disruption.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 41700,
    onshore_tuition_fee = 27800,
    apply_form = 'https://www.qut.edu.au/courses/graduate-diploma-in-digital-communication',
    updated_at = NOW()
WHERE cricos_course_code = '099301B';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>If having the flexibility to work across many industries appeals to you, a career in digital communication may be an excellent fit. You will learn new skills that are applicable to various media forms, including social media, data analytics, artificial intelligence and visualisation.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 83400,
    onshore_tuition_fee = 55600,
    apply_form = 'https://www.qut.edu.au/courses/master-of-digital-communication',
    updated_at = NOW()
WHERE cricos_course_code = '099302A';
-- 2 course pages share CRICOS 052768K
--   conflicting offshore_tuition_fee: [171600, 228800] -> kept 228800
--   conflicting onshore_tuition_fee: [28500, 38000] -> kept 38000
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Fast-track your career in healthcare or medical research by completing a vertical double degree designed to produce biomedical scientists with advanced skills in data science and analytics.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 228800,
    onshore_tuition_fee = 38000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-biomedical-science-master-of-data-science',
    updated_at = NOW()
WHERE cricos_course_code = '052768K';
-- 2 course pages share CRICOS 083020J
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>If you have a completed degree in another area, we’ll recognise your prior learning so you can complete your law degree sooner.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 134400,
    onshore_tuition_fee = 52200,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-laws-honours-graduate-entry',
    updated_at = NOW()
WHERE cricos_course_code = '083020J';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>If you have a passion for mathematics and a keen interest in data science, this course was designed for you. The combination of mathematics and data science expertise equips you with a unique skill set that is highly sought after in various industries. </p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 156800,
    onshore_tuition_fee = 20800,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-mathematics-master-of-data-science',
    updated_at = NOW()
WHERE cricos_course_code = '116997H';
-- 2 course pages share CRICOS 003501K
--   conflicting offshore_tuition_fee: [87000, 130500] -> kept 130500
--   conflicting onshore_tuition_fee: [11800, 17700] -> kept 17700
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Fast track your nursing degree and graduate in two years if you are an enrolled nurse (Division 2) who is registered with AHPRA. Learn from respected nursing experts and complete 800 hours of placement.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 130500,
    onshore_tuition_fee = 17700,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can''''t defer your offer in this course. You must start in the semester you apply for.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-nursing',
    updated_at = NOW()
WHERE cricos_course_code = '003501K';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Learn from some of Australia’s most respected nursing experts. Access purpose-built facilities, technology and equipment, and complete 800 hours of placement.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 90600,
    onshore_tuition_fee = 12000,
    entry_requirements = '<p>Admission to the course is based on prior study in addition to a selection rank.</p><p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can''''t defer your offer in this course. You must start in the semester you apply for.</p>',
    apply_form = 'https://www.qut.edu.au/courses/master-of-nursing-entry-to-practice',
    updated_at = NOW()
WHERE cricos_course_code = '107928G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Prepare registered nurses for advanced practice nursing roles, educator roles, middle and senior leadership positions, and research opportunities. Learn from expert nurse clinician academics in supportive, flexible learning environments with strong industry connections.</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 61200,
    onshore_tuition_fee = 41850,
    apply_form = 'https://www.qut.edu.au/courses/master-of-nursing',
    updated_at = NOW()
WHERE cricos_course_code = '113901A';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Pursue a rewarding career as a practicing optometrist through the Master of Optometry. Vision science graduates can further their clinical skills to be eligible for registration.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 79800,
    onshore_tuition_fee = 19000,
    apply_form = 'https://www.qut.edu.au/courses/master-of-optometry',
    updated_at = NOW()
WHERE cricos_course_code = '065379E';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Pursue a career as a medical physicist, health physicist or bio-engineer or continue onto a Master of Applied Science. </p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 50000,
    onshore_tuition_fee = 9900,
    apply_form = 'https://www.qut.edu.au/courses/graduate-diploma-in-applied-science-medical-physics',
    updated_at = NOW()
WHERE cricos_course_code = '020315D';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Further your career in the medical and health physics discipline with a course that deals with well-established and emerging areas, including clinical measurement, medical imaging, and radiological imaging sciences. </p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 75000,
    onshore_tuition_fee = 13200,
    apply_form = 'https://www.qut.edu.au/courses/master-of-applied-science-medical-physics',
    updated_at = NOW()
WHERE cricos_course_code = '043548G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Enhance your professional outlook and stand out to employers through our targeted Graduate Certificate in Project Management.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 21900,
    onshore_tuition_fee = 14900,
    apply_form = 'https://www.qut.edu.au/courses/graduate-certificate-in-project-management',
    updated_at = NOW()
WHERE cricos_course_code = '084926C';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Develop your skills as an innovative and adaptive project manager, capable of managing complex project constraints and responding effectively to rapid change.</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 66150,
    onshore_tuition_fee = 45000,
    apply_form = 'https://www.qut.edu.au/courses/master-of-project-management',
    updated_at = NOW()
WHERE cricos_course_code = '084927B';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Study for a professionally accredited graduate diploma in occupational health and safety. Learn how to successfully prevent and mitigate occupational risks and promote worker safety, health, wellbeing, and performance from strategic and tactical viewpoints at an enterprise level.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 40300,
    onshore_tuition_fee = 9400,
    apply_form = 'https://www.qut.edu.au/courses/graduate-diploma-in-occupational-health-and-safety',
    updated_at = NOW()
WHERE cricos_course_code = '061160A';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Learn to assess environmental health risks and combat a range of local and global environmental challenges. This course offers a pathway to a career as an Environmental Health Officer.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 40300,
    onshore_tuition_fee = 9500,
    apply_form = 'https://www.qut.edu.au/courses/graduate-diploma-in-environmental-health',
    updated_at = NOW()
WHERE cricos_course_code = '061302C';
-- 2 course pages share CRICOS 113903K
--   conflicting offshore_tuition_fee: [22100, 43800] -> kept 43800
--   conflicting onshore_tuition_fee: [7700, 29700] -> kept 29700
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Become a leader in the implementation, adoption, and meaningful use of digital health systems.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 43800,
    onshore_tuition_fee = 29700,
    apply_form = 'https://www.qut.edu.au/courses/graduate-diploma-in-health-management-and-leadership',
    updated_at = NOW()
WHERE cricos_course_code = '113903K';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Lead change and address complex problems in the health sector by developing skills in a wide range of health management and leadership competencies, including digital health, quality and patient safety, and emergency and disaster management.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 85600,
    onshore_tuition_fee = 58600,
    apply_form = 'https://www.qut.edu.au/courses/master-of-health-management-and-leadership',
    updated_at = NOW()
WHERE cricos_course_code = '113902M';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Develop advanced knowledge and skills in collaborative approaches to counselling, supervision and group work. Learn capacity focused and culturally sensitive approaches to therapeutic practice.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 55400,
    onshore_tuition_fee = 41600,
    apply_form = 'https://www.qut.edu.au/courses/master-of-counselling',
    updated_at = NOW()
WHERE cricos_course_code = '096589E';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>The Intensive Program helps you meet the academic and English language requirements to enter the first year of your bachelor degree at QUT.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 12240,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>Select the country where you completed your studies to see a guide to the grades you need to apply for this course.</p><p>If your country or qualification is not listed, you can still apply for this course and we will assess your eligibility.</p>',
    apply_form = 'https://www.qut.edu.au/courses/intensive-program',
    updated_at = NOW()
WHERE cricos_course_code = '098567F';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Standard Foundation helps you meet the academic and English language requirements to enter the first year of your QUT Bachelor degree.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 24480,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>Select the country where you completed your studies to see a guide to the grades you need to apply for this course.</p><p>If your country or qualification is not listed, you can still apply for this course and we will assess your eligibility.</p>',
    apply_form = 'https://www.qut.edu.au/courses/standard-foundation',
    updated_at = NOW()
WHERE cricos_course_code = '065045E';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>This course helps you improve your academic English language skills to achieve an IELTS 7.0 (sub-scores 7.0). </p>',
    course_duration_per_week = 10,
    offshore_tuition_fee = 5560,
    apply_form = 'https://www.qut.edu.au/courses/ielts-advanced',
    updated_at = NOW()
WHERE cricos_course_code = '073922J';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Improve your academic English language skills for further study at QUT College. Students with a higher English language score can complete the course sooner with our standard program.</p>',
    course_duration_per_week = 10,
    offshore_tuition_fee = 5560,
    apply_form = 'https://www.qut.edu.au/courses/english-for-academic-purposes-1-standard',
    updated_at = NOW()
WHERE cricos_course_code = '0100526';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Improve your academic English language skills for further study at QUT College. Complete our extended program in 15 weeks.</p>',
    course_duration_per_week = 15,
    offshore_tuition_fee = 8340,
    apply_form = 'https://www.qut.edu.au/courses/english-for-academic-purposes-1-extended',
    updated_at = NOW()
WHERE cricos_course_code = '0100527';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Improve your academic English language skills for further study at QUT College. Students with a higher English language score can complete the course sooner with our standard program.</p>',
    course_duration_per_week = 10,
    offshore_tuition_fee = 5560,
    apply_form = 'https://www.qut.edu.au/courses/english-for-academic-purposes-2-standard',
    updated_at = NOW()
WHERE cricos_course_code = '0100528';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Improve your academic English language skills for further study at QUT. Complete our extended program in 15 weeks.</p>',
    course_duration_per_week = 15,
    offshore_tuition_fee = 8340,
    apply_form = 'https://www.qut.edu.au/courses/english-for-academic-purposes-2-extended',
    updated_at = NOW()
WHERE cricos_course_code = '0100529';
-- 9 course pages share CRICOS 062077K
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>General English at QUT College is a great way to improve your English for school, work and everyday life.</p>',
    course_duration_per_week = 45,
    offshore_tuition_fee = 2260,
    entry_requirements = '<p>There are no specific entry requirements for this course. You’ll take a placement test on your first day to determine which level of English class you should be studying.</p>',
    apply_form = 'https://www.qut.edu.au/courses/general-english-program-45-weeks',
    updated_at = NOW()
WHERE cricos_course_code = '062077K';
-- 6 course pages share CRICOS 103173M
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Bring your passion for STEM to the teaching profession and inspire the next generation with our vertical double degree, Bachelor of Science/Master of Teaching (Secondary).</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 208400,
    onshore_tuition_fee = 39200,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-science-biological-sciences-master-of-teaching-secondary',
    updated_at = NOW()
WHERE cricos_course_code = '103173M';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>This vertical double degree is designed for individuals with a strong interest in science and who want to develop advanced skills in data science. In this degree, you will gain a solid foundation in science and statistics, and deepen your knowledge in your chosen science major. </p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 186400,
    onshore_tuition_fee = 34000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-science-master-of-data-science',
    updated_at = NOW()
WHERE cricos_course_code = '116998G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Develop expertise in casework, assessment and intervention, and graduate with an internationally recognised qualification in social work.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 73800,
    onshore_tuition_fee = 19000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can''''t defer your offer in this course. You must start in the semester you apply for.</p>',
    apply_form = 'https://www.qut.edu.au/courses/master-of-social-work-qualifying',
    updated_at = NOW()
WHERE cricos_course_code = '093236K';
UPDATE courses SET
    course_description = '<p>This course is only available to international students.</p><p>Do you want a unique life changing experience that will help you grow academically, personally and prepare you for your career? Then the QUT Study Abroad Semester is for you.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 12700,
    entry_requirements = '<p>This course is only available to international students.<br/> To apply for our Study Abroad program, you must meet the:</p><p><strong>Academic requirements</strong><br/> You must:</p><p><strong>English language proficiency requirements</strong><br/> We accept scores from:</p><p><strong>Do I have to provide an English language test result?</strong><br/> You may not have to provide a proficiency test result if:</p><p><strong>Don''''t meet our English language proficiency requirements?</strong><br/> If you meet the academic entry requirements but not the English language requirements, you may still be able to participate in Study Abroad by completing an English language subject.</p><p>See our <a href="https://www.qut.edu.au/international/study-abroad-and-exchange/subjects-you-can-study">subjects you can study</a> to check which English language subject is appropriate for you.</p>',
    apply_form = 'https://www.qut.edu.au/courses/university-study-abroad-semester',
    updated_at = NOW()
WHERE cricos_course_code = '050556E';
UPDATE courses SET
    course_description = '<p>Spending a semester at QUT, immersing yourself in another culture, is the best way to learn, experience life with a different flavour, and make friends from all over the world. The Exchange Semester is open to students currently studying with a QUT exchange partner institution. </p>',
    course_duration_per_week = 26,
    entry_requirements = '<p>This course is only available to international students.</p><p><strong>To apply for our exchange program, you must meet the:</strong></p><p><strong>Academic requirements</strong><br/> You must:<br/> be nominated by one of our partner institutions</p><p><strong>Partner institutions</strong><br/> We have partner institutions all over the world. Check if your university is one of <a href="https://www.qut.edu.au/international/study-abroad-and-exchange/applying/inbound-exchange/exchange-partner-institutions">our partner institutions</a>.<br/> If you do not attend one of our partner institutions, you can still come to QUT with <a href="https://www.qut.edu.au/international/study-abroad-and-exchange/applying/study-abroad">our Study Abroad program</a>.</p><p><strong>English language proficiency requirements</strong><br/> We accept scores from:</p><p><strong>Don''''t meet our English language proficiency requirements?</strong></p><p>If you meet the academic entry requirements but not the English language requirements, you may still be able to participate in Study Abroad by completing an English language subject.</p><p>See our <a href="https://www.qut.edu.au/international/study-abroad-and-exchange/subjects-you-can-study">subjects you can study</a> to check which English language subject is appropriate for you.</p>',
    apply_form = 'https://www.qut.edu.au/courses/university-exchange-semester',
    updated_at = NOW()
WHERE cricos_course_code = '050623K';
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 19000,
    apply_form = 'https://www.qut.edu.au/courses/international-transfer-semester',
    updated_at = NOW()
WHERE cricos_course_code = '096698M';
UPDATE courses SET
    course_description = '<p>The QUT Study Abroad Year is a fantastic opportunity for you to study at QUT in Brisbane, Australia for a full year (two semesters). </p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 12700,
    entry_requirements = '<p>Duration is 2 semesters</p><p>This course is only available to international students.<br/> To apply for our Study Abroad program, you must meet the:</p><p><strong>Academic requirements</strong><br/> You must:</p><p><strong>English language proficiency requirements</strong><br/> We accept scores from:</p><p><strong>Do I have to provide an English language test result?</strong><br/> You may not have to provide a proficiency test result if:</p><p><strong>Don''''t meet our English language proficiency requirements?</strong><br/> If you meet the academic entry requirements but not the English language requirements, you may still be able to participate in Study Abroad by completing an English language subject.</p><p>See our <a href="https://www.qut.edu.au/international/study-abroad-and-exchange/subjects-you-can-study">subjects you can study</a> to check which English language subject is appropriate for you.</p>',
    apply_form = 'https://www.qut.edu.au/courses/university-study-abroad-year',
    updated_at = NOW()
WHERE cricos_course_code = '012704B';
UPDATE courses SET
    course_description = '<p>This course is only available to international students</p><p>An Exchange Year is an excellent opportunity to see more of the world, experience new cultures and develop personally, academically and professionally. The Exchange Year is open to students currently studying with a QUT exchange partner institution. </p>',
    course_duration_per_week = 52,
    entry_requirements = '<p>Duration is 2 semesters</p><p>This course is only available to international students.</p><p><strong>To apply for our exchange program, you must meet the:</strong></p><p><strong>Academic requirements</strong><br/> You must:<br/> be nominated by one of our partner institutions</p><p><strong>Partner institutions</strong><br/> We have partner institutions all over the world. Check if your university is one of <a href="https://www.qut.edu.au/international/study-abroad-and-exchange/applying/inbound-exchange/exchange-partner-institutions">our partner institutions</a>.<br/> If you do not attend one of our partner institutions, you can still come to QUT with <a href="https://www.qut.edu.au/international/study-abroad-and-exchange/applying/study-abroad">our Study Abroad program</a>.</p><p><strong>English language proficiency requirements</strong><br/> We accept scores from:</p><p><strong>Don''''t meet our English language proficiency requirements?</strong></p><p>If you meet the academic entry requirements but not the English language requirements, you may still be able to participate in Study Abroad by completing an English language subject.</p><p>See our <a href="https://www.qut.edu.au/international/study-abroad-and-exchange/subjects-you-can-study">subjects you can study</a> to check which English language subject is appropriate for you.</p>',
    apply_form = 'https://www.qut.edu.au/courses/university-exchange-year',
    updated_at = NOW()
WHERE cricos_course_code = '050639B';
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 19000,
    apply_form = 'https://www.qut.edu.au/courses/international-transfer-year',
    updated_at = NOW()
WHERE cricos_course_code = '096699K';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Build your research skills with a university-wide postgraduate degree while setting yourself up for the opportunity to advance to a PhD.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 75200,
    onshore_tuition_fee = 70400,
    entry_requirements = '<p><strong>To be eligible for this course, you need either:</strong></p><p>Applications and proposed research projects are subject to supervisor availability and resources available within the faculty.</p>',
    apply_form = 'https://www.qut.edu.au/courses/master-of-philosophy',
    updated_at = NOW()
WHERE cricos_course_code = '095410G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Explore a broad range of health topics as you develop the essential knowledge and skills you need to successfully transition into popular QUT undergraduate health science degrees. </p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 35300,
    onshore_tuition_fee = 10900,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/diploma-in-health-science-health-studies',
    updated_at = NOW()
WHERE cricos_course_code = '118490H';
-- 2 course pages share CRICOS 077686F
--   conflicting offshore_tuition_fee: [122250, 195600] -> kept 195600
--   conflicting onshore_tuition_fee: [27500, 44000] -> kept 44000
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>If you have already completed a health-related degree, we’ll recognise your prior learning so you can complete your Bachelor of Podiatry sooner.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 195600,
    onshore_tuition_fee = 44000,
    entry_requirements = '<p>Note: Admission to course is based on prior study in addition to a selection rank. Please refer to Entry Requirements.</p><p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 2, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-podiatry',
    updated_at = NOW()
WHERE cricos_course_code = '077686F';
-- 8 course pages share CRICOS 012656E
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Master the skills to lead software innovation and design the digital infrastructure that shapes the future. </p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 134400,
    onshore_tuition_fee = 28800,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-information-technology-software-development',
    updated_at = NOW()
WHERE cricos_course_code = '012656E';
-- 2 course pages share CRICOS 113183D
--   conflicting offshore_tuition_fee: [129900, 216500] -> kept 216500
--   conflicting onshore_tuition_fee: [30000, 50000] -> kept 50000
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Start your journey to becoming an architect with Queensland’s most in-demand architecture degree. You’ll be taught by real-world architects working in the field, and complete up to 100 hours in a real architecture practice.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 216500,
    onshore_tuition_fee = 50000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-architectural-design-master-of-architecture',
    updated_at = NOW()
WHERE cricos_course_code = '113183D';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Plan, design and develop neighbourhoods, suburbs, cities and regions for positive societal impact.</p>',
    course_duration_per_week = 286,
    offshore_tuition_fee = 236500,
    onshore_tuition_fee = 55550,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-architectural-design-bachelor-of-built-environment-honours-urban-and-regional-planning',
    updated_at = NOW()
WHERE cricos_course_code = '114081B';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Gain sought-after skills and experience with a double degree in architectural design and construction management and quantity surveying. </p>',
    course_duration_per_week = 286,
    offshore_tuition_fee = 237600,
    onshore_tuition_fee = 55000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-architectural-design-bachelor-of-built-environment-honours-construction-management-and-quantity-surveying',
    updated_at = NOW()
WHERE cricos_course_code = '114082A';
UPDATE courses SET
    course_duration_per_week = 26,
    apply_form = 'https://www.qut.edu.au/courses/graduate-certificate-in-business-and-communication',
    updated_at = NOW()
WHERE cricos_course_code = '085449G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>This vertical double degree will provide you with a comprehensive business and data science education. You will acquire a solid foundation in business during your undergraduate studies and enhance your analytical skills in the postgraduate component. </p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 180000,
    onshore_tuition_fee = 69600,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-business-master-of-data-science',
    updated_at = NOW()
WHERE cricos_course_code = '116994M';
-- 12 course pages share CRICOS 003491G
--   conflicting offshore_tuition_fee: [45100, 135000, 140400] -> kept 140400
--   conflicting onshore_tuition_fee: [16900, 52200] -> kept NULL
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine business thinking with strategic design expertise to become a leader in your field, driving innovation and strategic decision-making.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 140400,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-business-strategic-business-analytics',
    updated_at = NOW()
WHERE cricos_course_code = '003491G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Develop advanced understanding in architectural design and research.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 89400,
    onshore_tuition_fee = 21400,
    apply_form = 'https://www.qut.edu.au/courses/master-of-architecture',
    updated_at = NOW()
WHERE cricos_course_code = '099089A';
-- 4 course pages share CRICOS 103170C
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Design intelligent data solutions and drive innovation with the power of artificial intelligence and machine learning. </p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 126900,
    onshore_tuition_fee = 22500,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-data-science-artificial-intelligence-and-machine-learning',
    updated_at = NOW()
WHERE cricos_course_code = '103170C';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine science and law to work as a barrister, intellectual property lawyer or inventor, or in areas including trade secrets, genetic modification and environmental law disputes.</p>',
    course_duration_per_week = 286,
    offshore_tuition_fee = 254100,
    onshore_tuition_fee = 73700,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-science-bachelor-of-laws-honours',
    updated_at = NOW()
WHERE cricos_course_code = '083029M';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine IT and law for careers in cyberlaw, intellectual property, regulation of the internet, software developer, business analyst or e-commerce developer.</p>',
    course_duration_per_week = 286,
    offshore_tuition_fee = 248050,
    onshore_tuition_fee = 75350,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-information-technology-bachelor-of-laws-honours',
    updated_at = NOW()
WHERE cricos_course_code = '083025D';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Study the relationship between the natural and the constructed environment for a rewarding career in building sustainable community spaces.</p>',
    course_duration_per_week = 286,
    offshore_tuition_fee = 245850,
    onshore_tuition_fee = 55550,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-built-environment-honours-landscape-architecture-bachelor-of-science',
    updated_at = NOW()
WHERE cricos_course_code = '116500E';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Design urban environments, informed by science, with positive impacts on human health, environmental quality, social relationships and urban systems.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 218500,
    onshore_tuition_fee = 50000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-built-environment-honours-urban-and-regional-planning-bachelor-of-science',
    updated_at = NOW()
WHERE cricos_course_code = '116501D';
UPDATE courses SET
    course_description = '<p>''''My honours degree gave me the skills I need for full-time research. I also gained a strong network of role models and supervisors. Towards the end of my undergraduate degree, I was lucky enough to pick up a sessional teaching position in a first-year IT unit. This uncovered my love for tertiary education and introduced me to the breadth of academic roles, including research. From here, I moved into the IT honours degree, and the rest is history.''''</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 45700,
    onshore_tuition_fee = 9500,
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-information-technology-honours',
    updated_at = NOW()
WHERE cricos_course_code = '017323G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>This honours degree provides extended, modern and rigorous training in mathematical sciences and related research, to prepare students both for higher-level graduate careers in industry and government, and for postgraduate research.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 38900,
    onshore_tuition_fee = 4700,
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-mathematics-honours',
    updated_at = NOW()
WHERE cricos_course_code = '080486K';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>The Bachelor of Science/Bachelor of Data Science double degree provides a comprehensive, interdisciplinary education that merges the fields of science and data science. This four-year program equips students with the skills to extract valuable insights from data, bridging scientific knowledge with advanced data analysis techniques. </p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 182800,
    onshore_tuition_fee = 33200,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-science-bachelor-of-data-science',
    updated_at = NOW()
WHERE cricos_course_code = '115277D';
-- 7 course pages share CRICOS 077696D
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Explore the forefront of climate science and make a meaningful impact on the future of our planet by acquiring sought-after skills in data analysis, problem-solving, and communication.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 139500,
    onshore_tuition_fee = 27000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-science-climate-science',
    updated_at = NOW()
WHERE cricos_course_code = '077696D';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Enhance your science expertise through a research project that aligns with your passion, guided by a dedicated QUT supervisor and mentor. Get ready to elevate your qualifications with a prestigious PhD or gain an extra edge as you enter the industry. </p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 47800,
    onshore_tuition_fee = 9500,
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-science-honours',
    updated_at = NOW()
WHERE cricos_course_code = '080487J';
-- 6 course pages share CRICOS 102820D
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Challenge yourself from day one of your degree, solve complex problems in your chosen area of specialisation, and be connected with leading researchers with advanced studies in science.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 184000,
    onshore_tuition_fee = 33200,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-science-advanced-honours-biological-sciences',
    updated_at = NOW()
WHERE cricos_course_code = '102820D';
UPDATE courses SET
    course_duration_per_week = 208,
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-design-master-of-design-strategic-design',
    updated_at = NOW()
WHERE cricos_course_code = '079947G';
-- 7 course pages share CRICOS 096754G
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Study a Master of Professional Engineering at QUT to advance your knowledge and skills in your chosen engineering field or to move into an engineering management role.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 98400,
    onshore_tuition_fee = 73600,
    apply_form = 'https://www.qut.edu.au/courses/master-of-professional-engineering-civil-and-construction',
    updated_at = NOW()
WHERE cricos_course_code = '096754G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Master your future with our comprehensive and affordable Master of Information Technology degree. Gain advanced knowledge and skills in seven areas of specialisation, including human-centred design, IT management, and process analytics and automation. </p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 90000,
    onshore_tuition_fee = 19200,
    apply_form = 'https://www.qut.edu.au/courses/master-of-information-technology',
    updated_at = NOW()
WHERE cricos_course_code = '083059E';
-- 11 course pages share CRICOS 120879B
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Explore how technology, culture and society intersect and develop the skills to make a real impact in your community and career.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 125700,
    entry_requirements = '<p>As this is a new course, the threshold will be available mid-January 2027.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-arts-community-education',
    updated_at = NOW()
WHERE cricos_course_code = '120879B';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine arts and law to understand society, shape policy and practise law in a world shaped by technology, culture and constant change. </p>',
    course_duration_per_week = 286,
    offshore_tuition_fee = 249700,
    entry_requirements = '<p>As this is a new course, the threshold will be available mid-January 2027.</p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-arts-bachelor-of-laws-honours',
    updated_at = NOW()
WHERE cricos_course_code = '120880J';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Tailor your studies to suit your career goals with this degree''''s wide range of majors in transport, renewable power, water modelling, robotic manufacturing, and bioprocess engineering. </p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 49700,
    onshore_tuition_fee = 35000,
    apply_form = 'https://www.qut.edu.au/courses/master-of-engineering-technology',
    updated_at = NOW()
WHERE cricos_course_code = '113914G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Accelerate your career with a Graduate Certificate to lead the digital advances in manufacturing including robotics, analytics, machine learning and more.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 24900,
    onshore_tuition_fee = 4800,
    apply_form = 'https://www.qut.edu.au/courses/graduate-certificate-in-digital-and-robotic-manufacturing',
    updated_at = NOW()
WHERE cricos_course_code = '120799B';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Benefit from the latest research in assessing and treating mental health problems and disorders. Graduates are eligible to apply for registration as a psychologist in Australia. </p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 73800,
    onshore_tuition_fee = 9400,
    entry_requirements = '<p>Selection is based on additional entry requirements only. Please refer to Requirements.</p><p>You can''''t defer your offer in this course. You must start in the semester you apply for.</p>',
    apply_form = 'https://www.qut.edu.au/courses/master-of-clinical-psychology',
    updated_at = NOW()
WHERE cricos_course_code = '052769J';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Pursue your passion to optimise learning and development, and work with individuals, families and communities to promote wellbeing and resilience.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 73800,
    onshore_tuition_fee = 9400,
    entry_requirements = '<p>Selection is based on additional entry requirements only. Please refer to Requirements.</p><p>You can''''t defer your offer in this course. You must start in the semester you apply for.</p>',
    apply_form = 'https://www.qut.edu.au/courses/master-of-psychology-educational-and-developmental',
    updated_at = NOW()
WHERE cricos_course_code = '053489J';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Accelerate your engineering degree with a Master of Biomedical Systems and Technology, equipping you with the skills to lead and shape impactful healthcare technology. </p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 238500,
    onshore_tuition_fee = 39500,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-master-of-biomedical-systems-and-technology',
    updated_at = NOW()
WHERE cricos_course_code = '118488B';
-- 5 course pages share CRICOS 096579G
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Develop business and communication skills and be able to think creatively and critically, communicate professionally, make ethical business decisions and work in a global context. </p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 171200,
    onshore_tuition_fee = 69600,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-business-bachelor-of-communication-promotional-communication',
    updated_at = NOW()
WHERE cricos_course_code = '096579G';
-- 6 course pages share CRICOS 096567M
--   conflicting offshore_tuition_fee: [171200, 176400] -> kept 176400
--   conflicting onshore_tuition_fee: [56800, 58000] -> kept 58000
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine business and experience design to gain cutting-edge design skills, learn to think creatively and critically, and prepare for careers in design, technology or innovation. </p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 176400,
    onshore_tuition_fee = 58000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-business-bachelor-of-design-experience-design',
    updated_at = NOW()
WHERE cricos_course_code = '096567M';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>The property sector is one of Australia’s largest industries and the second largest employer. Combine property economics and a business specialisation to use your unique skill-set to optimise returns and manage the performance of properties, think creatively and critically, communicate professionally, make ethical business decisions, and work in a global context.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 180000,
    onshore_tuition_fee = 68400,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-property-economics-bachelor-of-business',
    updated_at = NOW()
WHERE cricos_course_code = '099272B';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Expand your career opportunities in a growing industry. Gain the skills to advance occupational health and safety, and environmental management standards across organisations.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 80600,
    onshore_tuition_fee = 55600,
    apply_form = 'https://www.qut.edu.au/courses/master-of-health-safety-and-environment',
    updated_at = NOW()
WHERE cricos_course_code = '077704J';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Become a practicing dietitian. Learn from industry leaders and gain hands-on experience with real clients in QUT Health Clinics and on professional placements. </p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 59550,
    onshore_tuition_fee = 45900,
    apply_form = 'https://www.qut.edu.au/courses/master-of-nutrition-and-dietetics',
    updated_at = NOW()
WHERE cricos_course_code = '120800C';
-- 7 course pages share CRICOS 116102H
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Curate your career with a fully customisable degree at a university that empowers creativity. Smash boundaries with over 100 study options, allowing you to tailor your studies and forge your own unique path.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 119400,
    onshore_tuition_fee = 37500,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-creative-arts-film-and-screen',
    updated_at = NOW()
WHERE cricos_course_code = '116102H';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Gain a distinctive edge with training for stage, screen and emerging digital sectors. Access leading acting facilities, strong industry links, professional film crews, and voice and movement coaches to support the development of your craft.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 119100,
    onshore_tuition_fee = 32700,
    entry_requirements = '<p>Selection is based on additional entry requirements only. Please refer to Requirements.</p><p>You can''''t defer your offer in this course. You must start in the semester you apply for.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-creative-arts-acting',
    updated_at = NOW()
WHERE cricos_course_code = '116069D';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Develop your skills in labs and simulation facilities that mimic the pharmacy environment and complete more than 500 hours of professional placement.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 177200,
    onshore_tuition_fee = 38000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-pharmacy-honours',
    updated_at = NOW()
WHERE cricos_course_code = '089126F';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Prepare for a career as a radiographer. You’ll be taught by registered radiographers and gain supervised clinical experience from your first year.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 170800,
    onshore_tuition_fee = 38000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-medical-imaging-honours',
    updated_at = NOW()
WHERE cricos_course_code = '080484A';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Provide a foundation for lifelong learning in young minds. With extensive real-world experience you’ll be qualified to teach Prep to Year 6 in primary school.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 158000,
    onshore_tuition_fee = 24800,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-education-primary',
    updated_at = NOW()
WHERE cricos_course_code = '080480E';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Contribute to the development of young adults and share your passion for your teaching areas. Undertake extensive real-world experience and specialise in two teaching areas.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 161200,
    onshore_tuition_fee = 37600,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-education-secondary',
    updated_at = NOW()
WHERE cricos_course_code = '080477M';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine nursing and psychology to work as a nurse in emergency, mental health, palliative care or cancer departments, or take the first step towards a career as a registered psychologist.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 190800,
    onshore_tuition_fee = 28800,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can''''t defer your offer in this course. You must start in the semester you apply for.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-nursing-bachelor-of-behavioural-science-psychology',
    updated_at = NOW()
WHERE cricos_course_code = '065615J';
UPDATE courses SET
    course_duration_per_week = 260,
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-behavioural-science-psychology-bachelor-of-social-work',
    updated_at = NOW()
WHERE cricos_course_code = '065387E';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Merge your creative and IT skills for opportunities in content production, communications, graphic design and games development.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 171600,
    onshore_tuition_fee = 40800,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can''''t defer your offer in this course. You must start in the semester you apply for.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-creative-industries-bachelor-of-information-technology',
    updated_at = NOW()
WHERE cricos_course_code = '059227E';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine industrial design and engineering to create innovative, sustainable and user-friendly products and systems.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 131100,
    onshore_tuition_fee = 29400,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-design-industrial-design-bachelor-of-engineering-honours',
    updated_at = NOW()
WHERE cricos_course_code = '096569J';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine your studies in biomedical science and mathematics to turn data analysis into real-world patient outcomes.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 198800,
    onshore_tuition_fee = 30000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-biomedical-science-bachelor-of-mathematics',
    updated_at = NOW()
WHERE cricos_course_code = '0100982';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine business and data science for strategic roles in finance, investment, economics, risk management, marketing, logistics, defence and research.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 174800,
    onshore_tuition_fee = 51600,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-business-bachelor-of-data-science',
    updated_at = NOW()
WHERE cricos_course_code = '103857E';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine interior design and business to produce both functional and beautiful interior spaces. Set yourself up for management, marketing or other business aspects of design organisations.</p>',
    course_duration_per_week = 286,
    offshore_tuition_fee = 243650,
    onshore_tuition_fee = 73150,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-built-environment-honours-interior-design-bachelor-of-business',
    updated_at = NOW()
WHERE cricos_course_code = '114087G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine law with a business specialisation, opening doors to careers in corporate law, company takeovers, mergers and acquisitions or intellectual property law.</p>',
    course_duration_per_week = 286,
    offshore_tuition_fee = 246950,
    onshore_tuition_fee = 95700,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-business-bachelor-of-laws-honours',
    updated_at = NOW()
WHERE cricos_course_code = '083022G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine psychology and law for a career in legal, corporate, government, mental health or clinical health environments, or as the first step towards a career as a registered psychologist.</p>',
    course_duration_per_week = 286,
    offshore_tuition_fee = 232650,
    onshore_tuition_fee = 89100,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-behavioural-science-psychology-bachelor-of-laws-honours',
    updated_at = NOW()
WHERE cricos_course_code = '083021G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine biomedical science and law to work as an in-house counsel or lawyer to health departments or the pharmaceutical industry.</p>',
    course_duration_per_week = 286,
    offshore_tuition_fee = 283800,
    onshore_tuition_fee = 73150,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-biomedical-science-bachelor-of-laws-honours',
    updated_at = NOW()
WHERE cricos_course_code = '085232C';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine a passion for creative arts with psychology to equip you with a blend of creative expression, critical and cultural literacy and psychological insights to address real-world problems. </p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 158000,
    onshore_tuition_fee = 52400,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-creative-arts-bachelor-of-behavioural-science-psychology',
    updated_at = NOW()
WHERE cricos_course_code = '116310M';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine secondary education and creative arts to share your creative passion with the next generation.</p>',
    course_duration_per_week = 234,
    offshore_tuition_fee = 177750,
    onshore_tuition_fee = 39150,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-education-secondary-bachelor-of-creative-arts',
    updated_at = NOW()
WHERE cricos_course_code = '116649F';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine law and creative arts to unlock a range of careers, including intellectual property lawyer, media lawyer, or creative practitioner.</p>',
    course_duration_per_week = 286,
    offshore_tuition_fee = 232100,
    onshore_tuition_fee = 81400,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-creative-arts-bachelor-of-laws-honours',
    updated_at = NOW()
WHERE cricos_course_code = '116067F';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine a business and creative arts degree to gain business knowledge and entrepreneurial thinking as well as creative skills taught by industry experts.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 169200,
    onshore_tuition_fee = 58000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-business-bachelor-of-creative-arts',
    updated_at = NOW()
WHERE cricos_course_code = '116068E';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine business and IT for diverse career opportunities such as technical consultant, chief information officer, systems analyst or brand strategist.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 180400,
    onshore_tuition_fee = 54800,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-business-bachelor-of-information-technology',
    updated_at = NOW()
WHERE cricos_course_code = '059595C';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine science and business for roles such as a laboratory manager, venture capitalist financier, or project manager for a firm taking scientific research to the marketplace.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 183600,
    onshore_tuition_fee = 54800,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-science-bachelor-of-business',
    updated_at = NOW()
WHERE cricos_course_code = '078352J';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine business and mathematics for roles in finance, investment, economics, environmental management, health, marketing, logistics, defence and research.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 167200,
    onshore_tuition_fee = 43200,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-business-bachelor-of-mathematics',
    updated_at = NOW()
WHERE cricos_course_code = '059601K';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine behavioural science and justice and shape safer communities with transferrable skills across numerous sectors, to provide endless career opportunities.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 160400,
    onshore_tuition_fee = 51200,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-behavioural-science-psychology-bachelor-of-justice',
    updated_at = NOW()
WHERE cricos_course_code = '076302B';
UPDATE courses SET
    course_duration_per_week = 208,
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-human-services-bachelor-of-justice',
    updated_at = NOW()
WHERE cricos_course_code = '058290F';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Develop in-depth knowledge of justice systems and business strategy with a double degree that empowers you to drive positive change across industries. </p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 170400,
    onshore_tuition_fee = 69600,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-business-bachelor-of-justice',
    updated_at = NOW()
WHERE cricos_course_code = '099274M';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine biomedical science with one our business majors for a career in health innovation and commercialisation, or in the research sector.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 213200,
    onshore_tuition_fee = 51200,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-biomedical-science-bachelor-of-business',
    updated_at = NOW()
WHERE cricos_course_code = '085233B';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine business with games and interactive environments for a competitive advantage. Work in roles such as producer, project manager, content manager or marketer.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 180000,
    onshore_tuition_fee = 56400,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-business-bachelor-of-games-and-interactive-environments',
    updated_at = NOW()
WHERE cricos_course_code = '092651C';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>QUT is a global leader in the creative industries. Choose a combination of study areas to suit your creative interests and aspirations, and help you develop your creative niche.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 120000,
    onshore_tuition_fee = 39000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can''''t defer your offer in this course. You must start in the semester you apply for.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-creative-industries',
    updated_at = NOW()
WHERE cricos_course_code = '056186M';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Perform scientific investigations that monitor health and wellbeing, and diagnose and manage pathological conditions. Gain practical laboratory experience for diagnostic, research or healthcare sectors.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 228800,
    onshore_tuition_fee = 38000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-medical-laboratory-science',
    updated_at = NOW()
WHERE cricos_course_code = '076173F';
-- 4 course pages share CRICOS 049433D
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Build your mathematics skills to solve real-world problems with advanced mathematical, computational and statistical techniques taught by internationally recognised academics and researchers.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 118500,
    onshore_tuition_fee = 15600,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-mathematics-applied-and-computational-mathematics',
    updated_at = NOW()
WHERE cricos_course_code = '049433D';
UPDATE courses SET
    course_duration_per_week = 208,
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-mathematics-master-of-teaching-secondary',
    updated_at = NOW()
WHERE cricos_course_code = '103172A';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>We offer the only optometry training in Queensland. Care for real patients in the QUT Optometry Clinic. Complete training placements in Australia or overseas.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 146700,
    onshore_tuition_fee = 29700,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-vision-science',
    updated_at = NOW()
WHERE cricos_course_code = '065380A';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Take the first step towards becoming a psychologist or work in fields where knowledge of human behaviour is important. Complete a placement to match your career goals.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 118800,
    onshore_tuition_fee = 32400,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-behavioural-science-psychology',
    updated_at = NOW()
WHERE cricos_course_code = '034136C';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine science and mathematics for roles in natural resources, genetics, infection and disease control, bioinformatics, or physical measuring and imaging techniques.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 174400,
    onshore_tuition_fee = 28400,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-science-bachelor-of-mathematics',
    updated_at = NOW()
WHERE cricos_course_code = '078353G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine IT and mathematics to fields such as programming, data communications, business process management, software engineering and telecommunications.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 169600,
    onshore_tuition_fee = 30400,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-information-technology-bachelor-of-mathematics',
    updated_at = NOW()
WHERE cricos_course_code = '059226F';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Enhance your engineering capabilities with skills in mathematical modelling, analysis and design to help solve complex problems.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 219000,
    onshore_tuition_fee = 33500,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-bachelor-of-mathematics',
    updated_at = NOW()
WHERE cricos_course_code = '084922G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine science and IT for roles including scientific modeller, software developer, scientific programmer and computational scientist.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 184400,
    onshore_tuition_fee = 36000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-science-bachelor-of-information-technology',
    updated_at = NOW()
WHERE cricos_course_code = '080489G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Develop the skills to become an engineer and an IT professional, working in the development of consumer electronics, and computer and electrical systems.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 232500,
    onshore_tuition_fee = 44500,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-bachelor-of-information-technology',
    updated_at = NOW()
WHERE cricos_course_code = '084923F';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine games and interactive environments with maths and use your problem-solving skills and expertise in mathematics to develop realistic scenes in gaming environments.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 167600,
    onshore_tuition_fee = 32000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-games-and-interactive-environments-bachelor-of-mathematics',
    updated_at = NOW()
WHERE cricos_course_code = '092653A';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine engineering and science for roles in energy consultancy, environmental engineering, medical engineering or natural resource management.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 237500,
    onshore_tuition_fee = 42500,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-bachelor-of-science',
    updated_at = NOW()
WHERE cricos_course_code = '084924E';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine science with games and interactive environments, and use virtual reality and gaming technology to tackle issues such as the environmental impacts of mining.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 182000,
    onshore_tuition_fee = 36000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-science-bachelor-of-games-and-interactive-environments',
    updated_at = NOW()
WHERE cricos_course_code = '092649G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Work for social justice supporting individuals, families or communities experiencing social and economic adversity. Enjoy a broad variety of subjects that spark your interest. Complete 500 hours of professional experience.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 118500,
    onshore_tuition_fee = 28500,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>Evening only classes are not available.</p><p>Evening only classes are not available.</p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-human-services',
    updated_at = NOW()
WHERE cricos_course_code = '058285C';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Change the world by working with individuals, families, groups, and communities for a more just, participatory and sustainable way of life. Learn from experienced social workers and apply theory to practice in the real world. </p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 158000,
    onshore_tuition_fee = 38000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>Flexible delivery option exists allowing you to study most semesters part-time. More information is available under the What to Expect tab below.</p><p>Flexible delivery option exists allowing you to study most semesters part-time. More information is available under the What to Expect tab below.</p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-social-work',
    updated_at = NOW()
WHERE cricos_course_code = '063034B';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Navigate the complex world of property and transform cities for the better. </p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 133200,
    onshore_tuition_fee = 45900,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-property-economics',
    updated_at = NOW()
WHERE cricos_course_code = '080478K';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Flexible course allows you to explore career opportunities. Develop your skills with a real project improving health outcomes and work alongside other professionals.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 151500,
    onshore_tuition_fee = 28500,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-nutrition-science',
    updated_at = NOW()
WHERE cricos_course_code = '077703K';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Prepare for a career as an accredited sports scientist or exercise scientist. Complete 280 hours of professional placement.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 120600,
    onshore_tuition_fee = 43500,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-sport-and-exercise-science',
    updated_at = NOW()
WHERE cricos_course_code = '093231D';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Assess, prescribe and deliver exercise programs to help people. Graduate with 500 hours of professional placement.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 161200,
    onshore_tuition_fee = 58000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-clinical-exercise-physiology',
    updated_at = NOW()
WHERE cricos_course_code = '070085K';
-- 7 course pages share CRICOS 085448J
--   conflicting offshore_tuition_fee: [98600, 103000] -> kept 103000
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Accounting extends far beyond the stereotype of number crunching and is often referred to as the ''''language of business.'''' Accountants play a key role in delivering crucial financial and non-financial insights that inform the very core of all strategic decisions made by key stakeholders.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 103000,
    entry_requirements = '<p>You must have a recognised Bachelor degree (or higher) in any discipline with a minimum grade point average of 4.00 (on QUT’s 7 point scale).</p><p><strong>You must have one of:</strong></p><p>A recognised bachelor degree (or higher) in business or a related discipline with a minimum grade point average of 4.00 (on QUT’s 7 point scale); <strong><em>or</em></strong></p><p>A recognised bachelor degree (or higher) in any discipline with a minimum grade point average of 4.00 (on QUT’s 7 point scale) followed by at least seven years (or equivalent) work experience in business or a related discipline.</p><p><strong>You must have one of:</strong></p><p>A recognised bachelor honours degree in management with a minimum grade point average of 4.00 (on QUT’s 7 point scale); <strong><em>or</em></strong></p><p>A recognised bachelor degree <strong><em>plus </em></strong>graduate certificate both in management with a minimum grade point average of 4.00 (on QUT’s 7 point scale); <em>or</em></p><p>A recognised graduate diploma (or higher) in management with a minimum grade point average of 4.00 (on QUT’s 7 point scale); <strong><em>or</em></strong></p><p>A recognised bachelor degree in management with a minimum grade point average of 4.00 (on QUT’s 7 point scale) followed by at least seven years full-time full-time (or equivalent) work experience in management.</p>',
    apply_form = 'https://www.qut.edu.au/courses/master-of-business-human-resource-management',
    updated_at = NOW()
WHERE cricos_course_code = '085448J';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Accelerate your leadership journey with QUT''''s Executive MBA (EMBA). Learn from industry-leading academics, work with global brands &amp; collaborate with high-achieving peers. </p>',
    course_duration_per_week = 100,
    onshore_tuition_fee = 4000,
    apply_form = 'https://www.qut.edu.au/courses/executive-master-of-business-administration',
    updated_at = NOW()
WHERE cricos_course_code = '045502F';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine business and creative industries for careers including communication specialist, creative entrepreneur or social media marketer.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 169600,
    onshore_tuition_fee = 56800,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can''''t defer your offer in this course. You must start in the semester you apply for.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-business-bachelor-of-creative-industries',
    updated_at = NOW()
WHERE cricos_course_code = '059596B';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine psychology and business for a career as a market researcher, human resources manager or training and development consultant.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 168800,
    onshore_tuition_fee = 51600,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-behavioural-science-psychology-bachelor-of-business',
    updated_at = NOW()
WHERE cricos_course_code = '060816G';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine business and engineering for careers in planning, designing, constructing or managing engineering projects, or in management, finance or consulting.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 232000,
    onshore_tuition_fee = 64000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-business-bachelor-of-engineering-honours',
    updated_at = NOW()
WHERE cricos_course_code = '084925D';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Gain a double degree in Queensland''''s most in-demand architecture degree known for producing Australia''''s best interior design graduates.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 216500,
    onshore_tuition_fee = 50500,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-architectural-design-bachelor-of-built-environment-honours-interior-design',
    updated_at = NOW()
WHERE cricos_course_code = '114083M';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Advance your engineering degree with a Master of Advanced Manufacturing and learn how to build sustainability and resilience into a manufacturing process.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 243000,
    onshore_tuition_fee = 42000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-master-of-advanced-manufacturing',
    updated_at = NOW()
WHERE cricos_course_code = '113908E';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Accelerate your engineering degree with a Master of Data Science and position yourself as an expert in driving meaningful, data-driven change. </p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 234500,
    onshore_tuition_fee = 41500,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-master-of-data-science',
    updated_at = NOW()
WHERE cricos_course_code = '116995K';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Accelerate your engineering degree with a Master of Robotics and Artificial Intelligence. Study at Australia’s top robotics research institution and graduate with skills in high demand.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 237500,
    onshore_tuition_fee = 41500,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-master-of-robotics-and-artificial-intelligence',
    updated_at = NOW()
WHERE cricos_course_code = '111160E';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Accelerate your engineering degree with a Master of Renewable Energy and lead sustainable engineering projects with Queensland’s only master degree in renewable power.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 248500,
    onshore_tuition_fee = 43000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-master-of-renewable-energy',
    updated_at = NOW()
WHERE cricos_course_code = '113910M';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Accelerate your engineering degree with Queensland’s only Master of Sustainable Infrastructure, with industry demand for strong skills in sustainable infrastructure continuing to rise in the lead up to Brisbane 2032 Olympics. </p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 243500,
    onshore_tuition_fee = 41500,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-master-of-sustainable-infrastructure',
    updated_at = NOW()
WHERE cricos_course_code = '113909D';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Accelerate your engineering degree with a Master of Project Management to lead innovative projects of all scales and complexities.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 238500,
    onshore_tuition_fee = 41500,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-engineering-honours-master-of-project-management',
    updated_at = NOW()
WHERE cricos_course_code = '116498E';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine your passion for architecture and the environment with a double degree in architectural design and landscape architecture to create outdoor spaces that have a positive cultural and environmental impact.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 216500,
    onshore_tuition_fee = 50000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-architectural-design-bachelor-of-built-environment-honours-landscape-architecture',
    updated_at = NOW()
WHERE cricos_course_code = '114084K';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Take the first step towards becoming a psychologist or work in fields where knowledge of human behaviour is important with our APAC accredited program.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 39400,
    onshore_tuition_fee = 8800,
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-behavioural-science-honours-psychology',
    updated_at = NOW()
WHERE cricos_course_code = '061159E';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine the technical and creative aspects of construction and design to meet future architectural and civil engineering challenges. </p>',
    course_duration_per_week = 286,
    offshore_tuition_fee = 246950,
    onshore_tuition_fee = 46750,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-architectural-design-bachelor-of-engineering-honours-civil',
    updated_at = NOW()
WHERE cricos_course_code = '117242K';
UPDATE courses SET
    course_duration_per_week = 26,
    apply_form = 'https://www.qut.edu.au/courses/graduate-certificate-in-communication-for-information-technology',
    updated_at = NOW()
WHERE cricos_course_code = '086328J';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Balance architectural innovation with property economics and graduate ready to explore diverse and lucrative career opportunities across both industries. </p>',
    course_duration_per_week = 234,
    offshore_tuition_fee = 196650,
    onshore_tuition_fee = 63450,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-architectural-design-bachelor-of-property-economics',
    updated_at = NOW()
WHERE cricos_course_code = '116652M';
-- 7 course pages share CRICOS 031769E
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Turn your business ambition into action. Accelerate your next career move and grow your confidence with QUT’s Graduate Certificate in Business.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 12350,
    onshore_tuition_fee = 9200,
    apply_form = 'https://www.qut.edu.au/courses/graduate-certificate-in-business-applied-finance',
    updated_at = NOW()
WHERE cricos_course_code = '031769E';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Combine architecture and business to create spaces that are functional, beautiful and financially viable for communities, cities and urban systems.</p>',
    course_duration_per_week = 234,
    offshore_tuition_fee = 199800,
    onshore_tuition_fee = 63000,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-architectural-design-bachelor-of-business',
    updated_at = NOW()
WHERE cricos_course_code = '114085J';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Increase your global employment opportunities and develop your intercultural skills with a business degree that incorporates overseas study.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 180000,
    onshore_tuition_fee = 69600,
    entry_requirements = '<p> These thresholds are the lowest adjusted scores to which QUT made an offer in Semester 1, 2026. </p><p>Don''''t have a ATAR/selection rank?</p><p><a href="https://www.qut.edu.au/study/applying">Find out other ways you can apply</a></p><p>You can defer your offer and postpone the start of your course for one year.</p>',
    apply_form = 'https://www.qut.edu.au/courses/bachelor-of-business-international',
    updated_at = NOW()
WHERE cricos_course_code = '083019B';
UPDATE courses SET
    course_description = '<h4>About this course</h4><p>Advance your career with the QUT Master of Cyber Security. Gain in-demand skills, complete industry projects, and learn from top experts. Address the rising demand for cyber security professionals and prepare for roles such as cyber security specialist, information security analyst and penetration tester.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 89800,
    onshore_tuition_fee = 19000,
    apply_form = 'https://www.qut.edu.au/courses/master-of-cyber-security',
    updated_at = NOW()
WHERE cricos_course_code = '117577J';
