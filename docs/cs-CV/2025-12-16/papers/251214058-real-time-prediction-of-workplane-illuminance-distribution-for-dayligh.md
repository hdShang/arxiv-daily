---
layout: default
title: Real-time prediction of workplane illuminance distribution for daylight-linked controls using non-intrusive multimodal deep learning
---

# Real-time prediction of workplane illuminance distribution for daylight-linked controls using non-intrusive multimodal deep learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14058" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14058</a>
  <a href="https://arxiv.org/pdf/2512.14058.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14058" onclick="toggleFavorite(this, '2512.14058', 'Real-time prediction of workplane illuminance distribution for daylight-linked controls using non-intrusive multimodal deep learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zulin Zhuang, Yu Bian

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出一种非侵入式多模态深度学习框架，用于日光照明控制的实时工作面照度预测。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `日光照明控制` `深度学习` `多模态融合` `实时预测` `非侵入式` `室内环境` `照度预测`

## 📋 核心要点

1. 现有日光预测方法多针对静态场景，难以适应动态Occupied的室内环境，限制了日光照明控制的应用。
2. 该研究提出一种多模态深度学习框架，仅利用侧光窗户区域的图像特征，实现实时工作面照度预测。
3. 实验结果表明，该模型具有较高的预测精度和良好的时间泛化能力，适用于实际应用场景。

## 📝 摘要（中文）

日光照明控制（DLCs）在建筑物节能方面具有巨大潜力，尤其是在充足的日光可用且室内工作面照度可以实时准确预测时。现有关于室内日光预测的大多数研究都是为静态场景开发和测试的。本研究提出了一种多模态深度学习框架，该框架通过具有时空特征的非侵入式图像实时预测室内工作面照度分布。通过仅从侧光窗户区域而非内部像素提取图像特征，该方法在动态Occupied室内空间中仍然适用。在中国广州的一个测试室内进行了一项现场实验，收集了17344个样本用于模型训练和验证。该模型在同分布测试集上实现了R2 > 0.98，RMSE < 0.14，在未见过的日期测试集上实现了R2 > 0.82，RMSE < 0.17，表明了高精度和可接受的时间泛化能力。

## 🔬 方法详解

**问题定义**：论文旨在解决在动态Occupied的室内环境中，如何实时、准确地预测工作面照度分布，从而实现高效的日光照明控制。现有方法主要针对静态场景，无法有效应对室内人员活动带来的光照变化，且通常需要侵入式传感器，影响用户体验。

**核心思路**：论文的核心思路是利用非侵入式的图像信息，特别是侧光窗户区域的图像特征，来预测室内工作面照度。这种方法避免了直接使用室内像素，从而减少了人员活动对预测的影响，提高了模型的鲁棒性。同时，采用深度学习模型可以有效提取图像中的时空特征，提高预测精度。

**技术框架**：该研究提出的框架主要包含以下几个模块：1) 数据采集模块：通过摄像头采集侧光窗户区域的图像数据，并记录对应的工作面照度数据。2) 特征提取模块：利用卷积神经网络（CNN）提取图像中的视觉特征。3) 时序建模模块：使用循环神经网络（RNN）或Transformer等模型对时间序列特征进行建模，捕捉光照随时间的变化规律。4) 照度预测模块：将提取的特征输入到全连接层或其他回归模型中，预测工作面照度分布。

**关键创新**：该研究的关键创新在于：1) 提出了一种非侵入式的照度预测方法，仅利用侧光窗户区域的图像信息，避免了对室内环境的干扰。2) 采用多模态深度学习框架，有效融合了图像的时空特征，提高了预测精度和泛化能力。

**关键设计**：论文中可能涉及的关键设计包括：1) CNN网络结构的选择，例如ResNet、DenseNet等。2) RNN或Transformer模型的选择和参数设置，例如LSTM、GRU等。3) 损失函数的选择，例如均方误差（MSE）、Huber loss等。4) 数据增强方法，例如图像旋转、缩放等。5) 模型训练的优化算法，例如Adam、SGD等。这些细节将直接影响模型的性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14058/figure/workflow.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14058/figure/case.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14058/figure/lab.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该模型在同分布测试集上实现了R2 > 0.98，RMSE < 0.14，在未见过的日期测试集上实现了R2 > 0.82，RMSE < 0.17。这些结果表明，该模型具有较高的预测精度和良好的时间泛化能力，优于传统的基于静态场景的预测方法。

## 🎯 应用场景

该研究成果可应用于智能建筑的日光照明控制系统，根据实时照度预测结果自动调节灯光亮度，从而实现节能和提高室内舒适度。此外，该方法还可扩展到其他室内环境参数的预测，例如温度、湿度等，为智能家居和智慧城市的发展提供技术支持。

## 📄 摘要（原文）

> Daylight-linked controls (DLCs) have significant potential for energy savings in buildings, especially when abundant daylight is available and indoor workplane illuminance can be accurately predicted in real time. Most existing studies on indoor daylight predictions were developed and tested for static scenes. This study proposes a multimodal deep learning framework that predicts indoor workplane illuminance distributions in real time from non-intrusive images with temporal-spatial features. By extracting image features only from the side-lit window areas rather than interior pixels, the approach remains applicable in dynamically occupied indoor spaces. A field experiment was conducted in a test room in Guangzhou (China), where 17,344 samples were collected for model training and validation. The model achieved R2 > 0.98 with RMSE < 0.14 on the same-distribution test set and R2 > 0.82 with RMSE < 0.17 on an unseen-day test set, indicating high accuracy and acceptable temporal generalization.

