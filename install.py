import os
print('       ******  SkyDrive  ******     ')
print('                     ——open source')
print()
print('>>正在安装SkyDrive的依赖库，请稍后......')
print()
file = open('requirements.txt')
models = file.read().split()
for model in models:
    os.system('pip install {}'.format(model))
file.close()
print()
input('>>安装完毕，按任意键启动SkyDrive。')
os.system('start SkyDrive.pyw')
exit()