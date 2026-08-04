-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'January, February, July, September, October',
    updated_at = NOW()
WHERE cricos_provider_code = '00122A';

UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Push creative boundaries with this honours degree. Build your fine art practice, supported by teachers with local and international experience.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 43200,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-arts-fine-art-honours-bh052',
    updated_at = NOW()
WHERE cricos_course_code = '006591A';
-- Register-only (no site match): Bachelor of Arts (Photography)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 135360,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '006593K';
-- Register-only (no site match): Bachelor of Fashion (Design) (Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 48000,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '0100706';
-- Register-only (no site match): Bachelor of Textiles (Design)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 149760,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '0100707';
-- Register-only (no site match): Bachelor of Fashion (Enterprise)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 149760,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '0100708';
-- Register-only (no site match): Bachelor of Fashion (Design)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 149760,
    enrolment_fee = 1259,
    updated_at = NOW()
WHERE cricos_course_code = '0100709';
-- Register-only (no site match): Bachelor of Fashion and Textiles (Sustainable Innovation)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 149760,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '0100710';
-- Register-only (no site match): Graduate Diploma in Early Childhood Education
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 38400,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '0100711';
-- Register-only (no site match): Bachelor of Engineering (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '0100714';
-- Register-only (no site match): Master of Artificial Intelligence
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '0100716';
-- Register-only (no site match): Graduate Certificate in Fashion (Entrepreneurship)
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 22080,
    enrolment_fee = 186,
    updated_at = NOW()
WHERE cricos_course_code = '0100717';
-- Register-only (no site match): Graduate Diploma of Fashion (Entrepreneurship)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 45120,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '0100718';
-- Register-only (no site match): Master of Interior Design
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 101760,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '0100719';
-- Register-only (no site match): Bachelor of Science (Dean's Scholar, Food Science) (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 188160,
    enrolment_fee = 4140,
    updated_at = NOW()
WHERE cricos_course_code = '0100986';
-- Register-only (no site match): Master of Fashion (Design)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '0100990';
-- Register-only (no site match): Bachelor of International Studies
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 119520,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '0100991';
-- Register-only (no site match): Bachelor of International Studies (Development)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 119520,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '0100992';
-- Register-only (no site match): Bachelor of International Studies (Global Security)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 119520,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '0100993';
-- Register-only (no site match): Bachelor of International Studies (Languages)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 119520,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '0100994';
-- Register-only (no site match): Bachelor of Science (Biology) (Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '0101485';
-- Register-only (no site match): Bachelor of Science (Biotechnology) (Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '0101486';
-- Register-only (no site match): Bachelor of Science (Chemistry) (Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '0101487';
-- Register-only (no site match): Bachelor of Science (Environmental Science) (Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '0101488';
-- Register-only (no site match): Bachelor of Science (Physics) (Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '0101489';
-- Register-only (no site match): Bachelor of Science (Mathematics and Statistics) (Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '0101490';
-- Register-only (no site match): Bachelor of Science (Computer Science) (Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '0101491';
-- Register-only (no site match): Bachelor of Science (Food Technology) (Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '0101492';
-- Register-only (no site match): Bachelor of Criminal Justice
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 119520,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '012347G';
-- Register-only (no site match): Bachelor of Design (Communication Design)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 146880,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '012348F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This skills-focused journalism course combines practical and academic learning and gives you the skills needed to work in journalism and writing.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 37440,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-diplomas/graduate-diploma-in-journalism-gd074',
    updated_at = NOW()
WHERE cricos_course_code = '012959A';
-- Register-only (no site match): Graduate Diploma in Marketing
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 50400,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '014891M';
-- Register-only (no site match): International Study Program
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 24960,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '018594K';
-- Register-only (no site match): Bachelor of Applied Science (Aviation)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 149760,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '022041J';
-- Register-only (no site match): Bachelor of Nursing
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '023212J';
-- Register-only (no site match): Bachelor of Environment and Society
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 119520,
    enrolment_fee = 3165,
    updated_at = NOW()
WHERE cricos_course_code = '027119G';
-- Register-only (no site match): Graduate Diploma in Engineering Management
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 32640,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '029677E';
-- Register-only (no site match): Bachelor of Applied Science (Psychology)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '029765E';
-- Register-only (no site match): Bachelor of Social Science (Psychology)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 119520,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '035023D';
-- Register-only (no site match): Bachelor of Applied Science (Psychology) (Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '037200J';
-- Register-only (no site match): Bachelor of Business (Entrepreneurship)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 144480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '037963K';
-- Register-only (no site match): Graduate Diploma in Information Management
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 37440,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '039479F';
-- Register-only (no site match): Bachelor of Environmental Science/Bachelor of Business Management
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 183600,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '043570K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain high level skills in gene and protein technologies, bioinformatics, and various microbiology and food science disciplines.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-biotechnology-mc111',
    updated_at = NOW()
WHERE cricos_course_code = '045512D';
-- Register-only (no site match): Bachelor of Environmental Science/Bachelor of Environment and Society
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 172800,
    enrolment_fee = 4140,
    updated_at = NOW()
WHERE cricos_course_code = '048147G';
-- Register-only (no site match): Bachelor of Communication (Professional Communication)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 132480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '048665G';
-- Register-only (no site match): Bachelor of Communication (Public Relations)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 132480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '048666F';
-- Register-only (no site match): Bachelor of Communication (Media)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 132480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '048667E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain a thorough and practical understanding of media, develop invaluable skills and contacts, and take part in live productions of radio and television.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 132480,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-journalism-bp220',
    updated_at = NOW()
WHERE cricos_course_code = '048668D';
-- Register-only (no site match): Bachelor of Communication (Professional Communication)
UPDATE courses SET
    course_duration_per_week = 130,
    offshore_tuition_fee = 132480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '048722C';
-- Register-only (no site match): Bachelor of Science (Food Technology and Nutrition)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '048768M';
-- Register-only (no site match): Graduate Diploma of Commerce
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 50400,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '048770F';
-- Register-only (no site match): Bachelor of Legal and Dispute Studies
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 119520,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '052088A';
-- Register-only (no site match): Bachelor of Business (Management)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 144480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '052377C';
-- Register-only (no site match): International Study Program
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = NULL,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '053516M';
-- Register-only (no site match): Master of Cyber Security
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '055526D';
-- Register-only (no site match): Graduate Diploma in Professional Accounting
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 50400,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '055528B';
-- Register-only (no site match): Bachelor of Communication (Media)
UPDATE courses SET
    course_duration_per_week = 130,
    offshore_tuition_fee = 132480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '055813G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Take your biomedical science degree and use it to further your skills in medical laboratory science with this Master of Laboratory Medicine.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-laboratory-medicine-mc158',
    updated_at = NOW()
WHERE cricos_course_code = '056171G';
-- Register-only (no site match): Bachelor of Science (Biotechnology)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 136320,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '056416B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Get a headstart to become a social worker with a postgraduate course. Masters graduates are resilient, outspoken people who advocate for a fairer world.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-social-work-mc150',
    updated_at = NOW()
WHERE cricos_course_code = '058234C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Master corporate decision-making and build your problem-solving and leadership skills by enrolling in RMIT''s Executive Master of Business Administration.</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 82080,
    enrolment_fee = 559,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/executive-master-of-business-administration-mc162',
    updated_at = NOW()
WHERE cricos_course_code = '058615A';
-- Register-only (no site match): Graduate Diploma in Finance
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 50400,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '060584G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Take the next step to becoming a design architect with professional accreditation. Complete your masters in this internationally renowned program at RMIT.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 107520,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-architecture-mc163',
    updated_at = NOW()
WHERE cricos_course_code = '060829B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain the skills you need to be a leading architect. Work on real-world briefs and study in a world-class studio environment to create something that lasts.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 155520,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-architectural-design-bp250',
    updated_at = NOW()
WHERE cricos_course_code = '060830J';
-- Register-only (no site match): Bachelor of Computer Science
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '061076G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Immerse yourself in furniture design and learn to create sustainable, modern furniture and related products.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 76800,
    enrolment_fee = 1315,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/associate-degrees/associate-degree-in-design-furniture-ad007',
    updated_at = NOW()
WHERE cricos_course_code = '061154K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Use your advanced bilingual skills and understand underlying theories and industrial issues in this graduate interpreter and translator course.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 39840,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-diplomas/graduate-diploma-in-translating-and-interpreting-gd168',
    updated_at = NOW()
WHERE cricos_course_code = '061260G';
-- Register-only (no site match): Bachelor of Business (Professional Accountancy)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 197760,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '062993G';
-- Register-only (no site match): Bachelor of Business (Accountancy)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 144480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '063095M';
-- Register-only (no site match): Bachelor of Business (International Business)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 144480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '063096K';
-- Register-only (no site match): Bachelor of Business (International Business) (Applied)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 172800,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '063197E';
-- Register-only (no site match): Bachelor of Business (Economics and Finance)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 151200,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '063198D';
-- Register-only (no site match): Bachelor of Business (Economics and Finance) (Applied)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 197760,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '063199C';
-- Register-only (no site match): Bachelor of Business (Marketing)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 144480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '063200D';
-- Register-only (no site match): Bachelor of Business (Marketing) (Applied)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 197760,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '063201C';
-- Register-only (no site match): Bachelor of Business (Logistics and Supply Chain Management)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 144480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '063202B';
-- Register-only (no site match): Bachelor of Business (Logistics and Supply Chain Management) (Applied)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 197760,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '063203A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Become a leader and innovator in landscape architecture practice with this award-winning course. Explore landscape as a medium that exists at all scales.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 101760,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-landscape-architecture-mc172',
    updated_at = NOW()
WHERE cricos_course_code = '064392E';
-- Register-only (no site match): Bachelor of Communication (Advertising)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 132480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '064394C';
-- Register-only (no site match): Bachelor of Business (Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 46080,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '064712E';
-- Register-only (no site match): Bachelor of Arts (Creative Writing)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 132480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '065130G';
-- Register-only (no site match): Bachelor of Arts (Music Industry)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 129600,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '065131G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop design, construction and management skills in natural, urban, private and public spaces with a Landscape Architecture course at RMIT.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 149760,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-landscape-architectural-design-bp256',
    updated_at = NOW()
WHERE cricos_course_code = '066833B';
-- Register-only (no site match): Bachelor of Biomedical Science
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 144000,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '068159D';
-- Register-only (no site match): Bachelor of Information Technology
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '068389A';
-- Register-only (no site match): Bachelor of Science (Applied Sciences) (Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '068390G';
-- Register-only (no site match): Associate Degree in Information Technology
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 81600,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '071307D';
-- Register-only (no site match): Associate Degree in Applied Science
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 76320,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '071869C';
-- Register-only (no site match): Associate Degree in Fashion and Textile Merchandising
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 76800,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '071874F';
-- Register-only (no site match): Master of Engineering (Electrical and Electronic Engineering)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '072752G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This program prepares registered nurses for specialty mental health nursing practice.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 37440,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-diplomas/graduate-diploma-in-mental-health-nursing-gd158',
    updated_at = NOW()
WHERE cricos_course_code = '073315K';
-- Register-only (no site match): Bachelor of Science (Applied Chemistry)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '074349C';
-- Register-only (no site match): Bachelor of Science (Physics)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '074351J';
-- Register-only (no site match): Bachelor of Science (Biological Sciences)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '074352G';
-- Register-only (no site match): Associate Degree in Fashion Design and Technology
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 76800,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '074685J';
-- Register-only (no site match): Master of Statistics and Operations Research
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '074919G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Expand your abilities and further investigate your specialisation using advanced research and project skills in this media and communication honours course</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 42240,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-media-and-communication-honours-bh066',
    updated_at = NOW()
WHERE cricos_course_code = '074925J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Explore your creativity while developing essential writing and editing skills to become a published author, editor and/or communications professional.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 76320,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/associate-degrees/associate-degree-in-professional-writing-and-editing-ad016',
    updated_at = NOW()
WHERE cricos_course_code = '074927G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Turn your passion into a career. Explore the creative and technical elements of game design and develop your artistic practice.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 146880,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-games-bp214',
    updated_at = NOW()
WHERE cricos_course_code = '074978G';
-- Register-only (no site match): Graduate Diploma in Business Information Technology
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 49440,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '076022K';
-- Register-only (no site match): Bachelor of Business (Human Resource Management)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 144480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '076961M';
-- Register-only (no site match): Bachelor of Science (Biotechnology)/Bachelor of Biomedical Science
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 188160,
    enrolment_fee = 3538,
    updated_at = NOW()
WHERE cricos_course_code = '076962K';
-- Register-only (no site match): Bachelor of Science (Food Technology)/Bachelor of Business (Management)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 211680,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '076963J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Become a licensed commercial pilot and gain the skills needed to apply for other licences with our practical, accredited flight training course.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 167040,
    enrolment_fee = 1027,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/associate-degrees/associate-degree-in-aviation-professional-pilots-ad023',
    updated_at = NOW()
WHERE cricos_course_code = '077041K';
-- Register-only (no site match): Bachelor of Health Science / Bachelor of Applied Science (Chinese Medicine)
UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 239040,
    enrolment_fee = 1865,
    updated_at = NOW()
WHERE cricos_course_code = '077042J';
-- Register-only (no site match): Bachelor of Health Science / Bachelor of Applied Science (Osteopathy)
UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 239040,
    enrolment_fee = 1865,
    updated_at = NOW()
WHERE cricos_course_code = '077043G';
-- Register-only (no site match): Bachelor of Health Science / Bachelor of Applied Science (Chiropractic)
UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 239040,
    enrolment_fee = 1865,
    updated_at = NOW()
WHERE cricos_course_code = '077044G';
-- Register-only (no site match): Bachelor of Applied Science (Aviation)/ Bachelor of Business (Management)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 228960,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '077047D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>A professionally accredited accounting degree aimed at graduates of non-accounting disciplines who want to broaden their career prospects.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 103680,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-professional-accounting-mc194',
    updated_at = NOW()
WHERE cricos_course_code = '077509A';
-- Register-only (no site match): Master of Information Management
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 105600,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '077511G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This program provides current or aspiring managers with high-level skills in planning, directing, implementing and monitoring an organisation''s marketing.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 103680,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-marketing-mc197',
    updated_at = NOW()
WHERE cricos_course_code = '077512F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Build on your background in chemistry or physics to explore a range of nanotechnology applications in this industry-focused postgraduate course.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 103680,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-supply-chain-and-logistics-management-mc198',
    updated_at = NOW()
WHERE cricos_course_code = '077513E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>A Master of Business Administration (MBA) gives you an edge as you build a career with skills to solve real life problems with design thinking methodology.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 106080,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-business-administration-mc199',
    updated_at = NOW()
WHERE cricos_course_code = '077514D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain the skills to develop business information systems solutions and prepare for in-demand careers in business IT and information systems.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 101760,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-business-information-technology-mc200',
    updated_at = NOW()
WHERE cricos_course_code = '077515C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Building your understanding of econometrics and financial markets with the Master of Finance and prepare to lead in banker and finance manager roles.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 103680,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-finance-mc201',
    updated_at = NOW()
WHERE cricos_course_code = '077516B';
-- Register-only (no site match): Master of Commerce
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 103680,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '077517A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study the intersection between criminology and psychology in a course that covers the fundamentals of forensic studies, policing, youth justice and crimino</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 119520,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-criminology-and-psychology-bp295',
    updated_at = NOW()
WHERE cricos_course_code = '077658K';
-- Register-only (no site match): Master of Environmental Science and Technology
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 1142,
    updated_at = NOW()
WHERE cricos_course_code = '077662C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Join this industry-focused degree and work as a residential or commercial designer or decorator.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 76320,
    enrolment_fee = 1027,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/associate-degrees/associate-degree-in-interior-decoration-and-design-ad020',
    updated_at = NOW()
WHERE cricos_course_code = '078836M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study an Associate Degree in Graphic Design course. Develop specialist technical and creative skills to start your own business or work for design firms.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 76800,
    enrolment_fee = 1746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/associate-degrees/associate-degree-in-graphic-design-ad022',
    updated_at = NOW()
WHERE cricos_course_code = '078839G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study television, film and media production courses in this industry-focused Associate Degree. Learn from experts and kickstart your screen and media caree</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 76320,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/associate-degrees/associate-degree-in-screen-and-media-production-ad017',
    updated_at = NOW()
WHERE cricos_course_code = '078871G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Shape the future of our cities with a Master of Urban Design at RMIT. Explore models for future city-building through project-based coursework.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 108120,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-urban-design-mc193',
    updated_at = NOW()
WHERE cricos_course_code = '078873F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain the skills required to investigate complex problems and address the important challenges of sustainable international business.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 103680,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-international-business-mc192',
    updated_at = NOW()
WHERE cricos_course_code = '078875D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Become a master of interpreting and translating and deepen your understanding of language and communication in this world-class degree.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-translating-and-interpreting-mc214',
    updated_at = NOW()
WHERE cricos_course_code = '079083F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop cross-media skills in video, audio and media production with this postgraduate media course, and become a strategic leader in an evolving industry.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 90240,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-media-mc188',
    updated_at = NOW()
WHERE cricos_course_code = '079084E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Build the capabilities, knowledge, and confidence to create your own fashion enterprise and build a career within the global fashion industry.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-fashion-entrepreneurship-mc213',
    updated_at = NOW()
WHERE cricos_course_code = '079302M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Build core skills choose from a speciality in aerospace, civil, computer and networking, automation, mechatronics engineering, and more.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 83040,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/associate-degrees/associate-degree-in-engineering-technology-ad026',
    updated_at = NOW()
WHERE cricos_course_code = '079303K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Do meaningful work and explore human behaviour. Explore human behaviour, advocacy, social theory, economics and more.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1865,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-social-work-honoursbachelor-of-social-science-psychology-bh106',
    updated_at = NOW()
WHERE cricos_course_code = '079592G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study a postgraduate masters course in public policy to deepen your understanding of critical societal issues and engage in policy development in Melbourne.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-public-policy-mc216',
    updated_at = NOW()
WHERE cricos_course_code = '079593F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain highly sought after skills in crime management with Melbourne criminology masters courses that are designed by industry.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-justice-and-criminology-mc223',
    updated_at = NOW()
WHERE cricos_course_code = '079595D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover an essential role in social justice and advocacy. Reflect on core issues, explore social theory and politics, and create meaningful change.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 161280,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-social-work-honours-bh105',
    updated_at = NOW()
WHERE cricos_course_code = '079596C';
-- Register-only (no site match): Bachelor of Engineering (Biomedical Engineering) (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1608,
    updated_at = NOW()
WHERE cricos_course_code = '079597B';
-- Register-only (no site match): Bachelor of Engineering (Electrical Engineering) (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1608,
    updated_at = NOW()
WHERE cricos_course_code = '079598A';
-- Register-only (no site match): Bachelor of Engineering (Computer and Network Engineering) (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '079618B';
-- Register-only (no site match): Bachelor of Engineering (Electrical and Electronic Engineering) (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '079620G';
-- Register-only (no site match): Bachelor of Engineering (Computer and Network Engineering) (Honours) / Bachelor of Computer Science
UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 284064,
    enrolment_fee = 1981,
    updated_at = NOW()
WHERE cricos_course_code = '079622F';
-- Register-only (no site match): Bachelor of Engineering (Civil and Infrastructure) (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '079625C';
-- Register-only (no site match): Bachelor of Engineering (Chemical Engineering) (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '079626B';
-- Register-only (no site match): Bachelor of Engineering (Environmental Engineering) (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '079627A';
-- Register-only (no site match): Bachelor of Engineering (Civil and Infrastructure) (Honours) / Bachelor of Business (Management)
UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 277608,
    enrolment_fee = 1865,
    updated_at = NOW()
WHERE cricos_course_code = '079629K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In this program you will develop advanced skills in order to critically analyse information, synthesise knowledge, and communicate your research findings effectively for a variety of career settings.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-business-economics-finance--marketing-mr203',
    updated_at = NOW()
WHERE cricos_course_code = '079679M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Use your advanced research skills to contribute to new developments in applied physics.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 172800,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-applied-physics-dr230',
    updated_at = NOW()
WHERE cricos_course_code = '079680G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your advanced research skills and contribute to new developments in applied physics.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 82560,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-science-applied-physics-mr230',
    updated_at = NOW()
WHERE cricos_course_code = '079681F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In this program you will develop advanced skills in order to critically analyse information, synthesise knowledge, and communicate your research findings effectively for a variety of career settings.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-business-management-mr204',
    updated_at = NOW()
WHERE cricos_course_code = '079682E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Use your advanced research skills to contribute to new developments in applied biology and biotechnology.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 172800,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-applied-biology--biotechnology-dr231',
    updated_at = NOW()
WHERE cricos_course_code = '079683D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your advanced research skills and contribute to new developments in biomedical sciences.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 82560,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-science-applied-biology--biotechnology-mr231',
    updated_at = NOW()
WHERE cricos_course_code = '079684C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Use your advanced research skills to contribute to new developments in food sciences and nutrition.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 172800,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-food-science-dr232',
    updated_at = NOW()
WHERE cricos_course_code = '079685B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In this program you will develop advanced skills in order to critically analyse information, synthesise knowledge, and communicate your research findings effectively for a variety of career settings.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-business-business--law-mr205',
    updated_at = NOW()
WHERE cricos_course_code = '079686A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your advanced research skills and contribute to new developments in food sciences.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 82560,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-science-food-science-mr232',
    updated_at = NOW()
WHERE cricos_course_code = '079687M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The School of Architecture and Design is widely recognised for innovative leadership and contribution to excellence in design research.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-design-architecture--design-mr207',
    updated_at = NOW()
WHERE cricos_course_code = '079688K';
-- Register-only (no site match): Doctor of Philosophy (Biomedical Science)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 168960,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '079689J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This research degree offers an environment where the investigation of ideas and material practice pertinent to artistic research sits alongside and informs the production of art.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 78720,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-fine-art-mr208',
    updated_at = NOW()
WHERE cricos_course_code = '079690E';
-- Register-only (no site match): Master of Science (Biomedical Science)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '079691D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Shape the future of education with a Master of Education by Research promoting the interdependence of research, learning and change.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 72960,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-education-mr209',
    updated_at = NOW()
WHERE cricos_course_code = '079692C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This research degree develops advanced research principles, methods and mastery of a body of knowledge in the social sciences by completing a thesis or research project.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 72960,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-social-science-global-urban--social-studies-mr210',
    updated_at = NOW()
WHERE cricos_course_code = '079693B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Master of Design (Fashion and Textiles) by Research program enables you to develop an advanced body of knowledge that you may apply to a range of stimulating, real-life research contexts.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 78720,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-design-fashion--textiles-mr213',
    updated_at = NOW()
WHERE cricos_course_code = '079694A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Master of Technology (Fashion and Textiles) by Research program enables you to develop an advanced body of knowledge that you may apply to a range of stimulating, real-life research contexts.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 78720,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-technology-fashion--textiles-mr214',
    updated_at = NOW()
WHERE cricos_course_code = '079695M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your advanced engineering skills and contribute to industry focused research projects, identifying real-world solutions to electrical and electronic engineering problems.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 88320,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-engineering-electrical--electronic-engineering-mr220',
    updated_at = NOW()
WHERE cricos_course_code = '079696K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Further your research skills and contribute to advancements in computer science.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-science-computer-science-mr221',
    updated_at = NOW()
WHERE cricos_course_code = '079697J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Use your advanced research skills to contribute to new developments in radiotherapy, diagnostic medical procedures and health physics.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 82560,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-applied-science-health--medical-physics-mr233',
    updated_at = NOW()
WHERE cricos_course_code = '079700G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>NB: DR213 replaces the previous qualification of DR074.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 165120,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-fashion--textiles-dr213',
    updated_at = NOW()
WHERE cricos_course_code = '079719G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Apply your advanced engineering skills to industry focused research projects, identifying real-world solutions to electrical and electronic engineering problems.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 184320,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-electrical--electronic-engineering-dr220',
    updated_at = NOW()
WHERE cricos_course_code = '079720D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Use your advanced research skills to further the growth and development of computer science.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 168960,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-computer-science-dr221',
    updated_at = NOW()
WHERE cricos_course_code = '079721C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Join an active research community and work with academics, peers and partner organisations with demonstrated research success in a range of specialities.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 172800,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-mathematical-sciences-dr222',
    updated_at = NOW()
WHERE cricos_course_code = '079726J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Use your advanced research skills at the forefront of geospatial sciences development and implementation.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 172800,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-geospatial-sciences-dr223',
    updated_at = NOW()
WHERE cricos_course_code = '079727G';
-- Register-only (no site match): Doctor of Philosophy (Complementary Medicine)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 168960,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '079728G';
-- Register-only (no site match): Doctor of Philosophy (Nursing)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 168960,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '079729F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Apply your advanced research skills to understand the complexities of psychology and tackle key health challenges.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 168960,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-psychology-dr226',
    updated_at = NOW()
WHERE cricos_course_code = '079730B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In this program you will develop advanced skills in order to critically analyse information, synthesise knowledge, and communicate your research findings effectively for a variety of career settings.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-business-accountancy-mr200',
    updated_at = NOW()
WHERE cricos_course_code = '079731A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop advanced skills in order to critically analyse information, synthesise knowledge, and communicate your research findings.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-business-business-information-systems-mr201',
    updated_at = NOW()
WHERE cricos_course_code = '079732M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In this program you will develop advanced skills in order to critically analyse information, synthesise knowledge, and communicate your research findings effectively for a variety of career settings.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-business-supply-chain-logistics-mr202',
    updated_at = NOW()
WHERE cricos_course_code = '079733K';
-- Register-only (no site match): Bachelor of Engineering (Advanced Manufacturing and Mechatronics) (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1608,
    updated_at = NOW()
WHERE cricos_course_code = '079772C';
-- Register-only (no site match): Bachelor of Engineering (Mechanical Engineering) (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '079773B';
-- Register-only (no site match): Bachelor of Engineering (Automotive Engineering) (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '079774A';
-- Register-only (no site match): Bachelor of Engineering (Sustainable Systems Engineering) (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '079775M';
-- Register-only (no site match): Bachelor of Engineering (Aerospace Engineering) (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1608,
    updated_at = NOW()
WHERE cricos_course_code = '079776K';
-- Register-only (no site match): Bachelor of Engineering (Aerospace Engineering) (Honours) / Bachelor of Business (Management)
UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 284064,
    enrolment_fee = 1865,
    updated_at = NOW()
WHERE cricos_course_code = '079778G';
-- Register-only (no site match): Bachelor of Engineering (Automotive Engineering) (Honours) / Bachelor of Business (Management)
UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 284064,
    enrolment_fee = 1865,
    updated_at = NOW()
WHERE cricos_course_code = '079779G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Blend technical and creative skills to design and build specialist machinery and systems.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 284064,
    enrolment_fee = 1865,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineering-mechanical-engineering-honoursbachelor-of-industrial-design-honours-bh093',
    updated_at = NOW()
WHERE cricos_course_code = '079785J';
-- Register-only (no site match): Bachelor of Environmental Science / Bachelor of Engineering (Environmental Engineering) (Honours)
UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 239040,
    enrolment_fee = 4117,
    updated_at = NOW()
WHERE cricos_course_code = '079786G';
-- Register-only (no site match): Bachelor of Science (Applied Chemistry) / Bachelor of Engineering (Chemical Engineering) (Honours)
UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 239040,
    enrolment_fee = 1865,
    updated_at = NOW()
WHERE cricos_course_code = '079787G';
-- Register-only (no site match): Bachelor of Engineering (Sustainable Systems Engineering) (Honours) / Bachelor of Industrial Design (Honours)
UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 284064,
    enrolment_fee = 1865,
    updated_at = NOW()
WHERE cricos_course_code = '079789E';
-- Register-only (no site match): Bachelor of Science (Dean's Scholar) (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 188160,
    enrolment_fee = 4140,
    updated_at = NOW()
WHERE cricos_course_code = '079790A';
-- Register-only (no site match): Bachelor of Pharmacy (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 207360,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '079791M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In this program you will develop advanced research skills that will prepare you for a career in academia and other settings in which systematic and critical analytical skills are required.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 168960,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-accountancy-dr200',
    updated_at = NOW()
WHERE cricos_course_code = '079794G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your ICT skills and knowledge with the Master of Information Technology, and apply cutting-edge technology to provide solutions across industries.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-information-technology-mc208',
    updated_at = NOW()
WHERE cricos_course_code = '079795G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study this postgraduate project management degree and advance your skills for successfully delivering complex projects across many industries.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 103680,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-project-management-mc210',
    updated_at = NOW()
WHERE cricos_course_code = '079796F';
-- Register-only (no site match): Master of Engineering (Manufacturing)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '079797E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In this program you will develop advanced research skills that will prepare you for a career in academia and other settings in which systematic and critical analytical skills are required.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 168960,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-business-information-systems-dr201',
    updated_at = NOW()
WHERE cricos_course_code = '079798D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Take charge with a postgraduate engineering management degree. Develop strategic thinking, innovation, and problem-solving skills.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-engineering-management-mc226',
    updated_at = NOW()
WHERE cricos_course_code = '079801C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In this program you will develop advanced research skills that will prepare you for a career in academia and other settings in which systematic and critical analytical skills are required.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 168960,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-economics-finance--marketing-dr203',
    updated_at = NOW()
WHERE cricos_course_code = '079802B';
-- Register-only (no site match): Master of Engineering (Electronic Engineering)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '079804M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In this program you will develop advanced research skills that will prepare you for a career in academia and other settings in which systematic and critical analytical skills are required.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 168960,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-management-dr204',
    updated_at = NOW()
WHERE cricos_course_code = '079805K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In the business PhD program you will develop advanced research skills that will prepare you for a career in academia and other settings in which systematic and critical analytical skills are required.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 168960,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-business-dr205',
    updated_at = NOW()
WHERE cricos_course_code = '079807G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In the law PhD program you will develop advanced research skills that will prepare you for a career in academia and other settings in which systematic and critical analytical skills are required.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 168960,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-law-dr206',
    updated_at = NOW()
WHERE cricos_course_code = '079808G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The School of Architecture and Urban Design is widely recognised for innovative leadership and contribution to excellence in design research.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 192000,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-architecture--design-dr207',
    updated_at = NOW()
WHERE cricos_course_code = '079809F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This project-based Doctor of Philosophy (PhD) research degree will provide the framework, the focus and the discipline necessary to conduct speculative inquiry in the field of art.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 165120,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-art-dr208',
    updated_at = NOW()
WHERE cricos_course_code = '079810B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Shape the future of education with a Doctor of Philosophy (PhD) in Education by promoting the interdependence of research, learning and change</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 153600,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-education-dr209',
    updated_at = NOW()
WHERE cricos_course_code = '079811A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Doctor of Philosophy (PhD) in the humanities and social sciences cultivates high-level skills in research processes, advanced communication skills, analysis and synthesis of knowledge.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 153600,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-global-urban--social-studies-dr210',
    updated_at = NOW()
WHERE cricos_course_code = '079812M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In this program you will develop advanced research skills that will prepare you for a career in academia and other settings in which systematic and critical analytical skills are required.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 168960,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-supply-chain--logistics-dr202',
    updated_at = NOW()
WHERE cricos_course_code = '079813K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This Doctor of Philosophy (PhD) research degree will provide the framework, the focus and the discipline necessary to conduct speculative inquiry in the field of media and communication.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 165120,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-media--communication-dr211',
    updated_at = NOW()
WHERE cricos_course_code = '079814J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This research degree supports your engagement in communities of practice where learning is fundamentally a social phenomenon.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 78720,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-design-media--communication-mr211',
    updated_at = NOW()
WHERE cricos_course_code = '079815G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Apply your advanced engineering skills to industry focused research projects and identify real-world solutions to existing and emerging chemical engineering problems.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 184320,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-chemical-engineering-dr217',
    updated_at = NOW()
WHERE cricos_course_code = '079816G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Apply your advanced engineering skills to an industry focused research project and develop real-world solutions to existing and emerging civil engineering problems.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 184320,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-civil-engineering-dr218',
    updated_at = NOW()
WHERE cricos_course_code = '079817F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Apply your advanced engineering skills to an industry focused environmental engineering research project.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 184320,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-environmental-engineering-dr219',
    updated_at = NOW()
WHERE cricos_course_code = '079818E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your advanced engineering skills and contribute to industry focused research projects, identifying real-world solutions to existing and emerging chemical engineering problems.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 88320,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-engineering-chemical-engineering-mr217',
    updated_at = NOW()
WHERE cricos_course_code = '079819D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your advanced engineering skills by contributing to an industry focused research project and identify real-world solutions to existing and emerging civil engineering problems.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 88320,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-engineering-civil-engineering-mr218',
    updated_at = NOW()
WHERE cricos_course_code = '079820M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your advanced engineering skills and contribute to an industry focused environmental engineering research project.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 88320,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-engineering-environmental-engineering-mr219',
    updated_at = NOW()
WHERE cricos_course_code = '079821K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Use your advanced research skills to contribute to new developments in applied chemistry.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 172800,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-applied-chemistry-dr229',
    updated_at = NOW()
WHERE cricos_course_code = '079822J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your advanced research skills and contribute to new developments in applied chemistry.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 82560,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-science-applied-chemistry-mr229',
    updated_at = NOW()
WHERE cricos_course_code = '079823G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your logical, analytical and creative problem solving skills and further the growth of mathematical theory and application.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 82560,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-science-mathematical-sciences-mr222',
    updated_at = NOW()
WHERE cricos_course_code = '079824G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your advanced research skills and contribute to the forefront of geospatial sciences development and implementation.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 82560,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-science-geospatial-sciences-mr223',
    updated_at = NOW()
WHERE cricos_course_code = '079825F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your advanced research skills and contribute to new developments in psychology.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-science-psychology-mr226',
    updated_at = NOW()
WHERE cricos_course_code = '079828C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Through advanced coursework and research in the Doctor of Philosophy in the Built Environment, you will develop sophisticated research, technical and critical analytical skills.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 165120,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-built-environment-dr212',
    updated_at = NOW()
WHERE cricos_course_code = '079829B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Prepare for employment in research-based senior leadership and management positions with a Master of Applied Science (Built Environment).</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 78720,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-applied-science-built-environment-mr212',
    updated_at = NOW()
WHERE cricos_course_code = '079830J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Join an active research community, collaborating on the future of aerospace engineering and aviation.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 184320,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-aerospace-engineering-and-aviation-dr215',
    updated_at = NOW()
WHERE cricos_course_code = '079831G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your research skills and contribute to the growth of aerospace engineering.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 88320,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-engineering-aerospace-engineering-and-aviation-mr215',
    updated_at = NOW()
WHERE cricos_course_code = '079832G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Use your advanced research skills to further the growth and development of mechanical and manufacturing engineering.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 184320,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-mechanical-manufacturing-and-mechatronic-engineering-dr216',
    updated_at = NOW()
WHERE cricos_course_code = '079833F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop advanced research skills and further the growth of mechanical and manufacturing engineering.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 88320,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-engineering-mechanical-manufacturing-and-mechatronic-engineering-mr216',
    updated_at = NOW()
WHERE cricos_course_code = '079834E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Shape how cities are designed and constructed by studying urban planning and the art of creating liveable and sustainable urban spaces.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-urban-planning-and-environment-mc221',
    updated_at = NOW()
WHERE cricos_course_code = '079932C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn to improve energy efficiency and reduce the environmental impact of energy technologies with the Master of Engineering (Sustainable Energy)</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-engineering-sustainable-energy-mc229',
    updated_at = NOW()
WHERE cricos_course_code = '079934A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Join a new breed of automotive engineers involved in design and manufacture by completing the Master of Engineering (International Automotive Engineering)</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-engineering-international-automotive-engineering-mc230',
    updated_at = NOW()
WHERE cricos_course_code = '079935M';
-- Register-only (no site match): Master of Engineering (Telecommunication and Network Engineering)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '079936K';
-- Register-only (no site match): Master of Engineering (Electrical Engineering)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '079937J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Delve into the vibrant world of animation and explore 2D and 3D animation, motion graphics, special effects and more at a leading design university.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 146880,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-design-animation-and-interactive-media-bp203',
    updated_at = NOW()
WHERE cricos_course_code = '079976B';
-- Register-only (no site match): Bachelor of Business (Information Systems)(Applied)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 197760,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '079977A';
-- Register-only (no site match): Bachelor of Business (Information Systems)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 144480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '079978M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Designed for advanced professional development, this masters at RMIT explores the future of design practice and use of technology in evolving environments</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 97920,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-design-innovation-and-technology-mc231',
    updated_at = NOW()
WHERE cricos_course_code = '080000D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Shape the world around you. Explore planning law, climate change adaptation, urban economics, natural resource management, and more.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 161280,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-urban-and-regional-planning-honours-bh108',
    updated_at = NOW()
WHERE cricos_course_code = '080010B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Shape the world we live in. Create sustainable products, utilise design for cultural enrichment, and participate in technological development.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 207360,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-industrial-design-honours-bh104',
    updated_at = NOW()
WHERE cricos_course_code = '080225J';
-- Register-only (no site match): Bachelor of Design (Digital Media)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 146880,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '080226G';
-- Register-only (no site match): Master of Medical Physics
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '080227G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>A master''s course with a strong focus on consulting and work-integrated learning that will develop your analytic capabilities and make you business-ready.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-analytics-mc242',
    updated_at = NOW()
WHERE cricos_course_code = '081540A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Explore a creative, expansive practice that addresses the relation between people and their environments: how we live, work and play.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 207360,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-interior-design-honours-bh115',
    updated_at = NOW()
WHERE cricos_course_code = '083945G';
-- Register-only (no site match): Bachelor of Applied Science (Construction Management) (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 188160,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '083946G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Explore theoretical frameworks and practical applications of contemporary trends in this masters program, and become a communication industry leader.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 90240,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-communication-mc248',
    updated_at = NOW()
WHERE cricos_course_code = '083948E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In this masters dregree, you''ll explore communication processes with engaging professionals to further your knowledge and skills in advertising.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 90240,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-advertising-mc249',
    updated_at = NOW()
WHERE cricos_course_code = '083949D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Start an international career in animation, games, interactive media and multimedia with this postgraduate course.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 90240,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-animation-games-and-interactivity-mc232',
    updated_at = NOW()
WHERE cricos_course_code = '084348K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In this RMIT masters degree, you''ll develop visual communication and design practice expertise, focusing on entrepreneurship and strategic design thinking.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 90240,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-communication-design-mc250',
    updated_at = NOW()
WHERE cricos_course_code = '084351D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Lead the way in improving energy efficiency and reducing the environmental impact of energy technologies by completing this postgraduate degree.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 96000,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-energy-efficient-and-sustainable-building-mc209',
    updated_at = NOW()
WHERE cricos_course_code = '084668E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Take the first step towards your biomedical research career, or develop skills for a range of diverse career options with this Honours course.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 47040,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-health-and-biomedical-sciences-honours-bh058',
    updated_at = NOW()
WHERE cricos_course_code = '084885G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This accounting course is aimed at graduates of non-accounting disciplines who want to broaden their career prospects.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 24480,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-professional-accounting-gc119',
    updated_at = NOW()
WHERE cricos_course_code = '084995A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advance your career in logistics and supply chain management through RMIT''s graduate certificate.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 24480,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-supply-chain-and-logistics-management-gc055',
    updated_at = NOW()
WHERE cricos_course_code = '084996M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Suited to recent graduates with a degree in any discipline, this program teaches you how to approach and solve problems in a global business context.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 25440,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-business-administration-gc047',
    updated_at = NOW()
WHERE cricos_course_code = '084997K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain the skills required to investigate complex problems and address the important challenges of sustainable international business.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 24480,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-international-business-gc153',
    updated_at = NOW()
WHERE cricos_course_code = '084998J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This executive-level graduate certificate offers working professionals a learning experience that fosters leadership and strategic thinking.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 26880,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-business-administration-executive-gc129',
    updated_at = NOW()
WHERE cricos_course_code = '084999G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Understand the role of marketing and its relationship with other important functional areas in management.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 24480,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-marketing-gc053',
    updated_at = NOW()
WHERE cricos_course_code = '085022B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In the Graduate Certificate in Finance, you’ll learn about finance, econometrics, research and analysis of financial markets.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 24480,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-finance-gc048',
    updated_at = NOW()
WHERE cricos_course_code = '085023A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain cutting-edge business IT knowledge and learn how to create successful business information systems solutions.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 24000,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-business-information-technology-gc099',
    updated_at = NOW()
WHERE cricos_course_code = '085024M';
-- Register-only (no site match): Graduate Certificate of Commerce
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 24480,
    enrolment_fee = 186,
    updated_at = NOW()
WHERE cricos_course_code = '085025K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study the Master of Property and immerse yourself in a property management course. Develop your skills to work in this dynamic industry.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 96000,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-property-mc212',
    updated_at = NOW()
WHERE cricos_course_code = '085116G';
-- Register-only (no site match): Doctor of Philosophy (Laboratory and Clinical Sciences)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 168960,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '085837G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop specialist environmental engineering skills with a course that will further your career as a project leader, consultant or manager.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-engineering-environmental-engineering-mc254',
    updated_at = NOW()
WHERE cricos_course_code = '087983C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Graduate from this masters degree with advanced knowledge and skills in robotics and mechatronics and control systems.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-engineering-robotics-and-mechatronics-engineering-mc256',
    updated_at = NOW()
WHERE cricos_course_code = '087985A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This industry-focused Master of Civil Engineering deepens and broadens your civil engineering postgraduate knowledge, in preparation for a leadership role.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-engineering-civil-engineering-mc257',
    updated_at = NOW()
WHERE cricos_course_code = '087986M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain the skills to work as a designer, technical specialist, consultant or manager with the Master of Engineering (Mechanical Engineering).</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-engineering-mechanical-engineering-mc258',
    updated_at = NOW()
WHERE cricos_course_code = '087987K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Excel in editing and publishing, and develop your specialist knowledge with this industry-focused masters degree.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 90240,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-writing-and-publishing-mc262',
    updated_at = NOW()
WHERE cricos_course_code = '088089C';
-- Register-only (no site match): Master of Professional Accounting (CPA Australia Extension)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '088092G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your knowledge of contemporary HR practice and examine management issues in the context of global changes that impact people and workplaces.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 24480,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-human-resource-management-gc161',
    updated_at = NOW()
WHERE cricos_course_code = '088783C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>RMIT’s new human resource management program is focused on enhancing and updating your knowledge and skills to develop HR practice globally.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 103680,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-human-resource-management-mc263',
    updated_at = NOW()
WHERE cricos_course_code = '088784B';
-- Register-only (no site match): Bachelor of Arts (Fine Art)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 135360,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '088785A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In this master’s in aerospace engineering you’ll learn how to develop solutions to avionics engineering, scientific and technological problems.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-engineering-aerospace-mc225',
    updated_at = NOW()
WHERE cricos_course_code = '088786M';
-- Register-only (no site match): RMIT Inbound Internship
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = NULL,
    enrolment_fee = 186,
    updated_at = NOW()
WHERE cricos_course_code = '091377B';
-- Register-only (no site match): RMIT Inbound Internship
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = NULL,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '091378A';
-- Register-only (no site match): Master of Science (Aviation)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '092028D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study alongside industry in this intensive, practical degree and pursue your career goals in the pharmaceutical sector.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 47040,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-pharmaceutical-sciences-honours-bh121',
    updated_at = NOW()
WHERE cricos_course_code = '092331G';
-- Register-only (no site match): Bachelor of Business (Financial Planning)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 144480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '092360C';
-- Register-only (no site match): Bachelor of Business (Financial Planning) / Bachelor of Business (Accountancy)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 197760,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '092363M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study art at the next level at Australia''s leading fine art school. Be guided in a studio environment that promotes creativity and experimentation.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 86400,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-fine-art-mc266',
    updated_at = NOW()
WHERE cricos_course_code = '092466D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Launch your career in geospatial science and become an expert in geographic information systems, mapping, satellite positioning and remote sensing.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-geospatial-science-mc265',
    updated_at = NOW()
WHERE cricos_course_code = '092796G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your career in project management with a qualification that’s in demand across diverse industries.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 24960,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-project-management-gc042',
    updated_at = NOW()
WHERE cricos_course_code = '093311D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Start a career with a highly in-demand qualification that spans multiple industries.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 50880,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-diplomas/graduate-diploma-in-project-management-gd194',
    updated_at = NOW()
WHERE cricos_course_code = '093312C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Master of Data Science is designed to equip you with skills to analyse and manage big data and become in-demand data scientist.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-data-science-mc267',
    updated_at = NOW()
WHERE cricos_course_code = '093313B';
-- Register-only (no site match): Bachelor of Engineering (Chemical Engineering) (Honours) / Bachelor of Pharmaceutical Sciences
UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 277608,
    enrolment_fee = 1981,
    updated_at = NOW()
WHERE cricos_course_code = '093315M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Become a clinical psychologist with a Master of Psychology and be trained to work according to the scientist-professional model.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-clinical-psychology-mc002',
    updated_at = NOW()
WHERE cricos_course_code = '093570G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This program will equip you with the necessary knowledge and skills required to operate effectively in the food industry at various professional and management levels.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-food-science-and-technology-mc237',
    updated_at = NOW()
WHERE cricos_course_code = '094062G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This one-year shoe design course will help you forge a career path as a footwear designer.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 27750,
    enrolment_fee = 1003,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/certificates/certificate-iv-in-custommade-footwear-c4389',
    updated_at = NOW()
WHERE cricos_course_code = '094157A';
-- Register-only (no site match): Graduate Diploma in Public Policy
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 39840,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '096020B';
-- Register-only (no site match): Bachelor of Arts (Welfare and Society)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 119520,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '096090K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Designed to teach socially-engaged photographers to lead developments in the technological, cultural, environmental and political role of photography.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 86400,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-photography-mc270',
    updated_at = NOW()
WHERE cricos_course_code = '096091J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your talents and broaden your skill set as you study, research and practice photography at an advanced level.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 43200,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-arts-photography-honours-bh125',
    updated_at = NOW()
WHERE cricos_course_code = '096092G';
-- Register-only (no site match): Graduate Certificate in Cyber Security
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 22080,
    enrolment_fee = 186,
    updated_at = NOW()
WHERE cricos_course_code = '096093G';
-- Register-only (no site match): Graduate Diploma in Cyber Security
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = NULL,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '096094F';
-- Register-only (no site match): Bachelor of Textiles (Design) (Honours)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 48000,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '096891K';
-- Register-only (no site match): Bachelor of Youth Work and Youth Studies
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 119520,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '098456B';
-- Register-only (no site match): Bachelor of Education (Primary and Early Childhood Education)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 161280,
    enrolment_fee = 1877,
    updated_at = NOW()
WHERE cricos_course_code = '098534D';
-- Register-only (no site match): Advanced Diploma of Engineering Technology
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 47500,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '098561A';
-- Register-only (no site match): Master of Teaching Practice (Secondary Education)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 87120,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '098980D';
-- Register-only (no site match): Master of Teaching Practice (Primary Education)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 78720,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '098981C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Research and explore the boundaries of design thinking with an internationally recognised leader of design education and practice.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-design-mr235',
    updated_at = NOW()
WHERE cricos_course_code = '099062A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Research design with greater focus. Explore theory, practice and application as you work toward redefining aspects of design.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 192000,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-design-dr235',
    updated_at = NOW()
WHERE cricos_course_code = '099063M';
-- Register-only (no site match): Bachelor of Business (Digital Business)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 144480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '099577G';
-- Register-only (no site match): Bachelor of Business (Blockchain Enabled Business)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 144480,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '103204J';
-- Register-only (no site match): Graduate Diploma in Blockchain Enabled Business
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 50400,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '103205H';
-- Register-only (no site match): Master of Blockchain Enabled Business
UPDATE courses SET
    course_duration_per_week = 78,
    offshore_tuition_fee = 76320,
    enrolment_fee = 559,
    updated_at = NOW()
WHERE cricos_course_code = '103206G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>A postgraduate program designed for non-law graduates to enter a legal profession. Focused on business and international law and the justice system.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 156960,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/juris-doctor-mc161',
    updated_at = NOW()
WHERE cricos_course_code = '103207F';
-- Register-only (no site match): Graduate Certificate in Digital Economy
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 24480,
    enrolment_fee = 186,
    updated_at = NOW()
WHERE cricos_course_code = '103208E';
-- Register-only (no site match): Bachelor or Business Innovation and Enterprise
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 128160,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '103209D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Becoming a global, technology focussed lawyer for a changing world.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 144480,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-laws-bp335',
    updated_at = NOW()
WHERE cricos_course_code = '103210M';
-- Register-only (no site match): Bachelor of Data Science
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '103214G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This has been designed to develop specialised knowledge and skills in property and enable you to meet the needs of a dynamic and complex sector.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 47040,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-diplomas/graduate-diploma-in-property-gd090',
    updated_at = NOW()
WHERE cricos_course_code = '103216E';
-- Register-only (no site match): Graduate Diploma in Media
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '103217D';
-- Register-only (no site match): Graduate Diploma in Urban Design
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 49920,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '103218C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn about sustainable building, resources and efficiencies in building materials, water and energy.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 47040,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-diplomas/graduate-diploma-in-energy-efficient-and-sustainable-building-gd189',
    updated_at = NOW()
WHERE cricos_course_code = '103219B';
-- Register-only (no site match): Graduate Diploma of Animation, Games and Interactivity
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '103220J';
-- Register-only (no site match): Graduate Diploma of Communication
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '103221H';
-- Register-only (no site match): Graduate Diploma of Advertising
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '103222G';
-- Register-only (no site match): Graduate Diploma of Communication Design
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '103223F';
-- Register-only (no site match): Graduate Diploma of Writing and Publishing
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '103224E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This degree has been designed to develop specialised theoretical knowledge and technical skills in property and enable you to meet the needs of an increasingly dynamic, diverse and complex sector.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 23040,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-property-gc051',
    updated_at = NOW()
WHERE cricos_course_code = '103225D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Graduate Certificate that will expand your energy efficiency knowledge and sustainability horizon in the built environment.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 23040,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-energy-efficient-and-sustainable-building-gc163',
    updated_at = NOW()
WHERE cricos_course_code = '103226C';
-- Register-only (no site match): Graduate Diploma in Urban Planning and Environment
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 39840,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '103227B';
-- Register-only (no site match): Graduate Diploma in Justice and Criminology
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 39840,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '103228A';
-- Register-only (no site match): Graduate Diploma in Interior Design
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 49920,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '103229M';
-- Register-only (no site match): Bachelor of Computer Science
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '103230G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your software engineering skills to design, code, test and manage large quality-measured software systems. Discover more.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 188160,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-software-engineering-professional-bp096',
    updated_at = NOW()
WHERE cricos_course_code = '103231F';
-- Register-only (no site match): Graduate Certificate in Arts Management
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 20640,
    enrolment_fee = 186,
    updated_at = NOW()
WHERE cricos_course_code = '103233D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Start a career in gallery, event and museum project management with a degree that brings together a network of curators, academics, managers and artists.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 86400,
    enrolment_fee = 1387,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-arts-arts-management-mc280',
    updated_at = NOW()
WHERE cricos_course_code = '103234C';
-- Register-only (no site match): Master of Arts (Art in Public Space)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 86400,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '103235B';
-- Register-only (no site match): Graduate Diploma in Arts Management
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 42240,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '103236A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Evolve your knowledge of electronic products and processes.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 48000,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/advanced-diplomas/advanced-diploma-of-electronics-and-communications-engineering-c6178',
    updated_at = NOW()
WHERE cricos_course_code = '103390B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn about the planning, coordination, and control of medium-rise and wide-span building projects.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 45000,
    enrolment_fee = 884,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/diplomas/diploma-of-building-and-construction-building-c5415',
    updated_at = NOW()
WHERE cricos_course_code = '103765J';
-- Register-only (no site match): Diploma of Flying (Pilot Cadetship)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 117600,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '104537B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Prepare for a career in land and parks management, site assessment, water quality assessment and conservation.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 46000,
    enrolment_fee = 2273,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/diplomas/diploma-of-conservation-and-ecosystem-management-c5418',
    updated_at = NOW()
WHERE cricos_course_code = '104848J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Redefine your career trajectory and address the ecological and technological global challenges that face the world today.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 23520,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-of-design-innovation-and-technology-gc192',
    updated_at = NOW()
WHERE cricos_course_code = '104979J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Use your language skills to expand your career opportunities, and become a translator or interpreter with abilities that span all industries.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 20160,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-translating-and-interpreting-gc185',
    updated_at = NOW()
WHERE cricos_course_code = '104980E';
-- Register-only (no site match): Graduate Diploma of Design Innovation and Technology
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 48000,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '104982C';
-- Register-only (no site match): Associate Degree in Digital Technologies (Advanced Manufacturing)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 83040,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '104983B';
-- Register-only (no site match): Diploma of Fashion Styling
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 23375,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '105217K';
-- Register-only (no site match): Certificate IV in Design
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 20000,
    enrolment_fee = 186,
    updated_at = NOW()
WHERE cricos_course_code = '105791B';
-- Register-only (no site match): Diploma of Graphic Design
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 26250,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '105817H';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Become the architect of your own educational experience with the freedom to tap into your own interests.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 197760,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-business-professional-practice-bp344',
    updated_at = NOW()
WHERE cricos_course_code = '106622M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In this ever-changing world, do you wonder what the future of business is? Develop the tools to succeed in your professional future.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 144480,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-business-bp343',
    updated_at = NOW()
WHERE cricos_course_code = '106623K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Advance your skills in occupational health and safety with a degree that provides specialisations at the forefront of industry.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 94080,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-occupational-health-and-safety-mc282',
    updated_at = NOW()
WHERE cricos_course_code = '107034A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Make workplaces safer by studying an occupational health and safety (OHS) diploma at Melbourne''s leading vocational education provider.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 46080,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-diplomas/graduate-diploma-in-occupational-health-and-safety-gd052',
    updated_at = NOW()
WHERE cricos_course_code = '107035M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Build necessary skills in risk and hazard identification, management and prevention to build a safer workplace and community.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 22560,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-occupational-health-and-safety-gc035',
    updated_at = NOW()
WHERE cricos_course_code = '107036K';
-- Register-only (no site match): Graduate Diploma in Art in Public Space
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 42240,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '107037J';
-- Register-only (no site match): Graduate Certificate in Art in Public Space
UPDATE courses SET
    course_duration_per_week = 26,
    offshore_tuition_fee = 20640,
    enrolment_fee = 186,
    updated_at = NOW()
WHERE cricos_course_code = '107039G';
-- Register-only (no site match): Bachelor of Education Studies
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 118080,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '107040C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain new skills in the field of justice and criminology, and explore this exciting, challenging and essential field.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 19680,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-justice-and-criminology-gc195',
    updated_at = NOW()
WHERE cricos_course_code = '107041B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Make a global impact in international development, security, humanitarian emergencies and sustainability.​</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-global-studies-mc283',
    updated_at = NOW()
WHERE cricos_course_code = '107042A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn about programming, web development (PHP and content management systems), operating systems, networking, database modelling and implementation.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 25750,
    enrolment_fee = 365,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/diplomas/diploma-of-information-technology-c5402',
    updated_at = NOW()
WHERE cricos_course_code = '107251C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain a broad understanding of business with a diploma that will enhance your career.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 16000,
    enrolment_fee = 365,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/diplomas/diploma-of-business-c5406',
    updated_at = NOW()
WHERE cricos_course_code = '107881F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Work in live broadcast and live streaming productions across all technical areas of directing, camera, audio, graphics and editing.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 27000,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/diplomas/diploma-of-screen-and-media-c5421',
    updated_at = NOW()
WHERE cricos_course_code = '107883D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Want to forge a career in animation and game design?</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 27000,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/advanced-diplomas/advanced-diploma-of-screen-and-media-content-creation-and-design-c6173',
    updated_at = NOW()
WHERE cricos_course_code = '107884C';
-- Register-only (no site match): Diploma of Visual Arts
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 25000,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '108040F';
-- Register-only (no site match): Diploma of Photography and Digital Imaging
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 25500,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '108041E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover the expanding world of people analytics and its essential role in the management of people, organisation and work.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 24480,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-people-analytics-gc206',
    updated_at = NOW()
WHERE cricos_course_code = '108312J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Foundation Studies is chosen by international students all over the world as their pathway to higher education at RMIT.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 33000,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/pre-university-study/foundation-studies/foundation-studies-fs022',
    updated_at = NOW()
WHERE cricos_course_code = '108492M';
-- Register-only (no site match): Bachelor of Engineering (Electronic and Computer Systems Engineering) (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '108624D';
-- Register-only (no site match): Bachelor of Aviation (Pilot Training)
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 233760,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '108797E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your accounting and bookkeeping skills in our simulated small business practice firm environment.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 13000,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/certificates/certificate-iv-in-accounting-and-bookkeeping-c4435',
    updated_at = NOW()
WHERE cricos_course_code = '109949H';
-- Register-only (no site match): Advanced Diploma of Visual Arts
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 25500,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '110047C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain practical photography skills and begin building your professional photography portfolio.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 26500,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/certificates/certificate-iv-in-photography-and-digital-imaging-c4415',
    updated_at = NOW()
WHERE cricos_course_code = '110048B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your advanced engineering skills and contribute to industry-focused biomedical research projects.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 184320,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-biomedical-engineering-dr239',
    updated_at = NOW()
WHERE cricos_course_code = '110528H';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Contribute to industry-focused biomedical research projects, identifying solutions to engineering problems that affect the human body.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 88320,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-engineering-biomedical-engineering-mr239',
    updated_at = NOW()
WHERE cricos_course_code = '110529G';
-- Register-only (no site match): PhD (Health Science)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 168960,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '110530C';
-- Register-only (no site match): Master of Science (Health Science)
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '110531B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Apply your advanced research skills to shape the future of medicine and tackle key health challenges.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 168960,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-medical-science-dr238',
    updated_at = NOW()
WHERE cricos_course_code = '110532A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your advanced research skills and contribute to new developments in medical sciences.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-science-medical-science-mr238',
    updated_at = NOW()
WHERE cricos_course_code = '110533M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Apply your advanced research skills to shape the future of digital healthcare.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 168960,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/phd/phd-digital-health-dr236',
    updated_at = NOW()
WHERE cricos_course_code = '110534K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your advanced research skills and contribute to the advancement of digital health.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 80640,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/research-programs/masters-by-research/master-of-science-digital-health-mr236',
    updated_at = NOW()
WHERE cricos_course_code = '110535J';
-- Register-only (no site match): Diploma of Flying (Private Pilot License)
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 69120,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '110536H';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Diploma of Nursing has been designed to help you build knowledge and skills in a practical learning environment.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 41500,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/diplomas/diploma-of-nursing-c5417',
    updated_at = NOW()
WHERE cricos_course_code = '110709C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Tailor your study to your interests with this comprehensive and flexible double degree in the Bachelor of Laws/Bachelor of Business.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 252480,
    enrolment_fee = 1865,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-lawsbachelor-of-business-bp346',
    updated_at = NOW()
WHERE cricos_course_code = '110717C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Designed to equip you with in-depth knowledge of this essential field, the Bachelor of Accounting will prepare you for a challenging and varied career.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 144480,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-accounting-bp351',
    updated_at = NOW()
WHERE cricos_course_code = '110718B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Become a media professional and bring your vision to life. Explore 2D and 3D animation, graphic design, illustration, UX, UI and more.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 21600,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-animation-games-and-interactivity-gc205',
    updated_at = NOW()
WHERE cricos_course_code = '110719A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This top-ranking Bachelor of Computer Science will provide you with cutting-edge programming and software development skills. Find out more.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-computer-science-bp094',
    updated_at = NOW()
WHERE cricos_course_code = '110797J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Delve into the ever-expanding world of computer science, develop in-demand skills and customise your degree to suit your career aspirations.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 188160,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-computer-science-professional-bp347',
    updated_at = NOW()
WHERE cricos_course_code = '110798H';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your software engineering skills to design, code, test and manage large quality-measured software systems. Discover more.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 188160,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-software-engineering-professional-bp096',
    updated_at = NOW()
WHERE cricos_course_code = '110799G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Join the rapidly expanding field of data science and take steps toward a rewarding career as a data scientist.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-data-science-bp340',
    updated_at = NOW()
WHERE cricos_course_code = '110801G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Co-created with industry leaders, this Bachelor of IT will provide you with a broad range of IT and professional skills that will advance your career.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 188160,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-professional-bp349',
    updated_at = NOW()
WHERE cricos_course_code = '110802F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study a Bachelor of IT and develop essential, highly in-demand IT skills. Specialise in fields like blockchain, AI, data science and cloud computing.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-information-technology-bp162',
    updated_at = NOW()
WHERE cricos_course_code = '110803E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study the Bachelor of Data Science (Professional) and graduate with the practical experience and in-demand skills to succeed in this rapidly growing field.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 188160,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-data-science-professional-bp348',
    updated_at = NOW()
WHERE cricos_course_code = '110804D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Utilise practical skills and advanced mathematics to pursue a highly technical career in surveying, and let the world be your office.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 188160,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-surveying-honours-bh116',
    updated_at = NOW()
WHERE cricos_course_code = '110978D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study food technology and nutrition, developing advanced skills in manufacturing and packaging, marketing, quality assurance and education. Learn more.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 3165,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-food-technology-and-nutrition-bp199',
    updated_at = NOW()
WHERE cricos_course_code = '110979C';
-- Register-only (no site match): Bachelor of Geospatial Science (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 188160,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '110980K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Play an important role in protecting and advocating for the environment. Learn about biochemistry, geoscience and geospatial science. Learn more.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 4164,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-environmental-science-bp192',
    updated_at = NOW()
WHERE cricos_course_code = '110981J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Tailor your science degree to your interests and career goals. Study biotechnology, chemistry, food science, maths, physics and statistics. Learn more.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 3972,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-science-bp350',
    updated_at = NOW()
WHERE cricos_course_code = '110982H';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Do you want to be part of Space 2.0? Have you thought about human spaceflight, space tourism and even missions to Mars? Study space science at RMIT.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-space-science-bp330',
    updated_at = NOW()
WHERE cricos_course_code = '110983G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn about human behaviour, gaining in-depth knowledge of developmental, cognitive, biological and social psychology and research methods. Enquire today.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-psychology-bp154',
    updated_at = NOW()
WHERE cricos_course_code = '110984F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>From cells to systems, discover biomedical science. Gain practical skills and knowledge in anatomy and physiology, biochemistry and microbiology.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 144000,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-biomedical-science-bp231',
    updated_at = NOW()
WHERE cricos_course_code = '110985E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This pharmaceutical science degree will equip you for a career in the pharmaceutical industry. Study both the science and business of developing new drugs.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 146880,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-pharmaceutical-sciences-bp311',
    updated_at = NOW()
WHERE cricos_course_code = '110986D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Bachelor of Laboratory Medicine (Honours) will prepare you for a career in diagnostic pathology or medical research. Discover more.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 199680,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-laboratory-medicine-honours-bh129',
    updated_at = NOW()
WHERE cricos_course_code = '110987C';
-- Register-only (no site match): Bachelor of Engineering (Computer and Network Engineering) (Honours) / Bachelor of Computer Science
UPDATE courses SET
    course_duration_per_week = 260,
    offshore_tuition_fee = 284064,
    enrolment_fee = 1981,
    updated_at = NOW()
WHERE cricos_course_code = '110988B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This manufacturing and mechatronics degree develops skills in robotics and control, high-speed automation, manufacturing management and advanced materials.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1608,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineering-adv-manufacturing-and-mechatronics-honours-bh068',
    updated_at = NOW()
WHERE cricos_course_code = '110989A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study a biomedical engineering degree that bridges medicine and technology and provides solutions that can enhance and improve human health. Learn more.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1608,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineering-biomedical-engineering-honours-bh069',
    updated_at = NOW()
WHERE cricos_course_code = '110990H';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn about the conversion and control of energy and motion in machinery and systems by studying a mechanical engineering course at RMIT.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineering-mechanical-engineering-honours-bh070',
    updated_at = NOW()
WHERE cricos_course_code = '110991G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Guided by industry experts, you''ll develop electronic and computer systems engineering skills that will enable you to work in a variety of industries.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineering-electronic-and-computer-systems-engineering-honours-bh073',
    updated_at = NOW()
WHERE cricos_course_code = '110992F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This professionally accredited electrical engineering degree will equip you with the technical and management skills to succeed in a range of industries.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1608,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineering-electrical-engineering-honours-bh075',
    updated_at = NOW()
WHERE cricos_course_code = '110993E';
-- Register-only (no site match): Bachelor of Engineering (Sustainable Systems Engineering) (Honours)
UPDATE courses SET
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1492,
    updated_at = NOW()
WHERE cricos_course_code = '110994D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This internationally accredited civil and infrastructure engineering degree equips you with the skills to work on multidisciplinary infrastructure projects</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineering-civil-and-infrastructure-honours-bh077',
    updated_at = NOW()
WHERE cricos_course_code = '110995C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Build highly specialised aerospace engineering skills required to pursue an exciting global career in aeronautics and astronautics. Discover more.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1608,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineering-aerospace-engineering-honours-bh078',
    updated_at = NOW()
WHERE cricos_course_code = '110996B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain an internationally recognised qualification with a practical degree that gives you real-world experience in chemical engineering. Learn more.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineering-chemical-engineering-honours-bh079',
    updated_at = NOW()
WHERE cricos_course_code = '110997A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Solve critical global challenges with specialist study in land contamination, water and air pollution, energy and sustainable cities. Learn more.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineering-environmental-engineering-honours-bh080',
    updated_at = NOW()
WHERE cricos_course_code = '110998M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Prepare to become a leader. Combine manufacturing and mechatronics engineering with essential business skills and take your career to the next level.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 284064,
    enrolment_fee = 1981,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineering-adv-manufacturing--mechatronicshonsbachelor-of-business-bh086',
    updated_at = NOW()
WHERE cricos_course_code = '111184H';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Complete a double degree that will help you become an entrepreneur in mechanical engineering, by learning to design, analyse and improve products.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 284064,
    enrolment_fee = 1865,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineering-mechanical-engineering-honoursbachelor-of-business-bh089',
    updated_at = NOW()
WHERE cricos_course_code = '111185G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Become a future leader. Combine advanced civil engineering knowledge with practical business skills to lead major projects and manage teams. Discover more.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 277608,
    enrolment_fee = 1865,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineering-civil-and-infrastructure-honoursbachelor-of-business-bh088',
    updated_at = NOW()
WHERE cricos_course_code = '111186F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Combine your skills in design, analysis and mathematics with those in leadership, and prepare for a dynamic career in aerospace and business management.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 284064,
    enrolment_fee = 1865,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineering-aerospace-engineering-honoursbachelor-of-business-bh082',
    updated_at = NOW()
WHERE cricos_course_code = '111187E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Launch your career in the aviation industry to work in a range of operational, managerial, and planning roles. Discover more.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 149760,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-applied-science-aviation-bp070',
    updated_at = NOW()
WHERE cricos_course_code = '111188D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study with an industry leader. Gain aviation and business skills and launch your career as a manager in the aviation industry. Discover more.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 228960,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-applied-science-aviationbachelor-of-business-bp284',
    updated_at = NOW()
WHERE cricos_course_code = '111189C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Take flight and prepare for a career as a commercial pilot. Learn to fly at two airports - Point Cook and Bendigo airfields. Learn more.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 233760,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-aviation-pilot-training-bp345',
    updated_at = NOW()
WHERE cricos_course_code = '111190K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Become a future engineering manager. Study engineering and business, developing knowledge of electronic engineering, computer systems and business manageme</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 284064,
    enrolment_fee = 1865,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineering-electronic-and-computer-systems-engineeringhonoursbachelor-of-business-bh111',
    updated_at = NOW()
WHERE cricos_course_code = '111191J';
-- Register-only (no site match): Bachelor of Applied Mathematics and Statistics
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '111273G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course is the first of its kind, designed to address the Australian food industry''s need for technologists with strong business skills.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 211680,
    enrolment_fee = 3538,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-food-technology-and-nutritionbachelor-of-business-bp289',
    updated_at = NOW()
WHERE cricos_course_code = '111274F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Become a well-rounded accounting and legal professional with this immersive and challenging double degree in accounting and law.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 252480,
    enrolment_fee = 1865,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-accountingbachelor-of-laws-bp352',
    updated_at = NOW()
WHERE cricos_course_code = '111275E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This degree has been designed to equip you with the skills to launch a varied and exciting accounting career across any number of fields.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 197760,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-accountingbachelor-of-business-bp353',
    updated_at = NOW()
WHERE cricos_course_code = '111276D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Combine science-led knowledge and social science skills to address the way we adapt to environmental change, and help create a sustainable future.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 172800,
    enrolment_fee = 4140,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-environmental-sciencebachelor-of-sustainability-and-environment-bp193',
    updated_at = NOW()
WHERE cricos_course_code = '111277C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Diploma of Commerce is unlike any other one-year Diploma. It covers the fundamentals of business disciplines at an undergraduate level.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 37440,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/higher-education-diplomas/diploma-of-commerce-dp020',
    updated_at = NOW()
WHERE cricos_course_code = '111278B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Refine your professional skills and knowledge in a real or simulated business environment.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 74880,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/associate-degrees/associate-degree-in-business-ad029',
    updated_at = NOW()
WHERE cricos_course_code = '111279A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Join the field of interior design and explore modern and historical approaches colour, materials, interior construction, furniture, and more.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 55750,
    enrolment_fee = 1021,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/diplomas/diploma-of-interior-design-c5431',
    updated_at = NOW()
WHERE cricos_course_code = '111975K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop the advanced skills required to work in aerospace manufacturing, design and maintenance at a paraprofessional level.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 47500,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/advanced-diplomas/advanced-diploma-of-engineering-aeronautical-c6187',
    updated_at = NOW()
WHERE cricos_course_code = '112017D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study to become a lab technician and find a career in biotechnology, pathology, research, pharmaceuticals and more.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 21000,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/certificates/certificate-iv-in-laboratory-techniques-c4433',
    updated_at = NOW()
WHERE cricos_course_code = '112039J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Build the skills required to work in laboratories across a range of industries, and develop a broad-ranged knowledge of scientific principles.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 22875,
    enrolment_fee = 315,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/diplomas/diploma-of-laboratory-technology-c5434',
    updated_at = NOW()
WHERE cricos_course_code = '112044A';
-- Register-only (no site match): Certificate IV in Textile Design and Technology
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 22335,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '112049G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Extend your accounting skills in our simulated practice firm environment and explore a range of specialisations.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 13000,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/diplomas/diploma-of-accounting-c5424',
    updated_at = NOW()
WHERE cricos_course_code = '113125C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Deepen your understanding of contemporary accounting practice and apply your skills in an industry-based work placement.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 27000,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/advanced-diplomas/advanced-diploma-of-accounting-c6181',
    updated_at = NOW()
WHERE cricos_course_code = '113126B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Help construct our world. Learn to manage contractors, budgets and stakeholders, understand urban planning, and work in commercial and residential sectors.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 188160,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-construction-management-honours-bh114',
    updated_at = NOW()
WHERE cricos_course_code = '113362A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop the analytical, communication and problem solving skills required to oversee residential, commercial and industrial projects.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 188160,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-project-management-honours-bh112',
    updated_at = NOW()
WHERE cricos_course_code = '113427M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Join the booming property industry with knowledge in urban planning, economics, project management, property valuation, investment and more.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 188160,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-property-development-investment-and-valuation-honours-bh113',
    updated_at = NOW()
WHERE cricos_course_code = '113429J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop the skills you need to work in IT, and specialise in system administration, networking, programming, development, security, and more.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 81600,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/associate-degrees/associate-degree-in-information-technology-ad006',
    updated_at = NOW()
WHERE cricos_course_code = '113595F';
-- Register-only (no site match): Diploma of Information Technology
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 34560,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '113596E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>An Associate Degree in Applied Science can prepare you for a job or provide you access to study a degree in biotechnology, food or biomedical science.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 76320,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/associate-degrees/associate-degree-in-applied-science-ad012',
    updated_at = NOW()
WHERE cricos_course_code = '113597D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Design your own flexible program of study from existing RMIT postgraduate courses to meet your personal career aspirations.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 103680,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-commerce-mc288',
    updated_at = NOW()
WHERE cricos_course_code = '113702H';
-- Register-only (no site match): Graduate Diploma in Commerce
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 50400,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '113703G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Design your own course of study to meet your personal and career aspirations.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 24480,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-commerce-gc212',
    updated_at = NOW()
WHERE cricos_course_code = '113704F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Designed to equip you with in-depth knowledge of this essential field, the Bachelor of Professional Communication reflects the workplace reality of increas</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 132480,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-professional-communication-bp354',
    updated_at = NOW()
WHERE cricos_course_code = '113705E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain the skills and qualifications to become a secondary school teacher with the Master of Teaching Practice (Secondary Education).</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 87120,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-teaching-practice-secondary-education-mc220',
    updated_at = NOW()
WHERE cricos_course_code = '113706D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain the skills and experience you need to shape young minds with the Master of Teaching Practice (Primary Education)</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 78720,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-teaching-practice-primary-education-mc219',
    updated_at = NOW()
WHERE cricos_course_code = '113707C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Become a leader in education with a globally recognised teaching degree. RMIT offers qualifications in primary, secondary and early childhood education.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 161280,
    enrolment_fee = 1877,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-education-bp320',
    updated_at = NOW()
WHERE cricos_course_code = '113708B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Become a leader in education with a globally recognised teaching degree. RMIT offers qualifications in primary, secondary and early childhood education.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 161280,
    enrolment_fee = 1877,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-education-bp320',
    updated_at = NOW()
WHERE cricos_course_code = '113709A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Graduate Certificate in Creative and Cultural Production introduces you to contemporary issues in the field and builds your global capabilities</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 20640,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-creative-and-cultural-production-gc213',
    updated_at = NOW()
WHERE cricos_course_code = '113749D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Bachelor of Nursing will enable you to engage in clinical practice and explore a range of nursing specialisations.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-nursing-bp032',
    updated_at = NOW()
WHERE cricos_course_code = '114027H';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover everything that goes into a career in pharmacy: pharmacology, therapeutics, knowledge of drug development, clinical trials and more.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 207360,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-pharmacy-honours-bh102',
    updated_at = NOW()
WHERE cricos_course_code = '114028G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study an Associate Degree in Health Sciences and learn about the growing field of health promotion.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 76800,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/associate-degrees/associate-degree-in-health-sciences-ad019',
    updated_at = NOW()
WHERE cricos_course_code = '114235M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>From cells to systems, discover biomedical science. Gain practical skills and knowledge in anatomy and physiology, biochemistry and microbiology.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 144000,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-biomedical-science-bp231',
    updated_at = NOW()
WHERE cricos_course_code = '114236K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Build the essential knowledge and skills to make an impact in the constantly-expanding industry of information technology (IT) with specialist expertise.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 188160,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-cyber-security-professional-bp356',
    updated_at = NOW()
WHERE cricos_course_code = '114320C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop expansive skills in information technology and cyber security.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 138240,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-cyber-security-bp355',
    updated_at = NOW()
WHERE cricos_course_code = '114324K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain hands-on skills and knowledge to design unique commercial, residential and industrial buildings through RMIT’s award-winning architectural design prog</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 63875,
    enrolment_fee = 776,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/advanced-diplomas/advanced-diploma-of-building-design-architectural-c6188',
    updated_at = NOW()
WHERE cricos_course_code = '114568A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course will enable you to become an electrical engineer and start a career in a profession that is increasingly in demand.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 47500,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/advanced-diplomas/advanced-diploma-of-engineering-technology--electrical-c6182',
    updated_at = NOW()
WHERE cricos_course_code = '114569M';
-- Register-only (no site match): Diploma of Product Design
UPDATE courses SET
    course_duration_per_week = 104,
    offshore_tuition_fee = 53750,
    enrolment_fee = 746,
    updated_at = NOW()
WHERE cricos_course_code = '114571F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Master of Physiotherapy is a two-year graduate entry to professional practice degree.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 111360,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-physiotherapy-mc287',
    updated_at = NOW()
WHERE cricos_course_code = '115014E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain advanced understanding of commerce to conquer the digital disruption of global business.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 144480,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-commerce-bp357',
    updated_at = NOW()
WHERE cricos_course_code = '115036K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This double degree equips you with advanced accounting skills and trains you to be a forward-thinking leader capable of creating modern business solutions.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 197760,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-accountingbachelor-of-commerce-bp359',
    updated_at = NOW()
WHERE cricos_course_code = '115519B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Through this double degree program, you’ll be equipped with the knowledge and tools to navigate the evolving legal and global business environment.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 252480,
    enrolment_fee = 1865,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-lawsbachelor-of-commerce-bp358',
    updated_at = NOW()
WHERE cricos_course_code = '115520J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Software engineers are in high demand in the trending areas of artificial intelligence, embedded systems, robotics, virtual reality and big data.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 203520,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineering-software-engineering-honours-bh120',
    updated_at = NOW()
WHERE cricos_course_code = '115631B';
-- Register-only (no site match): Bachelor of Urban Policy
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 119520,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '116134M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Expand your worldview with international studies, exploring intercultural, social and political issues.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 119520,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-international-studies-bp332',
    updated_at = NOW()
WHERE cricos_course_code = '116297C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Become a leader in education with a globally recognised teaching degree. RMIT offers qualifications in primary, secondary and early childhood education.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 161280,
    enrolment_fee = 1877,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-education-bp320',
    updated_at = NOW()
WHERE cricos_course_code = '116298B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This degree is designed for students who wish to pursue careers in health and medical research or related government, medical and industry sectors</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 199680,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-biomedical-science-honours-bh130',
    updated_at = NOW()
WHERE cricos_course_code = '116392D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study the Psychology Honours degree at RMIT and become skilled in contemporary research methods that will give your career the edge.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-psychology-honours-bh000',
    updated_at = NOW()
WHERE cricos_course_code = '116393C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Blending technical expertise and business knowledge, this course gives you a solid foundation to start any career in the fashion industry.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 78720,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/associate-degrees/associate-degree-in-fashion-ad030',
    updated_at = NOW()
WHERE cricos_course_code = '116398J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain knowledge and skills in law, legal practice and professional communication, and a sound understanding of ethical requirements in both disciplines.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 252480,
    enrolment_fee = 1865,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-lawsbachelor-of-professional-communication-bp360',
    updated_at = NOW()
WHERE cricos_course_code = '116506K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop expertise and advance your career in the growth industry of electrical and electronic engineering by studying a master''s degree.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-engineering-electrical-and-electronic-engineering-mc180',
    updated_at = NOW()
WHERE cricos_course_code = '116507J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Rapid developments in global telecommunication and network technologies present exciting career opportunities for graduates of this masters degree.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-engineering-telecommunication-and-network-engineering-mc234',
    updated_at = NOW()
WHERE cricos_course_code = '116508H';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>The Master of Clinical Osteopathy gives you the advanced knowledge and clinical skills to ensure you are thoroughly prepared to become an osteopath.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-clinical-osteopathy-mc284',
    updated_at = NOW()
WHERE cricos_course_code = '116509G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study a Master of Electrical Engineering and prepare for a leadership role in the internationally growing sectors of power engineering and energy.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 99840,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-engineering-electrical-engineering-mc235',
    updated_at = NOW()
WHERE cricos_course_code = '116510C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop your software engineering skills to design, code, test and manage large quality-measured software systems. Discover more.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 188160,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-software-engineering-professional-bp096',
    updated_at = NOW()
WHERE cricos_course_code = '116687M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This master''s course aims to equip you with all the tools necessary to secure an organisation''s information systems.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 92160,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-cyber-security-mc159',
    updated_at = NOW()
WHERE cricos_course_code = '116688K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Dive deep into researching topics that challenge and expand our understanding of human interactions and their relationships with environments.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 38880,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-social-science-honours-bh131',
    updated_at = NOW()
WHERE cricos_course_code = '116817F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This course is designed to enhance your career in justice and alternative dispute resolution sector and other sectors including industrial relations, human resources, and project management.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 19680,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/graduate-certificates/graduate-certificate-in-dispute-resolution-gc218',
    updated_at = NOW()
WHERE cricos_course_code = '116818E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain an end-to-end understanding of how pharmaceutical products are designed and developed, as well as the process involved in the large scale production, for a successful career.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 277608,
    enrolment_fee = 1981,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineering-chemical-engineeringhonoursbachelor-of-pharmaceutical-sciences-bh122',
    updated_at = NOW()
WHERE cricos_course_code = '116911H';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Explore ways to improve health and treat disease while studying a double degree course about human, plant and animal biology.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 188160,
    enrolment_fee = 3538,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-science-biotechnologybachelor-of-biomedical-science-bp293',
    updated_at = NOW()
WHERE cricos_course_code = '116912G';
-- Register-only (no site match): Diploma of Health Sciences
UPDATE courses SET
    course_duration_per_week = 52,
    offshore_tuition_fee = 36480,
    enrolment_fee = 373,
    updated_at = NOW()
WHERE cricos_course_code = '117032J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Get accredited to work in medical radiations by studying this 4-year course. Specialise in either medical imaging, nuclear medicine or radiation therapy.</p>',
    course_duration_per_week = 182,
    offshore_tuition_fee = 199680,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-medical-radiation-bp321',
    updated_at = NOW()
WHERE cricos_course_code = '117342F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Get accredited to work in medical radiations by studying this 4-year course. Specialise in either medical imaging, nuclear medicine or radiation therapy.</p>',
    course_duration_per_week = 182,
    offshore_tuition_fee = 199680,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-medical-radiation-bp321',
    updated_at = NOW()
WHERE cricos_course_code = '117343E';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Shape the way our world communicates. Learn how spaces and sectors can be utilised to effectively start important conversations.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 146880,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-graphic-design-bp115',
    updated_at = NOW()
WHERE cricos_course_code = '117452M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>From working in the lab through to production, explore chemistry and chemical engineering to blend science, practice and design to solve global challenges.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 239040,
    enrolment_fee = 1865,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-sciencebachelor-of-engineering-chemical-engineering-honours-bh098',
    updated_at = NOW()
WHERE cricos_course_code = '117798G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Gain an advanced understanding of environmental issues and their solutions when you explore both science and engineering.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 239040,
    enrolment_fee = 4117,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-environmental-sciencebachelor-of-engineering-environmental-engineering-honours-bh096',
    updated_at = NOW()
WHERE cricos_course_code = '117799F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Discover how justice systems interact with law enforcement, explore human rights and global crime, and work on real cases as part of your study.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 119520,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-criminology-and-criminal-justice-bp023',
    updated_at = NOW()
WHERE cricos_course_code = '118024A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Immerse yourself in a creative environment and hone your artistic practice with studio specialisations at a world-leading art and design school.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 135360,
    enrolment_fee = 1760,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-fine-arts-bp201',
    updated_at = NOW()
WHERE cricos_course_code = '118025M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn how technology and innovation is making a positive change in the fashion and textiles industry, and build the knowledge to be part of it.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 149760,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-fashion-sustainability-bp326',
    updated_at = NOW()
WHERE cricos_course_code = '118026K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Master the art of photography. Learn in state-of-the-art facilities, and utilise the creative and practical tools to hone your talent behind the camera.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 135360,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-photography-bp117',
    updated_at = NOW()
WHERE cricos_course_code = '118027J';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This degree empowers you to create change by driving future solutions for biodiversity, climate resilience, sustainable resource management and corporate social responsibility.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 119520,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-sustainability-and-environment-bp362',
    updated_at = NOW()
WHERE cricos_course_code = '118028H';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Find your healthcare niche with a postgraduate degree in acupuncture where you''ll incorporate Western and Chinese medicine theories to treat various conditions.</p>',
    course_duration_per_week = 78,
    offshore_tuition_fee = 68160,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-applied-science-acupuncture-mc024',
    updated_at = NOW()
WHERE cricos_course_code = '118175H';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Be equipped with a practical understanding of how to develop new knowledge to answer industrial or theoretical needs.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 44160,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-computer-science-honours-bh013',
    updated_at = NOW()
WHERE cricos_course_code = '118225C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Equip yourself with advanced research skills in fashion enterprise and technology, preparing you for innovative roles and further study in the dynamic fash</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 48000,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-fashion-enterprise-and-technology-honours-bh132',
    updated_at = NOW()
WHERE cricos_course_code = '118226B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Study this double degree to gain knowledge of the hardware and structure of computer systems as well as the software that is used to control them.</p>',
    course_duration_per_week = 260,
    offshore_tuition_fee = 284064,
    enrolment_fee = 1981,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/honours-degrees/bachelor-of-engineeringelectronic--computer-systems-engineeringhonbachelor-of-computer-science-bh091',
    updated_at = NOW()
WHERE cricos_course_code = '118519M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Make your mark in the global fashion industry with the only nationally accredited fashion styling diploma in Australia.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 23375,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/diplomas/diploma-of-fashion-styling-c5442',
    updated_at = NOW()
WHERE cricos_course_code = '118551M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Build your design fundamentals and find your own path to further design studies.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 20000,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/certificates/certificate-iv-in-design-c4441',
    updated_at = NOW()
WHERE cricos_course_code = '119035A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Further develop your creative practice and hone your photography skills in this practical, industry-led diploma.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 25250,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/diplomas/diploma-of-photography-and-digital-imaging-c5446',
    updated_at = NOW()
WHERE cricos_course_code = '119064G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This degree offers comprehensive accounting knowledge, real-world experience, and skills for a lasting career, preparing you for professional practice and evolving industry demands.</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 197760,
    enrolment_fee = 1492,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-accounting-professional-practice-bp361',
    updated_at = NOW()
WHERE cricos_course_code = '119113C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Develop advanced analytics and AI skills through a strategic business lens, focusing on governance, ethics, policy, and digital transformation.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 103680,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/postgraduate-study/masters-by-coursework/master-of-business-analytics-and-ai-strategy-mc274',
    updated_at = NOW()
WHERE cricos_course_code = '119116M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn civil and structural engineering skills and gain knowledge in the fields of fluids, soil, concrete, CAD, roads, drainage and structures.</p>',
    course_duration_per_week = 104,
    offshore_tuition_fee = 47500,
    enrolment_fee = 746,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/advanced-diplomas/advanced-diploma-of-engineering-technology-civil-engineering-design-c6190',
    updated_at = NOW()
WHERE cricos_course_code = '119171D';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>RMIT UP’s Fast Track is an accelerated pathway for high-achieving international students, preparing you for university in half the time of a Foundation Studies course.</p>',
    course_duration_per_week = 26,
    offshore_tuition_fee = 23000,
    enrolment_fee = 186,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/pre-university-study/fast-track/university-pathways-fast-track-ft001',
    updated_at = NOW()
WHERE cricos_course_code = '119545A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>This practical studio-based course expands your textile skills and knowledge with access to state-of-the-art facilities and industry-connected instructors.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 29625,
    enrolment_fee = 653,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/diplomas/diploma-of-apparel-fashion-and-textiles-c5444',
    updated_at = NOW()
WHERE cricos_course_code = '119921D';
-- Register-only (no site match): Bachelor of Games
UPDATE courses SET
    course_duration_per_week = 156,
    offshore_tuition_fee = 149760,
    enrolment_fee = 1119,
    updated_at = NOW()
WHERE cricos_course_code = '120597A';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Explore trends and issues in music and gain the skills to pursue a career in sound engineering, artist and event management, journalism and more.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 132480,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-music-industry-bp047',
    updated_at = NOW()
WHERE cricos_course_code = '120598M';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Become a creative writing professional through this communications degree. Graduate ready to work as a freelance writer, editor, screenwriter or publisher.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 135360,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-creative-writing-bp257',
    updated_at = NOW()
WHERE cricos_course_code = '120599K';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>In the Advanced Diploma of Visual Arts at RMIT, you will have the opportunity to further develop your artistic practice and enhance your creative skills.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 24500,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/advanced-diplomas/advanced-diploma-of-visual-arts-c6192',
    updated_at = NOW()
WHERE cricos_course_code = '120662H';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>When you study visual arts at RMIT, you''ll create a professional folio of work.</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 25000,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/diplomas/diploma-of-visual-arts-c5448',
    updated_at = NOW()
WHERE cricos_course_code = '120663G';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Are you ready to explore the world of graphic design and develop creative and critical thinking for design?</p>',
    course_duration_per_week = 52,
    offshore_tuition_fee = 25750,
    enrolment_fee = 373,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/vocational-study/diplomas/diploma-of-graphic-design-c5449',
    updated_at = NOW()
WHERE cricos_course_code = '120664F';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Learn to lead fashion enterprises, and specialise in retail, product management or marketing to become a global fashion professional.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 152640,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-fashion-enterprise-bp327',
    updated_at = NOW()
WHERE cricos_course_code = '120689H';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Be the change you want to see and help create fairer, more hopeful futures by supporting individuals, groups and communities with their future aspirations.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 118080,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-social-science-bp363',
    updated_at = NOW()
WHERE cricos_course_code = '120990C';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Blend practical skills and creativity in this innovative degree. Build the skills you need to work across film, television, radio, social and digital media</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 135360,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-media-bp221',
    updated_at = NOW()
WHERE cricos_course_code = '120991B';
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Design interactive experiences and systems, create sound and music, build immersive environments, and craft digital stories.</p>',
    course_duration_per_week = 156,
    offshore_tuition_fee = 135360,
    enrolment_fee = 1119,
    apply_form = 'https://www.rmit.edu.au/study-with-us/levels-of-study/undergraduate-study/bachelor-degrees/bachelor-of-digital-design-bp366',
    updated_at = NOW()
WHERE cricos_course_code = '120992A';
