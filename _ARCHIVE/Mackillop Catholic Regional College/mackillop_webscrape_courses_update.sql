-- Update provider institution details
UPDATE provider_institution SET
    intake_date = 'term_string}"},"query-input":{"@type":"PropertyValueSpecification","valueRequired":true,"valueName":"search_term_string"}}],"inLanguage":"en-AU"}]}</script>
	<!-- / Yoast SEO plugin.',
    updated_at = NOW()
WHERE cricos_provider_code = '01220B';

-- Secondary Years 9 - 12 VCE
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Secondary Years 9 - 12 VCE</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 114000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English"
			class="glink nturl selected"><img data-gt-lazy-src="/wp-content/plugins/gtranslate/flags/24/en.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '015964B';

-- Secondary Years 9 - 12 VCAL
UPDATE courses SET
    course_description = '<h4>Course overview</h4><p>Secondary Years 9 - 12 VCAL</p>',
    course_duration_per_week = 208,
    offshore_tuition_fee = 114000,
    onshore_tuition_fee = NULL,
    enrolment_fee = 0,
    materials_fee = NULL,
    entry_requirements = '<h4>Entry Requirements</h4><p>English"
			class="glink nturl selected"><img data-gt-lazy-src="/wp-content/plugins/gtranslate/flags/24/en.</p>',
    updated_at = NOW()
WHERE cricos_course_code = '067261C';