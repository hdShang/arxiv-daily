---
layout: default
title: "GUARD: Guided Unlearning and Retention via Data Attribution for Large Language Models"
---

# GUARD: Guided Unlearning and Retention via Data Attribution for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10946" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10946v2</a>
  <a href="https://arxiv.org/pdf/2506.10946.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10946v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10946v2', 'GUARD: Guided Unlearning and Retention via Data Attribution for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peizhi Niu, Evelyn Ma, Huiting Zhou, Duo Zhou, Huan Zhang, S. Rasoul Etesami, Olgica Milenkovic

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-12 (更新: 2025-10-22)

---

## 💡 一句话要点

**提出GUARD框架以解决大语言模型中的非意图遗忘问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `反学习` `数据归因` `大语言模型` `知识保留` `隐私保护` `合规性` `机器学习`

## 📋 核心要点

1. 现有大语言模型的反学习方法常常导致非意图遗忘，影响模型效用和知识保留。
2. GUARD框架通过引入数据归因度量和自适应反学习权重，优化了反学习过程，减少了意外的保留损失。
3. 在TOFU和MUSE基准测试中，GUARD在保留集的效用损失减少了194.92%，知识保留率提高了16.20%。

## 📝 摘要（中文）

在大语言模型中，反学习变得越来越重要，尤其是在合规性、版权保护和隐私问题上。然而，现有方法在反学习过程中常常导致非意图遗忘，即删除特定数据时意外损害模型的效用。为了解决这一问题，本文提出了GUARD框架，通过引入轻量级的数据归因度量，量化遗忘集与保留集之间的对齐程度，并设计了自适应的非均匀反学习权重，从而减轻非意图的保留损失。实验结果表明，GUARD在多个大语言模型架构上显著提高了知识保留率，同时保持了与现有方法相当的遗忘指标。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型反学习中的非意图遗忘问题，现有方法在删除高影响数据时，常常导致模型保留有价值信息的能力下降。

**核心思路**：GUARD框架的核心思想是通过引入轻量级的数据归因度量，量化遗忘集与保留集之间的对齐程度，并根据归因得分为样本分配自适应的反学习权重，从而优化反学习过程。

**技术框架**：GUARD的整体架构包括数据归因度量模块、反学习权重分配模块和反学习目标设计。首先，通过数据归因度量评估样本的重要性，然后根据重要性调整反学习权重，最后优化反学习目标以减少非意图保留损失。

**关键创新**：GUARD的主要创新在于引入了轻量级的代理数据归因度量和自适应的非均匀反学习权重分配机制，这与现有方法的均匀权重分配形成了本质区别。

**关键设计**：在设计中，GUARD使用了代理归因得分来评估样本的重要性，并根据这些得分动态调整反学习权重，确保在遗忘高影响数据时，模型的知识保留能力得到保障。

## 📊 实验亮点

GUARD在TOFU Retain Set上减少了高达194.92%的效用损失，同时在MUSE NEWS Retain Set上提高了16.20%的知识保留率。与现有最先进的方法相比，GUARD在隐私损失方面保持了相对较小的增加，展现了其优越的性能。

## 🎯 应用场景

GUARD框架在大语言模型的反学习中具有广泛的应用潜力，特别是在需要遵循隐私法规和版权保护的场景中。通过优化反学习过程，GUARD能够帮助企业和机构更好地管理数据使用，确保合规性，同时保持模型的性能和知识保留，未来可能在多个领域产生深远影响。

## 📄 摘要（原文）

> Unlearning in large language models is becoming increasingly important due to regulatory compliance, copyright protection, and privacy concerns. However, a key challenge in LLM unlearning is unintended forgetting, where the removal of specific data inadvertently impairs the utility of the model and its retention of valuable, desired information. While prior work has primarily focused on architectural innovations, the influence of data-level factors on unlearning performance remains underexplored. As a result, existing methods often suffer from degraded retention when forgetting high-impact data. To address this problem, we propose GUARD, a novel framework for Guided Unlearning And Retention via Data attribution. At its core, GUARD introduces a lightweight proxy data attribution metric tailored for LLM unlearning, which quantifies the alignment between the Forget and Retain sets while remaining computationally efficient. Building on this, we design a novel unlearning objective that assigns adaptive, nonuniform unlearning weights to samples, inversely proportional to their proxy attribution scores. Through such a reallocation of unlearning power, GUARD mitigates unintended retention loss. We also provide rigorous theoretical guarantees that GUARD significantly improves retention while maintaining forgetting metrics comparable to prior methods. Extensive experiments on the TOFU and MUSE benchmarks across multiple LLM architectures demonstrate that GUARD reduces utility sacrifice on the TOFU Retain Set by up to 194.92 percent in terms of Truth Ratio when forgetting 10 percent of the training data, and improves knowledge retention on the MUSE NEWS Retain Set by 16.20 percent, with comparable or very moderate increases in privacy loss compared to state-of-the-art methods.

