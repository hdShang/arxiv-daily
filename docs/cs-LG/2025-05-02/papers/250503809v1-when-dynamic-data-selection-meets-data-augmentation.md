---
layout: default
title: When Dynamic Data Selection Meets Data Augmentation
---

# When Dynamic Data Selection Meets Data Augmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03809" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03809v1</a>
  <a href="https://arxiv.org/pdf/2505.03809.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03809v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03809v1', 'When Dynamic Data Selection Meets Data Augmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Suorong Yang, Peng Ye, Furao Shen, Dongzhan Zhou

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-05-02

**期刊**: ICML 2025

---

## 💡 一句话要点

**提出在线数据训练框架以解决动态数据选择与数据增强的协同问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动态数据选择` `数据增强` `在线训练框架` `模型泛化` `抗噪声能力`

## 📋 核心要点

1. 现有动态数据选择方法在加速训练的同时，往往会导致数据多样性不足，从而影响模型的泛化能力。
2. 本文提出了一种新颖的在线数据训练框架，首次将动态数据选择与数据增强相结合，以提升训练效率与模型性能。
3. 实验结果显示，该方法在多个基准数据集上表现优异，例如在ImageNet-1k上实现50%的训练成本降低且性能无损。

## 📝 摘要（中文）

动态数据选择旨在加速训练并保持性能，但减少训练数据会限制数据多样性，影响模型的泛化能力。尽管数据增强广泛应用于提升多样性，但通常未与选择优化结合，导致两者协同效应未能充分发挥。为此，本文首次提出了一种新颖的在线数据训练框架，统一了动态数据选择与增强，实现了训练效率与性能的双重提升。该方法通过估计每个样本的局部密度和多模态语义一致性的联合分布，能够有针对性地选择适合增强的样本，同时抑制噪声或模糊数据的包含，从而在不牺牲模型泛化能力的情况下显著减少数据集规模。实验结果表明，该方法在多个基准数据集和架构上优于现有最先进的方法，例如在ImageNet-1k上减少50%的训练成本而性能不损失。此外，该方法增强了抗噪声能力，提高了模型的鲁棒性，强化了其在实际场景中的应用价值。

## 🔬 方法详解

**问题定义**：本文旨在解决动态数据选择与数据增强之间的协同问题。现有方法在选择数据时，往往忽视了数据增强的优化，导致模型泛化能力不足。

**核心思路**：本文提出的框架通过估计样本的局部密度和多模态语义一致性，选择适合增强的样本，同时抑制噪声数据，从而实现更高效的训练。

**技术框架**：该框架包含数据选择模块和数据增强模块。首先，通过局部密度估计选择样本，然后对选中的样本进行增强处理，最后将增强样本用于模型训练。

**关键创新**：本文的创新在于首次将动态数据选择与数据增强有机结合，形成一个统一的在线训练框架，显著提升了训练效率和模型性能。

**关键设计**：在参数设置上，采用了局部密度和语义一致性作为选择标准，损失函数设计上考虑了增强样本的质量，网络结构则基于现有的深度学习架构进行优化。

## 📊 实验亮点

实验结果表明，本文方法在多个基准数据集上均优于现有最先进的技术。在ImageNet-1k上，成功实现了50%的训练成本降低，同时保持了性能不变，显示出显著的实用价值。此外，该方法在抗噪声能力和模型鲁棒性方面也有显著提升。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在计算机视觉、自然语言处理等领域。通过提高模型的训练效率和鲁棒性，该方法能够在资源受限的环境中实现高效学习，适用于实时系统和大规模数据处理场景。未来，该框架可能推动更多领域的智能应用发展，提升模型在复杂环境下的表现。

## 📄 摘要（原文）

> Dynamic data selection aims to accelerate training with lossless performance. However, reducing training data inherently limits data diversity, potentially hindering generalization. While data augmentation is widely used to enhance diversity, it is typically not optimized in conjunction with selection. As a result, directly combining these techniques fails to fully exploit their synergies. To tackle the challenge, we propose a novel online data training framework that, for the first time, unifies dynamic data selection and augmentation, achieving both training efficiency and enhanced performance. Our method estimates each sample's joint distribution of local density and multimodal semantic consistency, allowing for the targeted selection of augmentation-suitable samples while suppressing the inclusion of noisy or ambiguous data. This enables a more significant reduction in dataset size without sacrificing model generalization. Experimental results demonstrate that our method outperforms existing state-of-the-art approaches on various benchmark datasets and architectures, e.g., reducing 50\% training costs on ImageNet-1k with lossless performance. Furthermore, our approach enhances noise resistance and improves model robustness, reinforcing its practical utility in real-world scenarios.

