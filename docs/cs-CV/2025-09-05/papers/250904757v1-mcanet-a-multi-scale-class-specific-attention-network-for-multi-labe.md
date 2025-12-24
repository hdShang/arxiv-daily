---
layout: default
title: "MCANet: A Multi-Scale Class-Specific Attention Network for Multi-Label Post-Hurricane Damage Assessment using UAV Imagery"
---

# MCANet: A Multi-Scale Class-Specific Attention Network for Multi-Label Post-Hurricane Damage Assessment using UAV Imagery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04757" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04757v1</a>
  <a href="https://arxiv.org/pdf/2509.04757.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04757v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04757v1', 'MCANet: A Multi-Scale Class-Specific Attention Network for Multi-Label Post-Hurricane Damage Assessment using UAV Imagery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhangding Liu, Neda Mohammadi, John E. Taylor

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-05

**备注**: 34 pages, 7 figures

---

## 💡 一句话要点

**提出MCANet，利用多尺度类特定注意力网络进行无人机图像的飓风灾后多标签评估。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多标签分类` `灾后评估` `无人机图像` `多尺度特征` `注意力机制` `Res2Net` `类特定注意力`

## 📋 核心要点

1. 现有基于CNN的灾后评估方法难以有效捕捉多尺度空间特征，且难以区分视觉相似的破坏类型。
2. MCANet通过Res2Net骨干网络提取多尺度特征，并使用多头类特定残差注意力模块自适应关注相关区域。
3. 实验表明，MCANet在RescueNet数据集上mAP达到91.75%，优于多种主流模型，并能有效定位破坏区域。

## 📝 摘要（中文）

快速且准确的飓风灾后评估对于灾害响应和恢复至关重要。然而，现有的基于CNN的方法难以捕捉多尺度空间特征，并且难以区分视觉上相似或共现的破坏类型。为了解决这些问题，我们提出了MCANet，一个多标签分类框架，它学习多尺度表示并自适应地关注每个破坏类别的空间相关区域。MCANet采用基于Res2Net的分层骨干网络来丰富跨尺度的空间上下文，并采用多头类特定残差注意力模块来增强判别能力。每个注意力分支侧重于不同的空间粒度，平衡局部细节和全局上下文。我们在飓风迈克尔之后收集的4,494张无人机图像的RescueNet数据集上评估了MCANet。MCANet实现了91.75%的平均精度均值（mAP），优于ResNet、Res2Net、VGG、MobileNet、EfficientNet和ViT。使用八个注意力头时，性能进一步提高到92.35%，将“道路阻塞”等具有挑战性的类别的平均精度提高了6%以上。类激活图证实了MCANet定位破坏相关区域的能力，支持了可解释性。MCANet的输出可以为灾后风险图、紧急路线规划和基于数字孪生的灾害响应提供信息。未来的工作可以整合特定于灾害的知识图谱和多模态大型语言模型，以提高对未见灾害的适应性，并丰富对现实世界决策的语义理解。

## 🔬 方法详解

**问题定义**：论文旨在解决飓风灾后无人机图像多标签破坏评估问题。现有方法，特别是基于CNN的方法，在处理多尺度空间特征和区分视觉上相似的破坏类型时存在局限性，导致评估精度不高。

**核心思路**：论文的核心思路是利用多尺度特征表示和类特定注意力机制，使模型能够更有效地捕捉不同尺度的空间上下文信息，并自适应地关注与每个破坏类别相关的区域。通过这种方式，模型可以更好地区分不同类型的破坏，提高评估精度。

**技术框架**：MCANet的整体架构包括一个基于Res2Net的分层骨干网络和一个多头类特定残差注意力模块。Res2Net用于提取多尺度特征，多头注意力模块则针对每个破坏类别学习不同的空间注意力图。整个网络采用端到端的方式进行训练，以优化多标签分类性能。

**关键创新**：MCANet的关键创新在于提出了多头类特定残差注意力模块。该模块为每个破坏类别学习独立的注意力分支，每个分支关注不同的空间粒度，从而平衡了局部细节和全局上下文。这种设计使得模型能够更准确地识别与每个类别相关的区域，提高了分类精度。

**关键设计**：Res2Net骨干网络采用标准的Res2Net结构，通过分层连接增强了特征的多尺度表示能力。多头注意力模块包含多个独立的注意力分支，每个分支使用残差连接来加速训练。损失函数采用二元交叉熵损失，用于优化多标签分类任务。注意力头的数量设置为8，以平衡性能和计算复杂度。

## 📊 实验亮点

MCANet在RescueNet数据集上取得了显著的性能提升，mAP达到91.75%，优于ResNet、Res2Net、VGG、MobileNet、EfficientNet和ViT等基线模型。通过增加注意力头的数量到8，性能进一步提升至92.35%，尤其是在“道路阻塞”等具有挑战性的类别上，平均精度提升超过6%。类激活图可视化结果表明，MCANet能够准确地定位与破坏相关的区域。

## 🎯 应用场景

MCANet的研究成果可应用于灾后风险地图的快速生成、紧急救援路线的规划以及基于数字孪生的灾害响应系统。通过快速准确地评估灾害造成的破坏程度，可以为救援工作提供决策支持，提高救援效率，减少人员伤亡和财产损失。此外，该技术还可以应用于其他类型的灾害评估，具有广泛的应用前景。

## 📄 摘要（原文）

> Rapid and accurate post-hurricane damage assessment is vital for disaster response and recovery. Yet existing CNN-based methods struggle to capture multi-scale spatial features and to distinguish visually similar or co-occurring damage types. To address these issues, we propose MCANet, a multi-label classification framework that learns multi-scale representations and adaptively attends to spatially relevant regions for each damage category. MCANet employs a Res2Net-based hierarchical backbone to enrich spatial context across scales and a multi-head class-specific residual attention module to enhance discrimination. Each attention branch focuses on different spatial granularities, balancing local detail with global context. We evaluate MCANet on the RescueNet dataset of 4,494 UAV images collected after Hurricane Michael. MCANet achieves a mean average precision (mAP) of 91.75%, outperforming ResNet, Res2Net, VGG, MobileNet, EfficientNet, and ViT. With eight attention heads, performance further improves to 92.35%, boosting average precision for challenging classes such as Road Blocked by over 6%. Class activation mapping confirms MCANet's ability to localize damage-relevant regions, supporting interpretability. Outputs from MCANet can inform post-disaster risk mapping, emergency routing, and digital twin-based disaster response. Future work could integrate disaster-specific knowledge graphs and multimodal large language models to improve adaptability to unseen disasters and enrich semantic understanding for real-world decision-making.

