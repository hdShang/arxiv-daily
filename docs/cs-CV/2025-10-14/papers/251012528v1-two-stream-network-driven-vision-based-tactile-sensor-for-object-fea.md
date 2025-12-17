---
layout: default
title: Two-stream network-driven vision-based tactile sensor for object feature extraction and fusion perception
---

# Two-stream network-driven vision-based tactile sensor for object feature extraction and fusion perception

**arXiv**: [2510.12528v1](https://arxiv.org/abs/2510.12528) | [PDF](https://arxiv.org/pdf/2510.12528.pdf)

**作者**: Muxing Huang, Zibin Chen, Weiliang Xu, Zilan Li, Yuanzhi Zhou, Guoyuan Zhou, Wenjing Chen, Xinming Li

---

## 💡 一句话要点

**提出双流网络特征提取与融合策略，以提升视觉触觉传感器在物体识别中的准确性。**

**关键词**: `视觉触觉传感器` `双流网络` `特征融合` `物体识别` `卷积神经网络` `多模态感知`

## 📋 核心要点

1. 核心问题：视觉触觉传感器产生冗余信息，单维特征提取缺乏有效融合，限制识别精度提升。
2. 方法要点：采用双流网络分别提取物体内外特征，结合深度图和硬度信息，经CNN提取后加权融合。
3. 实验或效果：在标准测试中，硬度识别准确率98.0%，形状识别93.75%，实际抓取场景识别超98.5%。

## 📄 摘要（原文）

> Tactile perception is crucial for embodied intelligent robots to recognize
> objects. Vision-based tactile sensors extract object physical attributes
> multidimensionally using high spatial resolution; however, this process
> generates abundant redundant information. Furthermore, single-dimensional
> extraction, lacking effective fusion, fails to fully characterize object
> attributes. These challenges hinder the improvement of recognition accuracy. To
> address this issue, this study introduces a two-stream network feature
> extraction and fusion perception strategy for vision-based tactile systems.
> This strategy employs a distributed approach to extract internal and external
> object features. It obtains depth map information through three-dimensional
> reconstruction while simultaneously acquiring hardness information by measuring
> contact force data. After extracting features with a convolutional neural
> network (CNN), weighted fusion is applied to create a more informative and
> effective feature representation. In standard tests on objects of varying
> shapes and hardness, the force prediction error is 0.06 N (within a 12 N
> range). Hardness recognition accuracy reaches 98.0%, and shape recognition
> accuracy reaches 93.75%. With fusion algorithms, object recognition accuracy in
> actual grasping scenarios exceeds 98.5%. Focused on object physical attributes
> perception, this method enhances the artificial tactile system ability to
> transition from perception to cognition, enabling its use in embodied
> perception applications.

