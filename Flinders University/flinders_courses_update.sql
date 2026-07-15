-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'February, March, July, October',
    updated_at = NOW()
WHERE cricos_provider_code = '00114A';

UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Gain advanced skills to improve health outcomes, influence policy, and create healthier communities. Study the postgraduate Master of Public Health at Flinders.</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS Overall 6.5 Speaking: 6.0 Writing: 6.0 Pearson Overall 58 CRICOS 0100951</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/master-public-health',
    updated_at = NOW()
WHERE cricos_course_code = '0100951';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Step into senior leadership with Flinders’ Master of Project Management. Gain advanced skills to effectively lead and deliver enterprise projects.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 44100,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>English language requirements</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/master-project-management',
    updated_at = NOW()
WHERE cricos_course_code = '119404C';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>The Master of Business Administration Future Business provides a comprehensive foundation covering core business and management disciplines.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 66300,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>English language requirements</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/master-business-administration-future-business',
    updated_at = NOW()
WHERE cricos_course_code = '107690B';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Master business analytics with an MBA at Flinders. Build data-driven decision skills, leadership capability and real-world industry experience.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 73400,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>English language requirements</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/master-business-administration-business-analytics',
    updated_at = NOW()
WHERE cricos_course_code = '107691A';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Design, protect and analyse the wireless systems that power modern defence and communications.</p>',
    course_duration_per_week = NULL,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS Overall 6.0 Speaking: 6.0 Writing: 6.0 Pearson Overall 50</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/major-wireless-systems-security',
    updated_at = NOW()
WHERE cricos_course_code = '102680M';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Unleash creativity with the Visual Arts major at Flinders. Explore ceramics, digital media, drawing, jewellery, painting, photography, printmaking, sculpture and art theory while building skills for a creative or professional arts career.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 106500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/major-visual-arts',
    updated_at = NOW()
WHERE cricos_course_code = '002633F';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Design solutions that balance environmental, social and economic needs.</p>',
    course_duration_per_week = NULL,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS Overall 6.0 Speaking: 6.0 Writing: 6.0 Pearson Overall 50</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/major-sustainability',
    updated_at = NOW()
WHERE cricos_course_code = '055237B';
-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in Spanish | https://www.flinders.edu.au/study/courses/major-spanish

-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in Sociology | https://www.flinders.edu.au/study/courses/major-sociology

-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in Political Science | https://www.flinders.edu.au/study/courses/major-political-science

-- ⚠️ Skipped (CRICOS 055237B already emitted): Major in Physics | https://www.flinders.edu.au/study/courses/major-physics

-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in Philosophy | https://www.flinders.edu.au/study/courses/major-philosophy

-- ⚠️ Skipped (CRICOS 055237B already emitted): Major in Molecular Biology | https://www.flinders.edu.au/study/courses/major-molecular-biology

UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Learn to solve complex problems and unlock global career opportunities.</p>',
    course_duration_per_week = NULL,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS Overall 6.0 Speaking: 6.0 Writing: 6.0 Pearson Overall 50</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/major-mathematics',
    updated_at = NOW()
WHERE cricos_course_code = '075594D';
-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in Indonesian | https://www.flinders.edu.au/study/courses/major-indonesian

-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in History | https://www.flinders.edu.au/study/courses/major-history

-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in Geography and Environmental Studies | https://www.flinders.edu.au/study/courses/major-geography-environmental-studies

-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in Gender Studies | https://www.flinders.edu.au/study/courses/major-gender-studies

-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in French | https://www.flinders.edu.au/study/courses/major-french

-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in Film and Television | https://www.flinders.edu.au/study/courses/major-film-television-studies

-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in English | https://www.flinders.edu.au/study/courses/major-english

-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in Drama | https://www.flinders.edu.au/study/courses/major-drama

-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in Digital Heritage | https://www.flinders.edu.au/study/courses/major-digital-heritage

-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in Critical Indigenous Studies | https://www.flinders.edu.au/study/courses/major-critical-indigenous-studies

-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in Creative Writing | https://www.flinders.edu.au/study/courses/major-creative-writing

-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in Archaeology | https://www.flinders.edu.au/study/courses/major-archaeology

