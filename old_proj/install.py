import torch
import cv2 as cv
import pickle
import numpy as np



if __name__ == "__main__":
    ###################################################################################################################
    # Load saved per-trained model
    ###################################################################################################################
    print('===>Building model')
    modelpath = 'vgg16_netvlad_model_save/model_save.pt'
    # 设置参数加载网络
    device = torch.decive('cuda') # if not available,use 'cpu' instead
    encoder_dim = 512  # vgg16 network architecture
    num_clusters = 64  # netvlad default cluster num
    pool_size = encoder_dim
    model=torch.load(modelpath)#
    model=model.to(device)
    model.eval()

    ###################################################################################################################
    # Load image
    ###################################################################################################################
    print('===>Loading data')
    imgpath = 'data/'
    imgnum = 2 # num of input image
    # 准备数据集
    imgList = np.empty([imgnum,3,200,200],dtype=float)
    # 512x512是保存图片长宽
    for i in range(imgnum):
        tmp = cv.imread((imgpath + '{}.png'.format('pub_recruit_'+str(i))))
        cv.resize(tmp,(200,200))# 图片尺寸根据需要设置，网络可以自动适配图片长宽
        # 注意高分辨图片需要申请大量显存
        imgList[i,:] = tmp.transpose((2,1,0))
        # shape of img is [height,width,channel=3],
        # but shape of network input is [channel=3,width,height]

    ###################################################################################################################
    # Retrieving feature with model
    ###################################################################################################################
    print('===>Retrieving features')
    imgInput = np.empty([3,3,200,200],dtype=float)
    # 用于输入网络的图片batch，每batch输入3张图
    dbFeat = np.empty([imgnum,pool_size*num_clusters])
    # 特征值存储队列
    with torch.no_grad():
        for i in range(imgnum):
            imgInput[:] = imgList[i:i+3,:]
            imgInput = imgInput.type(torch.FloatTensor)
            imgInput = imgInput.to(device)
            # 使用模型计算特征值
            image_encoding = model.encoder(imgInput)
            vlad_encoding = model.pool(image_encoding)

            dbFeat[i:i+3,:] = vlad_encoding.detach().cpu().numpy()

    print('===>Saving features to file')
    featfile = open(r'imgFeat.pkl','wb')
    pickle.dump(dbFeat,featfile)







