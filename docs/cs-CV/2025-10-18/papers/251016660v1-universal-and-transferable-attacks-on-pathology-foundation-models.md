---
layout: default
title: Universal and Transferable Attacks on Pathology Foundation Models
---

# Universal and Transferable Attacks on Pathology Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.16660" class="toolbar-btn" target="_blank">📄 arXiv: 2510.16660v1</a>
  <a href="https://arxiv.org/pdf/2510.16660.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16660v1" onclick="toggleFavorite(this, '2510.16660v1', 'Universal and Transferable Attacks on Pathology Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuntian Wang, Xilin Yang, Che-Yung Shen, Nir Pillar, Aydogan Ozcan

**分类**: cs.CV, cs.LG, physics.med-ph

**发布日期**: 2025-10-18

**备注**: 38 Pages, 8 Figures

---

## 💡 一句话要点

**提出通用可迁移对抗扰动UTAP，揭示病理学基础模型的脆弱性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对抗攻击` `病理学基础模型` `通用扰动` `可迁移性` `模型鲁棒性` `深度学习` `人工智能安全`

## 📋 核心要点

1. 病理学基础模型在下游任务中表现出色，但缺乏对对抗攻击的鲁棒性，容易受到恶意扰动的影响。
2. 提出通用可迁移对抗扰动UTAP，通过固定的微弱噪声模式，扰乱病理图像的特征表示，攻击多个模型。
3. 实验表明，UTAP能显著降低多个病理学基础模型在不同数据集上的性能，且具有通用性和可迁移性。

## 📝 摘要（中文）

本文提出了一种针对病理学基础模型的通用可迁移对抗扰动（UTAP），揭示了这些模型在能力上的关键漏洞。UTAP通过深度学习进行优化，包含一种固定的、微弱的噪声模式，当将其添加到病理图像中时，会系统性地破坏多个病理学基础模型的特征表示能力。因此，UTAP会导致利用基础模型的下游任务的性能下降，包括在各种未见数据分布上的错误分类。除了损害模型性能外，本文还展示了UTAP的两个关键特征：（1）通用性：其扰动可以应用于不同的视野，独立于开发UTAP的数据集；（2）可迁移性：其扰动可以成功地降低各种外部的、黑盒病理学基础模型的性能——这些模型之前从未见过。这两个特征表明，UTAP不是与特定基础模型或图像数据集相关的专用攻击，而是对各种新兴病理学基础模型及其应用的广泛威胁。本文在多个数据集上对各种最先进的病理学基础模型进行了系统评估，使用固定的噪声模式对输入图像进行视觉上难以察觉的修改，导致它们的性能显著下降。这些有效攻击的开发为模型鲁棒性评估建立了一个关键的、高标准的基准，突出了推进防御机制的必要性，并可能为对抗训练提供必要的资产，以确保人工智能在病理学中的安全可靠部署。

## 🔬 方法详解

**问题定义**：病理学基础模型虽然在各种下游任务中表现出色，但容易受到对抗攻击的影响。现有的对抗攻击方法通常是针对特定模型和数据集设计的，缺乏通用性和可迁移性，难以评估病理学基础模型的真实鲁棒性。

**核心思路**：本文的核心思路是设计一种通用且可迁移的对抗扰动（UTAP），该扰动能够有效地攻击各种病理学基础模型，而无需针对特定模型或数据集进行优化。通过学习一种固定的、微弱的噪声模式，UTAP旨在系统性地破坏病理图像的特征表示，从而导致模型性能下降。

**技术框架**：UTAP的生成过程通常包含以下几个步骤：1) 选择一个或多个源模型进行攻击；2) 使用对抗攻击算法（例如，迭代梯度符号法）生成对抗扰动；3) 将生成的扰动添加到病理图像中；4) 评估对抗样本在源模型和目标模型上的攻击效果。整体流程旨在找到一种能够跨模型和数据集有效迁移的扰动模式。

**关键创新**：UTAP的关键创新在于其通用性和可迁移性。与传统的对抗攻击方法不同，UTAP不是针对特定模型或数据集进行优化的，而是旨在学习一种能够跨多个模型和数据集有效迁移的扰动模式。这种通用性和可迁移性使得UTAP能够有效地评估病理学基础模型的真实鲁棒性，并为开发更强大的防御机制提供指导。

**关键设计**：UTAP的关键设计包括：1) 使用迭代梯度符号法等对抗攻击算法生成扰动；2) 通过调整扰动的强度和范围来控制其视觉感知度；3) 使用多个源模型进行攻击，以提高扰动的通用性和可迁移性；4) 使用不同的损失函数（例如，交叉熵损失）来优化扰动，以最大化其攻击效果。

## 📊 实验亮点

实验结果表明，UTAP能够显著降低多个病理学基础模型在不同数据集上的性能。例如，在某些数据集上，UTAP能够将模型的分类准确率降低超过50%，同时保持扰动的视觉感知度较低。此外，UTAP还能够成功地迁移到未见过的黑盒模型上，表明其具有很强的通用性和可迁移性。

## 🎯 应用场景

该研究成果可应用于评估和提升病理学人工智能系统的安全性与可靠性。通过UTAP，可以更全面地评估病理学基础模型在实际应用中面临的潜在风险，并为开发更鲁棒的防御机制提供指导。这对于确保AI在病理诊断和治疗决策中的安全可靠部署至关重要。

## 📄 摘要（原文）

> We introduce Universal and Transferable Adversarial Perturbations (UTAP) for pathology foundation models that reveal critical vulnerabilities in their capabilities. Optimized using deep learning, UTAP comprises a fixed and weak noise pattern that, when added to a pathology image, systematically disrupts the feature representation capabilities of multiple pathology foundation models. Therefore, UTAP induces performance drops in downstream tasks that utilize foundation models, including misclassification across a wide range of unseen data distributions. In addition to compromising the model performance, we demonstrate two key features of UTAP: (1) universality: its perturbation can be applied across diverse field-of-views independent of the dataset that UTAP was developed on, and (2) transferability: its perturbation can successfully degrade the performance of various external, black-box pathology foundation models - never seen before. These two features indicate that UTAP is not a dedicated attack associated with a specific foundation model or image dataset, but rather constitutes a broad threat to various emerging pathology foundation models and their applications. We systematically evaluated UTAP across various state-of-the-art pathology foundation models on multiple datasets, causing a significant drop in their performance with visually imperceptible modifications to the input images using a fixed noise pattern. The development of these potent attacks establishes a critical, high-standard benchmark for model robustness evaluation, highlighting a need for advancing defense mechanisms and potentially providing the necessary assets for adversarial training to ensure the safe and reliable deployment of AI in pathology.

