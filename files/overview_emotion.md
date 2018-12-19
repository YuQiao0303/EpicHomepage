﻿<div style="text-align :center;">
<img src="images/emotion1.jpg" alt="">
</div>

　　情感识别与交互算法具备实时情感识别的功能，上图展示了基于语音和人脸表情的实时情感识别Demo原型。上图左下部分展示了所采用的人脸情感识别深度卷积神经网络算法模型， 同时也建立了相应的人脸情感库。上图右上部分则介绍了基于深度卷积神经网络设计的语音情感识别算法，首先将语音转化为多段语谱图，基于单个语谱图采用深度神经网络模型获取局部特征，再采用特定方法将局部特征融合为定长的全局特征，最后基于支持向量机算法进行情感分类模型的训练，取得了很好的情感识别效果。

<div style="text-align :center;">
<img src="images/emotion2.png" alt="">
</div>

　　无标签情感认知: 通过筛选大量无标签的情感数据，将置信度高的自主标签数据加入到训练集中; 从无标签数据的特征层和决策层两个角度考虑，利用相似度模型和熵模型，提出混合的无标签数据自主标签策略。为了进一步提高加入数据的置信度，需对自主标签的数据重新进行筛选.