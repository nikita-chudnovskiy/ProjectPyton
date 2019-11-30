# N школьников делят K яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику?
skolniki =int(input())
yabloki = int(input())
kolKagdomu = yabloki//skolniki
kolVkorzine= yabloki%skolniki
print('Яблок каждому',kolKagdomu,'яблок в корзине',kolVkorzine)