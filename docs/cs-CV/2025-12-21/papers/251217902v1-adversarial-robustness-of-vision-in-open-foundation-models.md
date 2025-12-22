---
layout: default
title: Adversarial Robustness of Vision in Open Foundation Models
---

# Adversarial Robustness of Vision in Open Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17902" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17902v1</a>
  <a href="https://arxiv.org/pdf/2512.17902.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17902v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17902v1', 'Adversarial Robustness of Vision in Open Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jonathon Fox, William J Buchanan, Pavlos Papadopoulos

**分类**: cs.CV, cs.AI, cs.CR

**发布日期**: 2025-12-19

**期刊**: IEEE Access, 2025

**DOI**: [10.1109/ACCESS.2025.3645997](https://doi.org/10.1109/ACCESS.2025.3645997)

---

## 💡 一句话要点

**研究揭示开放视觉基础模型在对抗攻击下的脆弱性，并发现鲁棒性与基准性能不直接相关。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对抗攻击` `视觉基础模型` `鲁棒性评估` `PGD攻击` `VQA` `LLaVA` `Llama 3.2 Vision`

## 📋 核心要点

1. 现有视觉模型易受对抗攻击影响，攻击者通过微小扰动即可降低模型性能，但模型内在脆弱性尚不明确。
2. 本文通过对抗攻击评估LLaVA-1.5-13B和Llama 3.2 Vision-8B-2的鲁棒性，分析模型在视觉模态下的脆弱程度。
3. 实验表明，Llama 3.2 Vision在基线性能较低的情况下，对抗攻击下的性能下降幅度小于LLaVA，揭示鲁棒性与基准性能的非直接相关性。

## 📝 摘要（中文）

随着深度学习的普及，理解AI系统识别物体的内在机制变得日益困难。因此，攻击者可以通过添加未见过的元素来修改图像，从而混淆AI对实体的识别。本文研究了LLaVA-1.5-13B和Meta的Llama 3.2 Vision-8B-2的对抗鲁棒性。使用PGD（Projected Gradient Descent）方法对视觉输入模态进行非目标攻击，并在Visual Question Answering (VQA) v2数据集的子集上进行实证评估。使用标准的VQA准确率指标量化对抗攻击的结果。然后将此评估与LLaVA和Llama 3.2 Vision的准确率下降（accuracy drop）进行比较。一个关键发现是，尽管Llama 3.2 Vision在这种设置下的基线准确率较低，但在攻击下的性能下降幅度小于LLaVA，尤其是在较高的扰动水平下。总体而言，研究结果证实，视觉模态是降低当代开放权重VLM（包括Meta的Llama 3.2 Vision）性能的可行攻击向量。此外，它们强调对抗鲁棒性不一定与标准基准性能直接相关，并且可能受到底层架构和训练因素的影响。

## 🔬 方法详解

**问题定义**：论文旨在研究开放视觉基础模型在对抗攻击下的鲁棒性。现有方法虽然在标准数据集上表现良好，但容易受到对抗样本的攻击，即通过对输入图像进行微小但精心设计的扰动，导致模型产生错误的预测。现有方法的痛点在于缺乏对模型内在脆弱性的深入理解，以及对抗鲁棒性与标准性能之间的关系。

**核心思路**：论文的核心思路是通过对抗攻击来评估模型的鲁棒性，并分析模型在不同扰动程度下的性能下降情况。通过比较不同模型的性能下降幅度，可以了解模型对对抗攻击的敏感程度，并揭示对抗鲁棒性与标准性能之间的关系。这种方法可以帮助我们更好地理解模型的内在脆弱性，并为提高模型的鲁棒性提供指导。

**技术框架**：论文的技术框架主要包括以下几个步骤：1) 选择两个开放视觉基础模型：LLaVA-1.5-13B和Meta的Llama 3.2 Vision-8B-2；2) 使用PGD（Projected Gradient Descent）方法生成对抗样本，对视觉输入模态进行非目标攻击；3) 在Visual Question Answering (VQA) v2数据集的子集上进行实验评估；4) 使用标准的VQA准确率指标量化对抗攻击的结果；5) 比较不同模型在对抗攻击下的性能下降幅度。

**关键创新**：论文的关键创新在于揭示了对抗鲁棒性与标准基准性能之间的非直接相关性。实验结果表明，即使一个模型在标准数据集上表现良好，它也可能在对抗攻击下表现不佳。这表明，对抗鲁棒性是一个独立于标准性能的指标，需要单独进行评估和优化。此外，论文还发现，不同的模型在对抗攻击下的表现差异很大，这表明模型的架构和训练方式对抗鲁棒性有重要影响。

**关键设计**：论文的关键设计包括：1) 使用PGD方法生成对抗样本，该方法是一种常用的对抗攻击方法，可以有效地生成能够欺骗模型的对抗样本；2) 在VQA v2数据集上进行实验评估，该数据集是一个常用的视觉问答数据集，可以有效地评估模型在视觉理解方面的能力；3) 使用标准的VQA准确率指标量化对抗攻击的结果，该指标可以有效地衡量模型在对抗攻击下的性能下降情况。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17902v1/figs/transformer.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17902v1/figs/panda_original.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17902v1/figs/pertubation.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Llama 3.2 Vision虽然基线VQA准确率低于LLaVA，但在PGD对抗攻击下，性能下降幅度明显小于LLaVA，尤其是在高扰动水平下。这表明Llama 3.2 Vision在一定程度上更具对抗鲁棒性，同时也揭示了标准基准性能与对抗鲁棒性之间可能存在负相关关系。

## 🎯 应用场景

该研究成果可应用于提升视觉模型的安全性与可靠性，例如在自动驾驶、医疗影像诊断等安全攸关领域，增强模型抵御恶意攻击的能力，避免因对抗样本导致的误判。此外，该研究有助于开发更鲁棒的视觉模型训练方法，提高模型在真实世界复杂环境中的泛化能力。

## 📄 摘要（原文）

> With the increase in deep learning, it becomes increasingly difficult to understand the model in which AI systems can identify objects. Thus, an adversary could aim to modify an image by adding unseen elements, which will confuse the AI in its recognition of an entity. This paper thus investigates the adversarial robustness of LLaVA-1.5-13B and Meta's Llama 3.2 Vision-8B-2. These are tested for untargeted PGD (Projected Gradient Descent) against the visual input modality, and empirically evaluated on the Visual Question Answering (VQA) v2 dataset subset. The results of these adversarial attacks are then quantified using the standard VQA accuracy metric. This evaluation is then compared with the accuracy degradation (accuracy drop) of LLaVA and Llama 3.2 Vision. A key finding is that Llama 3.2 Vision, despite a lower baseline accuracy in this setup, exhibited a smaller drop in performance under attack compared to LLaVA, particularly at higher perturbation levels. Overall, the findings confirm that the vision modality represents a viable attack vector for degrading the performance of contemporary open-weight VLMs, including Meta's Llama 3.2 Vision. Furthermore, they highlight that adversarial robustness does not necessarily correlate directly with standard benchmark performance and may be influenced by underlying architectural and training factors.

