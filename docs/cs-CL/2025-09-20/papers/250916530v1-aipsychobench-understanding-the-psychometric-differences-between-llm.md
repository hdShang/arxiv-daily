---
layout: default
title: "AIPsychoBench: Understanding the Psychometric Differences between LLMs and Humans"
---

# AIPsychoBench: Understanding the Psychometric Differences between LLMs and Humans

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16530" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16530v1</a>
  <a href="https://arxiv.org/pdf/2509.16530.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16530v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16530v1', 'AIPsychoBench: Understanding the Psychometric Differences between LLMs and Humans')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei Xie, Shuoyoucheng Ma, Zhenhua Wang, Enze Wang, Kai Chen, Xiaobing Sun, Baosheng Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-20

**备注**: Thank you for your attention. This paper was accepted by the CogSci 2025 conference in April and published in August. The location in the proceedings is: https://escholarship.org/uc/item/39k8f46q

---

## 💡 一句话要点

**AIPsychoBench：构建LLM心理测量基准，揭示其与人类的差异及多语言影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `心理测量` `基准测试` `角色扮演提示` `多语言评估`

## 📋 核心要点

1. 现有方法直接套用人类心理量表评估LLM，忽略了LLM与人类的本质区别，导致评估效果不佳，且缺乏多语言支持。
2. AIPsychoBench通过轻量级角色扮演提示绕过LLM对齐，提高响应率并降低偏差，从而更有效地评估LLM的心理属性。
3. 实验表明，AIPsychoBench显著提高了LLM的响应率，降低了偏差，并揭示了语言对LLM心理测量属性的显著影响。

## 📝 摘要（中文）

大规模语言模型（LLMs）通过学习海量互联网数据展现出类似人类的智能。然而，大型神经网络的不可解释性引发了对LLM可靠性的担忧。现有研究试图通过借鉴人类心理学的概念来评估LLM的心理测量属性，以增强其可解释性，但未能充分考虑LLM与人类之间的根本差异，导致直接重用人类量表时拒绝率很高，且不支持测量LLM在不同语言中的心理属性变化。本文提出了AIPsychoBench，这是一个专门为评估LLM心理属性而定制的基准。它使用轻量级的角色扮演提示来绕过LLM对齐，将平均有效响应率从70.12%提高到90.40%。同时，平均偏差仅为3.3%（正向）和2.1%（负向），远低于传统越狱提示导致的9.8%和6.9%的偏差。此外，在总共112个心理测量子类别中，七种语言相对于英语的分数偏差在43个子类别中为5%到20.2%，首次提供了语言对LLM心理测量影响的全面证据。

## 🔬 方法详解

**问题定义**：现有方法在评估大型语言模型（LLM）的心理测量属性时，主要面临两个痛点：一是直接沿用人类的心理测量量表，忽略了LLM与人类在认知和行为方式上的根本差异，导致评估结果的有效性降低；二是缺乏对LLM在不同语言环境下心理属性差异的有效测量手段，限制了对LLM跨语言行为的理解。

**核心思路**：本文的核心思路是构建一个专门针对LLM的心理测量基准AIPsychoBench。该基准通过设计轻量级的角色扮演提示，引导LLM进入特定的心理状态，从而绕过LLM的对齐机制，提高其响应率和评估的准确性。同时，AIPsychoBench支持多语言评估，能够捕捉LLM在不同语言环境下的心理属性差异。

**技术框架**：AIPsychoBench的整体框架包括以下几个主要模块：1) 心理测量量表构建模块：选择或设计适合LLM特点的心理测量量表；2) 角色扮演提示生成模块：生成轻量级的角色扮演提示，引导LLM进入特定的心理状态；3) LLM响应生成模块：利用角色扮演提示，引导LLM生成相应的响应；4) 心理属性评估模块：根据LLM的响应，评估其心理属性；5) 多语言支持模块：将心理测量量表和角色扮演提示翻译成多种语言，支持LLM在不同语言环境下的评估。

**关键创新**：AIPsychoBench最重要的技术创新点在于其轻量级的角色扮演提示设计。与传统的越狱提示相比，该方法能够更有效地绕过LLM的对齐机制，提高响应率并降低偏差。此外，AIPsychoBench首次提供了对LLM多语言心理属性差异的全面评估，为理解LLM的跨语言行为提供了重要依据。

**关键设计**：AIPsychoBench的关键设计包括：1) 角色扮演提示的轻量化设计，避免触发LLM的防御机制；2) 心理测量量表的选择，确保其能够有效评估LLM的心理属性；3) 多语言翻译的质量控制，保证不同语言版本的一致性；4) 偏差评估指标的设计，用于评估角色扮演提示对LLM行为的影响。

## 📊 实验亮点

AIPsychoBench通过轻量级角色扮演提示，将LLM的平均有效响应率从70.12%提高到90.40%，同时将平均偏差降低到3.3%（正向）和2.1%（负向），远低于传统越狱提示的9.8%和6.9%。此外，研究发现，在112个心理测量子类别中，七种语言相对于英语的分数偏差在43个子类别中为5%到20.2%，揭示了语言对LLM心理测量属性的显著影响。

## 🎯 应用场景

AIPsychoBench的研究成果可应用于多个领域。例如，可以用于评估不同LLM的心理属性，从而选择更适合特定任务的模型。此外，该基准还可以用于研究LLM的偏见和价值观，从而开发更安全、更可靠的LLM。未来，AIPsychoBench有望成为LLM心理学研究的重要工具，促进我们对LLM智能的深入理解。

## 📄 摘要（原文）

> Large Language Models (LLMs) with hundreds of billions of parameters have exhibited human-like intelligence by learning from vast amounts of internet-scale data. However, the uninterpretability of large-scale neural networks raises concerns about the reliability of LLM. Studies have attempted to assess the psychometric properties of LLMs by borrowing concepts from human psychology to enhance their interpretability, but they fail to account for the fundamental differences between LLMs and humans. This results in high rejection rates when human scales are reused directly. Furthermore, these scales do not support the measurement of LLM psychological property variations in different languages. This paper introduces AIPsychoBench, a specialized benchmark tailored to assess the psychological properties of LLM. It uses a lightweight role-playing prompt to bypass LLM alignment, improving the average effective response rate from 70.12% to 90.40%. Meanwhile, the average biases are only 3.3% (positive) and 2.1% (negative), which are significantly lower than the biases of 9.8% and 6.9%, respectively, caused by traditional jailbreak prompts. Furthermore, among the total of 112 psychometric subcategories, the score deviations for seven languages compared to English ranged from 5% to 20.2% in 43 subcategories, providing the first comprehensive evidence of the linguistic impact on the psychometrics of LLM.

