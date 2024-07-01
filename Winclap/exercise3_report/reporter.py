import duckdb
import pathlib
import os



def reportByCampaign(dataset_file):

    str_query=f"SELECT \
                    campaign_id, \
                    campaign_name, \
                    #?#, \
                    sum(coalesce(impressions,0)) as number_of_impressions, \
                    sum(coalesce(clicks,0)) as number_of_clicks, \
                    sum(coalesce(installs,0)) as number_of_installs, \
                    sum(coalesce(spend,0)) as amount_of_spend, \
                    number_of_clicks/number_of_impressions as CTR, \
                    amount_of_spend/number_of_installs as CTI, \
                    FROM read_csv('{pathlib.Path(__file__).parent.resolve().joinpath(dataset_file)}') \
                group by 1, \
                        2, \
                        3, \
                order by 1, \
                        2, \
                        3"
    try:
        #duckdb formatted according to the ISO 8601 format ( YYYY-MM-DD ).
        #if number_of_impressions is 0 then CTR will by null
        result_data_frame=duckdb.sql(str_query.replace('#?#', 'summary_date'))

        result_data_frame_annual=duckdb.sql(str_query.replace('#?#', 'year(summary_date) as year'))
        result_data_frame_quarter=duckdb.sql(str_query.replace('#?#', '(year(summary_date)||quarter(summary_date)) as year_quarter'))
        result_data_frame_monthly=duckdb.sql(str_query.replace('#?#', '(year(summary_date)||month(summary_date)) as year_month'))
        result_data_frame_weekly=duckdb.sql(str_query.replace('#?#', 'yearweek(summary_date) as year_week'))

        

    except(duckdb.duckdb.IOException):
        raise Exception(f'The "{dataset_file}" file must exist in the directory: {pathlib.Path(__file__).parent.resolve()}')
    
    result_data_frame.write_csv('result_data_set.csv')
    result_data_frame_annual.write_csv(os.path.join('plus','result_data_set_annual.csv'))
    result_data_frame_quarter.write_csv(os.path.join('plus','result_data_set_quarter.csv'))
    result_data_frame_monthly.write_csv(os.path.join('plus','result_data_set_monthly.csv'))
    result_data_frame_weekly.write_csv(os.path.join('plus','result_data_set_weekly.csv'))

    #Print some rows    
    print(result_data_frame)


def plusReportByCampaign(dataset_file):
    try:
        #duckdb formatted according to the ISO 8601 format ( YYYY-MM-DD ).
        #if number_of_impressions is 0 then CTR will by null
        result_data_frame=duckdb.sql(f"SELECT \
                                        campaign_id, \
                                        campaign_name, \
                                        summary_date, \
                                        sum(coalesce(impressions,0)) as number_of_impressions, \
                                        sum(coalesce(clicks,0)) as number_of_clicks, \
                                        sum(coalesce(installs,0)) as number_of_installs, \
                                        sum(coalesce(spend,0)) as amount_of_spend, \
                                        number_of_clicks/number_of_impressions as CTR, \
                                        amount_of_spend/number_of_installs as CTI, \
                                FROM read_csv('{pathlib.Path(__file__).parent.resolve().joinpath(dataset_file)}') \
                                group by campaign_id, \
                                            campaign_name, \
                                            summary_date, \
                                order by campaign_id, \
                                        campaign_name, \
                                        summary_date")
    except(duckdb.duckdb.IOException):
        raise Exception(f'The "{dataset_file}" file must exist in the directory: {pathlib.Path(__file__).parent.resolve()}')
    
    result_data_frame.write_csv('result_data_set_.csv')

if __name__ == "__main__":
    reportByCampaign('dataset.csv')
