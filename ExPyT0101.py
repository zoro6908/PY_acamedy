# import matplotlib as mat

# 기본 파일 경로 찾기
# print(mat.matplotlib_fname())

# 폰트 이름, 경로 찾기
import matplotlib.font_manager as fm

for f in fm.fontManager.ttflist:
    if f.name == 'NanumGothic':
        print(f'Font : {f.name}, Path : {f.fname}', {f.style}, {f.variant}, {f.weight}, {f.stretch}, {f.size})
        print(f)
# ttflist 구조 : class matplotlib.font_manager.FontEntry
# name='', fname='', style='normal', variant='normal', weight='normal', stretch='normal', size='medium'

# import matplotlib.font_manager as fm
# ll = [map(lambda x: True if x == 'NanumGothic', fm.fontManager.ttflist)]
# print(ll)

# print(type(fm.fontManager.ttflist))

# print((fm.fontManager.ttflist))

# for f in fm.fontManager.ttflist:
#     if 'Nanum' in f.name:
#         print(f.name)

# ## 폰트 이름
# title_font_name = 'NanumGothic'
# tick_label_font_name = 'Nanum Pen Script'
#
# ## 폰트 경로
# title_font_path = [f.fname for f in fm.fontManager.ttflist if title_font_name in f.name][0]
# tick_label_font_path = [f.fname for f in fm.fontManager.ttflist if tick_label_font_name in f.name][0]
#
# ## 폰트 사이즈
# title_font_size = 30
# tick_label_font_size = 25
#
# ## FontProperties 인스턴스 생성
# title_font_prop = fm.FontProperties(fname=title_font_path, size=title_font_size)
# tick_label_font_prop = fm.FontProperties(fname=tick_label_font_path, size=tick_

