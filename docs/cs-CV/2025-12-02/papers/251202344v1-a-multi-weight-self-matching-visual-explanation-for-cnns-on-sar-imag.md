---
layout: default
title: A multi-weight self-matching visual explanation for cnns on sar images
---

# A multi-weight self-matching visual explanation for cnns on sar images

**arXiv**: [2512.02344v1](https://arxiv.org/abs/2512.02344) | [PDF](https://arxiv.org/pdf/2512.02344.pdf)

**作者**: Siyuan Sun, Yongping Zhang, Hongcheng Zeng, Yamin Wang, Wei Yang, Wanting Yang, Jie Chen

---

## 💡 一句话要点

**提出多权重自匹配类激活映射以增强合成孔径雷达图像中卷积神经网络的解释性**

**关键词**: `合成孔径雷达图像` `卷积神经网络解释性` `类激活映射` `弱监督目标定位` `视觉解释方法`

## 📋 核心要点

1. 核心问题：卷积神经网络在合成孔径雷达任务中内部机制复杂且不透明，限制其高可靠性应用。
2. 方法要点：通过匹配图像与特征图及梯度，结合通道和元素权重可视化模型决策依据。
3. 实验或效果：在自建数据集上验证方法能更准确突出感兴趣区域并捕获细节特征，提升解释性。

## 📄 摘要（原文）

> In recent years, convolutional neural networks (CNNs) have achieved significant success in various synthetic aperture radar (SAR) tasks. However, the complexity and opacity of their internal mechanisms hinder the fulfillment of high-reliability requirements, thereby limiting their application in SAR. Improving the interpretability of CNNs is thus of great importance for their development and deployment in SAR. In this paper, a visual explanation method termed multi-weight self-matching class activation mapping (MS-CAM) is proposed. MS-CAM matches SAR images with the feature maps and corresponding gradients extracted by the CNN, and combines both channel-wise and element-wise weights to visualize the decision basis learned by the model in SAR images. Extensive experiments conducted on a self-constructed SAR target classification dataset demonstrate that MS-CAM more accurately highlights the network's regions of interest and captures detailed target feature information, thereby enhancing network interpretability. Furthermore, the feasibility of applying MS-CAM to weakly-supervised obiect localization is validated. Key factors affecting localization accuracy, such as pixel thresholds, are analyzed in depth to inform future work.

