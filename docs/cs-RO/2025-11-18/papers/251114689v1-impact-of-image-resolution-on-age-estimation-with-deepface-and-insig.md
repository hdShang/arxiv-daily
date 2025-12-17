---
layout: default
title: Impact of Image Resolution on Age Estimation with DeepFace and InsightFace
---

# Impact of Image Resolution on Age Estimation with DeepFace and InsightFace

**arXiv**: [2511.14689v1](https://arxiv.org/abs/2511.14689) | [PDF](https://arxiv.org/pdf/2511.14689.pdf)

**作者**: Shiyar Jamo

---

## 💡 一句话要点

**评估图像分辨率对DeepFace和InsightFace年龄估计准确性的影响**

**关键词**: `年龄估计` `图像分辨率` `DeepFace` `InsightFace` `MAE评估`

## 📋 核心要点

1. 核心问题：图像分辨率变化对自动年龄估计准确性的影响。
2. 方法要点：使用IMDB-Clean数据集，在七种分辨率下测试DeepFace和InsightFace。
3. 实验或效果：224x224像素时性能最优，MAE分别为10.83年和7.46年。

## 📄 摘要（原文）

> Automatic age estimation is widely used for age verification, where input images often vary considerably in resolution. This study evaluates the effect of image resolution on age estimation accuracy using DeepFace and InsightFace. A total of 1000 images from the IMDB-Clean dataset were processed in seven resolutions, resulting in 7000 test samples. Performance was evaluated using Mean Absolute Error (MAE), Standard Deviation (SD), and Median Absolute Error (MedAE). Based on this study, we conclude that input image resolution has a clear and consistent impact on the accuracy of age estimation in both DeepFace and InsightFace. Both frameworks achieve optimal performance at 224x224 pixels, with an MAE of 10.83 years (DeepFace) and 7.46 years (InsightFace). At low resolutions, MAE increases substantially, while very high resolutions also degrade accuracy. InsightFace is consistently faster than DeepFace across all resolutions.

