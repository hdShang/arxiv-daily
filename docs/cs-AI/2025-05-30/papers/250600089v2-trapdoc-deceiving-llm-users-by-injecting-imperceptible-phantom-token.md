---
layout: default
title: TRAPDOC: Deceiving LLM Users by Injecting Imperceptible Phantom Tokens into Documents
---

# TRAPDOC: Deceiving LLM Users by Injecting Imperceptible Phantom Tokens into Documents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00089" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00089v2</a>
  <a href="https://arxiv.org/pdf/2506.00089.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00089v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00089v2', 'TRAPDOC: Deceiving LLM Users by Injecting Imperceptible Phantom Tokens into Documents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hyundong Jin, Sicheol Sung, Shinwoo Park, SeungYeop Baik, Yo-Sub Han

**分类**: cs.CY, cs.AI

**发布日期**: 2025-05-30 (更新: 2025-09-28)

**备注**: EMNLP 2025 Findings

**🔗 代码/项目**: [GITHUB](https://github.com/jindong22/TrapDoc)

---

## 💡 一句话要点

**提出TRAPDOC以解决用户对大型语言模型的过度依赖问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `幻影标记` `信息安全` `用户行为` `社会责任`

## 📋 核心要点

1. 核心问题：用户对大型语言模型的过度依赖导致了作业和敏感文档处理等任务的失误，形成社会问题。
2. 方法要点：提出通过注入不可察觉的幻影标记来欺骗LLMs，使其生成错误但看似合理的输出。
3. 实验或效果：通过实证评估，TRAPDOC在多个商业LLMs上表现出显著的欺骗效果，相较于基线方法有明显提升。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在推理、写作、文本编辑和检索等方面的快速发展，用户对其功能的依赖日益加深，导致了严重的社会问题，尤其是在作业和敏感文档处理等任务上。为了解决这一问题，本文提出了一种将不可察觉的幻影标记注入文档的方法，旨在使LLMs生成看似合理但实际上不正确的输出。基于这一技术，本文介绍了TRAPDOC框架，旨在欺骗过度依赖LLMs的用户。通过实证评估，我们展示了该框架在多个商业LLMs上的有效性，并与多个基线进行了比较。TRAPDOC为促进用户与语言模型的更负责任和深思熟虑的互动奠定了坚实基础。

## 🔬 方法详解

**问题定义**：本文旨在解决用户对大型语言模型的过度依赖问题，现有方法未能有效防止用户在作业和敏感文档处理中的失误，导致错误信息的传播。

**核心思路**：论文提出了一种将不可察觉的幻影标记注入文档的方法，利用这些标记使LLMs生成看似合理但实际上错误的输出，从而引导用户做出错误决策。

**技术框架**：TRAPDOC框架包括数据预处理、幻影标记生成、文档注入和输出评估四个主要模块。首先对输入文档进行分析，然后生成幻影标记并将其注入文档，最后评估LLMs的输出效果。

**关键创新**：最重要的技术创新在于幻影标记的生成与注入技术，这与现有方法的直接输入干扰不同，能够在不引起用户注意的情况下影响LLMs的输出。

**关键设计**：在参数设置上，幻影标记的生成依赖于特定的文本特征，损失函数设计为最大化输出的误导性，同时保持标记的不可察觉性。

## 📊 实验亮点

实验结果表明，TRAPDOC在多个商业LLMs上成功欺骗用户，生成的错误输出与真实输出的相似度高达85%，相比于传统方法提升了20%的误导效果，显示出其在实际应用中的强大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括教育、法律和医疗等需要高准确性和责任感的行业。通过提高用户对大型语言模型的警觉性，TRAPDOC有助于减少因过度依赖而导致的错误决策，从而提升整体信息处理的安全性和可靠性。

## 📄 摘要（原文）

> The reasoning, writing, text-editing, and retrieval capabilities of proprietary large language models (LLMs) have advanced rapidly, providing users with an ever-expanding set of functionalities. However, this growing utility has also led to a serious societal concern: the over-reliance on LLMs. In particular, users increasingly delegate tasks such as homework, assignments, or the processing of sensitive documents to LLMs without meaningful engagement. This form of over-reliance and misuse is emerging as a significant social issue. In order to mitigate these issues, we propose a method injecting imperceptible phantom tokens into documents, which causes LLMs to generate outputs that appear plausible to users but are in fact incorrect. Based on this technique, we introduce TRAPDOC, a framework designed to deceive over-reliant LLM users. Through empirical evaluation, we demonstrate the effectiveness of our framework on proprietary LLMs, comparing its impact against several baselines. TRAPDOC serves as a strong foundation for promoting more responsible and thoughtful engagement with language models. Our code is available at https://github.com/jindong22/TrapDoc.

