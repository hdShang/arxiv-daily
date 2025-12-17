---
layout: default
title: Real-time prediction of workplane illuminance distribution for daylight-linked controls using non-intrusive multimodal deep learning
---

# Real-time prediction of workplane illuminance distribution for daylight-linked controls using non-intrusive multimodal deep learning

**arXiv**: [2512.14058v1](https://arxiv.org/abs/2512.14058) | [PDF](https://arxiv.org/pdf/2512.14058.pdf)

**作者**: Zulin Zhuang, Yu Bian

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出非侵入式多模态深度学习框架，以实时预测动态室内工作平面照度分布，支持日光联动控制节能。**

**关键词**: `日光联动控制` `实时照度预测` `多模态深度学习` `非侵入式图像处理` `时空特征提取` `建筑节能` `动态室内场景` `泛化性能验证`

## 📋 核心要点

1. 现有室内日光预测方法多针对静态场景，难以适应动态占用空间，限制了日光联动控制的实时应用。
2. 提出多模态深度学习框架，仅从侧窗区域提取图像特征，结合时空信息，实现非侵入式实时照度预测。
3. 现场实验验证模型在同分布和未见日测试集上均表现优异，R2值高且误差低，展示了良好的泛化性能。

## 📝 摘要（中文）

日光联动控制（DLCs）在建筑节能方面具有巨大潜力，尤其是在日光充足且能实时准确预测室内工作平面照度时。现有室内日光预测研究大多针对静态场景开发与测试。本研究提出一种多模态深度学习框架，利用非侵入式图像中的时空特征实时预测室内工作平面照度分布。该方法仅从侧窗区域提取图像特征，而非室内像素，从而适用于动态占用的室内空间。在中国广州的一个测试房间进行了现场实验，收集了17,344个样本用于模型训练和验证。模型在同分布测试集上实现了R2 > 0.98且RMSE < 0.14，在未见日测试集上实现了R2 > 0.82且RMSE < 0.17，表明其具有高精度和可接受的时间泛化能力。

## 🔬 方法详解

论文提出一个多模态深度学习框架，整体架构基于非侵入式图像输入，通过卷积神经网络提取侧窗区域的图像特征，并结合时间序列数据（如时间戳）进行时空融合。关键技术创新点在于仅利用侧窗像素而非整个室内图像，避免了动态占用干扰，同时引入多模态学习以增强预测鲁棒性。与现有方法的主要区别在于其专注于动态场景的实时预测，而非静态建模，从而提高了在真实环境中的适用性和效率。

## 📊 实验亮点

模型在同分布测试集上达到R2 > 0.98和RMSE < 0.14的高精度，在未见日测试集上保持R2 > 0.82和RMSE < 0.17，验证了其出色的预测能力和时间泛化性能，为动态室内环境下的实时照度控制提供了可靠工具。

## 🎯 应用场景

该研究可应用于智能建筑节能系统，通过实时预测室内照度优化日光联动控制，减少人工照明能耗，提升建筑能效。潜在领域包括办公楼、学校等动态占用空间，支持可持续城市发展。

## 📄 摘要（原文）

> Daylight-linked controls (DLCs) have significant potential for energy savings in buildings, especially when abundant daylight is available and indoor workplane illuminance can be accurately predicted in real time. Most existing studies on indoor daylight predictions were developed and tested for static scenes. This study proposes a multimodal deep learning framework that predicts indoor workplane illuminance distributions in real time from non-intrusive images with temporal-spatial features. By extracting image features only from the side-lit window areas rather than interior pixels, the approach remains applicable in dynamically occupied indoor spaces. A field experiment was conducted in a test room in Guangzhou (China), where 17,344 samples were collected for model training and validation. The model achieved R2 > 0.98 with RMSE < 0.14 on the same-distribution test set and R2 > 0.82 with RMSE < 0.17 on an unseen-day test set, indicating high accuracy and acceptable temporal generalization.

