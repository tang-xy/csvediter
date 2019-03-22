SELECT *
FROM 利润表采掘业,现金流量表采掘业,资产负债表采掘业
WHERE (利润表采掘业.Stkcd = 现金流量表采掘业.Stkcd
AND 利润表采掘业.Stkcd = 资产负债表采掘业.Stkcd
AND 利润表采掘业.Accper = 现金流量表采掘业.Accper
AND 利润表采掘业.Accper = 资产负债表采掘业.Accper)
AND 利润表采掘业.Typrep = 'A' 
AND 现金流量表采掘业.Typrep = 'A'
AND 资产负债表采掘业.Typrep = 'A'
AND (利润表采掘业.Accper = '2013-01-01' OR 利润表采掘业.Accper = '2014-01-01' OR 利润表采掘业.Accper = '2015-01-01' OR 利润表采掘业.Accper = '2016-01-01' OR 利润表采掘业.Accper = '2017-01-01')