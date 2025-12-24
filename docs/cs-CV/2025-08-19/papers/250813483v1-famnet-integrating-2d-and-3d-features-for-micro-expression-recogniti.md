---
layout: default
title: "FAMNet: Integrating 2D and 3D Features for Micro-expression Recognition via Multi-task Learning and Hierarchical Attention"
---

# FAMNet: Integrating 2D and 3D Features for Micro-expression Recognition via Multi-task Learning and Hierarchical Attention

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13483" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13483v1</a>
  <a href="https://arxiv.org/pdf/2508.13483.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13483v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13483v1', 'FAMNet: Integrating 2D and 3D Features for Micro-expression Recognition via Multi-task Learning and Hierarchical Attention')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liangyu Fu, Xuecheng Wu, Danlei Huang, Xinyi Yin

**分类**: cs.CV

**发布日期**: 2025-08-19

**备注**: 8 pages, 6 figures. Accepted to IJCNN 2025

---

## 💡 一句话要点

**提出FAMNet以解决微表情识别中的特征提取挑战**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `微表情识别` `多任务学习` `层次注意力` `2D CNN` `3D CNN` `特征提取` `深度学习`

## 📋 核心要点

1. 现有微表情识别方法在特征提取上存在不足，难以有效捕捉微表情的细粒度和时空特征。
2. 论文提出的FAMNet通过融合2D和3D CNN，采用多任务学习和层次注意力机制，提升微表情的特征提取能力。
3. 在SAMM、CASME II和MMEW数据集上，FAMNet分别达到了83.75%（UAR）和84.03%（UF1）的识别率，表现显著优于现有方法。

## 📝 摘要（中文）

微表情识别（MER）在多个领域具有重要应用价值，但由于微表情的短暂性和低强度，识别面临巨大挑战。现有深度学习方法主要包括静态图像、动态图像序列及两者结合的数据加载方式，如何有效提取微表情的细粒度时空特征仍然是一个难题。本文提出了一种基于多任务学习和层次注意力的新型MER方法，通过融合2D和3D卷积神经网络（CNN）全面提取微表情的全方位特征。实验结果表明，FAMNet在多个数据集上显著提高了识别性能。

## 🔬 方法详解

**问题定义**：论文旨在解决微表情识别中的特征提取问题，现有方法在捕捉微表情的细粒度和时空特征方面存在明显不足。

**核心思路**：FAMNet通过融合2D CNN和3D CNN，结合多任务学习和层次注意力机制，全面提取微表情的多维特征，从而提高识别精度。

**技术框架**：FAMNet的整体架构包括一个共享的主干网络Resnet18，以及针对2D和3D特征提取的AMNet2D和AMNet3D模块。模型在训练过程中采用不同的数据加载方式，分别适应两个特定网络，并共同训练微表情识别和面部动作单元检测任务。

**关键创新**：FAMNet的主要创新在于通过参数硬共享实现信息关联，增强了微表情识别任务的效果，这一设计与传统方法的特征提取方式有本质区别。

**关键设计**：模型采用了共享的Resnet18作为主干网络，结合了注意力模块以提升特征提取的有效性，损失函数设计上采用了适应性策略，以优化多任务学习的效果。

## 📊 实验亮点

FAMNet在多个数据集上表现出色，特别是在SAMM、CASME II和MMEW数据集上，分别达到了83.75%（UAR）和84.03%（UF1）的识别率。此外，在具有挑战性的CAS(ME)$^3$数据集上，FAMNet也取得了51%（UAR）和43.42%（UF1）的成绩，显示出其优越的性能。

## 🎯 应用场景

该研究在情感计算、心理学研究及人机交互等领域具有广泛的应用潜力。通过提高微表情识别的准确性，FAMNet可以帮助改善情感分析、欺诈检测及安全监控等实际应用，未来可能推动相关技术的进一步发展与应用。

## 📄 摘要（原文）

> Micro-expressions recognition (MER) has essential application value in many fields, but the short duration and low intensity of micro-expressions (MEs) bring considerable challenges to MER. The current MER methods in deep learning mainly include three data loading methods: static images, dynamic image sequence, and a combination of the two streams. How to effectively extract MEs' fine-grained and spatiotemporal features has been difficult to solve. This paper proposes a new MER method based on multi-task learning and hierarchical attention, which fully extracts MEs' omni-directional features by merging 2D and 3D CNNs. The fusion model consists of a 2D CNN AMNet2D and a 3D CNN AMNet3D, with similar structures consisting of a shared backbone network Resnet18 and attention modules. During training, the model adopts different data loading methods to adapt to two specific networks respectively, jointly trains on the tasks of MER and facial action unit detection (FAUD), and adopts the parameter hard sharing for information association, which further improves the effect of the MER task, and the final fused model is called FAMNet. Extensive experimental results show that our proposed FAMNet significantly improves task performance. On the SAMM, CASME II and MMEW datasets, FAMNet achieves 83.75% (UAR) and 84.03% (UF1). Furthermore, on the challenging CAS(ME)$^3$ dataset, FAMNet achieves 51% (UAR) and 43.42% (UF1).

