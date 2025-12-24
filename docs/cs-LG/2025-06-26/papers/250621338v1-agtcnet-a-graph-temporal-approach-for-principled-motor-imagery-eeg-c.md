---
layout: default
title: "AGTCNet: A Graph-Temporal Approach for Principled Motor Imagery EEG Classification"
---

# AGTCNet: A Graph-Temporal Approach for Principled Motor Imagery EEG Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21338" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21338v1</a>
  <a href="https://arxiv.org/pdf/2506.21338.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21338v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21338v1', 'AGTCNet: A Graph-Temporal Approach for Principled Motor Imagery EEG Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Galvin Brice S. Lim, Brian Godwin S. Lim, Argel A. Bandala, John Anthony C. Jose, Timothy Scott C. Chu, Edwin Sybingco

**分类**: cs.LG, cs.HC

**发布日期**: 2025-06-26

**备注**: This work has been submitted to the IEEE for possible publication

**期刊**: IEEE Access. 13(2025) 187383-187409

**DOI**: [10.1109/ACCESS.2025.3627419](https://doi.org/10.1109/ACCESS.2025.3627419)

---

## 💡 一句话要点

**提出AGTCNet以解决脑机接口EEG分类中的时空依赖问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `脑机接口` `EEG分类` `图卷积网络` `时空特征` `运动想象` `深度学习` `注意力机制`

## 📋 核心要点

1. 现有的脑机接口EEG分类方法未能有效捕捉多通道信号中的复杂时空依赖性，导致分类性能不足。
2. AGTCNet通过引入图卷积注意网络，利用EEG电极的拓扑结构来学习时空特征，从而提高分类准确性。
3. AGTCNet在多个数据集上表现优异，主体独立分类准确率达66.82%，并在微调后提升至82.88%，显示出显著的性能提升。

## 📝 摘要（中文）

脑机接口（BCI）技术利用脑电图（EEG）为运动障碍者提供了与环境互动的机会。然而，由于个体间和时间上的神经活动复杂性，开发具有主体不变性和会话不变性的BCI系统仍然面临重大挑战。现有方法未能有效捕捉多通道EEG信号中的复杂时空依赖性。本研究提出了一种新的图-时间卷积网络（AGTCNet），通过利用EEG电极的拓扑配置作为归纳偏置，并结合图卷积注意网络（GCAT）共同学习表达性时空EEG表示。AGTCNet在BCI Competition IV Dataset 2a上实现了66.82%的主体独立分类准确率，并在微调后提升至82.88%。在EEG运动运动/想象数据集上，AGTCNet分别在4类和2类主体独立分类中达到了64.14%和85.22%的准确率，进一步提升至72.13%和90.54%进行主体特定分类。

## 🔬 方法详解

**问题定义**：本研究旨在解决脑机接口EEG分类中存在的主体不变性和会话不变性问题。现有方法未能有效捕捉EEG信号中的复杂时空依赖性，导致分类性能不足。

**核心思路**：AGTCNet通过结合图卷积注意网络（GCAT）与EEG电极的拓扑结构，旨在共同学习EEG信号的时空特征，从而提高分类的准确性和鲁棒性。

**技术框架**：AGTCNet的整体架构包括输入层、图卷积层、注意力机制层和输出层。输入层接收EEG信号，图卷积层提取时空特征，注意力机制层增强重要特征，最终输出分类结果。

**关键创新**：AGTCNet的主要创新在于引入了图卷积注意网络，能够有效捕捉EEG信号中的复杂时空依赖性，与传统方法相比，显著提升了分类性能。

**关键设计**：模型在设计上采用了紧凑的架构，减少了49.87%的模型大小，并优化了推理时间，提升了64.65%。损失函数和网络结构经过精心设计，以确保模型的高效性和准确性。

## 📊 实验亮点

AGTCNet在BCI Competition IV Dataset 2a上实现了66.82%的主体独立分类准确率，并在微调后提升至82.88%。在EEG运动运动/想象数据集上，AGTCNet在4类和2类主体独立分类中分别达到了64.14%和85.22%的准确率，进一步提升至72.13%和90.54%进行主体特定分类，显示出显著的性能提升。

## 🎯 应用场景

该研究的成果在脑机接口技术中具有广泛的应用潜力，能够帮助运动障碍者更好地与环境互动。AGTCNet的高效性和准确性使其在医疗康复、智能家居控制等领域具有实际价值，未来可能推动BCI技术的普及与发展。

## 📄 摘要（原文）

> Brain-computer interface (BCI) technology utilizing electroencephalography (EEG) marks a transformative innovation, empowering motor-impaired individuals to engage with their environment on equal footing. Despite its promising potential, developing subject-invariant and session-invariant BCI systems remains a significant challenge due to the inherent complexity and variability of neural activity across individuals and over time, compounded by EEG hardware constraints. While prior studies have sought to develop robust BCI systems, existing approaches remain ineffective in capturing the intricate spatiotemporal dependencies within multichannel EEG signals. This study addresses this gap by introducing the attentive graph-temporal convolutional network (AGTCNet), a novel graph-temporal model for motor imagery EEG (MI-EEG) classification. Specifically, AGTCNet leverages the topographic configuration of EEG electrodes as an inductive bias and integrates graph convolutional attention network (GCAT) to jointly learn expressive spatiotemporal EEG representations. The proposed model significantly outperformed existing MI-EEG classifiers, achieving state-of-the-art performance while utilizing a compact architecture, underscoring its effectiveness and practicality for BCI deployment. With a 49.87% reduction in model size, 64.65% faster inference time, and shorter input EEG signal, AGTCNet achieved a moving average accuracy of 66.82% for subject-independent classification on the BCI Competition IV Dataset 2a, which further improved to 82.88% when fine-tuned for subject-specific classification. On the EEG Motor Movement/Imagery Dataset, AGTCNet achieved moving average accuracies of 64.14% and 85.22% for 4-class and 2-class subject-independent classifications, respectively, with further improvements to 72.13% and 90.54% for subject-specific classifications.