-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in Applied Linguistics | https://www.flinders.edu.au/study/courses/major-applied-linguistics

-- ⚠️ Skipped (CRICOS 002633F already emitted): Major in Ancient, Medieval and Early Modern Studies | https://www.flinders.edu.au/study/courses/major-ancient-medieval-early-modern-studies

UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Take the next step in your career with Flinders’ Graduate Diploma in Project Management. Gain advanced tools to lead projects and drive organisational success.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 35600,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>English language requirements</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/graduate-diploma-project-management',
    updated_at = NOW()
WHERE cricos_course_code = '119405B';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>In just six months, gain future-focused leadership capabilities and strategic business insight that position you for senior roles or seamless entry into the MBA.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 44200,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>English language requirements</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/graduate-diploma-business-administration',
    updated_at = NOW()
WHERE cricos_course_code = '107692M';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>A bridging course to the Master of Teaching at Flinders—build academic skills and explore Australian curriculum and education system foundations.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 19050,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>English language requirements</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/graduate-certificate-teaching-studies',
    updated_at = NOW()
WHERE cricos_course_code = '119310J';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Gain foundational skills in public health, from epidemiology to health promotion. Build practical capability and create a pathway to the Master of Public Health.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS Overall 6.5 Speaking: 6.0 Writing: 6.0 Pearson Overall 58 CRICOS 0940</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/graduate-certificate-public-health',
    updated_at = NOW()
WHERE cricos_course_code = '094009B';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Advance your career with the Graduate Certificate in Project Management. In six months, gain the skills to lead, plan, and deliver successful projects.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 22050,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>English language requirements</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/graduate-certificate-project-management',
    updated_at = NOW()
WHERE cricos_course_code = '119406A';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>The Graduate Certificate in Health Promotion equips you with practical, evidence-based skills to design, implement and evaluate health promotion initiatives that improve community and population health outcomes. Grounded in public health principles, the course focuses on addressing health inequities, promoting disease prevention, and supporting wellbeing across diverse settings.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 20700,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>English language requirements</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/graduate-certificate-health-promotion',
    updated_at = NOW()
WHERE cricos_course_code = '073816M';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Become a better leader in 3 months with Flinders University''s Graduate Certificate in Business Administration.</p>',
    course_duration_per_week = 13,
    offshore_tuition_fee = 22100,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>English language requirements</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/graduate-certificate-business-administration',
    updated_at = NOW()
WHERE cricos_course_code = '107693K';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Study 2D, 3D, Animation or VFX. Learn from the best in the animation, film, TV and gaming industry - in partnership with CDW Studios.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 106500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>Portfolio and written statement</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-visual-effects-entertainment-design',
    updated_at = NOW()
WHERE cricos_course_code = '119230J';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Build a career sustainably shaping cities and regions, and improve community futures.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 106500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-urban-regional-planning',
    updated_at = NOW()
WHERE cricos_course_code = '117650E';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Study sport, coaching, outdoor education or sports business at Flinders. Gain hands-on experience and graduate ready for a career in sport and active recreation.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 107100,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Writing 6.0 Speaking 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-sport-active-recreation',
    updated_at = NOW()
WHERE cricos_course_code = '113275M';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Discover the Bachelor of Social Work program at Flinders University. Learn more about the career opportunities and pathways available. Start your journey today!</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 145200,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 7.0 Writing 7.0 Speaking 7.0 Listening 7.0 Reading 7.0 Pearson overall 65</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-social-work',
    updated_at = NOW()
WHERE cricos_course_code = '083453F';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Unearth ancient life and build a scientific career with Australia’s only dedicated palaeontology degree. Study at Flinders and dig into your future—apply now!</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 130500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-science-palaeontology',
    updated_at = NOW()
WHERE cricos_course_code = '098228C';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Explore marine ecosystems with a Bachelor of Science in Marine Biology at Flinders University. Dive into a career in marine conservation.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 130500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-science-marine-biology',
    updated_at = NOW()
WHERE cricos_course_code = '033068G';
UPDATE courses SET
    course_description = '',
    course_duration_per_week = 208,
    offshore_tuition_fee = 146000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50 Information about</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-science-honours-coasts-oceans',
    updated_at = NOW()
