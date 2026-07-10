-- Update provider institution intakes
UPDATE provider_institution SET
    intake_date = 'February, July',
    updated_at = NOW()
WHERE cricos_provider_code = '00002J';

UPDATE courses SET
    course_description = '<p>In the Bachelor of Information Technology, you''ll acquire foundational skills in programming, data storage and modelling, networking and cybersecurity. You''ll develop broad and coherent knowledge and skills from an area of information technology - such as software design and construction, applied data modelling and analysis, or security problem detection and mitigation - and learn how to apply that knowledge to solve real-world problems. And you''ll learn how to relate your knowledge and skills in information technology to a broader societal context, and make sound decisions regarding ethical and security concerns.</p> <p>In the professionally accredited Bachelor of Actuarial Studies, you''ll learn how to apply mathematical, statistical, economic and financial analysis to a range of practical problems in long-term risk management, finance and insurance.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 46600,
    onshore_tuition_fee = 46600,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-actuarial-studies-and-bachelor-of-information-technology/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Bachelor of Actuarial Studies with Professional Practice (Honours) | https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-actuarial-studies-with-professional-practice-honours/

UPDATE courses SET
    course_description = '<p>Specialising in applying mathematical, statistical and financial analysis, actuaries are key to helping businesses all over the world prosper. They''re in high demand across the many industries that use data - from finance, insurance, superannuation and trading to airlines, energy, healthcare and startups. Actuaries advise corporations, government and non-government organisations on financial management, risk management, product design and complex transactions.</p> <p>As the world''s first accredited actuarial degree, the Bachelor of Actuarial Studies has a legacy of excellence, and unparalleled ties with trailblazing firms that actively seek out our graduates. We''ve produced many of the country''s most prominent and influential actuaries, each of whom continues to have a lasting impact across the sector. We''re recognised as a Centre of Actuarial Excellence by the Society of Actuaries, and by studying here, you''ll gain a strategic advantage via deep industry connections that provide pathways into this highly paid profession. </p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 95 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> HSC Mathematics Extension 1 or equivalent. For International Baccalaureate (IB) applicants, this is equivalent to Mathematics (HL).</p> <p><strong>Recommended Studies:</strong> <p>HSC Mathematics Extension 2 (Band E4) or equivalent. For International Baccalaureate (IB) applicants, this is equivalent to a grade of 6 or 7 in Further Mathematics (HL) or Mathematics: Analysis and Approaches (HL).</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-actuarial-studies/',
    updated_at = NOW()
WHERE cricos_course_code = '067838M';

UPDATE courses SET
    course_description = '<p>The Bachelor of Applied Finance will equip you with comprehensive corporate finance and investment management skills. With the ability to help organisations create value, invest wisely and control risk, you''ll find yourself in demand across the globe.</p> <p>In the professionally accredited Bachelor of Actuarial Studies, you''ll learn how to apply mathematical, statistical, economic and financial analysis to a range of practical problems in long-term risk management, finance and insurance.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-applied-finance-and-bachelor-of-actuarial-studies/',
    updated_at = NOW()
WHERE cricos_course_code = '099516J';

UPDATE courses SET
    course_description = '<p>The multidisciplinary Bachelor of Business Analytics - developed and refined in consultation with industry so content is always current and relevant - equips you with the knowledge and skills to help businesses better understand their consumers, innovate, reduce their risk and maximise opportunities.</p> <p>The Bachelor of Applied Finance will equip you with comprehensive corporate finance and investment management skills. With the ability to help organisations create value, invest wisely and control risk, you''ll find yourself in demand across the globe.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-applied-finance-and-bachelor-of-business-analytics/',
    updated_at = NOW()
WHERE cricos_course_code = '099520B';

UPDATE courses SET
    course_description = '<p>The Bachelor of Economics will provide you with a sound understanding of today''s complex economic environment and the skills to design economic systems that promote welfare, fairness and sustainability. You''ll learn about how modern economies operate, trade and grow; the role of prices and markets in allocating scarce resources; and the sorts of policy interventions that can be introduced when economic outcomes are less than optimal.</p> <p>The Bachelor of Applied Finance will equip you with comprehensive corporate finance and investment management skills. With the ability to help organisations create value, invest wisely and control risk, you''ll find yourself in demand across the globe.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-applied-finance-and-bachelor-of-economics/',
    updated_at = NOW()
WHERE cricos_course_code = '099521A';

UPDATE courses SET
    course_description = '<p>The Bachelor of Applied Finance will equip you with comprehensive corporate finance and investment management skills. With the ability to help organisations create value, invest wisely and control risk, you''ll find yourself in demand across the globe.</p> <p>The Bachelor of Professional Accounting will enable you to understand the challenges and issues facing the world and the accounting profession at present, and will help you meet the requirements for professional accreditation in accounting.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-applied-finance-and-bachelor-of-professional-accounting/',
    updated_at = NOW()
WHERE cricos_course_code = '099522M';

UPDATE courses SET
    course_description = '<p>The finance world is continuously evolving, making it a remarkably exciting field to work in. Being able to expertly navigate the complex world of financial markets, investment banking, corporate finance, superannuation, trading and fintech innovations - and use that expertise to provide optimal advice on growing wealth - is highly desirable in today''s economy.<br/>And as financial landscapes shift, those who can adapt and offer strategic insights will be in demand.</p> <p>The Bachelor of Applied Finance is a practical degree closely aligned to the needs of the job market. Through immersive work-integrated learning and a capstone project developed in consultation with industry experts, you''ll engage in simulations and projects that mirror industry - ensuring real-world insights and challenges thoroughly prepare you to meet workplace expectations. In our state-of-the art Finance Decision Lab, you''ll develop the skills to use multiple databases and apply them in the real world. You''ll also benefit from a connected community that brings together thought leaders and enriching professional development opportunities.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 85 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> HSC Mathematics Advanced or equivalent. If you don''t have assumed knowledge you are advised to include a mathematics or quantitative methods elective unit in your first year of study.</p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-applied-finance/',
    updated_at = NOW()
WHERE cricos_course_code = '027342M';

UPDATE courses SET
    course_description = '',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 44100,
    onshore_tuition_fee = 44100,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-arts-and-bachelor-of-business/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '<p>The Bachelor of Arts has been reimagined by our world-leading academics in consultation with industry partners and public-sector organisations, so you can be assured you''ll acquire the transferable and technical skills needed for success in today''s and tomorrow''s workplaces. Our approach allows you to turn your passion into a career by exploring your interests in-depth, and by honing your skills and knowledge through practical experiences and expert teaching.</p> <p>The Bachelor of Commerce will prepare you to become a business professional in a wide range of careers. You''ll study a set of extensive and integrated foundation units that will orient you to business, followed by one or two majors to develop depth in your chosen discipline. Professional experiences are available with leading industry partners.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 44100,
    onshore_tuition_fee = 44100,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-arts-and-bachelor-of-commerce/',
    updated_at = NOW()
WHERE cricos_course_code = '099530M';

UPDATE courses SET
    course_description = '<p>The Bachelor of Arts has been reimagined by our world-leading academics in consultation with industry partners and public-sector organisations, so you can be assured you''ll acquire the transferable and technical skills needed for success in today''s and tomorrow''s workplaces. Our approach allows you to turn your passion into a career by exploring your interests in-depth, and by honing your skills and knowledge through practical experiences and expert teaching.</p> <p>In the Bachelor of Information Technology, you''ll acquire foundational skills in programming, data storage and modelling, networking and cybersecurity. You''ll develop broad and coherent knowledge and skills from an area of information technology - such as software design and construction, applied data modelling and analysis, or security problem detection and mitigation - and learn how to apply that knowledge to solve real-world problems. And you''ll learn how to relate your knowledge and skills in information technology to a broader societal context, and make sound decisions regarding ethical and security concerns.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 43800,
    onshore_tuition_fee = 43800,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-arts-and-bachelor-of-information-technology/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '<p>The Bachelor of Arts has been reimagined by our world-leading academics in consultation with industry partners and public-sector organisations, so you can be assured you''ll acquire the transferable and technical skills needed for success in today''s and tomorrow''s workplaces. Our approach allows you to turn your passion into a career by exploring your interests in-depth, and by honing your skills and knowledge through practical experiences and expert teaching.</p> <p>The hallmark of Macquarie''s Bachelor of Laws is its recognition of the way legal frameworks underpin such global issues. You''ll be challenged to think critically about the law to seek innovative solutions to legal problems - skills highly valued by employers. With the option to combine your law degree with any other Macquarie bachelor degree, you can open the way to an array of careers in legal practice, private industry, government, education and community services.</p>',
    total_course_duration = 'Full time: 5 years',
    offshore_tuition_fee = 45500,
    onshore_tuition_fee = 45500,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 7</li><li>Minimum 6.5 in reading</li><li>Minimum 6.5 in writing</li><li>Minimum 6.5 in listening</li><li>Minimum 6.5 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-arts-and-bachelor-of-laws/',
    updated_at = NOW()
WHERE cricos_course_code = '099537D';

UPDATE courses SET
    course_description = '<p>The Bachelor of Arts has been reimagined by our world-leading academics in consultation with industry partners and public-sector organisations, so you can be assured you''ll acquire the transferable and technical skills needed for success in today''s and tomorrow''s workplaces. Our approach allows you to turn your passion into a career by exploring your interests in-depth, and by honing your skills and knowledge through practical experiences and expert teaching.</p> <p>The Bachelor of Science is for those excited by discovery and who question the norm. You''ll learn from world-renowned researchers who are addressing the big issues facing our global society, such as the changing environment, future materials and fuels, and biotechnology. You''ll be able to study complementary disciplines or non-science units that feed your curiosity. And you''ll be part of a community that has led many significant initiatives in recent years, including early climate change research, photonics, evolutionary biology and groundbreaking research in earth''s crustal systems.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 43400,
    onshore_tuition_fee = 43400,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-arts-and-bachelor-of-science/',
    updated_at = NOW()
WHERE cricos_course_code = '099540J';

UPDATE courses SET
    course_description = '<p>Arts graduates are sought after by employers because arts degrees ensure you develop strong capabilities in analysis, creativity, research, critical thinking, intercultural awareness and communication - capabilities that are in demand by employers and essential for success in the 21st-century workplace. Arts graduates are recognised by employers for their advanced skills in problem-solving and their ability to make ethical judgements.</p> <p>The Bachelor of Arts has been reimagined by our world-leading academics in consultation with industry partners and public-sector organisations, so you can be assured you''ll acquire the transferable and technical skills needed for success in today''s and tomorrow''s workplaces. Our approach allows you to turn your passion into a career by exploring your interests in-depth, and by honing your skills and knowledge through practical experiences and expert teaching.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 41200,
    onshore_tuition_fee = 41200,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 70 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-arts/',
    updated_at = NOW()
WHERE cricos_course_code = '001357G';

UPDATE courses SET
    course_description = '<p>The survival of all life on earth depends on properly functioning ecosystems. Without biodiversity, ecosystems break down. When this happens, our water systems, the air we breathe and the environments in which we grow food are all impacted. Conserving the environment has become a global priority, and those with specialist skills in not only reducing our footprint but also identifying strategies for preserving our rich diversity are in demand.</p> <p>The broad and flexible Bachelor of Biodiversity and Conservation - which uniquely combines studies in plant and animal sciences, ecology and new remote sensing with environmental and conservation management - will equip you with such specialist skills.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 45600,
    onshore_tuition_fee = 45600,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 75 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Recommended Studies:</strong> <p>HSC Biology or HSC Chemistry plus HSC Mathematics Advanced or equivalent</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-biodiversity-and-conservation/',
    updated_at = NOW()
WHERE cricos_course_code = '067848J';

UPDATE courses SET
    course_description = '<p>The Bachelor of Economics will provide you with a sound understanding of today''s complex economic environment and the skills to design economic systems that promote welfare, fairness and sustainability. You''ll learn about how modern economies operate, trade and grow; the role of prices and markets in allocating scarce resources; and the sorts of policy interventions that can be introduced when economic outcomes are less than optimal.</p> <p>The multidisciplinary Bachelor of Business Analytics - developed and refined in consultation with industry so content is always current and relevant - equips you with the knowledge and skills to help businesses better understand their consumers, innovate, reduce their risk and maximise opportunities.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-business-analytics-and-bachelor-of-economics/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '<p>Big data is big business, and individuals with the ability to extract value from these data sources to help businesses better understand their consumers, innovate, reduce their risk and maximise opportunities are in demand across the globe.</p> <p>The interdisciplinary Bachelor of Business Analytics - developed and frequently refined in consultation with industry - offers a unique blend of business and computing innovation. Whether you tailor your degree towards the business or technical aspects of data analytics, you''ll develop an unrivalled ability to solve problems and create value. You''ll also gain insights into the transformative impact of artificial intelligence on business analytics, and how to effectively use it to drive value and innovation - across organisations and society at large. And like former graduates of Sydney''s only standalone undergraduate business analytics degree, being at the cutting-edge of this discipline will give you a competitive edge when seeking employment at a top-tier employer.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 80 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> HSC Mathematics Advanced or equivalent. If you don''t have the assumed knowledge you''re advised to include a mathematics or quantitative methods elective unit in your first year of study.</p> <p><strong>Recommended Studies:</strong> <p>HSC Mathematics Extension 1 or equivalent.</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-business-analytics/',
    updated_at = NOW()
