import pickle
from scipy.spatial.distance import cdist
import torch
import cv2 as cv
import numpy as np
from PIL import Image

class netvlad(object):
    def __init__(self):
        ###################################################################################################################
        # Load saved per-trained model
        ###################################################################################################################
        print('===>Building model')
        modelpath = 'vgg16_netvlad_model_save/model_save.pt'
        # 设置参数加载网络
        self.device = torch.device('cuda')  # if not available,use 'cpu' instead
        self.encoder_dim = 512  # vgg16 network architecture
        self.num_clusters = 64  # netvlad default cluster num
        self.pool_size = self.encoder_dim
        model = torch.load(modelpath)  #
        self.model = model.to(self.device)
        self.model.eval()

    def gen_ref(self):
        ###################################################################################################################
        # Load image
        ###################################################################################################################
        print('===>Loading data')
        imgpath = 'data/'
        imgnum = 2  # num of input image
        # 准备数据集
        imgList = np.empty([3, 3, 200, 200], dtype=float)
        # 512x512是保存图片长宽
        for i in range(imgnum):
            tmp = cv.imread((imgpath + '{}.png'.format('pub_recruit_' + str(i))))
            tmp = cv.resize(tmp, (200, 200))  # 图片尺寸根据需要设置，网络可以自动适配图片长宽
            # 注意高分辨图片需要申请大量显存
            imgList[i, :] = tmp.transpose((2, 1, 0))
            # shape of img is [height,width,channel=3],
            # but shape of network input is [channel=3,width,height]

        ###################################################################################################################
        # Retrieving feature with model
        ###################################################################################################################
        print('===>Retrieving features')
        imgInput = np.empty([3, 3, 200, 200], dtype=float)
        # 用于输入网络的图片batch，每batch输入3张图
        dbFeat = np.empty([3, self.pool_size * self.num_clusters])
        # 特征值存储队列
        with torch.no_grad():
            for i in range(0,imgnum,3):
                imgInput[:] = imgList[i:i + 3, :]
                imgInput = torch.from_numpy(imgInput).type(torch.FloatTensor)
                imgInput = imgInput.to(self.device)
                # 使用模型计算特征值
                image_encoding = self.model.encoder(imgInput)
                vlad_encoding = self.model.pool(image_encoding)

                dbFeat[i:i + 3, :] = vlad_encoding.detach().cpu().numpy()

        print('===>Saving features to file')
        featfile = open(r'dbFeat.pkl', 'wb')
        pickle.dump(dbFeat, featfile)

    def pub_recruit_check(self, img):
        # 加载参考
        with open('dbFeat.pkl', 'rb') as f:
            dbFeat = pickle.load(f)

        imgList = np.empty([1, 3, 200, 200], dtype=float)# 第一个1是图片数
        tmp = img
        tmp = cv.cvtColor(np.asarray(tmp), cv.COLOR_RGB2BGR)
        tmp = cv.resize(tmp, (200, 200))  # 图片尺寸根据需要设置，网络可以自动适配图片长宽

        # 注意高分辨图片需要申请大量显存
        imgList[0, :] = tmp.transpose((2, 1, 0))
        imgInput = np.empty([3, 3, 200, 200], dtype=float)
        imgInput[0,:] = imgList[:]

        testFeat = np.empty([1, self.pool_size * self.num_clusters])

        with torch.no_grad():
            imgInput = torch.from_numpy(imgInput).type(torch.FloatTensor)
            imgInput = imgInput.to(self.device)
            # 使用模型计算特征值
            image_encoding = self.model.encoder(imgInput)
            vlad_encoding = self.model.pool(image_encoding)
            testFeat = vlad_encoding.detach().cpu().numpy()

        F = cdist(testFeat, dbFeat[0:2,:])
        idx = np.argmin(F[0])
        if idx == 1:
            return True
        elif idx ==0:
            return False

'''
matcher = netvlad()
# matcher.gen_ref()
imgpath = "data/"
testimg1 = cv.imread((imgpath + 'test1.png'))
testimg2 = cv.imread((imgpath + 'test2.png'))
matcher.pub_recruit_check(testimg1)
matcher.pub_recruit_check(testimg2)
'''










