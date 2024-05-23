import streamlit as st

# 设置页面标题
st.title("MobileNet与MobileNetV2介绍")


st.header("前言")
st.write("随着深度学习的火热，计算机视觉领域内的卷积神经网络模型也层出不穷。从1998年的LeNet，到2012年引爆深度学习热潮的AlexNet，再到后来2014年的VGG，2015年的ResNet，深度学习网络模型在图像处理中应用的效果越来越好。神经网络体积越来越大，结构越来越复杂，预测和训练需要的硬件资源也逐步增多，往往只能在高算力的服务器中运行深度学习神经网络模型。移动设备因硬件资源和算力的限制，很难运行复杂的深度学习网络模型。")
st.image('data/light nn.jpeg', use_column_width=True)
st.write("深度学习领域内也在努力促使神经网络向小型化发展。在保证模型准确率的同时体积更小，速度更快。到了2016年直至现在，业内提出了SqueezeNet、ShuffleNet、NasNet、MnasNet以及MobileNet等轻量级网络模型。这些模型使移动终端、嵌入式设备运行神经网络模型成为可能。而MobileNet在轻量级神经网络中较具代表性。")
# MobileNet介绍
st.header("MobileNet简介")
st.write("""
**MobileNet** 是Google在2017年推出的一种轻量级的深度学习模型，专为移动和嵌入式设备设计。它基于卷积神经网络（CNN）架构，通过使用深度可分离卷积（Depthwise Convolution）大大减少了模型的参数量，使得模型体积小巧，同时保持了较好的性能。这对于资源受限的环境尤其重要，因为它可以在保持较低功耗的同时，实现实时的图像分类和对象检测任务。
""")
st.image('data/MobileNet CNN Architecture.webp', caption="MobileNet结构",use_column_width=True)
# MobileNet图片展示（假设你有这张图片放在'app/static'目录下）
#image_path = "mobile_net.png"
#st.image(image_path, caption="MobileNet架构示意图", use_column_width=True)

# MobileNetV2介绍
st.header("MobileNetV2：更进一步的优化")
st.write("""
**MobileNetV2** 在2018年作为MobileNet的升级版发布，它引入了创新的逆残差结构（Inverted Residuals）和线性瓶颈（Linear Bottleneck），进一步提升了模型效率。逆残差结构意味着在残差连接中，输入先经过一个线性层，然后是非线性变换（ReLU6激活），这样的设计让模型在低维度上做更多的计算，提高了效率。此外，V2版还改进了模型的宽度乘数和分辨率缩放策略，使得模型在不同资源约束下都能找到最佳平衡点。
""")
st.image('data/MobileNetV2.png', caption="MobileNetV2结构",use_column_width=True)
# MobileNetV2图片展示（假设你有这张图片放在'app/static'目录下）
#image_path_v2 = "mobile_net_v2.png"
#st.image(image_path_v2, caption="MobileNetV2架构示意图", use_column_width=True)

# 结尾部信息
st.write("""
#### 以上就是MobileNet与MobileNetV2的基本介绍。它们在移动视觉任务中因其高效和高性能而广泛被采用，是深度学习领域轻量化模型的典范。\n
#### 下一章我们将使用MobileNetV2模型进行图像识别。
""")

# 如果有进一步的交互或模型演示，这里可以继续添加更多代码