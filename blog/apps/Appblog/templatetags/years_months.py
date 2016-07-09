from django import template
from ..models import Entrada

register = template.Library()

@register.assignment_tag

def get_year_list():
	year = Entrada.objects.raw("select strftime('%Y',fecha) as year,id from appblog_entrada group by strftime('%Y',fecha)")
	return year
@register.assignment_tag
def get_year_month_list():
	year = Entrada.objects.raw('''
			SELECT 
				strftime('%Y',fecha) as year, 
				case strftime('%m', fecha) 
						when '01' then 'January' 
						when '02' then 'Febuary' 
						when '03' then 'March' 
						when '04' then 'April' 
						when '05' then 'May' 
						when '06' then 'June' 
						when '07' then 'July' 
						when '08' then 'August' 
						when '09' then 'September' 
						when '10' then 'October' 
						when '11' then 'November' 
						when '12' then 'December' 
						else '' 
				end as month, 
			strftime('%m',fecha) as idmonth,
			id
			FROM Appblog_entrada 
			GROUP BY 
				case strftime('%m', fecha) 
						when '01' then 'January' 
						when '02' then 'Febuary' 
						when '03' then 'March' 
						when '04' then 'April' 
						when '05' then 'May' 
						when '06' then 'June' 
						when '07' then 'July' 
						when '08' then 'August' 
						when '09' then 'September' 
						when '10' then 'October' 
						when '11' then 'November' 
						when '12' then 'December' 
						else '' 
				end,
				strftime('%Y',fecha)
			ORDER BY
				strftime('%Y',fecha) desc,
				strftime('%m',fecha)

		''')
	return year