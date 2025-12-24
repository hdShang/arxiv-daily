---
layout: default
title: PhysLLM: Harnessing Large Language Models for Cross-Modal Remote Physiological Sensing
---

# PhysLLM: Harnessing Large Language Models for Cross-Modal Remote Physiological Sensing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03621" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03621v1</a>
  <a href="https://arxiv.org/pdf/2505.03621.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03621v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03621v1', 'PhysLLM: Harnessing Large Language Models for Cross-Modal Remote Physiological Sensing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiping Xie, Bo Zhao, Mingtong Dai, Jian-Ping Zhou, Yue Sun, Tao Tan, Weicheng Xie, Linlin Shen, Zitong Yu

**分类**: cs.CV

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**提出PhysLLM以解决远程生理信号测量中的噪声敏感问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `远程生理监测` `光电容积描记法` `跨模态学习` `大型语言模型` `信号处理` `生理统计` `环境上下文` `动态适应`

## 📋 核心要点

1. 现有的远程生理信号测量方法在光照变化和运动伪影下表现不佳，导致测量结果不稳定。
2. 本文提出PhysLLM，通过将大型语言模型与rPPG组件结合，利用文本原型引导策略实现跨模态对齐。
3. 在四个基准数据集上的实验表明，PhysLLM在准确性和鲁棒性方面优于现有方法，具有更好的泛化能力。

## 📝 摘要（中文）

远程光电容积描记法（rPPG）能够实现非接触式生理测量，但对光照变化、运动伪影和时间建模能力有限。大型语言模型（LLMs）在捕捉长距离依赖方面表现出色，但由于其文本中心设计，难以处理连续且对噪声敏感的rPPG信号。为此，本文提出PhysLLM，一个协同优化框架，将LLMs与特定领域的rPPG组件结合。具体而言，提出了文本原型引导（TPG）策略，通过将血流动力学特征投影到LLM可解释的语义空间中，建立跨模态对齐。此外，提出了一种新颖的双域静态（DDS）算法，通过自适应时频域特征重加权解决信号不稳定性。最后，通过生理统计、环境上下文回答和任务描述，系统性地注入生理先验，利用跨模态学习整合视觉和文本信息，使其能够动态适应光照变化和受试者运动等挑战场景。经过四个基准数据集的评估，PhysLLM在准确性和鲁棒性上达到了最先进的水平，展示了在光照变化和运动场景下的优越泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决远程光电容积描记法（rPPG）在光照变化和运动伪影下的信号不稳定性问题。现有方法在处理连续且对噪声敏感的生理信号时，常常受到限制，导致测量结果的准确性下降。

**核心思路**：论文的核心思路是将大型语言模型（LLMs）与领域特定的rPPG组件结合，通过文本原型引导（TPG）策略实现跨模态对齐，从而有效地将生理信号与语言符号之间的表示差距缩小。

**技术框架**：整体架构包括三个主要模块：首先，通过TPG策略将血流动力学特征映射到LLM可解释的语义空间；其次，采用双域静态（DDS）算法进行信号的不稳定性处理；最后，通过任务特定的线索注入生理先验信息，整合视觉和文本信息。

**关键创新**：最重要的技术创新在于TPG策略和DDS算法的结合，前者实现了跨模态对齐，后者则通过自适应特征重加权解决了信号的不稳定性。这与现有方法的本质区别在于，PhysLLM能够动态适应复杂环境下的生理信号变化。

**关键设计**：在参数设置上，采用了自适应时频域特征重加权策略，损失函数设计考虑了生理统计和环境上下文的影响，网络结构则结合了LLMs与rPPG特征提取模块，确保了信息的有效融合。

## 📊 实验亮点

在四个基准数据集上的实验结果显示，PhysLLM在准确性和鲁棒性方面达到了最先进的水平，尤其在光照变化和运动场景下的泛化能力显著提升，具体性能数据未详述，但整体表现优于现有方法。

## 🎯 应用场景

该研究的潜在应用领域包括医疗监测、运动健康管理和远程生理数据采集等。通过提高rPPG信号的准确性和鲁棒性，PhysLLM能够在多种复杂环境下实现可靠的生理监测，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Remote photoplethysmography (rPPG) enables non-contact physiological measurement but remains highly susceptible to illumination changes, motion artifacts, and limited temporal modeling. Large Language Models (LLMs) excel at capturing long-range dependencies, offering a potential solution but struggle with the continuous, noise-sensitive nature of rPPG signals due to their text-centric design. To bridge this gap, we introduce PhysLLM, a collaborative optimization framework that synergizes LLMs with domain-specific rPPG components. Specifically, the Text Prototype Guidance (TPG) strategy is proposed to establish cross-modal alignment by projecting hemodynamic features into LLM-interpretable semantic space, effectively bridging the representational gap between physiological signals and linguistic tokens. Besides, a novel Dual-Domain Stationary (DDS) Algorithm is proposed for resolving signal instability through adaptive time-frequency domain feature re-weighting. Finally, rPPG task-specific cues systematically inject physiological priors through physiological statistics, environmental contextual answering, and task description, leveraging cross-modal learning to integrate both visual and textual information, enabling dynamic adaptation to challenging scenarios like variable illumination and subject movements. Evaluation on four benchmark datasets, PhysLLM achieves state-of-the-art accuracy and robustness, demonstrating superior generalization across lighting variations and motion scenarios.

