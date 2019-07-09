import pandas as pd


def main():
    data_file = "rpi_data_long.csv"

    column_names = ['Type A', 'Measure A', 'Units A',
                    'Type B', 'Measure B', 'Units B',
                    'Type C', 'Measure C', 'Units C',
                    'Datetime']

    with open(data_file, 'r') as file:
        df_redundant = pd.read_csv(file, names=column_names)

        df_compact = df_redundant.copy()
        df_compact.rename(columns={'Measure A': 'Ping (ms)',
                                   'Measure B': 'Download (Mbit/s)',
                                   'Measure C': 'Upload (Mbit/s)'}, inplace=True)
        print("Dataframe with renamed columns: ")
        print(df_compact.head(3))

        df_compact.drop(['Type A', 'Type B', 'Type C',
                         'Units A', 'Units B', 'Units C'], axis=1, inplace=True)

        df_compact['Datetime'] = pd.to_datetime(df_compact['Datetime'])
        df_compact['Date'] = df_compact['Datetime'].dt.date
        df_compact['Time'] = df_compact['Datetime'].dt.time

        df_compact.drop('Datetime', axis=1, inplace=True)

        print('Changed data: ')
        print(df_compact.head(3))

        print(df_compact['Date'][0], type(df_compact['Date'][0]))
        print(df_compact['Time'][0], type(df_compact['Time'][0]))

        df_compact.to_csv('rpi_data_compact.csv')


if __name__ == '__main__':
    main()