WHERE cricos_course_code = '079306G';

UPDATE courses SET
    course_description = '',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 46600,
    onshore_tuition_fee = 46600,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-business-and-bachelor-of-information-technology/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 45300,
    onshore_tuition_fee = 45300,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-business-and-bachelor-of-international-studies/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '',
    total_course_duration = 'Full time: 5 years',
    offshore_tuition_fee = 47800,
    onshore_tuition_fee = 47800,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 7</li><li>Minimum 6.5 in reading</li><li>Minimum 6.5 in writing</li><li>Minimum 6.5 in listening</li><li>Minimum 6.5 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-business-and-bachelor-of-laws/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 45400,
    onshore_tuition_fee = 45400,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-business-and-bachelor-of-psychology/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 46300,
    onshore_tuition_fee = 46300,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-business-and-bachelor-of-science/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '<p>In today''s globalised world, where competition among businesses is at an all-time high, there are few careers in which a comprehensive knowledge of business isn''t well-regarded. Those with strong leadership, management and communication skills, as well as capabilities in marketing, human resources, business administration or entrepreneurship, are increasingly respected as influencers in the contemporary workplace.</p> <p>The Bachelor of Business is taught by industry-connected, research-active and award-winning teachers, which ensures it stays ahead of evolving industry needs while equipping you with a broad range of future-focused skills. It will enhance your employability by providing you with the skills employers demand: agility, innovation, strategic thinking and digital fluency. From day one, you''ll build your career toolkit through an integrated employability program that prepares you to expertly navigate a dynamic workforce. Whether you want to launch your own venture, lead in a corporate setting or work globally, you''ll graduate with in-demand, future-focused capabilities that set you apart.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 75 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> HSC Mathematics Standard 2 or equivalent. If you don''t have the assumed knowledge, you''re advised to include a quantitative methods elective unit in your first year of study.</p> <p><strong>Recommended Studies:</strong> <p>None</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-business/',
    updated_at = NOW()
WHERE cricos_course_code = '111851M';

UPDATE courses SET
    course_description = '<p>Chiropractic is an allied health profession focused on the diagnosis, treatment and prevention of musculoskeletal disorders and their effects on body function and overall health. Practitioners have a deep understanding of the relationship between body structure and function, and take a holistic approach to care. Using a range of non-invasive treatments, including manual therapy, therapeutic exercise, patient education, lifestyle advice and self-management strategies, they help people of all ages live full, active and healthy lives.</p> <p>The Bachelor of Chiropractic Science - the longest-running degree of its kind in Australia - will provide you with a strong foundation in health sciences, including human anatomy and physiology, that can be applied to a diverse range of health careers. Importantly, the degree offers a direct pathway into the Master of Chiropractic, which will prepare you to work as a registered chiropractor in private practice, sports medicine, rehabilitation or allied health, or in areas such as health insurance, consulting, work health and safety, or research.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 49300,
    onshore_tuition_fee = 49300,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 80 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> None</p> <p><strong>Recommended Studies:</strong> <p>HSC Biology, HSC chemistry or equivalent</p> <p>HSC Health and Movement Science or equivalent</p> <p>HSC Health and Movement Science Life Skills or equivalent</p> <p>HSC Personal Development, Health and Physical Education or equivalent</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-chiropractic-science/',
    updated_at = NOW()
WHERE cricos_course_code = '028866G';

UPDATE courses SET
    course_description = '<p>A career in medicine, allied health or medical research is about more than treating illness - it''s about changing lives. Driven by compassion and a commitment to helping others, health professionals play a vital role in shaping healthier communities. And with growth and job security projected to continue in Australia and overseas, these dynamic and diverse careers offer the chance to make a real and rewarding difference now and in the future.</p> <p>The Bachelor of Clinical Science is your fast track into medicine, physiotherapy, audiology, speech and language pathology, and public health. By taking advantage of an intensive summer session, you''ll complete the degree in just two years and progress to postgraduate studies sooner. You''ll study in state-of-the-art wet and dry labs, and in small classes where you''ll learn from internationally recognised clinicians, researchers and practicing professionals in a research-intensive environment. And, if you place as a top-30 GEMSAS-admissions-ranked clinical science student and you meet minimum Doctor of Medicine entry requirements, you''ll be guaranteed an interview for the MD.</p>',
    total_course_duration = 'Full time: 2 years',
    offshore_tuition_fee = 74850,
    onshore_tuition_fee = 74850,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 90 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 7 (Minimum 6.5 in reading, 6.5 in writing, 6.5 in listening, and 6.5 in speaking.).</p> <p><strong>Recommended Studies:</strong> <p>HSC Chemistry and HSC Mathematics Advanced, or equivalent. If you haven''t completed HSC Chemistry and HSC Mathematics Advanced, you are advised to undertake relevant bridging courses prior to commencing your degree.</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-clinical-science/',
    updated_at = NOW()
WHERE cricos_course_code = '087679M';

UPDATE courses SET
    course_description = '',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-commerce-and-bachelor-of-actuarial-studies/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-commerce-and-bachelor-of-economics/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '<p>The Bachelor of Commerce will prepare you to become a business professional in a wide range of careers. You''ll study a set of extensive and integrated foundation units that will orient you to business, followed by one or two majors to develop depth in your chosen discipline. Professional experiences are available with leading industry partners.</p> <p>The flexible Bachelor of Engineering (Honours) has a strong focus on practical learning and offers you the choice of five specialisations. You''ll learn how to identify complex problems and determine how to formulate innovative solutions to today''s complex problems. And you''ll be equipped with the skills you''ll need to mix it with history''s greatest engineers - maybe you''ll have the honour of creating the next lifesaving medical device, a clean water system for remote communities in Africa, or a mobile phone app that keeps children safe.</p>',
    total_course_duration = 'Full time: 5.5 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-commerce-and-bachelor-of-engineering-honours/',
    updated_at = NOW()
WHERE cricos_course_code = '109315J';

UPDATE courses SET
    course_description = '<p>The Bachelor of Commerce will prepare you to become a business professional in a wide range of careers. You''ll study a set of extensive and integrated foundation units that will orient you to business, followed by one or two majors to develop depth in your chosen discipline. Professional experiences are available with leading industry partners.</p> <p>In the Bachelor of Information Technology, you''ll acquire foundational skills in programming, data storage and modelling, networking and cybersecurity. You''ll develop broad and coherent knowledge and skills from an area of information technology - such as software design and construction, applied data modelling and analysis, or security problem detection and mitigation - and learn how to apply that knowledge to solve real-world problems. And you''ll learn how to relate your knowledge and skills in information technology to a broader societal context, and make sound decisions regarding ethical and security concerns.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 46600,
    onshore_tuition_fee = 46600,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-commerce-and-bachelor-of-information-technology/',
    updated_at = NOW()
WHERE cricos_course_code = '099533G';

UPDATE courses SET
    course_description = '<p>The Bachelor of Commerce will prepare you to become a business professional in a wide range of careers. You''ll study a set of extensive and integrated foundation units that will orient you to business, followed by one or two majors to develop depth in your chosen discipline. Professional experiences are available with leading industry partners.</p> <p>The hallmark of Macquarie''s Bachelor of Laws is its recognition of the way legal frameworks underpin such global issues. You''ll be challenged to think critically about the law to seek innovative solutions to legal problems - skills highly valued by employers. With the option to combine your law degree with any other Macquarie bachelor degree, you can open the way to an array of careers in legal practice, private industry, government, education and community services.</p>',
    total_course_duration = 'Full time: 5 years',
    offshore_tuition_fee = 47800,
    onshore_tuition_fee = 47800,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 7</li><li>Minimum 6.5 in reading</li><li>Minimum 6.5 in writing</li><li>Minimum 6.5 in listening</li><li>Minimum 6.5 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-commerce-and-bachelor-of-laws/',
    updated_at = NOW()
WHERE cricos_course_code = '099538C';

UPDATE courses SET
    course_description = '<p>The Bachelor of Commerce will prepare you to become a business professional in a wide range of careers. You''ll study a set of extensive and integrated foundation units that will orient you to business, followed by one or two majors to develop depth in your chosen discipline. Professional experiences are available with leading industry partners.</p> <p>The Bachelor of Psychology will provide you with a scientific understanding of the psychological processes that underlie behaviour. You''ll get exposure to a range of fundamental psychological concepts, as well as to specialised areas such as child psychology, neuropsychology, social and personality psychology, organisational psychology, cognition and perception, and psychopathology. When followed by an honours year, this degree is a pathway to postgraduate study, which will enable you to become a qualified psychologist.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 45400,
    onshore_tuition_fee = 45400,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-commerce-and-bachelor-of-psychology/',
    updated_at = NOW()
WHERE cricos_course_code = '099529D';

UPDATE courses SET
    course_description = '<p>The Bachelor of Science is for those excited by discovery and who question the norm. You''ll learn from world-renowned researchers who are addressing the big issues facing our global society, such as the changing environment, future materials and fuels, and biotechnology. You''ll be able to study complementary disciplines or non-science units that feed your curiosity. And you''ll be part of a community that has led many significant initiatives in recent years, including early climate change research, photonics, evolutionary biology and groundbreaking research in earth''s crustal systems.</p> <p>The Bachelor of Commerce will prepare you to become a business professional in a wide range of careers. You''ll study a set of extensive and integrated foundation units that will orient you to business, followed by one or two majors to develop depth in your chosen discipline. Professional experiences are available with leading industry partners.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 46300,
    onshore_tuition_fee = 46300,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-commerce-and-bachelor-of-science/',
    updated_at = NOW()
WHERE cricos_course_code = '099531K';

UPDATE courses SET
    course_description = '<p>In today''s fast-moving and complex business environment, those with advanced technical skills in accounting, analytics, economics, finance, information systems and marketing insights will find themselves in demand in every area of business. A knowledge of commerce is also increasingly valuable for careers in fields such as health, law, psychology, science and technology.</p> <p>The Bachelor of Commerce focuses on data-driven decision-making, which, when combined with interdisciplinary learning and extensive industry engagement, will set you apart when you graduate. Your competitive edge is further enhanced via an embedded employability unit - learn to craft a standout CV and LinkedIn profile, refine your personal brand and sharpen your interview skills - and tailored industry events that facilitate networking opportunities. And you''ll become adept in key competencies highly regarded by today''s top employers: data literacy, business analysis, teamwork, communication, conflict resolution, problem-solving and critical thinking - all with a global mindset.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 80 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> For business analytics, economics, finance majors: HSC Mathematics Advanced or equivalent. For accounting, business information systems, cyber security governance, human resource management, international business, marketing, and marketing insights and analytics majors: HSC Mathematics Standard 2 or equivalent. If you don''t have the assumed knowledge, you''re advised to include a mathematics or quantitative methods elective unit in your first year of study.</p> <p><strong>Recommended Studies:</strong> <p>For accounting, business information systems majors: HSC Mathematics Advanced or equivalent.</p> <p>For finance major: HSC Mathematics Extension 1 or equivalent.</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-commerce/',
    updated_at = NOW()
WHERE cricos_course_code = '048246D';

UPDATE courses SET
    course_description = '',
    total_course_duration = 'Full time: 5 years',
    offshore_tuition_fee = 45500,
    onshore_tuition_fee = 45500,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 7</li><li>Minimum 6.5 in reading</li><li>Minimum 6.5 in writing</li><li>Minimum 6.5 in listening</li><li>Minimum 6.5 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-criminology-and-bachelor-of-laws/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '<p>Criminology is a rich, interdisciplinary field that weaves together specialties across the social sciences, law, politics and psychology. It''s an exciting and dynamic profession that''s ever-changing due to the way modern societies - and the criminals within - constantly evolve.</p> <p>The Bachelor of Criminology cultivates a critical comprehension of crime and injustice. You''ll learn about key institutions of criminal justice, including the police, courts and prisons. You''ll build your knowledge around historical understandings of crime; the enduring relationship between inequality and crime; and how crime intersects with topics such as race, gender, Indigeneity, age and sexuality. You''ll also examine criminological responses to contemporary challenges, including environmental crime, transnational crime, terrorism, cybercrime and security. The degree will empower you to think innovatively and ethically when addressing the persistent challenges of crime, whether you choose to pursue further education, engage in research or enter the workforce.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 41200,
    onshore_tuition_fee = 41200,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>Academic Requirements</strong></td><td>Selection Rank of 75 (or equivalent)</td></tr><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-criminology/',
    updated_at = NOW()
