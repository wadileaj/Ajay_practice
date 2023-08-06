import pandas as pd
import requests
def get_movie_data(i):
    response=requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=6ba4639bed0e5d6c8a3c76166c862609&&language=en-US&page={}'.format(i))
    Jsondata=response.json()['results']
    return Jsondata

def concat_dataframe():
    initial_df=pd.DataFrame()
    for i in range(1,5):
        Jsondata=get_movie_data(i)
        df=pd.DataFrame(Jsondata)
        temp_df=df[['id','title','overview','release_date','popularity','vote_average','vote_count']]
        final_df=initial_df.append(temp_df,ignore_index=True)
    print(final_df)
def lambda_handler(event,context):
    concat_dataframe()

