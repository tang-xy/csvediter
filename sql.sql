SELECT *
FROM �����ɾ�ҵ,�ֽ�������ɾ�ҵ,�ʲ���ծ��ɾ�ҵ
WHERE (�����ɾ�ҵ.Stkcd = �ֽ�������ɾ�ҵ.Stkcd
AND �����ɾ�ҵ.Stkcd = �ʲ���ծ��ɾ�ҵ.Stkcd
AND �����ɾ�ҵ.Accper = �ֽ�������ɾ�ҵ.Accper
AND �����ɾ�ҵ.Accper = �ʲ���ծ��ɾ�ҵ.Accper)
AND �����ɾ�ҵ.Typrep = 'A' 
AND �ֽ�������ɾ�ҵ.Typrep = 'A'
AND �ʲ���ծ��ɾ�ҵ.Typrep = 'A'
AND (�����ɾ�ҵ.Accper = '2013-01-01' OR �����ɾ�ҵ.Accper = '2014-01-01' OR �����ɾ�ҵ.Accper = '2015-01-01' OR �����ɾ�ҵ.Accper = '2016-01-01' OR �����ɾ�ҵ.Accper = '2017-01-01')