WHERE cricos_course_code = '115579A';

UPDATE courses SET
    course_description = '<p>Every day, cybercriminals exploit the speed, convenience and anonymity of the internet to commit crimes such as phishing, password cracking and ransomware attacks. Cybercrime is on the rise, yet globally there''s a shortfall of more than three million cybersecurity professionals due to a lack of skilled graduates. With demand projected to grow by a further 35 per cent in the next five years, the need for qualified experts has never been greater.</p> <p>The Bachelor of Cyber Security will equip you with the skills to meet the growing demand for experts capable of tackling current and emerging cybercrime challenges. You''ll have access to our $10 million Cyber Security Hub - a space where academia, industry and government join forces to address real-world challenges. This collaboration ensures your learning is informed by the latest developments and that you''re well-prepared for the workforce. You''ll also be mentored by experts with more than 100 years'' combined experience - including specialists in AI, cyber defence and online fraud prevention - and be exposed to cutting-edge research across computing, engineering, business, criminology, law and psychology.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 46300,
    onshore_tuition_fee = 46300,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 75 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Recommended Studies:</strong> <p>HSC Mathematics Extension 1 or HSC Mathematics Extension 2 plus Information Processes and Technology and/or Software Design and Development, or equivalent.</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-cyber-security/',
    updated_at = NOW()
WHERE cricos_course_code = '099143M';

UPDATE courses SET
    course_description = '',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-economics-and-bachelor-of-actuarial-studies/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '',
    total_course_duration = 'Full time: 5 years',
    offshore_tuition_fee = 47800,
    onshore_tuition_fee = 47800,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 7</li><li>Minimum 6.5 in reading</li><li>Minimum 6.5 in writing</li><li>Minimum 6.5 in listening</li><li>Minimum 6.5 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-economics-and-bachelor-of-laws/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '<p>Economic issues are inherent in our everyday lives. Economics affects us as consumers, employees, producers, investors, manufacturers, carers and much more. As members of society, we need to be able to make informed decisions about the optimal allocation of our limited resources.</p> <p>The Bachelor of Economics will arm you with the integrated problem-solving and data analysis skills to tackle this challenge. You''ll develop industry-relevant capabilities from day one through work-integrated learning that prepares you for diverse job prospects, such as consultant, policy analyst, economist, loans offer or risk analyst. And by combining the degree with a second in a high-demand field such as actuarial studies, applied finance, business analytics, commerce or law - or by pursuing a second major in a complementary or entirely different area - you''ll gain a powerful mix of skills and knowledge that broadens your expertise and enhances your career prospects.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 80 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> HSC Mathematics Advanced or equivalent. If you do not have the assumed knowledge, we highly recommend enrolling in a quantitative methods elective unit, such as ECON1031, during your first year of study.</p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-economics/',
    updated_at = NOW()
WHERE cricos_course_code = '001362K';

UPDATE courses SET
    course_description = '<p>Early childhood teachers provide young children with a strong foundation for learning, and help them develop their social and emotional skills. Primary teachers build on these capabilities, helping children develop their literacy and numeracy skills; as well as their physical, arts, social and emotional competencies.</p> <p>The Bachelor of Education (Early Childhood and Primary) is part of an innovative suite of new education degrees being pioneered by Macquarie. Streamlined and future focused, the degrees provide the opportunity to undertake full-time employment as a conditionally accredited teacher during fourth year. Your studies will be integrated into your work via a hybrid program of ''learn, plan, do, reflect'' cycles delivered through education networks helmed by expert teachers. In your first year, you''ll study a set of core units that explore inclusive practices, technology in the classroom, cultural and linguistic diversity, sustainability teaching, the integration of Indigenous knowledge in the classroom, and how children learn. You''ll also undertake your first professional experience placement. In your second and third years, you''ll study units focused on early childhood education and primary teaching. The streamlined nature of the degree, in conjunction with the extensive placements, means you''ll graduate wholly equipped with the knowledge and skills to manage modern early childhood education and primary school settings.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 40400,
    onshore_tuition_fee = 40400,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>Academic Requirements</strong></td><td>Selection Rank of 70 (or equivalent)</td></tr><tr><td><strong>English Proficiency</strong></td><td>IELTS overall score of 7.5 (minimum 7 in reading, 7 in writing, 8 in listening, and 8 in speaking)</td></tr><tr><td><strong>Assumed Knowledge</strong></td><td>HSC Mathematics Standard 2 (Band 4) or equivalent</td></tr><tr><td><strong>Additional Requirements</strong></td><td>If Band 4 or equivalent not met, must undertake unit EDST1234 Mathematics for Primary Teachers</td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-education-early-childhood-and-primary/',
    updated_at = NOW()
WHERE cricos_course_code = '116114D';

UPDATE courses SET
    course_description = '<p>When children are exposed to positive educational experiences prior to school, their learning capabilities - and in turn, their chances of excelling in school - are greatly improved. Quality early childhood education provides a strong foundation for learning, and helps young children develop their social and emotional skills.</p> <p>The Bachelor of Education (Early Childhood) is part of an innovative suite of new education degrees being pioneered by Macquarie. Streamlined and future focused, the degrees provide the opportunity to undertake full-time employment as a conditionally accredited teacher during fourth year. Your studies will be integrated into your work via a hybrid program of ''learn, plan, do, reflect'' cycles delivered through education networks helmed by expert teachers. In your first year, you''ll study a set of core units that explore inclusive practices, technology in the classroom, cultural and linguistic diversity, sustainability teaching, the integration of Indigenous knowledge in the classroom, and how children learn. You''ll also undertake your first professional experience placement. In your second and third years, you''ll study units focused on early childhood education. The streamlined nature of the degree, in conjunction with the extensive placements, means you''ll graduate wholly equipped with the knowledge and skills to manage modern early childhood education settings.</p> <p>Note: Session 2 commencement is available to <a href="https://www.mq.edu.au/faculty-of-arts/schools/macquarie-school-of-education/bachelor-of-education-early-childhood-stepahead">Bachelor of Education (Early Childhood) - StepAhead Program</a> students only.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 40400,
    onshore_tuition_fee = 40400,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 70 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 7.5 (Minimum 7 in reading, 7 in writing, 8 in listening, and 8 in speaking.).</p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-education-early-childhood/',
    updated_at = NOW()
WHERE cricos_course_code = '116113E';

UPDATE courses SET
    course_description = '<p>Primary educators encourage children to reach their full potential, helping them develop foundational skills in areas such as literacy and numeracy, and assisting them to grow their physical, arts, social and emotional competencies.</p> <p>The Bachelor of Education (Primary) is part of an innovative suite of new education degrees being pioneered by Macquarie. Streamlined and future focused, the degrees provide the opportunity to undertake full-time employment as a conditionally accredited teacher during fourth year. Your studies will be integrated into your work via a hybrid program of ''learn, plan, do, reflect'' cycles delivered through education networks helmed by expert teachers. In your first year, you''ll study a set of core units that explore inclusive practices, technology in the classroom, cultural and linguistic diversity, sustainability teaching, the integration of Indigenous knowledge in the classroom, and how children learn. In your second and third years, you''ll study units focused on primary teaching, and you''ll undertake your first professional placements. The streamlined nature of the degree, in conjunction with the extensive placements, means you''ll graduate wholly equipped with the capabilities to manage modern primary school settings.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 40400,
    onshore_tuition_fee = 40400,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>Academic Requirements</strong></td><td>Selection Rank of 70 (or equivalent)</td></tr><tr><td><strong>English Proficiency</strong></td><td>IELTS overall score of 7.5 (minimum 7 in reading, 7 in writing, 8 in listening, and 8 in speaking)</td></tr><tr><td><strong>Assumed Knowledge</strong></td><td>HSC Mathematics Standard 2 (Band 4) or equivalent</td></tr><tr><td><strong>Additional Requirements</strong></td><td>If Band 4 or equivalent not met, must undertake unit EDST1234 Mathematics for Primary Teachers</td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-education-primary/',
    updated_at = NOW()
WHERE cricos_course_code = '116111G';

UPDATE courses SET
    course_description = '<p>Secondary education teachers guide and support high school students during what can be an exciting and challenging period in their lives. High-quality high school teachers inspire a love of learning and enquiry in their students, and help them develop skills that enable them to reach their full potential.</p> <p>The Bachelor of Education (Secondary) is part of an innovative suite of new education degrees being pioneered by Macquarie. Streamlined and future focused, the degrees provide the opportunity to undertake full-time employment as a conditionally accredited teacher during fourth year. Your studies will be integrated into your work via a hybrid program of ''learn, plan, do, reflect'' cycles delivered through education networks helmed by expert teachers. In your first year, you''ll study a set of core units that explore inclusive practices, technology in the classroom, cultural and linguistic diversity, sustainability teaching, the integration of Indigenous knowledge in the classroom, and how children learn. In your second and third years, you''ll study units focused on secondary teaching, and you''ll undertake your first professional experience placements. The streamlined nature of the degree, in conjunction with the extensive placements, means you''ll graduate wholly equipped with the knowledge and skills to manage modern secondary school settings.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 40400,
    onshore_tuition_fee = 40400,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 70 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 7.5 (Minimum 7 in reading, 7 in writing, 8 in listening, and 8 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> For Mathematics as a First or Second teaching area: HSC Mathematics Advanced Band 4 and above or Extension 1 Band E2 and above or Extension 2 Band E2 and above.</p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-education-secondary/',
    updated_at = NOW()
WHERE cricos_course_code = '116112F';

UPDATE courses SET
    course_description = '<p>From the first tools and machines to renewable energy systems, robotics and artificial intelligence, engineering has always driven progress. Engineers imagine and create the technologies that power societies, shape communities and improve everyday life. And with global challenges increasingly demanding innovative, ethical and sustainable solutions, there''s never been a more exciting time to become an engineer.</p> <p>The Bachelor of Engineering (Honours) offers a hands-on, multidisciplinary learning experience that connects you with industry from day one. You''ll study in our new state-of-the-art engineering building - home to mega labs featuring renewable-energy, satellite, geotechnical and drone facilities; rapid prototyping, robotics, wifi and VR spaces; and dedicated areas for collaboration and innovation. Through project-based learning, you''ll design creative solutions to real-world challenges with a focus on sustainability, community impact and ethical responsibility, while developing the technical expertise and professional skills employers value. Surrounded by an active community of researchers, educators and student teams, you''ll graduate ready to engineer a better future.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 80 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> HSC Mathematics Advanced (Band 4) or equivalent. If you don''t have the assumed knowledge, you''re advised to undertake a bridging course in mathematics.</p> <p><strong>Recommended Studies:</strong> <p>HSC Mathematics Extension 1 or HSC Mathematics Extension 2 plus HSC Physics, or equivalent. HSC Software Design and Development or equivalent.</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-engineering-honours/',
    updated_at = NOW()
WHERE cricos_course_code = '087876F';

UPDATE courses SET
    course_description = '<p>The Bachelor of Environment explores critical environmental systems and processes, relationships between humans and their environments, and the interactions that influence sustainable futures. It''s founded in the scientific aspects of the environment, the effects of human-induced changes, and the management of resources. You''ll become highly knowledgeable about how individuals, societies and governments can best navigate a path towards sustainability, and economic and social prosperity. With huge growth projected in the environment sector in the coming years, this skill set will see you in high demand.</p> <p>The hallmark of Macquarie''s Bachelor of Laws is its recognition of the way legal frameworks underpin such global issues. You''ll be challenged to think critically about the law to seek innovative solutions to legal problems - skills highly valued by employers. With the option to combine your law degree with any other Macquarie bachelor degree, you can open the way to an array of careers in legal practice, private industry, government, education and community services.</p>',
    total_course_duration = 'Full time: 5 years',
    offshore_tuition_fee = 47300,
    onshore_tuition_fee = 47300,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 7</li><li>Minimum 6.5 in reading</li><li>Minimum 6.5 in writing</li><li>Minimum 6.5 in listening</li><li>Minimum 6.5 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-environment-and-bachelor-of-laws/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '<p>Climate change and the environment are major concerns of our time. Environmental scientists and managers play important roles in addressing environmental issues, such as air, water and land degradation; ecosystem health; pollution and contamination; management of natural resources; and species extinction.</p> <p>The Bachelor of Environment explores critical environmental systems and processes, relationships between humans and their environments, and the interactions that influence sustainable futures. It''s founded in the scientific aspects of the environment, the effects of human-induced changes, and the management of resources. You''ll become highly knowledgeable about how individuals, societies and governments can best navigate a path towards sustainability, and economic and social prosperity. With huge growth projected in the environment sector in the coming years, this skill set will see you in high demand.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 45600,
    onshore_tuition_fee = 45600,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 75 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Recommended Studies:</strong> <p>HSC Earth and Environmental Science, HSC Biology, HSC Geography, HSC Chemistry, HSC Mathematics Advanced, or equivalent.</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-environment/',
    updated_at = NOW()
WHERE cricos_course_code = '067858G';

UPDATE courses SET
    course_description = '<p>With demand rising for performance, rehabilitation and preventative health support, exercise scientists are increasingly shaping outcomes across sport, healthcare and community settings. These include working with elite athletes, supporting injury recovery, contributing to workplace health initiatives, and collaborating with medical and allied health professionals. They''re employed in private practice, hospitals, gyms, aged care, government agencies and professional sport.</p> <p>The Bachelor of Exercise and Sports Science positions you to meet this demand - preparing you to apply evidence-based practice across sport, health and performance-focused careers. You''ll deepen your understanding of human movement and apply that theory during practical work in our world-class facilities, and during in-depth placements in real-world settings. You''ll learn from leading researchers with expertise in running injuries, cardiac rehabilitation, and defence and military performance - with opportunities available to participate in their projects. And you''ll benefit from our academic ties to peak bodies, including Exercise and Sports Science Australia, and the Council of Heads of Exercise, Sport and Movement Sciences.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 45700,
    onshore_tuition_fee = 45700,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>Academic Requirements</strong></td><td>Selection Rank of 80 (or equivalent)</td></tr><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 7</li><li>Minimum 6.5 in reading</li><li>Minimum 6.5 in writing</li><li>Minimum 6.5 in listening</li><li>Minimum 6.5 in speaking</li></ul></td></tr><tr><td><strong>Assumed Knowledge</strong></td><td>None</td></tr><tr><td><strong>Recommended Studies</strong></td><td><ul><li>HSC Personal Development, Health and Physical Education (PDHPE)</li><li>HSC Mathematics Advanced</li><li>or equivalent</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-exercise-and-sports-science/',
    updated_at = NOW()
WHERE cricos_course_code = '108721C';

UPDATE courses SET
    course_description = '<p>From Triple-A titles such as Minecraft, Grand Theft Auto and Mario Kart, to indie hits like Hollow Knight and mobile favourite Fruit Ninja, the games industry today is worth billions of dollars - and continues to grow and diversify. As gaming technology advances, new opportunities emerge: mobile devices have put games in our pockets, while virtual and augmented reality are expanding the ways we play and create. People of all ages, genders and backgrounds now engage with games not only as players, but as makers - using them to tell stories, communicate ideas and build communities. Far from being just entertainment, games have become a mass medium shaping culture, creativity and careers.</p> <p>The unique Bachelor of Game Design and Development will prepare you for a successful career designing and creating the next wave of popular video games and virtual worlds. You''ll learn from experienced teachers who write, design, program, produce and publish video and tabletop games. You''ll be mentored by industry experts through a work-integrated learning unit that simulates the developer-producer relationship, and have ample opportunities to grow your professional portfolio and develop agile project management skills - then put them into practice. No coding experience is required, as programming is taught from the ground up.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 46300,
    onshore_tuition_fee = 46300,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>Academic Requirements</strong></td><td>Selection Rank of 75 (or equivalent)</td></tr><tr><td><strong>English Proficiency</strong></td><td>IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking)</td></tr><tr><td><strong>Recommended Studies</strong></td><td><ul><li>HSC Information Processes and Technology and/or HSC Software Design and Development, or equivalent</li><li>HSC Mathematics Advanced Band 4 and above or Extension 1 Band E2 and above or Extension 2 Band E2 and above</li><li>Students who have not achieved this level of HSC Mathematics should enroll in MATH1000 as an elective unit in their first year</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-game-design-and-development/',
    updated_at = NOW()
