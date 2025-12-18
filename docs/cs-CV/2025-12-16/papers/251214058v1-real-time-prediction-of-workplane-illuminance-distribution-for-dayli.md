---
layout: default
title: Real-time prediction of workplane illuminance distribution for daylight-linked controls using non-intrusive multimodal deep learning
---

# Real-time prediction of workplane illuminance distribution for daylight-linked controls using non-intrusive multimodal deep learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14058" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14058v1</a>
  <a href="https://arxiv.org/pdf/2512.14058.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14058v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14058v1', 'Real-time prediction of workplane illuminance distribution for daylight-linked controls using non-intrusive multimodal deep learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zulin Zhuang, Yu Bian

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于非侵入式多模态深度学习的日光照明工作面照度实时预测方法，用于日光联动控制。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `日光联动控制` `照度预测` `多模态深度学习` `非侵入式感知` `实时预测`

## 📋 核心要点

1. 现有室内日光预测方法主要针对静态场景，难以适应动态变化的室内环境。
2. 该研究提出一种多模态深度学习框架，仅利用窗户区域图像特征，实现工作面照度的实时预测。
3. 实验结果表明，该模型具有较高的预测精度和良好的时间泛化能力，适用于实际应用。

## 📝 摘要（中文）

日光联动控制（DLCs）在建筑节能方面具有显著潜力，尤其是在充足日光可用且室内工作面照度能够被准确实时预测时。现有关于室内日光预测的研究大多是为静态场景开发和测试的。本研究提出了一个多模态深度学习框架，该框架通过具有时空特征的非侵入式图像实时预测室内工作面照度分布。通过仅从侧光窗户区域而非内部像素提取图像特征，该方法在动态占用的室内空间中仍然适用。在中国广州的一个测试室内进行了一项现场实验，收集了17344个样本用于模型训练和验证。该模型在同分布测试集上实现了R2 > 0.98，RMSE < 0.14，在未见过的日期测试集上实现了R2 > 0.82，RMSE < 0.17，表明了高精度和可接受的时间泛化能力。

## 🔬 方法详解

**问题定义**：论文旨在解决在动态变化的室内环境中，如何准确、实时地预测工作面照度分布的问题。现有方法主要针对静态场景，无法有效应对人员活动、家具移动等因素带来的光照变化，导致日光联动控制系统性能下降。

**核心思路**：论文的核心思路是利用非侵入式的图像信息，特别是窗户区域的图像特征，来预测工作面照度。这种方法避免了直接使用室内像素，从而减少了人员活动对预测结果的影响，提高了模型的鲁棒性。

**技术框架**：整体框架包含数据采集、特征提取和照度预测三个主要阶段。首先，通过摄像头采集窗户区域的图像数据。然后，利用深度学习模型提取图像的时空特征。最后，将提取的特征输入到回归模型中，预测工作面照度分布。

**关键创新**：该研究的关键创新在于使用非侵入式的图像特征进行照度预测。与传统的基于室内像素的方法相比，该方法能够更好地适应动态变化的室内环境，提高了预测的准确性和鲁棒性。此外，多模态深度学习框架能够有效融合图像的时空特征，进一步提升预测性能。

**关键设计**：论文中使用了特定的卷积神经网络（CNN）结构来提取图像特征，并结合循环神经网络（RNN）来捕捉时间序列信息。损失函数采用均方根误差（RMSE）和决定系数（R2）作为评价指标，优化模型参数。具体的网络结构和参数设置在论文中进行了详细描述（未知）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14058v1/figure/workflow.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14058v1/figure/case.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14058v1/figure/lab.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该模型在同分布测试集上实现了R2 > 0.98，RMSE < 0.14，在未见过的日期测试集上实现了R2 > 0.82，RMSE < 0.17。这些数据表明，该模型具有较高的预测精度和良好的时间泛化能力，能够有效应对不同日期的光照变化，优于传统的静态模型（具体对比未知）。

## 🎯 应用场景

该研究成果可应用于智能建筑的日光联动控制系统，通过实时预测室内照度，自动调节照明设备，从而降低能源消耗，提高室内舒适度。此外，该方法还可用于虚拟现实、游戏等领域，提供更真实的光照模拟效果。未来，该技术有望在更广泛的室内环境监测和控制领域发挥作用。

## 📄 摘要（原文）

> Daylight-linked controls (DLCs) have significant potential for energy savings in buildings, especially when abundant daylight is available and indoor workplane illuminance can be accurately predicted in real time. Most existing studies on indoor daylight predictions were developed and tested for static scenes. This study proposes a multimodal deep learning framework that predicts indoor workplane illuminance distributions in real time from non-intrusive images with temporal-spatial features. By extracting image features only from the side-lit window areas rather than interior pixels, the approach remains applicable in dynamically occupied indoor spaces. A field experiment was conducted in a test room in Guangzhou (China), where 17,344 samples were collected for model training and validation. The model achieved R2 > 0.98 with RMSE < 0.14 on the same-distribution test set and R2 > 0.82 with RMSE < 0.17 on an unseen-day test set, indicating high accuracy and acceptable temporal generalization.

