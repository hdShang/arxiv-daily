---
layout: default
title: "COSMIC: Generalized Refusal Direction Identification in LLM Activations"
---

# COSMIC: Generalized Refusal Direction Identification in LLM Activations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00085" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00085v1</a>
  <a href="https://arxiv.org/pdf/2506.00085.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00085v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00085v1', 'COSMIC: Generalized Refusal Direction Identification in LLM Activations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vincent Siu, Nicholas Crispino, Zihao Yu, Sam Pan, Zhun Wang, Yang Liu, Dawn Song, Chenguang Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-30

**备注**: 9 pages, Accepted to ACL 2025 Findings

---

## 💡 一句话要点

**提出COSMIC框架以自动识别大型语言模型中的拒绝行为**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `拒绝行为识别` `余弦相似性` `自动化框架` `对抗性设置` `安全性引导`

## 📋 核心要点

1. 现有方法在识别大型语言模型中的拒绝行为时，往往依赖于预定义模板或手动分析，效率低下且不够灵活。
2. COSMIC框架通过余弦相似性自动识别拒绝行为的引导方向，避免了对模型输出的依赖，提升了识别的准确性和效率。
3. COSMIC在多种对抗性环境中表现出色，能够有效引导模型向更安全的行为转变，同时保持虚假拒绝的增加在最低水平。

## 📝 摘要（中文）

大型语言模型（LLMs）在其激活空间中编码了拒绝等行为，但识别这些行为仍然是一个重大挑战。现有方法通常依赖于可在输出标记中检测到的预定义拒绝模板或需要手动分析。我们提出了COSMIC（概念反演的余弦相似性度量），这是一个自动化的方向选择框架，利用余弦相似性识别可行的引导方向和目标层，完全独立于模型输出。COSMIC在不需要对模型拒绝行为的假设（如特定拒绝标记的存在）的情况下，达到了与先前方法相当的引导性能。它在对抗性设置和弱对齐模型中可靠地识别拒绝方向，并能够在最小增加虚假拒绝的情况下，引导这些模型朝向更安全的行为，展示了在广泛对齐条件下的鲁棒性。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型中拒绝行为的识别问题。现有方法依赖于特定的输出标记或手动分析，导致识别效率低且灵活性不足。

**核心思路**：COSMIC框架的核心思路是利用余弦相似性度量来自动识别模型的拒绝行为方向，完全独立于模型的输出。这种方法避免了对模型行为的假设，使得识别过程更加普适和高效。

**技术框架**：COSMIC的整体架构包括方向选择和目标层识别两个主要模块。首先，通过计算激活空间中的余弦相似性，识别出潜在的引导方向；然后，选择合适的目标层进行进一步的行为引导。

**关键创新**：COSMIC的主要创新在于其完全独立于模型输出的方向识别能力，能够在没有特定拒绝标记的情况下，可靠地识别拒绝行为。这一特性使其在对抗性环境和弱对齐模型中表现出色。

**关键设计**：在技术细节方面，COSMIC采用了特定的余弦相似性计算方法，并在选择目标层时考虑了模型的激活特征。框架的设计确保了在引导过程中虚假拒绝的增加保持在最低水平。

## 📊 实验亮点

COSMIC在多种对抗性设置中表现出色，能够可靠地识别拒绝方向，并在引导模型向更安全行为的过程中，虚假拒绝的增加保持在最低水平。与现有方法相比，COSMIC的引导性能相当，但不依赖于特定的拒绝标记，展示了其在广泛对齐条件下的鲁棒性。

## 🎯 应用场景

COSMIC框架的潜在应用场景包括安全性敏感的对话系统、自动内容审核和人机交互等领域。通过有效识别和引导拒绝行为，该研究能够提升大型语言模型在实际应用中的安全性和可靠性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) encode behaviors such as refusal within their activation space, yet identifying these behaviors remains a significant challenge. Existing methods often rely on predefined refusal templates detectable in output tokens or require manual analysis. We introduce \textbf{COSMIC} (Cosine Similarity Metrics for Inversion of Concepts), an automated framework for direction selection that identifies viable steering directions and target layers using cosine similarity - entirely independent of model outputs. COSMIC achieves steering performance comparable to prior methods without requiring assumptions about a model's refusal behavior, such as the presence of specific refusal tokens. It reliably identifies refusal directions in adversarial settings and weakly aligned models, and is capable of steering such models toward safer behavior with minimal increase in false refusals, demonstrating robustness across a wide range of alignment conditions.