WHERE cricos_course_code = '089671C';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Investigate crime and analyse evidence. Gain forensic and chemistry skills with hands-on labs, minors and majors.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 130500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>SACE stage two chemistry or equivalent.</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-science-forensic-analytical-science',
    updated_at = NOW()
WHERE cricos_course_code = '023581F';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Explore how oceans, coasts and water systems shape our planet. Study climate change, marine science and sustainable water management to protect Australia’s environment.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 130500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-science-environmental-science',
    updated_at = NOW()
WHERE cricos_course_code = '036355J';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Study biotechnology at Flinders. Gain lab skills, explore genetics, microbiology and bioinformatics, and prepare for careers in health, agriculture and industry.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 130500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-science-biotechnology',
    updated_at = NOW()
WHERE cricos_course_code = '074771M';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Protect the planet’s ecosystems. Study biodiversity and conservation science with field experience in South Australia.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 130500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-science-biodiversity-conservation',
    updated_at = NOW()
WHERE cricos_course_code = '039816E';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Explore how and why animals behave the way they do. Learn more about animal behaviour.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 130500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-science-animal-behaviour',
    updated_at = NOW()
WHERE cricos_course_code = '074770A';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Designed for high-achievers, this research-focused science degree offers majors, minors, and real-world projects to prepare you for advanced study or scientific careers.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 130500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-science-advanced-science',
    updated_at = NOW()
WHERE cricos_course_code = '118382A';
-- ⚠️ Skipped (CRICOS 055237B already emitted): Bachelor of Science | https://www.flinders.edu.au/study/courses/bachelor-science

UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Study the Bachelor of Public Health at Flinders University and prepare for a rewarding career improving community health. Learn from leaders in public health, gain hands-on experience, and explore pathways into research, health promotion, and policy.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 112200,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-public-health',
    updated_at = NOW()
WHERE cricos_course_code = '102949J';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Discover the Bachelor of Psychology (Honours) program at Flinders University. Learn more about the exciting career opportunities in psychology. Apply now!</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 156400,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.5 Speaking 6.0 Writing 6.0 Listening 6.0 Reading 6.0 Pearson overall 58</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-psychology-honours',
    updated_at = NOW()
WHERE cricos_course_code = '017912J';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Explore the Bachelor of Psychological Science at Flinders University. Learn more about the exciting career opportunities in psychology and related fields. Start your journey today!</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 117300,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.5 Speaking 6.0 Writing 6.0 Listening 6.0 Reading 6.0 Pearson overall 58</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-psychological-science',
    updated_at = NOW()
WHERE cricos_course_code = '077358M';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Create original performances on stage and behind the scenes.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 106500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://flinders.edu.au/study/courses/bachelor-performance-theatre-making',
    updated_at = NOW()
WHERE cricos_course_code = '113438H';
-- ⚠️ Skipped (CRICOS 113438H already emitted): Bachelor of Performance (Directing) | https://flinders.edu.au/study/courses/bachelor-performance-directing

-- ⚠️ Skipped (CRICOS 113438H already emitted): Bachelor of Performance (Acting) | https://www.flinders.edu.au/study/courses/bachelor-performance-acting

UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Discover the exciting world of paramedicine with Flinders University''s Bachelor of Paramedicine. Gain hands-on experience and develop critical skills to become a paramedic.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 127800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 7.0 Writing 7.0 Speaking 7.0 Listening 7.0 Reading 7.0 Pearson overall 65</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-paramedicine',
    updated_at = NOW()
WHERE cricos_course_code = '111908K';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Be bold to face the local and global medical challenges of tomorrow in the rapidly advancing and growing field of laboratory medicine. Discover the competencies required to be a medical scientist equipped with specialist skills and desire for knowledge to work in diagnostic pathology laboratories.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 174000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-of-medical-science-laboratory-medicine',
    updated_at = NOW()
WHERE cricos_course_code = '107262M';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Become a registered nurse with Flinders'' accredited Nursing (Preregistration) degree, featuring clinical placements and flexible study options.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 132900,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 7.0 Writing 6.5 Speaking 7.0 Listening 7.0 Reading 7.0 Pearson overall 63</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-nursing-preregistration',
    updated_at = NOW()
