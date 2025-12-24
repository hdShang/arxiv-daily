---
layout: default
title: "IsoNet: Causal Analysis of Multimodal Transformers for Neuromuscular Gesture Classification"
---

# IsoNet: Causal Analysis of Multimodal Transformers for Neuromuscular Gesture Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16744" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16744v1</a>
  <a href="https://arxiv.org/pdf/2506.16744.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16744v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16744v1', 'IsoNet: Causal Analysis of Multimodal Transformers for Neuromuscular Gesture Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eion Tyacke, Kunal Gupta, Jay Patel, Rui Li

**分类**: cs.LG, cs.RO, eess.SP

**发布日期**: 2025-06-20

---

## 💡 一句话要点

**提出IsoNet以解决多模态手势分类中的信息融合问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态融合` `手势分类` `神经肌肉信号` `层次Transformer` `注意力机制` `隔离网络` `生物信号处理`

## 📋 核心要点

1. 现有方法通常依赖单一生物信号模态，导致信息利用不足，影响手势分类的准确性。
2. 本文提出了一种层次Transformer架构，结合注意力机制进行多模态信息融合，以提高分类性能。
3. 实验结果显示，层次Transformer在两个数据集上的准确率显著高于传统方法，验证了多模态融合的有效性。

## 📝 摘要（中文）

手势是人类运动系统的主要输出，但解码其神经肌肉特征仍是基础神经科学和辅助技术（如假肢）的瓶颈。传统的人机接口依赖单一生物信号模态，而多模态融合可以利用传感器的互补信息。本文系统比较了线性和基于注意力的融合策略，评估了多模态MLP、多模态Transformer和层次Transformer在单模态和多模态输入场景下的表现。实验使用了两个公开数据集：NinaPro DB2（sEMG和加速度计）和HD-sEMG 65-Gesture（高密度sEMG和力）。结果表明，层次Transformer与基于注意力的融合策略在两个数据集上均表现最佳，准确率超过基线10%以上。通过引入隔离网络，定量分析了模态间交互对决策的贡献，发现跨模态交互约占决策信号的30%。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态手势分类中信息融合不足的问题。现有方法多依赖单一模态，导致对手势的解码能力有限，影响了神经肌肉信号的分类准确性。

**核心思路**：论文提出了一种层次Transformer架构，结合注意力机制进行多模态信息融合，旨在充分利用不同模态间的互补信息，从而提升分类性能。

**技术框架**：整体架构包括三个主要模块：多模态MLP、多模态Transformer和层次Transformer。每个模块都采用不同的融合策略，比较其在单模态和多模态输入下的表现。

**关键创新**：最重要的技术创新是引入了隔离网络，能够选择性地静音单模态或跨模态的注意力通道，从而量化不同模态交互对决策的贡献。这一机制与传统的融合方法本质上不同，强调了注意力驱动的融合在信息利用上的重要性。

**关键设计**：在网络设计中，采用了层次结构和注意力机制，关键参数设置包括注意力头数和层数。损失函数采用交叉熵损失，以优化分类性能。

## 📊 实验亮点

实验结果显示，层次Transformer与注意力融合策略在NinaPro DB2数据集上准确率提高超过10%，在HD-sEMG数据集上提高3.7%。跨模态交互对决策信号的贡献约为30%，强调了多模态融合的重要性。

## 🎯 应用场景

该研究在神经机器人系统的传感器阵列设计中具有潜在应用价值，能够提升假肢等辅助设备的控制精度和响应速度。通过更好地解码神经肌肉信号，未来可能改善人机交互体验，推动相关技术的发展。

## 📄 摘要（原文）

> Hand gestures are a primary output of the human motor system, yet the decoding of their neuromuscular signatures remains a bottleneck for basic neuroscience and assistive technologies such as prosthetics. Traditional human-machine interface pipelines rely on a single biosignal modality, but multimodal fusion can exploit complementary information from sensors. We systematically compare linear and attention-based fusion strategies across three architectures: a Multimodal MLP, a Multimodal Transformer, and a Hierarchical Transformer, evaluating performance on scenarios with unimodal and multimodal inputs. Experiments use two publicly available datasets: NinaPro DB2 (sEMG and accelerometer) and HD-sEMG 65-Gesture (high-density sEMG and force). Across both datasets, the Hierarchical Transformer with attention-based fusion consistently achieved the highest accuracy, surpassing the multimodal and best single-modality linear-fusion MLP baseline by over 10% on NinaPro DB2 and 3.7% on HD-sEMG. To investigate how modalities interact, we introduce an Isolation Network that selectively silences unimodal or cross-modal attention pathways, quantifying each group of token interactions' contribution to downstream decisions. Ablations reveal that cross-modal interactions contribute approximately 30% of the decision signal across transformer layers, highlighting the importance of attention-driven fusion in harnessing complementary modality information. Together, these findings reveal when and how multimodal fusion would enhance biosignal classification and also provides mechanistic insights of human muscle activities. The study would be beneficial in the design of sensor arrays for neurorobotic systems.

