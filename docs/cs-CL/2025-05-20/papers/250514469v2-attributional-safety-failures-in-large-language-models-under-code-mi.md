---
layout: default
title: Attributional Safety Failures in Large Language Models under Code-Mixed Perturbations
---

# Attributional Safety Failures in Large Language Models under Code-Mixed Perturbations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14469" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14469v2</a>
  <a href="https://arxiv.org/pdf/2505.14469.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14469v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14469v2', 'Attributional Safety Failures in Large Language Models under Code-Mixed Perturbations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Somnath Banerjee, Pratyush Chatterjee, Shanu Kumar, Sayan Layek, Parag Agrawal, Rima Hazra, Animesh Mukherjee

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-20 (更新: 2025-11-30)

---

## 💡 一句话要点

**提出SDA框架以解决代码混合下LLM的安全性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `安全性` `代码混合` `显著性漂移归因` `多语言处理` `内容审核` `社交媒体` `人工智能安全`

## 📋 核心要点

1. 现有大型语言模型在多语言环境下的安全性表现不佳，尤其在代码混合情况下，安全防护机制失效。
2. 论文提出了显著性漂移归因（SDA）框架，旨在揭示模型在代码混合输入下的注意力分布变化，从而改善安全性。
3. 实验结果表明，采用翻译恢复策略后，模型的安全性恢复率可达80%，显著提高了在代码混合环境下的安全性表现。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）在英语中表现出较强的安全性，但我们发现其在代码混合扰动下存在严重的安全漏洞。系统评估显示，代码混合会导致安全防护失效，攻击成功率从单一英语的9%激增至69%，在阿拉伯语和印地语等非西方语境中甚至超过90%。为了解释这一现象，我们引入了显著性漂移归因（SDA）框架，揭示了模型在代码混合情况下对安全关键标记的注意力漂移。最后，我们提出了一种轻量级的基于翻译的恢复策略，能够恢复约80%的安全性损失，为提升LLM的安全性提供了切实可行的路径。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在代码混合输入下的安全性失效问题。现有方法在多语言环境中未能有效应对代码混合带来的挑战，导致安全防护机制失效。

**核心思路**：论文提出显著性漂移归因（SDA）框架，通过分析模型在代码混合情况下的注意力分布，揭示其对安全关键标记的忽视，从而为恢复安全性提供依据。

**技术框架**：整体架构包括数据预处理、模型训练和恢复策略三个主要模块。首先，通过代码混合生成训练数据；其次，利用SDA框架分析模型的注意力分布；最后，实施翻译恢复策略以提升安全性。

**关键创新**：最重要的技术创新在于引入了SDA框架，能够有效识别模型在代码混合情况下的注意力漂移，提供了新的视角来理解模型的安全性问题。与现有方法相比，SDA框架更具解释性和针对性。

**关键设计**：在模型训练过程中，采用了特定的损失函数来强化对安全关键标记的关注，同时在翻译恢复策略中，利用轻量级的翻译模型进行实时恢复，确保高效性与准确性。

## 📊 实验亮点

实验结果显示，在代码混合输入下，攻击成功率从9%激增至69%，在阿拉伯语和印地语等非西方语境中甚至超过90%。采用翻译恢复策略后，模型的安全性恢复率可达80%，显著提升了模型在多语言环境下的安全性表现。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容审核、在线聊天机器人和多语言客户服务等。通过提升大型语言模型在多语言环境下的安全性，能够有效保护用户免受有害内容的影响，具有重要的社会价值和实际意义。未来，该研究可能推动更广泛的安全性标准在多语言AI系统中的应用。

## 📄 摘要（原文）

> While LLMs appear robustly safety-aligned in English, we uncover a catastrophic, overlooked weakness: attributional collapse under code-mixed perturbations. Our systematic evaluation of open models shows that the linguistic camouflage of code-mixing -- ``blending languages within a single conversation'' -- can cause safety guardrails to fail dramatically. Attack success rates (ASR) spike from a benign 9\% in monolingual English to 69\% under code-mixed inputs, with rates exceeding 90\% in non-Western contexts such as Arabic and Hindi. These effects hold not only on controlled synthetic datasets but also on real-world social media traces, revealing a serious risk for billions of users. To explain why this happens, we introduce saliency drift attribution (SDA), an interpretability framework that shows how, under code-mixing, the model's internal attention drifts away from safety-critical tokens (e.g., ``violence'' or ``corruption''), effectively blinding it to harmful intent. Finally, we propose a lightweight translation-based restoration strategy that recovers roughly 80\% of the safety lost to code-mixing, offering a practical path toward more equitable and robust LLM safety.