WHERE cricos_course_code = '099144K';

UPDATE courses SET
    course_description = '<p>With advances in science, technology and wellness driving transformative change in the healthcare sector, health sciences professionals are more in-demand than ever. Enhancing our understanding of health, disease prevention and healthcare delivery is paramount to improving human wellbeing. A career in health sciences offers job security, a competitive salary and diverse career paths in traditional and holistic healthcare.</p> <p>The Bachelor of Health Sciences is an innovative and versatile degree. You''ll build foundational skills through a set of core units, before broadening your knowledge via one of four interdisciplinary majors in coaching, counselling, digital health or health administration. You''ll master the fundamentals of human health and explore the social and societal factors that influence it, equipping you with the knowledge to make a meaningful impact on the health sector. With hands-on learning in our world-class health precinct, you''ll set yourself apart as you prepare for a successful career in the ever-evolving healthcare industry. </p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 41200,
    onshore_tuition_fee = 41200,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 80 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> None</p> <p><strong>Recommended Studies:</strong> <p>HSC Health and Movement Science or equivalent</p> <p>HSC Health and Movement Science Life Skills or equivalent</p> <p>HSC Personal Development, Health and Physical Education or equivalent</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-health-sciences/',
    updated_at = NOW()
WHERE cricos_course_code = '117556C';

UPDATE courses SET
    course_description = '<p>The way we interpret history shapes how we understand the world today. By exploring events, people and ideas across centuries, historians learn to question sources, challenge assumptions and uncover how power, culture, conflict and identity have shaped society. From analysing ancient inscriptions and archaeological evidence to working with digital archives, the study of history cultivates critical thinking, rigorous research and clear communication.</p> <p>The Bachelor of History offers a dynamic exploration of the human experience - from ancient civilisations to contemporary global societies. Built around a multidisciplinary core and four comprehensive majors, the degree allows you to tailor your studies to your passions - be it ancient or modern history, archaeology, or public history and heritage. Furthermore, the degree is shaped by insights from cultural heritage professionals, and includes opportunities for internships, museum work, fieldwork and digital projects. Together, these ensure you graduate with practical, job-ready skills. Whether you want to work in policy, media, education, heritage or beyond, you''ll graduate ready to think analytically, work with emerging technologies and question the world around you.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 41200,
    onshore_tuition_fee = 41200,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>Academic Requirements</strong></td><td>Selection Rank of 75 (or equivalent)</td></tr><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-history/',
    updated_at = NOW()
WHERE cricos_course_code = '118456K';

UPDATE courses SET
    course_description = '<p>In the Bachelor of Information Technology, you''ll acquire foundational skills in programming, data storage and modelling, networking and cybersecurity. You''ll develop broad and coherent knowledge and skills from an area of information technology - such as software design and construction, applied data modelling and analysis, or security problem detection and mitigation - and learn how to apply that knowledge to solve real-world problems. And you''ll learn how to relate your knowledge and skills in information technology to a broader societal context, and make sound decisions regarding ethical and security concerns.</p> <p>The flexible Bachelor of Engineering (Honours) has a strong focus on practical learning and offers you the choice of five specialisations. You''ll learn how to identify complex problems and determine how to formulate innovative solutions to today''s complex problems. And you''ll be equipped with the skills you''ll need to mix it with history''s greatest engineers - maybe you''ll have the honour of creating the next lifesaving medical device, a clean water system for remote communities in Africa, or a mobile phone app that keeps children safe.</p>',
    total_course_duration = 'Full time: 5 years',
    offshore_tuition_fee = 46700,
    onshore_tuition_fee = 46700,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-information-technology-and-bachelor-of-engineering-honours/',
    updated_at = NOW()
WHERE cricos_course_code = '109315J';

UPDATE courses SET
    course_description = '<p>Information technology powers the systems, software and data that underpin how the world communicates, trades and innovates. From cybersecurity and artificial intelligence to app development and data analytics, IT professionals design, build and protect the digital solutions that keep our world running. As information grows exponentially and technology continues to evolve, specialists who can integrate technical knowledge with creativity and problem-solving are in high demand across every sector.</p> <p>The Bachelor of Information Technology will equip you with the technical, analytical and professional expertise needed for the IT careers of the future. Co-designed with industry leaders, the degree connects you with partners such as Microsoft, IBM, TCS, Amazon, CSIRO Data61 and DSTG. You''ll study in one of Australia''s leading high-tech precincts, complete projects that solve real-world challenges, and access internships and employment opportunities with more than 300 leading companies on our doorstep. With invaluable hands-on experience and industry insight, you''ll graduate ready to shape technology-driven solutions that transform organisations and society.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 46300,
    onshore_tuition_fee = 46300,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 75 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Recommended Studies:</strong> <p>HSC Mathematics Extension 1 or HSC Mathematics Extension 2 plus HSC Information Processes and Technology and/or HSC Software Design and Development, or equivalent.</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-information-technology/',
    updated_at = NOW()
WHERE cricos_course_code = '047327M';

UPDATE courses SET
    course_description = '<p>The Bachelor of International Studies, which combines the study of cultures and global society with the acquisition of advanced foreign language and communication skills and knowledge about global diversity and mobility, will equip you with transferable intercultural skills that are highly valued in today''s globalised job market.</p> <p>The hallmark of Macquarie''s Bachelor of Laws is its recognition of the way legal frameworks underpin such global issues. You''ll be challenged to think critically about the law to seek innovative solutions to legal problems - skills highly valued by employers. With the option to combine your law degree with any other Macquarie bachelor degree, you can open the way to an array of careers in legal practice, private industry, government, education and community services.</p>',
    total_course_duration = 'Full time: 5 years',
    offshore_tuition_fee = 46500,
    onshore_tuition_fee = 46500,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 7</li><li>Minimum 6.5 in reading</li><li>Minimum 6.5 in writing</li><li>Minimum 6.5 in listening</li><li>Minimum 6.5 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-international-studies-and-bachelor-of-laws/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 42900,
    onshore_tuition_fee = 42900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-international-studies-and-bachelor-of-media-and-communications/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 44700,
    onshore_tuition_fee = 44700,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-international-studies-and-bachelor-of-security-studies/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '<p>Our connected world is facing a growing set of intersecting challenges - from escalating climate change and recurring pandemics to shifting geopolitical alliances and emerging technologies. As the landscape evolves, new opportunities arise, and those who can respond to complexity with a global, cross-disciplinary mindset are in demand. Now more than ever, the world needs thinkers who see the bigger picture - and have the insight, foresight and agility to drive meaningful change.</p> <p>In the Bachelor of International Studies, you''ll collaborate with changemakers, research experts and global communities to co-create practical responses to emerging global needs. You''ll explore the political, social and economic drivers of change, and develop your own adaptive toolkit - blending cultural intelligence, storytelling, tech fluency, mediation and strategic thinking. Whether your interests lie in public policy, global business, diplomacy, social enterprise or tech ethics, you''ll graduate with a real-world portfolio; an international network; and the ability to anticipate disruption, engage diverse perspectives and collaborate globally.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 43700,
    onshore_tuition_fee = 43700,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>Academic Requirements</strong></td><td>Selection Rank of 75 (or equivalent)</td></tr><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-international-studies/',
    updated_at = NOW()
WHERE cricos_course_code = '118457J';

UPDATE courses SET
    course_description = '<p>The Bachelor of Psychology will provide you with a scientific understanding of the psychological processes that underlie behaviour. You''ll get exposure to a range of fundamental psychological concepts, as well as to specialised areas such as child psychology, neuropsychology, social and personality psychology, organisational psychology, cognition and perception, and psychopathology. When followed by an honours year, this degree is a pathway to postgraduate study, which will enable you to become a qualified psychologist.</p> <p>The hallmark of Macquarie''s Bachelor of Laws is its recognition of the way legal frameworks underpin such global issues. You''ll be challenged to think critically about the law to seek innovative solutions to legal problems - skills highly valued by employers. With the option to combine your law degree with any other Macquarie bachelor degree, you can open the way to an array of careers in legal practice, private industry, government, education and community services.</p>',
    total_course_duration = 'Full time: 5 years',
    offshore_tuition_fee = 46600,
    onshore_tuition_fee = 46600,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 7</li><li>Minimum 6.5 in reading</li><li>Minimum 6.5 in writing</li><li>Minimum 6.5 in listening</li><li>Minimum 6.5 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-laws-and-bachelor-of-psychology/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '<p>Law shapes the way societies function. It governs everything from how we respond to environmental disasters to how we manage conflict, safeguard privacy and uphold human rights. As global challenges evolve, the world needs people who can analyse complex issues, interpret competing interests and design solutions that balance justice, ethics and impact. This is why legal know-how is valued far beyond the courtroom - in business, government, finance and advocacy - anywhere clear thinking and strong reasoning are essential.</p> <p>The Bachelor of Laws is built around real experience and genuine connection with industry. You''ll have opportunities to complete an internship for academic credit at a leading firm, including Allens, Ashurst, Clayton Utz or MinterEllison - a springboard many former students have leveraged to secure a permanent role - or gain client-facing experience at Wallumatta Legal, our not-for-profit family law firm dedicated to improving access to justice. You''ll be encouraged to further build your practical capabilities by working with our Social Justice and Strategic Litigation Clinics, and you''ll learn within a modern law precinct that facilitates collaboration with your peers and academics.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 48400,
    onshore_tuition_fee = 48400,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 90 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 7 (Minimum 6.5 in reading, 6.5 in writing, 6.5 in listening, and 6.5 in speaking.).</p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-laws/',
    updated_at = NOW()