WHERE cricos_course_code = '005195K';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Accelerate your nursing career with Flinders University''s 2-year Bachelor of Nursing (Graduate Entry), designed for graduates from non-nursing disciplines.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 88600,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>English language requirements</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-nursing-graduate-entry',
    updated_at = NOW()
WHERE cricos_course_code = '002701K';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Start a rewarding midwifery career with Flinders'' 3-year degree, featuring hands-on clinical experience and modern facilities.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 132900,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 7.0 Writing 7.0 Speaking 7.0 Listening 7.0 Reading 7.0 Pearson overall 66</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-midwifery-preregistration',
    updated_at = NOW()
WHERE cricos_course_code = '039814G';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Over four years of immersive learning, you’ll deepen your scientific understanding, sharpen your analytical skills, and carry out a significant individual research project that bridges theory and practice in Medical Science.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 174000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-medical-science-honours',
    updated_at = NOW()
WHERE cricos_course_code = '113274A';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Explore the human body with Flinders'' Bachelor of Medical Science. Discover biochemistry, molecular biology, and more while preparing for a range of career pathways.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 130500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-medical-science',
    updated_at = NOW()
WHERE cricos_course_code = '028940C';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>A digital-focused course designed with industry in mind.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 106500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-media-communication',
    updated_at = NOW()
WHERE cricos_course_code = '098433J';
-- ⚠️ Skipped (CRICOS 075594D already emitted): Bachelor of Mathematical Sciences | https://www.flinders.edu.au/study/courses/bachelor-mathematical-sciences

UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Become a lawyer faster with Flinders’ Bachelor of Laws (Honours) – Legal Practice Entry. Build real-world skills and graduate ready for legal practice.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 168800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 7.0 Writing 6.5 Speaking 6.5 Listening 6.5 Reading 6.5 Pearson overall 65</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-laws-honours',
    updated_at = NOW()
WHERE cricos_course_code = '113537E';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Study law and receive legal training with a future-focused, innovative curriculum.</p>',
    course_duration_per_week = 182,
    offshore_tuition_fee = 147700,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 7.0 Writing 6.5 Speaking 6.5 Listening 6.5 Reading 6.5 Pearson overall 65</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-laws',
    updated_at = NOW()
WHERE cricos_course_code = '0100911';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Prepare for a global career.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 106500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-languages',
    updated_at = NOW()
WHERE cricos_course_code = '069017K';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Explore the Bachelor of International Relations and Political Science at Flinders University. Learn more about our program and start your journey towards a rewarding career today!</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 108900,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-international-relations-political-science',
    updated_at = NOW()
WHERE cricos_course_code = '0100840';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Gain hands-on skills in cybersecurity and networking. Learn to protect systems, data and infrastructure with industry-focused IT training.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 130800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-information-technology-network-cybersecurity-systems',
    updated_at = NOW()
WHERE cricos_course_code = '083451G';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Master AI and data-driven tech with a degree in Machine Learning at Flinders Uni. Gain industry experience and global certifications.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 130800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-information-technology-machine-learning',
    updated_at = NOW()
WHERE cricos_course_code = '020067D';
-- ⚠️ Skipped (CRICOS 020067D already emitted): Bachelor of Information Technology (Game Development) | https://www.flinders.edu.au/study/courses/bachelor-information-technology-game-development

UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Study digital forensics and cybercrime investigation. Gain IT and forensic skills for careers in law enforcement, cybersecurity and digital evidence analysis.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 130800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-information-technology-digital-forensics',
    updated_at = NOW()
WHERE cricos_course_code = '111205H';
-- ⚠️ Skipped (CRICOS 020067D already emitted): Bachelor of Information Technology (Data Analytics) | https://www.flinders.edu.au/study/courses/bachelor-information-technology-data-analytics

-- ⚠️ Skipped (CRICOS 020067D already emitted): Bachelor of Information Technology (Business and Information Systems) | https://www.flinders.edu.au/study/courses/bachelor-information-technology-business-information-systems

-- ⚠️ Skipped (CRICOS 020067D already emitted): Bachelor of Information Technology | https://www.flinders.edu.au/study/courses/bachelor-information-technology

UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Study Flinders'' 3-year Human Nutrition degree to explore the link between diet, health, and disease prevention through evidence-based practice.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 138000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.5 Writing 6.0 Speaking 6.0 Listening 6.0 Reading 6.0 Pearson overall 58</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-human-nutrition',
    updated_at = NOW()
WHERE cricos_course_code = '069219M';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Study Physiotherapy to develop skills for a versatile career, focusing on maximising movement and preparing for diverse health settings.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 233500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 7.0 Writing 6.5 Speaking 6.5 Listening 6.5 Reading 6.5 Pearson overall 65 Information about English language requirem</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-health-sciences-master-physiotherapy',
    updated_at = NOW()
WHERE cricos_course_code = '0100688';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Start a healthy career by gaining an excellent grounding in all aspects of the health sector with a particular focus on Ageing, Health Management, Health Promotion or Innovation.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 140100,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-health-sciences',
    updated_at = NOW()
WHERE cricos_course_code = '020920E';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Study the Bachelor of Health Sciences (Vision Science) / Master of Optometry at Flinders University,</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 233500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 7.0 Speaking 6.5 Writing 6.5 Listening 6.5 Reading 6.5 Pearson overall 65 Information about English language requirem</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-health-science-vision-science-master-optometry',
    updated_at = NOW()
WHERE cricos_course_code = '110760M';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Start your amazing journey to become a Surveyor. Study Bachelor of Geospatial Information Systems / Bachelor of Surveying at Flinders.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 174400,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50 Information about</li></ul></td></tr></tbody></table>',
    apply_form = 'https://flinders.edu.au/study/courses/bachelor-geospatial-information-systems-bachelor-surveying',
    updated_at = NOW()
WHERE cricos_course_code = '114450D';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Study GIS at Flinders. Combine maps, drones, and data to solve global challenges in environment, defence, and planning.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 130800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-geospatial-information-systems',
    updated_at = NOW()
WHERE cricos_course_code = '110618F';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Build a career making games.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 106500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>Portfolio, CV and written statement</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-game-design',
    updated_at = NOW()
WHERE cricos_course_code = '118383M';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Learn to make films, documentaries, music videos & commercials, plus uniquely shoot on 16 mm film.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 106500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>Portfolio, CV, interview and written statement</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-film-television-screen-production',
    updated_at = NOW()
WHERE cricos_course_code = '119234E';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Create a TV pilot, gain hands‑on production skills, and graduate with a professional portfolio.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 106500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-film-television-screen-industries',
    updated_at = NOW()
WHERE cricos_course_code = '119233F';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Flinders University’s combined Bachelor of Exercise & Sport Science / Master of Clinical Exercise Physiology is a five-year full-time degree that equips you with in-depth training in exercise science, clinical placements, and accredited skills to prevent and treat chronic and complex health conditions.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 233500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.5 Speaking 6.0 Writing 6.0 Listening 6.0 Reading 6.0 Pearson overall 58</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-exercise-sport-science-master-clinical-exercise-physiology',
    updated_at = NOW()
WHERE cricos_course_code = '105500G';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Study Flinders'' 3-year Exercise & Sport Science degree to boost health and performance with hands-on learning and industry placements.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 140100,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.5 Speaking 6.0 Writing 6.0 Listening 6.0 Reading 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-exercise-sport-science',
    updated_at = NOW()
WHERE cricos_course_code = '091862M';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Flinders University offers this unique course. Find out why it’s one of the best ways to get an industry relevant engineering degree and start your long, successful career now.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 141900,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50 Information about</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-technology-advanced-manufacturing-digital-design',
    updated_at = NOW()
WHERE cricos_course_code = '110754J';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Design the code that runs the world. Study Software Engineering at Flinders and build the future through smart systems, apps and innovation. Apply now!</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 189200,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>SACE stage two general mathematics or equivalent</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-software-honours',
    updated_at = NOW()
WHERE cricos_course_code = '083450J';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Create a career designing the robot workforce of the future. This degree will see you graduate with the latest learning in robotics technologies, preparing you to become a key player in developing the robots that will populate our future.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 236500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50 Information about</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-robotics-honours-master-engineering-electrical-electronic',
    updated_at = NOW()
