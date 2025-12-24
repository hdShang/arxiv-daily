---
layout: default
title: "FusionNet: Physics-Aware Representation Learning for Multi-Spectral and Thermal Data via Trainable Signal-Processing Priors"
---

# FusionNet: Physics-Aware Representation Learning for Multi-Spectral and Thermal Data via Trainable Signal-Processing Priors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19504" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19504v1</a>
  <a href="https://arxiv.org/pdf/2512.19504.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19504v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19504v1', 'FusionNet: Physics-Aware Representation Learning for Multi-Spectral and Thermal Data via Trainable Signal-Processing Priors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Georgios Voulgaris

**分类**: cs.CV

**发布日期**: 2025-12-22

**备注**: Preprint. Under review at IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing (JSTARS)

---

## 💡 一句话要点

**FusionNet：通过可训练信号处理先验实现多光谱与热数据的物理感知表征学习**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多光谱数据融合` `物理感知学习` `深度学习` `信号处理` `热红外` `短波红外` `表征学习`

## 📋 核心要点

1. 现有深度学习模型在多模态视觉信号处理中，缺乏与物理过程对齐的归纳偏置，导致性能在跨光谱和真实场景下表现不佳。
2. 论文提出FusionNet，一种物理感知表征学习框架，通过可训练的信号处理先验，融合短波红外和热红外数据，建模长期物理过程的稳定特征。
3. 实验结果表明，FusionNet在多光谱数据处理上优于现有方法，且ImageNet预训练反而会降低热红外性能，强调了模态感知训练的重要性。

## 📝 摘要（中文）

现代深度学习模型在处理多模态视觉信号时，常常依赖于与信号形成相关的物理过程不一致的归纳偏置，导致在跨光谱和真实世界条件下性能不稳定。特别是，优先考虑直接热线索的方法难以捕捉由持续热排放引起的间接但持久的环境变化。本文提出了一种物理感知表征学习框架，该框架利用多光谱信息来建模长期物理过程的稳定特征。具体而言，将对土壤性质变化敏感的地质短波红外（SWIR）比率与热红外（TIR）数据通过中间融合架构（FusionNet）集成。所提出的骨干网络在卷积层中嵌入可训练的微分信号处理先验，结合混合池化策略，并采用更宽的感受野，以增强跨光谱模态的鲁棒性。系统消融实验表明，每个架构组件都有助于性能提升，DGCNN在SWIR比率上实现了88.7%的准确率，FusionNet达到了90.6%，优于五种光谱配置下的最先进基线。迁移学习实验进一步表明，ImageNet预训练会降低TIR性能，突出了模态感知训练对于跨光谱学习的重要性。在真实世界数据上的评估结果表明，将物理感知特征选择与有原则的深度学习架构相结合，可以产生鲁棒且可泛化的表征，说明了第一性原理信号建模如何改善具有挑战性条件下的多光谱学习。

## 🔬 方法详解

**问题定义**：论文旨在解决多光谱和热数据融合中，现有深度学习模型缺乏物理感知能力，导致在真实场景和跨光谱条件下性能不佳的问题。现有方法通常直接处理热数据，忽略了由长期热排放引起的间接环境变化，并且缺乏对不同光谱模态之间物理关系的有效建模。

**核心思路**：论文的核心思路是引入物理感知的先验知识，通过可训练的信号处理模块，将短波红外（SWIR）和热红外（TIR）数据进行融合，从而更好地捕捉长期物理过程的稳定特征。这种方法旨在克服现有方法对直接热线索的过度依赖，并提高模型在复杂环境下的鲁棒性和泛化能力。

**技术框架**：FusionNet的整体架构包含以下几个主要模块：1) 输入层：接收SWIR和TIR数据；2) 可训练的微分信号处理层：嵌入在卷积层中，用于提取物理相关的特征；3) 混合池化层：结合不同类型的池化操作，增强特征的鲁棒性；4) 宽感受野卷积层：用于捕捉更大范围的上下文信息；5) 融合层：将SWIR和TIR特征进行融合；6) 输出层：输出最终的预测结果。

**关键创新**：论文最重要的技术创新点在于引入了可训练的微分信号处理先验，并将其嵌入到卷积层中。这种方法允许模型学习与物理过程相关的特征，从而更好地理解多光谱数据。与现有方法相比，FusionNet更加注重对物理过程的建模，而不是仅仅依赖于数据驱动的学习。

**关键设计**：在网络结构方面，FusionNet采用了混合池化策略，结合了最大池化和平均池化，以增强特征的鲁棒性。此外，网络还使用了更宽的感受野，以便捕捉更大范围的上下文信息。在训练方面，论文强调了模态感知训练的重要性，避免使用ImageNet等通用数据集进行预训练，而是针对多光谱数据进行专门的训练。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19504v1/Figures/CementChip.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19504v1/Figures/DataChips.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19504v1/Figures/DeepFusionModel_3.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，FusionNet在SWIR比率预测任务中达到了90.6%的准确率，优于DGCNN（88.7%）和其他基线方法。消融实验证明了每个架构组件对性能提升的贡献。此外，迁移学习实验表明，ImageNet预训练会降低TIR性能，突出了模态感知训练的重要性。在真实世界数据上的评估结果验证了FusionNet的鲁棒性和泛化能力。

## 🎯 应用场景

该研究成果可应用于遥感图像分析、地质勘探、环境监测、火灾检测等领域。通过结合物理感知的深度学习模型，可以更准确地识别和分析地表特征，为资源管理、灾害预警和环境保护提供更可靠的信息支持。未来，该方法有望扩展到其他多模态数据融合任务中，例如医学图像分析和自动驾驶。

## 📄 摘要（原文）

> Modern deep learning models operating on multi-modal visual signals often rely on inductive biases that are poorly aligned with the physical processes governing signal formation, leading to brittle performance under cross-spectral and real-world conditions. In particular, approaches that prioritise direct thermal cues struggle to capture indirect yet persistent environmental alterations induced by sustained heat emissions.
>   This work introduces a physics-aware representation learning framework that leverages multi-spectral information to model stable signatures of long-term physical processes. Specifically, a geological Short Wave Infrared (SWIR) ratio sensitive to soil property changes is integrated with Thermal Infrared (TIR) data through an intermediate fusion architecture, instantiated as FusionNet. The proposed backbone embeds trainable differential signal-processing priors within convolutional layers, combines mixed pooling strategies, and employs wider receptive fields to enhance robustness across spectral modalities.
>   Systematic ablations show that each architectural component contributes to performance gains, with DGCNN achieving 88.7% accuracy on the SWIR ratio and FusionNet reaching 90.6%, outperforming state-of-the-art baselines across five spectral configurations. Transfer learning experiments further show that ImageNet pretraining degrades TIR performance, highlighting the importance of modality-aware training for cross-spectral learning.
>   Evaluated on real-world data, the results demonstrate that combining physics-aware feature selection with principled deep learning architectures yields robust and generalisable representations, illustrating how first-principles signal modelling can improve multi-spectral learning under challenging conditions.