WHERE cricos_course_code = '080288E';

UPDATE courses SET
    course_description = '<p>Digital media has had a profound influence on the marketing landscape. Google Ads, email campaigns, influencer marketing, gamification, paid search, SEO and social media are all essential elements for marketing success, and for any business wishing to build mutually rewarding relationships with its customers.</p> <p>The Bachelor of Marketing and Media provides a uniquely integrated approach to marketing and media studies. It''s a boutique degree that fosters an open, collaborative and agile mindset, which will set you up to excel in a variety of professional roles across FMCG, media and communications, hospitality, pharmaceutical, retail, technology, e-commerce, travel and beyond. Ensuring the degree lives up to its reputation, you''ll be taught by award-winning teachers frequently sought for expert commentary and have access to state-of-the-art facilities, including one of Australia''s best-equipped screen studios, a high-spec digital newsroom, and advanced radio and podcasting production studios.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 85 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> HSC Mathematics Standard 2 or equivalent. If you don''t have the assumed knowledge, you''re advised to include a quantitative methods elective unit in your first year of study.</p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-marketing-and-media/',
    updated_at = NOW()
WHERE cricos_course_code = '074754A';

UPDATE courses SET
    course_description = '<p>The Bachelor of Media and Communications will equip you with the skills you''ll need to respond to today''s - and tomorrow''s - rapidly evolving media environment. Whether you''re interested in making your own films or music videos, writing for print and online publications, designing interactive and media-rich websites, producing radio podcasts and broadcasts, streaming live media or managing public relations campaigns, this degree will position you at the heart of content creation.</p> <p>The hallmark of Macquarie''s Bachelor of Laws is its recognition of the way legal frameworks underpin such global issues. You''ll be challenged to think critically about the law to seek innovative solutions to legal problems - skills highly valued by employers. With the option to combine your law degree with any other Macquarie bachelor degree, you can open the way to an array of careers in legal practice, private industry, government, education and community services.</p>',
    total_course_duration = 'Full time: 5 years',
    offshore_tuition_fee = 45800,
    onshore_tuition_fee = 45800,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 7</li><li>Minimum 6.5 in reading</li><li>Minimum 6.5 in writing</li><li>Minimum 6.5 in listening</li><li>Minimum 6.5 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-media-and-communications-and-bachelor-of-laws/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '<p>In today''s always-on environment where seemingly everyone wants news and entertainment at their fingertips, the heart of storytelling is an exciting and powerful place to be.</p> <p>The Bachelor of Media and Communications will equip you with the skills you''ll need to respond to today''s - and tomorrow''s - rapidly evolving media environment. Whether you''re interested in making your own films or music videos, writing for print and online publications, designing interactive and media-rich websites, producing radio podcasts and broadcasts, streaming live media or managing public relations campaigns, this degree will position you at the heart of content creation.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 42000,
    onshore_tuition_fee = 42000,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>Academic Requirements</strong></td><td>Selection Rank of 75 (or equivalent)</td></tr><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-media-and-communications/',
    updated_at = NOW()
WHERE cricos_course_code = '099147G';

UPDATE courses SET
    course_description = '<p>The interdisciplinary Bachelor of Medical Sciences will provide you with a broad background in biological, chemical, biomolecular and biomedical sciences - the knowledge and skills you''ll need for a career in health and medical science fields. Whether that be unravelling the molecular building blocks that underpin disease, developing new drugs to treat or cure disease, implementing biosecurity procedures to overcome emerging disease threats, or applying your scientific knowledge to help solve crimes.</p> <p>The hallmark of Macquarie''s Bachelor of Laws is its recognition of the way legal frameworks underpin such global issues. You''ll be challenged to think critically about the law to seek innovative solutions to legal problems - skills highly valued by employers. With the option to combine your law degree with any other Macquarie bachelor degree, you can open the way to an array of careers in legal practice, private industry, government, education and community services.</p>',
    total_course_duration = 'Full time: 5 years',
    offshore_tuition_fee = 47300,
    onshore_tuition_fee = 47300,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 7</li><li>Minimum 6.5 in reading</li><li>Minimum 6.5 in writing</li><li>Minimum 6.5 in listening</li><li>Minimum 6.5 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-medical-sciences-and-bachelor-of-laws/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '<p>Medical science drives the discoveries that save lives and improve global health. From understanding the molecular mechanisms of disease to developing new drugs and therapies, medical scientists are at the forefront of tackling the world''s most complex health challenges. As health remains one of the fastest-growing global sectors, demand is high for professionals who can link scientific discovery with real-world medical outcomes.</p> <p>The interdisciplinary Bachelor of Medical Sciences will equip you with the expertise to address complex challenges across the full spectrum of human health and disease. You''ll learn from leaders in genomics, modern therapeutics, personalised medicine, proteomics and glycomics. Through small-group learning, you''ll engage closely with academics and peers while gaining hands-on experience in world-class facilities on campus, and within specialist affiliate research laboratories. And you''ll build connections with leading industry partners, positioning you to help drive the future of health and medical science.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 45600,
    onshore_tuition_fee = 45600,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 85 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Recommended Studies:</strong> <p>HSC Mathematics Advanced, HSC Chemistry, or equivalent.</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-medical-sciences/',
    updated_at = NOW()
WHERE cricos_course_code = '020161F';

UPDATE courses SET
    course_description = '<p>Urban and regional planning is a profession that shapes the places where people live, work and play. Planners aim to improve the social and environmental fabric of cities by creating vibrant, healthy and equitable communities, and by facilitating sustainable transport, infrastructure and growth. How we plan our cities and regions today will profoundly affect future generations in a climate-changed world.</p> <p>Innovative in its approach to understanding contemporary social, urban and environmental issues in urban and regional planning, the Bachelor of Planning focuses on recognising the social and cultural diversity of places, and the importance of cross-cultural approaches to research, plan-making and impact assessment. It will not only prepare you for a career in planning in which you have the power to shape more liveable and sustainable futures, but will also give you a distinctive edge among your peers..</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 45700,
    onshore_tuition_fee = 45700,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>Academic Requirements</strong></td><td>Selection Rank of 75 (or equivalent)</td></tr><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-planning/',
    updated_at = NOW()
WHERE cricos_course_code = '060724M';

UPDATE courses SET
    course_description = '<p>Accounting - often referred to as the language of business - is the collection, measurement and communication of financial information for strategic planning, reporting and decision-making. Understanding this language gives accountants the privileged position of being key contributors to a business'' success - from helping companies track their carbon footprint to ensuring ethical and sustainable supply chains, accountants are at the forefront of environmental responsibility and social impact. And with 10,000 new accounting positions needed every year in Australia alone, they are in demand.</p> <p>The Bachelor of Professional Accounting - accredited by Australia''s major professional bodies - is the only undergraduate accounting degree to offer forensic accounting and blockchain units. Designed with input from 150 of Sydney''s leading CFOs, the degree offers a comprehensive curriculum that balances the acquisition of data analysis and practical business skills with industry-standard software training. As such, it offers unrivalled employability outcomes at top-tier firms and across a wide range of dynamic industries such as finance, healthcare, technology, entertainment and more.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 80 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> HSC Mathematics Standard 2 or equivalent. If you don''t have the assumed knowledge, you''re advised to include a mathematics or quantitative methods elective unit in your first year of study.</p> <p><strong>Recommended Studies:</strong> <p>HSC Mathematics Advanced or equivalent.</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-professional-accounting/',
    updated_at = NOW()
WHERE cricos_course_code = '099149E';

UPDATE courses SET
    course_description = '<p>Psychology is a discipline that involves both scientific research and applied professional practice. Psychologists seek to understand how the mind works - they focus on the complexities of human behaviour and provide strategies that can help people lead happier, healthier and more productive lives.</p> <p>The prestigious Bachelor of Psychological Sciences (Honours) is intended for high-achieving students aiming for a career in a specialist field such as clinical neuropsychology, clinical psychology, organisational psychology or professional psychology. You''ll study advanced topics in psychology and professional practice, receive further training in the analysis of data and research methodologies, and conduct a substantive piece of research. Through these studies, you''ll advance your scientific understanding of the psychological processes that underlie behaviour, including cognition, emotion, learning, motivation, perception and personality.</p>',
    total_course_duration = 'Full time: 1 year',
    offshore_tuition_fee = 43900,
    onshore_tuition_fee = 43900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> Admission Requirements: Hold a Level 1 Australian Psychology Accreditation Council (APAC) approved Psychology Bachelors Degree (AQF level 7), or APAC endorsed equivalent, with a minimum performance equivalent to a MQ WAM of 75+. Admission is competitive; meeting the minimum requirement does not guarantee admission. Assumed Knowledge: Competence in research methods and statistics (equivalent to MQ PSYU3349)</p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-psychological-sciences-honours/',
    updated_at = NOW()
WHERE cricos_course_code = '113700K';

UPDATE courses SET
    course_description = '<p>Defined as the study of the human mind and behaviour, and characterised by both scientific research and applied professional practice, psychology plays an important role in modern society. Its insights are extremely valuable not only in clinical settings but across a wide range of fields - including human resources, law, education, social work, criminology, market research and computer programming.</p> <p>In the Bachelor of Psychology, you''ll build foundational skills through a set of core units before broadening your knowledge via one of three interdisciplinary majors in cognitive science, counselling or psychological science. Many of your teachers are psychologists who actively practice or consult with major organisations, such as the Australian Defence Force and elite sporting clubs. Their deep research expertise in areas such as mental health, cognition, behaviour, human experience and challenges across the lifespan ensures your learning is tied to real-world insight. When followed by an honours year, this degree is a pathway to postgraduate study, which will enable you to become a qualified psychologist.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 43900,
    onshore_tuition_fee = 43900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 80 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Recommended Studies:</strong> <p>HSC Mathematics Advanced or equivalent.</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-psychology/',
    updated_at = NOW()
WHERE cricos_course_code = '099150A';

UPDATE courses SET
    course_description = '<p>The Bachelor of Science is for those excited by discovery and who question the norm. You''ll learn from world-renowned researchers who are addressing the big issues facing our global society, such as the changing environment, future materials and fuels, and biotechnology. You''ll be able to study complementary disciplines or non-science units that feed your curiosity. And you''ll be part of a community that has led many significant initiatives in recent years, including early climate change research, photonics, evolutionary biology and groundbreaking research in earth''s crustal systems.</p> <p>In the professionally accredited Bachelor of Actuarial Studies, you''ll learn how to apply mathematical, statistical, economic and financial analysis to a range of practical problems in long-term risk management, finance and insurance.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 46300,
    onshore_tuition_fee = 46300,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-science-and-bachelor-of-actuarial-studies/',
    updated_at = NOW()
WHERE cricos_course_code = '099515K';

UPDATE courses SET
    course_description = '<p>The Bachelor of Science is for those excited by discovery and who question the norm. You''ll learn from world-renowned researchers who are addressing the big issues facing our global society, such as the changing environment, future materials and fuels, and biotechnology. You''ll be able to study complementary disciplines or non-science units that feed your curiosity. And you''ll be part of a community that has led many significant initiatives in recent years, including early climate change research, photonics, evolutionary biology and groundbreaking research in earth''s crustal systems.</p> <p>The flexible Bachelor of Engineering (Honours) has a strong focus on practical learning and offers you the choice of five specialisations. You''ll learn how to identify complex problems and determine how to formulate innovative solutions to today''s complex problems. And you''ll be equipped with the skills you''ll need to mix it with history''s greatest engineers - maybe you''ll have the honour of creating the next lifesaving medical device, a clean water system for remote communities in Africa, or a mobile phone app that keeps children safe.</p>',
    total_course_duration = 'Full time: 5 years',
    offshore_tuition_fee = 46400,
    onshore_tuition_fee = 46400,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-science-and-bachelor-of-engineering-honours/',
    updated_at = NOW()
WHERE cricos_course_code = '0100918';

