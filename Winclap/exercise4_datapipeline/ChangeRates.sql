SELECT 
	week_start_date,
	sessions,
	page_views,
	users,
	bounce_rate,
	conversion_rate,
	sessions/LAG(sessions,1, NULL) OVER( ORDER BY  week_start_date) change_rate_sessions,
	page_views/LAG(page_views,1, NULL) OVER( ORDER BY  week_start_date) change_rate_views,
	users/LAG(users,1, NULL) OVER( ORDER BY  week_start_date) change_rate_users,
	bounce_rate/LAG(bounce_rate,1, NULL) OVER( ORDER BY  week_start_date) change_rate_bounce_rate,
	conversion_rate/LAG(conversion_rate,1, NULL) OVER( ORDER BY  week_start_date) change_rate_conversion_rate
FROM  production.My_Web_Events