WHERE cricos_course_code = '105092G';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Build intelligent machines with the Bachelor of Engineering (Robotics) (Honours) at Flinders. Learn to design autonomous systems and launch your future in robotics. Apply now!</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 189200,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>SACE Stage 2 (Year 12) Specialist Mathematics or Mathematical Methods or equivalent International Baccalaureate subjects is normally required</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-robotics-honours',
    updated_at = NOW()
WHERE cricos_course_code = '083449B';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Gain a strong foundation in both the theoretical and the practical aspects of mechanical engineering and engineering management. Find out more.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 236500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50 Information about</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-mechanical-honours-master-engineering-management',
    updated_at = NOW()
WHERE cricos_course_code = '111211K';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Master both mechanical and biomedical engineering with this dual program at Flinders University. Lead innovation in healthcare technologies.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 236500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50 Information about</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-mechanical-honours-master-engineering-biomedical',
    updated_at = NOW()
WHERE cricos_course_code = '083445F';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Design the future of transport, energy and technology. Study Mechanical Engineering at Flinders and turn ideas into powerful real-world solutions.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 189200,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>SACE stage two specialist mathematics or mathematical methods or equivalent</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-mechanical-honours',
    updated_at = NOW()
WHERE cricos_course_code = '083446E';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Navigate the future of maritime engineering with a degree from Flinders University. Gain skills for marine industry careers.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 189200,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>SACE stage two specialist mathematics or mathematical methods or equivalent</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-maritime-honours',
    updated_at = NOW()
WHERE cricos_course_code = '092433B';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Not sure which engineering path to take? Start broad with general entry at Flinders, then specialise later. Build the foundation to become the kind of engineer you want to be.</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 70950,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>SACE stage two general mathematics or SACE stage one mathematics</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-honours-general-entry',
    updated_at = NOW()
WHERE cricos_course_code = '102681K';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Explore your engineering interests with flexible first-year entry at Flinders. Build your skills and choose your specialisation later. Learn more about this adaptable pathway today!</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 47300,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>SACE stage two specialist mathematics or mathematical methods or equivalent</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-honours-flexible-entry',
    updated_at = NOW()
WHERE cricos_course_code = '093042J';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>This combined degree takes all the advantages of being an in-demand environmental engineer and combines it with the knowledge needed to become an accredited civil engineer.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 236500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50 Information about</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-environmental-honours-master-engineering-civil',
    updated_at = NOW()
WHERE cricos_course_code = '105091H';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Tackle the world’s biggest environmental challenges with engineering skills. Study Environmental Engineering at Flinders. Design a greener future—apply now!</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 189200,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>SACE stage two specialist mathematics or mathematical methods or equivalent</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-environmental-honours',
    updated_at = NOW()
WHERE cricos_course_code = '102907H';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Blend electrical, electronic, and mechanical engineering skills at Flinders University. Prepare for interdisciplinary engineering roles.</p>',
    course_duration_per_week = 286,
    offshore_tuition_fee = 260150,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50 Information about</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-electrical-electronic-honours-master-engineering-mechanical',
    updated_at = NOW()
WHERE cricos_course_code = '105090J';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Build a strong foundation in both the theoretical and the practical aspects of engineering and engineering management related to electrical and electronic solutions.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 236500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50 Information about</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-electrical-electronic-honours-master-engineering-management',
    updated_at = NOW()
WHERE cricos_course_code = '111210M';
-- ⚠️ Skipped (CRICOS 102680M already emitted): Bachelor of Engineering (Electrical and Electronic) (Honours) | https://www.flinders.edu.au/study/courses/bachelor-engineering-electrical-electronic-honours

UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Gain a strong foundation in the theoretical and practical aspects of civil engineering and engineering management. Find out more.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 236500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50 Information about</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-civil-honours-master-engineering-management',
    updated_at = NOW()
WHERE cricos_course_code = '111209D';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Design the infrastructure of tomorrow. Study Civil Engineering at Flinders and build your future in transport, water, energy and sustainable construction.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 189200,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>SACE stage two specialist mathematics or mathematical methods or equivalent</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-civil-honours',
    updated_at = NOW()
WHERE cricos_course_code = '083441K';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Advance in biomedical engineering with a combined Bachelor and Master at Flinders University. Innovate in healthcare technology.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 236500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50 Information about</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-biomedical-honours-master-engineering-biomedical',
    updated_at = NOW()
