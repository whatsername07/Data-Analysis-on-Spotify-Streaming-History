import pandas as pd

def historySplit(df, year):
    return df[df['ts'].dt.year == year]

def topArtists(df):
    allArtists = df['master_metadata_album_artist_name'].unique()
    topArtists = pd.DataFrame({'Artists': allArtists})
    topArtists['time_played'] = topArtists['Artists'].apply(lambda x: df[df['master_metadata_album_artist_name'] == x]['ms_played'].sum())
    topArtists.sort_values(by='time_played', ascending=False, inplace=True)
    topArtists.reset_index(drop=True, inplace=True)
    topArtists['time_played'] = topArtists['time_played'].apply(lambda x: x / 60000)
    topArtists['time_played'] = topArtists['time_played'].apply(lambda x: round(x, 2))
    return topArtists

def topTracks(df):
    artists_tracks = df[['master_metadata_album_artist_name', 'master_metadata_track_name']].drop_duplicates()
    artists_tracks['time_played'] = artists_tracks.apply(lambda row: df[(df['master_metadata_album_artist_name'] == row['master_metadata_album_artist_name']) & (df['master_metadata_track_name'] == row['master_metadata_track_name'])]['ms_played'].sum(), axis=1)
    artists_tracks.sort_values(by='time_played', ascending=False, inplace=True)
    artists_tracks.reset_index(drop=True, inplace=True)
    artists_tracks['time_played'] = artists_tracks['time_played'].apply(lambda x: x / 60000)  # convert ms to minutes
    artists_tracks['time_played'] = artists_tracks['time_played'].apply(lambda x: round(x, 2))  # round to 2 decimal places
    return artists_tracks

def filter_by_hour(df, hour):
    return df[df['ts'].dt.hour == hour]