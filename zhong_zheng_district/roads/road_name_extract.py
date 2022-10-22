import pandas as pd
road_guiyang = '貴陽街1段'
road_zhonghua = '中華路1段'
road_bo_ai = '博愛路'
road_yanping_south = '延平南路'
road_aiguo_west = '愛國西路'
road_taoyuan = '桃源街'
road_baoqing = '寶慶路'
road_hengyang = '衡陽路'
road_chongqing_south = '重慶南路1段'

df = pd.read_csv('zhong_zheng_district/zz_106_to_110.csv')


# df_guiyang = df[df['肇事地點'].str.contains(road_guiyang) & ~df['肇事地點'].str.contains('口')]
# df_zhonghua = df[df['肇事地點'].str.contains(road_zhonghua) & ~df['肇事地點'].str.contains('口')]
# df_bo_ai = df[df['肇事地點'].str.contains(road_bo_ai) & ~df['肇事地點'].str.contains('口')]
# df_yanping_south = df[df['肇事地點'].str.contains(road_yanping_south) & ~df['肇事地點'].str.contains('口')]
# df_aiguo_west = df[df['肇事地點'].str.contains(road_aiguo_west) & ~df['肇事地點'].str.contains('口')]

df_chongqing_south = df[df['肇事地點'].str.contains(
    road_chongqing_south) & ~df['肇事地點'].str.contains('口')]
df_taoyuan = df[df['肇事地點'].str.contains(
    road_taoyuan) & ~df['肇事地點'].str.contains('口')]
df_baoqing = df[df['肇事地點'].str.contains(
    road_baoqing) & ~df['肇事地點'].str.contains('口')]
df_hengyang = df[df['肇事地點'].str.contains(
    road_hengyang) & ~df['肇事地點'].str.contains('口')]


# df_guiyang.to_csv('zhong_zheng_district/roads/guiyang_road_accidents.csv', index_label = False, index=False)
# df_zhonghua.to_csv('zhong_zheng_district/roads/zhonghua_road_accidents.csv', index_label = False, index=False)
# df_bo_ai.to_csv('zhong_zheng_district/roads/bo_ai_road_accidents.csv', index_label = False, index=False)
# df_yanping_south.to_csv('zhong_zheng_district/roads/yanping_south_road_accidents.csv', index_label = False, index=False)
# df_aiguo_west.to_csv('zhong_zheng_district/roads/aiguo_west_road_accidents.csv', index_label = False, index=False)
df_chongqing_south.to_csv(
    'zhong_zheng_district/roads/chongqing_south_accidents.csv', index_label=False, index=False)
df_taoyuan.to_csv('zhong_zheng_district/roads/taoyuan_accidents.csv',
                  index_label=False, index=False)
df_baoqing.to_csv('zhong_zheng_district/roads/baoqing_accidents.csv',
                  index_label=False, index=False)
df_hengyang.to_csv('zhong_zheng_district/roads/hengyang_accidents.csv',
                   index_label=False, index=False)