WHERE cricos_course_code = '083440M';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Design life-changing tech with the Biomedical Engineering at Flinders. Graduate career-ready for roles in medtech and innovation. Learn more today!</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS Overall 6.0 Speaking: 6.0 Writing: 6.0 Pearson Overall 50 CRICOS code 083439D</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-engineering-biomedical-honours',
    updated_at = NOW()
WHERE cricos_course_code = '083439D';
-- ⚠️ Skipped (CRICOS 020920E already emitted): Bachelor of Education (Secondary Health and Physical Education) | https://www.flinders.edu.au/study/courses/bachelor-education-secondary-health-physical-education

UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Explore the Bachelor of Education (Secondary) at Flinders University. Learn more about our program and start your journey towards a rewarding career in secondary education today!</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 142800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 7.0 Writing 7.0 Speaking 7.0 Listening 7.0 Reading 7.0 Pearson overall 65</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-education-secondary',
    updated_at = NOW()
WHERE cricos_course_code = '107186G';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Discover Flinders University''s Bachelor of Education (Primary) – a 4-year degree with hands-on placements, no prerequisites, and strong career outcomes. Start your teaching journey today.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 142800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 7.0 Writing 7.0 Speaking 7.0 Listening 7.0 Reading 7.0 Pearson overall 65</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-education-primary',
    updated_at = NOW()
WHERE cricos_course_code = '107185H';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Become a specialist inclusive education teacher, equipped to support students with diverse learning needs.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 142800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 7.0 Writing 7.0 Speaking 7.0 Listening 7.0 Reading 7.0 Pearson overall 65</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-education-inclusive',
    updated_at = NOW()
WHERE cricos_course_code = '117254F';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Study the Bachelor of Early Childhood Education (Birth–8) at Flinders and become a qualified teacher, with hands-on experience to graduate career-ready.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 142800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 7.0 Writing 7.0 Speaking 7.0 Listening 7.0 Reading 7.0 Pearson overall 65</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-early-childhood-education-birth-8',
    updated_at = NOW()
WHERE cricos_course_code = '107184J';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Discover the rewarding career opportunities in early childhood education with a Bachelor of Early Childhood Education (Birth to 5) at Flinders University. Learn more about our program today!</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 107100,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 7.0 Writing 7.0 Speaking 7.0 Listening 7.0 Reading 7.0 Pearson overall 65</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-early-childhood-education-birth-5',
    updated_at = NOW()
WHERE cricos_course_code = '116862A';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Gain skills to support people with disabilities through Flinders'' accredited BDDE degree, with practical placements and inclusive education.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 186800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-disability-developmental-education',
    updated_at = NOW()
WHERE cricos_course_code = '058482J';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Study Flinders'' 3-year Disability & Community Inclusion degree to become a skilled practitioner, with pathways for further specialisation.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 140100,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-disability-community-inclusion',
    updated_at = NOW()
WHERE cricos_course_code = '102685F';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Advance your criminology expertise with Flinders'' Bachelor of Criminology (Honours). Gain in-depth knowledge and research skills for careers in justice, policy, and social change.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 145200,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-criminology-honours',
    updated_at = NOW()
WHERE cricos_course_code = '096843G';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Discover the exciting world of criminology at Flinders University. Learn about crime prevention, law enforcement, and criminal justice. Start your journey today!</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 108900,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-criminology',
    updated_at = NOW()
WHERE cricos_course_code = '092879E';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Write your own future.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 106500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-creative-writing',
    updated_at = NOW()
WHERE cricos_course_code = '119232G';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Explore our VET pathway options to enter into the Bachelor of Creative Arts (Fashion) and start a bespoke career in the fashion industry.</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 53250,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Pearson overall 50 Information about</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-creative-arts-fashion-vet-pathway',
    updated_at = NOW()
WHERE cricos_course_code = '091846M';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Stitch together the skills for a career in this trillion-dollar industry.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 106500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-creative-arts-fashion',
    updated_at = NOW()
WHERE cricos_course_code = '115226D';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Bring characters to life through costume design.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 106500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-creative-arts-costume-design',
    updated_at = NOW()