UPDATE courses SET
    course_description = '<p>The Bachelor of Science is for those excited by discovery and who question the norm. You''ll learn from world-renowned researchers who are addressing the big issues facing our global society, such as the changing environment, future materials and fuels, and biotechnology. You''ll be able to study complementary disciplines or non-science units that feed your curiosity. And you''ll be part of a community that has led many significant initiatives in recent years, including early climate change research, photonics, evolutionary biology and groundbreaking research in earth''s crustal systems.</p> <p>In the Bachelor of Information Technology, you''ll acquire foundational skills in programming, data storage and modelling, networking and cybersecurity. You''ll develop broad and coherent knowledge and skills from an area of information technology - such as software design and construction, applied data modelling and analysis, or security problem detection and mitigation - and learn how to apply that knowledge to solve real-world problems. And you''ll learn how to relate your knowledge and skills in information technology to a broader societal context, and make sound decisions regarding ethical and security concerns.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 46000,
    onshore_tuition_fee = 46000,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-science-and-bachelor-of-information-technology/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '<p>Science underpins every major advancement shaping our world - from tackling climate change and improving health outcomes to developing new technologies and materials. It''s a field driven by curiosity, creativity and evidence, where scientists combine analytical thinking with innovation to uncover insights that transform lives and our planet''s future.</p> <p>The Bachelor of Science will equip you with the expertise to thrive in this ever-evolving field. Co-designed with CSIRO, J&amp;J and ResMed, the degree blends practical, apprenticeship-style learning with industry collaboration, ensuring you develop both technical and transferable skills. You''ll study in world-class facilities - including Australia''s first genome foundry, quantum physics labs, seawater and plant-growth facilities, a nuclear magnetic resonance spectroscopy facility and an 11-hectare fauna park - while gaining the communication and problem-solving abilities to help lead scientific innovation and discovery.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 45600,
    onshore_tuition_fee = 45600,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 75 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> For astronomy and astrophysics, mathematics, statistical data science and applied physics majors: HSC Mathematics Advanced (Band 4), or equivalent. If you haven''t met the required minimum level of achievement (Band 4 or equivalent), you can undertake an alternative introductory unit of study in that area.</p> <p><strong>Recommended Studies:</strong> <p>HSC Mathematics Advanced or equivalent, at least 2 units of science.</p> <p>For astronomy and astrophysics, and applied physics majors: HSC Physics.</p> <p>For mathematics major: HSC Mathematics Extension 1 (Band E2) or HSC Mathematics Extension 2, or equivalent.</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-science/',
    updated_at = NOW()
WHERE cricos_course_code = '001365G';

UPDATE courses SET
    course_description = '<p>Our practice-oriented Bachelor of Security Studies will prepare you to meet the needs of this rapidly changing sector by teaching you about security from a range of perspectives, including risk management, emergency response, national resilience, business continuity planning, law enforcement and the use of military force.</p> <p>The hallmark of Macquarie''s Bachelor of Laws is its recognition of the way legal frameworks underpin such global issues. You''ll be challenged to think critically about the law to seek innovative solutions to legal problems - skills highly valued by employers. With the option to combine your law degree with any other Macquarie bachelor degree, you can open the way to an array of careers in legal practice, private industry, government, education and community services.</p>',
    total_course_duration = 'Full time: 5 years',
    offshore_tuition_fee = 47300,
    onshore_tuition_fee = 47300,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 7</li><li>Minimum 6.5 in reading</li><li>Minimum 6.5 in writing</li><li>Minimum 6.5 in listening</li><li>Minimum 6.5 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-security-studies-and-bachelor-of-laws/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '<p>Security risks are shifting fast, driven by geopolitical tension, technological disruption and threats that move across borders, sectors and systems. From online extremism and cyberattacks to transnational crime and foreign interference, today''s challenges are complex, interconnected and constantly evolving. In this environment, governments, businesses and communities rely on people who can interpret uncertainty, assess risk and make decisions grounded in evidence.</p> <p>Our unique Bachelor of Security Studies will equip you with the skills to navigate this landscape with confidence. As the only degree in New South Wales specialising in security - and the only one in Australia to take a truly multidisciplinary approach spanning counterterrorism, cybersecurity, intelligence, and strategy and defence - it will provide you with capabilities that set you apart. Guided by academics who are active practitioners in policing, defence and national security, you''ll build in-demand skills in risk mitigation, intelligence analysis and strategic planning. And with our location in the Connect Macquarie Park Innovation District, you''ll have opportunities to network with organisations driving advances in security and defence, such as NEXTDC, Raytheon Australia, Meridian IT and Hubify.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 45700,
    onshore_tuition_fee = 45700,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>Academic Requirements</strong></td><td>Selection Rank of 75 (or equivalent)</td></tr><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-security-studies/',
    updated_at = NOW()
WHERE cricos_course_code = '083744F';

UPDATE courses SET
    course_description = '',
    total_course_duration = 'Full time: 5 years',
    offshore_tuition_fee = 46500,
    onshore_tuition_fee = 46500,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 7</li><li>Minimum 6.5 in reading</li><li>Minimum 6.5 in writing</li><li>Minimum 6.5 in listening</li><li>Minimum 6.5 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-social-sciences-and-bachelor-of-laws/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '<p>How can societies and individuals manage change in times of uncertainty? How might we address inequalities; nurture health and wellbeing; and meet the challenges of climate change, rapidly changing workplaces and emerging technologies? What skills are required to thrive in the labour market and find fulfilling work? What kind of evidence, values and decision-making processes are needed to guide our choices towards a fairer, healthier and more secure world for all?</p> <p>The Bachelor of Social Sciences is designed for those who are passionate about seeking meaningful answers to these pressing questions and who wish to create purposeful change in the world. You''ll forge foundational skills in the social sciences via a set of core units, while deepening your knowledge through an interdisciplinary major exploring the social construction of health and wellbeing. In your final year, you''ll collaborate with peers to research, analyse and present solutions to a driving concern pitched by industry partners. With a unique skill set that bridges the arts and sciences, you''ll graduate with the capabilities to manage complex stakeholders, bring diverse technical experts together and progress multifaceted policy debates.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 43700,
    onshore_tuition_fee = 43700,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>Academic Requirements</strong></td><td>Selection Rank of 75 (or equivalent)</td></tr><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-social-sciences/',
    updated_at = NOW()
WHERE cricos_course_code = '115580H';

UPDATE courses SET
    course_description = '<p>The Bachelor of Speech and Hearing Sciences will prepare you for postgraduate study towards a career in a number of professions, including clinical work or research in audiology and speech and language pathology, forensic speech science, the development of associated speech and hearing technologies, or teaching English to speakers of other languages (TESOL).</p> <p>The Bachelor of Psychology will provide you with a scientific understanding of the psychological processes that underlie behaviour. You''ll get exposure to a range of fundamental psychological concepts, as well as to specialised areas such as child psychology, neuropsychology, social and personality psychology, organisational psychology, cognition and perception, and psychopathology. When followed by an honours year, this degree is a pathway to postgraduate study, which will enable you to become a qualified psychologist.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 46900,
    onshore_tuition_fee = 46900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6.5</li><li>Minimum 6 in reading</li><li>Minimum 6 in writing</li><li>Minimum 6 in listening</li><li>Minimum 6 in speaking</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-speech-and-hearing-sciences-and-bachelor-of-psychology/',
    updated_at = NOW()
WHERE cricos_course_code = '098526D';

UPDATE courses SET
    course_description = '<p>Being able to communicate with others is a fundamental human pursuit. Speech, hearing and language professionals have the privilege of bringing that gift to the community - whether that be through helping someone hear for the first time, assisting a stroke patient to speak again or investigating how children acquire language.</p> <p>The Bachelor of Speech and Hearing Sciences - Australia''s only integrated undergraduate speech and hearing sciences degree - will position you to join these professionals in unlocking the power of communication for others. The degree''s unique structure will equip you for a diverse range of postgraduate opportunities, including in speech pathology, audiology, linguistics, TESOL, editing and publishing, and speech and hearing research. And by providing a strong foundation in the science of language - processes, structure and acquisition - it will also open doors to extensive career opportunities immediately after graduation. Think: clinical administration, management or marketing; speech technology; language revitalisation in Indigenous communities; or language support for multicultural communities - to name a few. </p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 49900,
    onshore_tuition_fee = 49900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>Academic Requirements</strong></td><td>Selection Rank of 80 (or equivalent).</td></tr><tr><td><strong>English Proficiency</strong></td><td>IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking).</td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/bachelor-of-speech-and-hearing-sciences/',
    updated_at = NOW()
WHERE cricos_course_code = '099151M';

UPDATE courses SET
    course_description = '<p>The Diploma of Arts Media and Communications introduces you to the fundamental concepts of digital media, media practice and production, and modes of communication, as well as critical thinking.</p> <p>The diploma is equivalent to the first year of an undergraduate degree. If you successfully complete the diploma and meet the entry requirements, you can progress directly into the second year of the following degrees without losing any time, as you''ll receive credit for the units you complete in the diploma: Bachelor of Arts, Bachelor of Media and Communications.</p>',
    total_course_duration = 'Full time: 0.8 years',
    offshore_tuition_fee = 37900,
    onshore_tuition_fee = 37900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 60 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6 (Minimum 5.5 in reading, 5.5 in writing, 5.5 in listening, and 5.5 in speaking.).</p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/diploma-of-arts-media-and-communications/',
    updated_at = NOW()
WHERE cricos_course_code = '099295F';

UPDATE courses SET
    course_description = '<p>The Diploma of Business Analytics introduces you to the fundamental concepts of accounting, business statistics, computer programming, database design and management.</p> <p>The diploma is equivalent to the first year of an undergraduate degree. If you successfully complete the diploma and meet the entry requirements, you can progress directly into the second year of the following degrees without losing any time, as you''ll receive credit for the units you complete in the diploma: Bachelor of Business Analytics, Bachelor of Commerce, Bachelor of Information Technology.</p>',
    total_course_duration = 'Full time: 0.8 years',
    offshore_tuition_fee = 37900,
    onshore_tuition_fee = 37900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 60 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6 (Minimum 5.5 in reading, 5.5 in writing, 5.5 in listening, and 5.5 in speaking.).</p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/diploma-of-business-analytics/',
    updated_at = NOW()
WHERE cricos_course_code = '106809M';

UPDATE courses SET
    course_description = '<p>The Diploma of Business introduces you to the fundamental concepts of entrepreneurship, human resource management, management and marketing.</p> <p>The diploma is equivalent to the first year of an undergraduate degree and is recommended if you''re interested in studying the entrepreneurship, international, management and marketing side of business, rather than the commerce or numeracy side of business. If you successfully complete the diploma and meet the entry requirements, you can progress directly into the second year of the following degrees without losing any time, as you''ll receive credit for the units you complete in the diploma: Bachelor of Business, Bachelor of Commerce.</p>',
    total_course_duration = 'Full time: 0.8 years',
    offshore_tuition_fee = 37900,
    onshore_tuition_fee = 37900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 60 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6 (Minimum 5.5 in reading, 5.5 in writing, 5.5 in listening, and 5.5 in speaking.).</p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/diploma-of-business/',
    updated_at = NOW()
WHERE cricos_course_code = '108687M';

