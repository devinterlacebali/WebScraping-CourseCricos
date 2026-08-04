-- Update provider institution details
UPDATE provider_institution SET
    intake_date = '',
    updated_at = NOW()
WHERE cricos_provider_code = '03560K';