WHERE cricos_course_code = '115225E';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Learn AI, robotics, and machine learning. Gain skills for smart tech careers with industry placements and ACS accreditation.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 130800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>SACE stage two general mathematics or equivalent.</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-computer-science-artificial-intelligence',
    updated_at = NOW()
WHERE cricos_course_code = '064064K';
-- ⚠️ Skipped (CRICOS 064064K already emitted): Bachelor of Computer Science | https://www.flinders.edu.au/study/courses/bachelor-computer-science

UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Flinders Bachelor of Commerce degree equips you with a diverse range of work-ready skills to prepare you for a professional career in private and public enterprise. Apply today.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 117000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-commerce',
    updated_at = NOW()
WHERE cricos_course_code = '002627D';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Fast-track your medical career with Flinders'' 6-year Clinical Sciences and Medicine degree. Gain hands-on experience and training for medical registration.</p>',
    course_duration_per_week = 312,
    offshore_tuition_fee = 313800,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 7.0 Writing 7.0 Speaking 7.0 Listening 7.0 Reading 7.0 Pearson overall 65</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-clinical-sciences-doctor-medicine',
    updated_at = NOW()
WHERE cricos_course_code = '080922F';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Study Sports Management with a Bachelor of Business at Flinders University. Gain skills and direct access to industry to shape the game behind-the-scenes.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 117000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-business/sports-management',
    updated_at = NOW()
WHERE cricos_course_code = '058294B';
-- ⚠️ Skipped (CRICOS 058294B already emitted): Bachelor of Business majoring in Small Business Leadership | https://www.flinders.edu.au/study/courses/bachelor-business/small-business-leadership

-- ⚠️ Skipped (CRICOS 058294B already emitted): Bachelor of Business majoring in Marketing | https://www.flinders.edu.au/study/courses/bachelor-business/marketing

-- ⚠️ Skipped (CRICOS 058294B already emitted): Bachelor of Business majoring in Management | https://www.flinders.edu.au/study/courses/bachelor-business/management

-- ⚠️ Skipped (CRICOS 058294B already emitted): Bachelor of Business majoring in Leading Change | https://www.flinders.edu.au/study/courses/bachelor-business/leading-change

-- ⚠️ Skipped (CRICOS 058294B already emitted): Bachelor of Business majoring in International Business | https://www.flinders.edu.au/study/courses/bachelor-business/international-business

-- ⚠️ Skipped (CRICOS 058294B already emitted): Bachelor of Business majoring in Human Resource Management | https://www.flinders.edu.au/study/courses/bachelor-business/human-resource-management

-- ⚠️ Skipped (CRICOS 058294B already emitted): Bachelor of Business majoring in Event Management and Tourism | https://www.flinders.edu.au/study/courses/bachelor-business/event-management-tourism

UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Discover the exciting world of business analytics at Flinders University. Learn more about our Bachelor of Business Analytics program today.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = NULL,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS Overall 6.0 Speaking: 6.0 Writing: 6.0 Pearson Overall 50 CRICOS code 116920G</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-business-analytics',
    updated_at = NOW()
WHERE cricos_course_code = '116920G';
-- ⚠️ Skipped (CRICOS 058294B already emitted): Bachelor of Business | https://www.flinders.edu.au/study/courses/bachelor-business

UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Study arts and science together in one flexible degree. Combine creativity and scientific inquiry to build broad, versatile skills for tomorrow’s world.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 130500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-arts-science',
    updated_at = NOW()
WHERE cricos_course_code = '088518J';
-- ⚠️ Skipped (CRICOS 002633F already emitted): Bachelor of Arts | https://www.flinders.edu.au/study/courses/bachelor-arts

UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Your future lies in the past.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 106500,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-archaeology',
    updated_at = NOW()
WHERE cricos_course_code = '024778G';
UPDATE courses SET
    course_description = '<h4>Overview</h4><p>Discover the Bachelor of Accounting at Flinders University. Learn more about our program and start your journey towards a successful career in accounting.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 117000,
    onshore_tuition_fee = NULL,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall 6.0 Speaking 6.0 Writing 6.0 Pearson overall 50</li></ul></td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.flinders.edu.au/study/courses/bachelor-accounting',
    updated_at = NOW()
WHERE cricos_course_code = '058295A';