UPDATE courses SET
    course_description = '<p>The Diploma of Commerce introduces you to the fundamental concepts of accounting, business statistics, economics, finance, management and marketing.</p> <p>The diploma is equivalent to the first year of an undergraduate degree. If you successfully complete the diploma and meet the entry requirements, you can progress directly into the second year of the following degrees without losing any time, as you''ll receive credit for the units you complete in the diploma: Bachelor of Actuarial Studies, Bachelor of Applied Finance, Bachelor of Business, Bachelor of Commerce, Bachelor of Economics, Bachelor of Professional Accounting.</p> <p>You may need to undertake a mathematics diagnostic test at the beginning of your diploma. Depending on the outcome, we may recommend that you complete a mathematics module, which may increase the time it takes to complete your diploma.</p>',
    total_course_duration = 'Full time: 0.8 years',
    offshore_tuition_fee = 37900,
    onshore_tuition_fee = 37900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 60 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6 (Minimum 5.5 in reading, 5.5 in writing, 5.5 in listening, and 5.5 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> HSC Mathematics Advanced or HSC Mathematics Standard 2, or equivalent. For progression into Bachelor of Actuarial Studies: HSC Mathematics Advanced (Band 3) or equivalent is required to enrol in the core mathematics unit.</p> <p><strong>Recommended Studies:</strong> <p>For progression to actuarial studies degrees: HSC Mathematics Advanced (Band 4) or HSC Mathematics Extension 1 or 2, or equivalent.</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/diploma-of-commerce/',
    updated_at = NOW()
WHERE cricos_course_code = '099296E';

UPDATE courses SET
    course_description = '<p>The Diploma of Engineering introduces you to the fundamental concepts of civil, electrical and electronic, mechanical and mechatronic engineering, as well as computing, mathematics and physics.</p> <p>The diploma is equivalent to the first year of an undergraduate degree. If you successfully complete the diploma and meet the entry requirements, you can progress directly into the second year of the following degrees without losing any time, as you''ll receive credit for the units you complete in the diploma: Bachelor of Engineering (Honours) with a specialisation in Civil Engineering, Electrical and Electronic Engineering, Mechanical Engineering, Mechatronic Engineering; Bachelor of Science with a specialisation in Astronomy and Astrophysics, Mathematics or Physics.</p>',
    total_course_duration = 'Full time: 0.8 years',
    offshore_tuition_fee = 37900,
    onshore_tuition_fee = 37900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 60 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6 (Minimum 5.5 in reading, 5.5 in writing, 5.5 in listening, and 5.5 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> HSC Mathematics Advanced Band 3 or equivalent</p> <p><strong>Recommended Studies:</strong> <p>HSC Mathematics Advanced (Band 4) or HSC Mathematics Extension 1 or HSC Mathematics Extension 2, HSC Chemistry and HSC Physics, or equivalent.</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/diploma-of-engineering/',
    updated_at = NOW()
WHERE cricos_course_code = '095020K';

UPDATE courses SET
    course_description = '<p>The Diploma of Health Sciences introduces you to the fundamental concepts of health and wellbeing, evidence-based health practice and health systems.</p> <p>The diploma is equivalent to the first year of an undergraduate degree. If you successfully complete the diploma and meet the entry requirements, you can progress directly into the second year of the Bachelor of Health Sciences without losing any time, as you''ll receive credit for the units you complete in the diploma.</p>',
    total_course_duration = 'Full time: 0.8 years',
    offshore_tuition_fee = 37900,
    onshore_tuition_fee = 37900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>Academic Requirements</strong></td><td>Selection Rank of 60 (or equivalent)</td></tr><tr><td><strong>English Proficiency</strong></td><td><ul><li>IELTS overall score of 6</li><li>Minimum 5.5 in reading</li><li>Minimum 5.5 in writing</li><li>Minimum 5.5 in listening</li><li>Minimum 5.5 in speaking</li></ul></td></tr><tr><td><strong>Assumed Knowledge</strong></td><td>None</td></tr><tr><td><strong>Recommended Studies</strong></td><td><ul><li>HSC Health and Movement Science or equivalent</li><li>HSC Health and Movement Science Life Skills or equivalent</li><li>HSC Personal Development, Health and Physical Education or equivalent</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/diploma-of-health-sciences/',
    updated_at = NOW()
WHERE cricos_course_code = '117670A';

UPDATE courses SET
    course_description = '<p>The Diploma of Information Technology introduces you to the fundamental concepts of business systems, computer science, cybersecurity, database design, games design, programming and software engineering.</p> <p>The diploma is equivalent to the first year of an undergraduate degree. If you successfully complete the diploma and meet the entry requirements, you can progress directly into the second year of the following degrees without losing any time, as you''ll receive credit for the units you complete in the diploma: Bachelor of Business Analytics, Bachelor of Cyber Security, Bachelor of Engineering (Honours) with a specialisation in Software Engineering, Bachelor of Information Technology.</p>',
    total_course_duration = 'Full time: 0.8 years',
    offshore_tuition_fee = 37900,
    onshore_tuition_fee = 37900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 60 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6 (Minimum 5.5 in reading, 5.5 in writing, 5.5 in listening, and 5.5 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> For progression into Bachelor of Information Technology there is no assumed knowledge. For progression into Bachelor of Engineering (Honours) in Software Engineering: HSC Mathematics Advanced Band 4 or equivalent is assumed. If you don''t have the assumed knowledge, you are advised to undertake a bridging course in mathematics.</p> <p><strong>Recommended Studies:</strong> <p>For progression into Bachelor of Engineering (Honours) in Software Engineering or Bachelor of Information Technology: HSC Information Processes and Technology and/or HSC Software Design and Development, HSC Mathematics Extension 1 or HSC Mathematics Extension 2, or equivalent.</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/diploma-of-information-technology/',
    updated_at = NOW()
WHERE cricos_course_code = '095021J';

UPDATE courses SET
    course_description = '<p>The Diploma of Marketing and Media introduces you to the fundamental concepts of brand management, digital media production and marketing strategy.</p> <p>The diploma is equivalent to the first year of an undergraduate degree. If you successfully complete the diploma and meet the entry requirements, you can progress directly into the second year of the following degrees without losing any time, as you''ll receive credit for the units you complete in the diploma: Bachelor of Commerce, Bachelor of Marketing and Media, Bachelor of Media and Communications.</p>',
    total_course_duration = 'Full time: 0.8 years',
    offshore_tuition_fee = 37900,
    onshore_tuition_fee = 37900,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>Minimum Academic Requirements:</strong> Selection Rank of 60 (or equivalent).</p> <p><strong>English Language Requirements:</strong> IELTS overall score of 6 (Minimum 5.5 in reading, 5.5 in writing, 5.5 in listening, and 5.5 in speaking.).</p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/diploma-of-marketing-and-media/',
    updated_at = NOW()
WHERE cricos_course_code = '106810G';

UPDATE courses SET
    course_description = '<p>Today''s rapidly evolving and globally focused healthcare landscape requires medical professionals who not only excel in clinical expertise, but who also understand the complexities of healthcare policy, ethical decision-making and the social determinants of health. Doctors who are patient-centred, safety-focused and culturally responsive, and who are equipped to work within digital health systems, are in demand.</p> <p>The four-year graduate-entry Doctor of Medicine will embed you within Macquarie University Health - Australia''s first university-led integrated health centre. Home to the nation''s only not-for-profit hospital on a university campus and 30 specialist clinics, this cutting-edge environment seamlessly integrates learning with patient-centred clinical care, and world-class health and medical research. Structured Australian and international clinical experiences are integral to the degree, giving you unrivalled opportunities to experience diverse health systems, cultures and clinical presentations. You may also apply for our GP Intensive Stream: created to address workforce shortages, it will prepare you to become a specialist GP.</p>',
    total_course_duration = 'Full time: 4 years',
    offshore_tuition_fee = 93200,
    onshore_tuition_fee = 93200,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>English Language Requirements:</strong> IELTS overall score of 7 (Minimum 7 in reading, 7 in writing, 7 in listening, and 7 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> The assumed knowledge on entry to the Doctor of Medicine (Macquarie MD) will be in Human Anatomy and Human Physiology.</p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/doctor-of-medicine/',
    updated_at = NOW()
WHERE cricos_course_code = '095798D';

UPDATE courses SET
    course_description = '<p>Ageing, disease, environmental factors, and occupational and sporting hazards, can all impact our physical function, limiting our ability to participate in life''s activities as we wish. Physiotherapists work with people of all ages to prevent and treat a wide range of health conditions, including musculoskeletal, neurological and cardiorespiratory conditions, in order to maximise quality of life.</p> <p>The Doctor of Physiotherapy -the first three-year master-level professional-entry physiotherapy degree in New South Wales - will develop your skills so that when you graduate you''re able to work with individuals across the lifespan to optimise their physical function. You''ll learn to effectively assess, diagnose and treat individuals with a range of health conditions. You''ll also learn how to encourage people to change their behaviour and self-manage their conditions to maximise their physical health.</p>',
    total_course_duration = 'Full time: 3 years',
    offshore_tuition_fee = 63100,
    onshore_tuition_fee = 63100,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>English Language Requirements:</strong> IELTS overall score of 7 (Minimum 7 in reading, 6.5 in writing, 7 in listening, and 7 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> The assumed knowledge on entry to the Doctor of Physiotherapy will be Human Anatomy (System and Musculoskeletal), Human Physiology (Cell and System), Psychology and Research Methods.</p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/doctor-of-physiotherapy/',
    updated_at = NOW()
WHERE cricos_course_code = '075265K';

UPDATE courses SET
    course_description = '<p>Accountants and those with a strong understanding of accounting principles play a critical role in all businesses and organisations. Because they''re responsible for budgeting, planning and evaluating performance, it''s virtually impossible to make strategic business decisions without them.</p> <p>The Graduate Certificate of Accounting Practice is ideal for those wishing to transition to a role in accounting or those seeking to understand the principles of accounting practice to progress in their existing field. You''ll study four key contemporary accounting units via structured learning activities facilitated by teachers with extensive industry experience. This course is a pathway to the Graduate Diploma of Accounting Practice, the Master of Accounting and the Master of Professional Accounting.</p>',
    total_course_duration = 'Full time: 0.5 years',
    offshore_tuition_fee = 23100,
    onshore_tuition_fee = 23100,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><table><tbody><tr><td><strong>English Proficiency</strong></td><td>IELTS overall score of 6.5 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</td></tr><tr><td><strong>Academic Requirements</strong></td><td><ul><li>Assumed Knowledge: None</li><li>Recommended Studies: None</li></ul></td></tr></tbody></table>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/graduate-certificate-of-accounting-practice/',
    updated_at = NOW()
WHERE cricos_course_code = '111135F';

UPDATE courses SET
    course_description = '<p>The best administrators are equally talented at managing tasks as they are at managing people - they''re leaders, innovators, clear communicators, strategic thinkers, planners, decision makers and creative problem-solvers.</p> <p>The Graduate Certificate of Business Administration is designed for those wishing to learn or update their knowledge of key elements of business management. It will develop your understanding of key business practices related to people, finance, marketing and strategy.</p> <p>The Graduate Certificate of Business Administration is primarily delivered at our City Campus. However, some units are delivered at our Wallumattagal Campus in Macquarie Park or online. To successfully complete the course, you may need to attend classes at both campuses and/or online.</p>',
    total_course_duration = 'Full time: 0.5 years',
    offshore_tuition_fee = 23250,
    onshore_tuition_fee = 23250,
    enrolment_fee = NULL,
    materials_fee = NULL,
    entry_requirements = '<p><strong>English Language Requirements:</strong> IELTS overall score of 7 (Minimum 6 in reading, 6 in writing, 6 in listening, and 6 in speaking.).</p> <p><strong>Assumed Knowledge:</strong> None</p> <p><strong>Recommended Studies:</strong> <p>None</p></p>',
    apply_form = 'https://www.mq.edu.au/study/find-a-course/courses/graduate-certificate-of-business-administration/',
    updated_at = NOW()
WHERE cricos_course_code = '111137D';

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Certificate of Clinical Trial Operations | https://www.mq.edu.au/study/find-a-course/courses/graduate-certificate-of-clinical-trial-operations/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Certificate of Conservation Biology | https://www.mq.edu.au/study/find-a-course/courses/graduate-certificate-of-conservation-biology/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Certificate of Editing and Electronic Publishing | https://www.mq.edu.au/study/find-a-course/courses/graduate-certificate-of-editing-and-electronic-publishing/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Certificate of Environment | https://www.mq.edu.au/study/find-a-course/courses/graduate-certificate-of-environment/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Certificate of Finance | https://www.mq.edu.au/study/find-a-course/courses/graduate-certificate-of-finance/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Certificate of Financial Integrity Law | https://www.mq.edu.au/study/find-a-course/courses/graduate-certificate-of-financial-integrity-law/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Certificate of Information Technology | https://www.mq.edu.au/study/find-a-course/courses/graduate-certificate-of-information-technology/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Certificate of Laws | https://www.mq.edu.au/study/find-a-course/courses/graduate-certificate-of-laws/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Certificate of Research in Arts | https://www.mq.edu.au/study/find-a-course/courses/graduate-certificate-of-research-in-arts/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Certificate of Research in Business | https://www.mq.edu.au/study/find-a-course/courses/graduate-certificate-of-research-in-business/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Certificate of Research in Medicine, Health and Human Sciences | https://www.mq.edu.au/study/find-a-course/courses/graduate-certificate-of-research-in-medicine-health-and-human-sciences/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Certificate of Research in Science and Engineering | https://www.mq.edu.au/study/find-a-course/courses/graduate-certificate-of-research-in-science-and-engineering/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Certificate of Strategic Policy | https://www.mq.edu.au/study/find-a-course/courses/graduate-certificate-of-strategic-policy/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Certificate of TESOL | https://www.mq.edu.au/study/find-a-course/courses/graduate-certificate-of-tesol/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Diploma of Accounting Practice | https://www.mq.edu.au/study/find-a-course/courses/graduate-diploma-of-accounting-practice/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Diploma of Applied Finance | https://www.mq.edu.au/study/find-a-course/courses/graduate-diploma-of-applied-finance/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Diploma of Auslan-English Interpreting | https://www.mq.edu.au/study/find-a-course/courses/graduate-diploma-of-auslan-english-interpreting/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Diploma of Biotechnology | https://www.mq.edu.au/study/find-a-course/courses/graduate-diploma-of-biotechnology/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Diploma of Business Administration | https://www.mq.edu.au/study/find-a-course/courses/graduate-diploma-of-business-administration/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Diploma of Conservation Biology | https://www.mq.edu.au/study/find-a-course/courses/graduate-diploma-of-conservation-biology/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Diploma of Environment | https://www.mq.edu.au/study/find-a-course/courses/graduate-diploma-of-environment/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Diploma of Research in Arts | https://www.mq.edu.au/study/find-a-course/courses/graduate-diploma-of-research-in-arts/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Diploma of Research in Business | https://www.mq.edu.au/study/find-a-course/courses/graduate-diploma-of-research-in-business/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Diploma of Research in Medicine, Health and Human Sciences | https://www.mq.edu.au/study/find-a-course/courses/graduate-diploma-of-research-in-medicine-health-and-human-sciences/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Graduate Diploma of Research in Science and Engineering | https://www.mq.edu.au/study/find-a-course/courses/graduate-diploma-of-research-in-science-and-engineering/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Intensive Program | https://www.mq.edu.au/study/find-a-course/courses/intensive-program/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Juris Doctor | https://www.mq.edu.au/study/find-a-course/courses/juris-doctor/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Listing | https://www.mq.edu.au/study/find-a-course/courses/listing/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Marketo | https://www.mq.edu.au/study/find-a-course/courses/marketo/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Accounting | https://www.mq.edu.au/study/find-a-course/courses/master-of-accounting/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Actuarial Practice | https://www.mq.edu.au/study/find-a-course/courses/master-of-actuarial-practice/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Applied Economics and Master of Banking and Finance | https://www.mq.edu.au/study/find-a-course/courses/master-of-applied-economics-and-master-of-banking-and-finance/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Applied Economics and Master of Management | https://www.mq.edu.au/study/find-a-course/courses/master-of-applied-economics-and-master-of-management/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Applied Economics | https://www.mq.edu.au/study/find-a-course/courses/master-of-applied-economics/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Applied Finance | https://www.mq.edu.au/study/find-a-course/courses/master-of-applied-finance/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Applied Linguistics and TESOL | https://www.mq.edu.au/study/find-a-course/courses/master-of-applied-linguistics-and-tesol/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Banking and Finance and Master of Commerce | https://www.mq.edu.au/study/find-a-course/courses/master-of-banking-and-finance-and-master-of-commerce/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Banking and Finance and Master of International Business | https://www.mq.edu.au/study/find-a-course/courses/master-of-banking-and-finance-and-master-of-international-business/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Banking and Finance and Master of Management | https://www.mq.edu.au/study/find-a-course/courses/master-of-banking-and-finance-and-master-of-management/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Banking and Finance and Master of Marketing | https://www.mq.edu.au/study/find-a-course/courses/master-of-banking-and-finance-and-master-of-marketing/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Banking and Finance | https://www.mq.edu.au/study/find-a-course/courses/master-of-banking-and-finance/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Biotechnology | https://www.mq.edu.au/study/find-a-course/courses/master-of-biotechnology/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Business Administration | https://www.mq.edu.au/study/find-a-course/courses/master-of-business-administration/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Business Analytics | https://www.mq.edu.au/study/find-a-course/courses/master-of-business-analytics/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Chiropractic | https://www.mq.edu.au/study/find-a-course/courses/master-of-chiropractic/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Clinical Audiology | https://www.mq.edu.au/study/find-a-course/courses/master-of-clinical-audiology/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Clinical Neuropsychology | https://www.mq.edu.au/study/find-a-course/courses/master-of-clinical-neuropsychology/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Clinical Psychology | https://www.mq.edu.au/study/find-a-course/courses/master-of-clinical-psychology/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Commerce and Master of International Business | https://www.mq.edu.au/study/find-a-course/courses/master-of-commerce-and-master-of-international-business/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Commerce and Master of Management | https://www.mq.edu.au/study/find-a-course/courses/master-of-commerce-and-master-of-management/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Commerce and Master of Marketing | https://www.mq.edu.au/study/find-a-course/courses/master-of-commerce-and-master-of-marketing/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Commerce and Master of Media and Communications | https://www.mq.edu.au/study/find-a-course/courses/master-of-commerce-and-master-of-media-and-communications/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Commerce | https://www.mq.edu.au/study/find-a-course/courses/master-of-commerce/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Conference Interpreting | https://www.mq.edu.au/study/find-a-course/courses/master-of-conference-interpreting/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Conservation Biology | https://www.mq.edu.au/study/find-a-course/courses/master-of-conservation-biology/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Creative Industries and Master of Management | https://www.mq.edu.au/study/find-a-course/courses/master-of-creative-industries-and-master-of-management/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Creative Industries and Master of Marketing | https://www.mq.edu.au/study/find-a-course/courses/master-of-creative-industries-and-master-of-marketing/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Creative Industries and Master of Media and Communications | https://www.mq.edu.au/study/find-a-course/courses/master-of-creative-industries-and-master-of-media-and-communications/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Creative Industries | https://www.mq.edu.au/study/find-a-course/courses/master-of-creative-industries/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Creative Writing | https://www.mq.edu.au/study/find-a-course/courses/master-of-creative-writing/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Criminology and Master of Intelligence | https://www.mq.edu.au/study/find-a-course/courses/master-of-criminology-and-master-of-intelligence/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Criminology and Master of International Relations | https://www.mq.edu.au/study/find-a-course/courses/master-of-criminology-and-master-of-international-relations/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Criminology and Master of Laws | https://www.mq.edu.au/study/find-a-course/courses/master-of-criminology-and-master-of-laws/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Criminology and Master of Strategy and Security | https://www.mq.edu.au/study/find-a-course/courses/master-of-criminology-and-master-of-strategy-and-security/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Criminology | https://www.mq.edu.au/study/find-a-course/courses/master-of-criminology/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Data Science | https://www.mq.edu.au/study/find-a-course/courses/master-of-data-science/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Disability Studies | https://www.mq.edu.au/study/find-a-course/courses/master-of-disability-studies/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Education | https://www.mq.edu.au/study/find-a-course/courses/master-of-education/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Engineering Management | https://www.mq.edu.au/study/find-a-course/courses/master-of-engineering-management/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Engineering (Professional) in Civil and Construction Engineering | https://www.mq.edu.au/study/find-a-course/courses/master-of-engineering-professional-in-civil-and-construction-engineering/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Engineering (Professional) in Environmental Engineering | https://www.mq.edu.au/study/find-a-course/courses/master-of-engineering-professional-in-environmental-engineering/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Engineering (Professional) in Mechanical Engineering | https://www.mq.edu.au/study/find-a-course/courses/master-of-engineering-professional-in-mechanical-engineering/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Engineering (Professional) in Mechatronics and Automation Engineering | https://www.mq.edu.au/study/find-a-course/courses/master-of-engineering-professional-in-mechatronics-and-automation-engineering/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Engineering (Professional) in Renewable Energy and Electrical Engineering | https://www.mq.edu.au/study/find-a-course/courses/master-of-engineering-professional-in-renewable-energy-and-electrical-engineering/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Engineering (Professional) | https://www.mq.edu.au/study/find-a-course/courses/master-of-engineering-professional/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Environment and Master of Sustainable Development | https://www.mq.edu.au/study/find-a-course/courses/master-of-environment-and-master-of-sustainable-development/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Environment | https://www.mq.edu.au/study/find-a-course/courses/master-of-environment/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Information Systems Management | https://www.mq.edu.au/study/find-a-course/courses/master-of-information-systems-management/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Information Technology in Artificial Intelligence | https://www.mq.edu.au/study/find-a-course/courses/master-of-information-technology-in-artificial-intelligence/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Information Technology in Cyber Security | https://www.mq.edu.au/study/find-a-course/courses/master-of-information-technology-in-cyber-security/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Information Technology | https://www.mq.edu.au/study/find-a-course/courses/master-of-information-technology/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Intelligence and Master of International Relations | https://www.mq.edu.au/study/find-a-course/courses/master-of-intelligence-and-master-of-international-relations/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Intelligence and Master of Laws | https://www.mq.edu.au/study/find-a-course/courses/master-of-intelligence-and-master-of-laws/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Intelligence and Master of Strategy and Security | https://www.mq.edu.au/study/find-a-course/courses/master-of-intelligence-and-master-of-strategy-and-security/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Intelligence | https://www.mq.edu.au/study/find-a-course/courses/master-of-intelligence/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of International Business and Master of International Relations | https://www.mq.edu.au/study/find-a-course/courses/master-of-international-business-and-master-of-international-relations/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of International Business and Master of Laws | https://www.mq.edu.au/study/find-a-course/courses/master-of-international-business-and-master-of-laws/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of International Business and Master of Management | https://www.mq.edu.au/study/find-a-course/courses/master-of-international-business-and-master-of-management/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of International Business and Master of Marketing | https://www.mq.edu.au/study/find-a-course/courses/master-of-international-business-and-master-of-marketing/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of International Business and Master of Media and Communications | https://www.mq.edu.au/study/find-a-course/courses/master-of-international-business-and-master-of-media-and-communications/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of International Business | https://www.mq.edu.au/study/find-a-course/courses/master-of-international-business/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of International Relations and Master of Strategy and Security | https://www.mq.edu.au/study/find-a-course/courses/master-of-international-relations-and-master-of-strategy-and-security/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of International Relations | https://www.mq.edu.au/study/find-a-course/courses/master-of-international-relations/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Laws | https://www.mq.edu.au/study/find-a-course/courses/master-of-laws/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Management and Master of Marketing | https://www.mq.edu.au/study/find-a-course/courses/master-of-management-and-master-of-marketing/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Management and Master of Media and Communications | https://www.mq.edu.au/study/find-a-course/courses/master-of-management-and-master-of-media-and-communications/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Management | https://www.mq.edu.au/study/find-a-course/courses/master-of-management/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Marketing and Master of Media and Communications | https://www.mq.edu.au/study/find-a-course/courses/master-of-marketing-and-master-of-media-and-communications/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Marketing | https://www.mq.edu.au/study/find-a-course/courses/master-of-marketing/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Media and Communications | https://www.mq.edu.au/study/find-a-course/courses/master-of-media-and-communications/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Organisational Psychology | https://www.mq.edu.au/study/find-a-course/courses/master-of-organisational-psychology/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Professional Accounting | https://www.mq.edu.au/study/find-a-course/courses/master-of-professional-accounting/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Professional Practice | https://www.mq.edu.au/study/find-a-course/courses/master-of-professional-practice/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Professional Psychology | https://www.mq.edu.au/study/find-a-course/courses/master-of-professional-psychology/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Public Health | https://www.mq.edu.au/study/find-a-course/courses/master-of-public-health/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Research in Arts | https://www.mq.edu.au/study/find-a-course/courses/master-of-research-in-arts/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Research in Business | https://www.mq.edu.au/study/find-a-course/courses/master-of-research-in-business/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Research in Medicine, Health and Human Sciences | https://www.mq.edu.au/study/find-a-course/courses/master-of-research-in-medicine-health-and-human-sciences/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Research in Science and Engineering | https://www.mq.edu.au/study/find-a-course/courses/master-of-research-in-science-and-engineering/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Speech and Language Pathology | https://www.mq.edu.au/study/find-a-course/courses/master-of-speech-and-language-pathology/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Strategy and Security | https://www.mq.edu.au/study/find-a-course/courses/master-of-strategy-and-security/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Sustainable Development | https://www.mq.edu.au/study/find-a-course/courses/master-of-sustainable-development/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Teaching (Birth to Five Years) | https://www.mq.edu.au/study/find-a-course/courses/master-of-teaching-birth-to-five-years/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Teaching (Primary) | https://www.mq.edu.au/study/find-a-course/courses/master-of-teaching-primary/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Teaching (Secondary) | https://www.mq.edu.au/study/find-a-course/courses/master-of-teaching-secondary/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Master of Translation and Interpreting Studies (Advanced) | https://www.mq.edu.au/study/find-a-course/courses/master-of-translation-and-interpreting-studies-advanced/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Masters Qualifying Program (Accelerated) | https://www.mq.edu.au/study/find-a-course/courses/masters-qualifying-program-accelerated/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Masters Qualifying Program (Standard) | https://www.mq.edu.au/study/find-a-course/courses/masters-qualifying-program-standard/

-- ⚠️ Skipped (no CRICOS code found or domestic-only): Standard Foundation Program | https://www.mq.edu.au/study/find-a-course/courses/standard-foundation-program/

