---
layout: default
title: "Using Contrastive Learning to Improve Two-Way Reasoning in Large Language Models: The Obfuscation Task as a Case Study"
---

# Using Contrastive Learning to Improve Two-Way Reasoning in Large Language Models: The Obfuscation Task as a Case Study

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05553" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05553v1</a>
  <a href="https://arxiv.org/pdf/2509.05553.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05553v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05553v1', 'Using Contrastive Learning to Improve Two-Way Reasoning in Large Language Models: The Obfuscation Task as a Case Study')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Serge Lionel Nikiema, Jordan Samhi, Micheline Bénédicte Moumoula, Albérick Euraste Djiré, Abdoul Kader Kaboré, Jacques Klein, Tegawendé F. Bissyandé

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-06

---

## 💡 一句话要点

**提出对比学习微调方法，提升大语言模型在代码混淆任务中的双向推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对比学习` `双向推理` `大语言模型` `代码混淆` `认知专业化`

## 📋 核心要点

1. 现有大语言模型在正向任务上表现良好，但在反向推理任务中表现不佳，表明模型可能只是在进行模式匹配，缺乏真正的理解。
2. 论文提出对比微调（CFT）方法，通过引入正、负样本和正向混淆样本，鼓励模型学习深层语义，从而提升双向推理能力。
3. 实验结果表明，CFT方法能够有效提升模型在代码混淆任务中的双向推理能力，在保持正向性能的同时，显著提升反向性能。

## 📝 摘要（中文）

本研究探讨了一个人工智能领域的基础问题：大型语言模型是真正理解概念，还是仅仅识别模式？作者提出双向推理能力作为衡量模型是否真正理解概念的标准，即模型无需在反向方向上进行显式训练，也能应用反向转换。研究发现，模型在正向任务上微调后，性能提升，但双向推理能力显著下降，作者称之为认知专业化。为了解决这个问题，他们开发了对比微调（CFT）方法，使用三类样本训练模型：保持语义含义的正样本、具有不同语义的负样本和正向混淆样本。该方法旨在培养更深层次的理解，而非表面模式识别，并允许反向能力在没有显式反向训练的情况下自然发展。实验表明，CFT成功实现了双向推理，在保持正向任务能力的同时，实现了强大的反向性能。作者认为，双向推理既是评估真正理解的理论框架，也是开发更强大AI系统的实用训练方法。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在双向推理能力上的不足，尤其是在代码混淆任务中。现有方法，如直接在正向任务上进行微调，会导致模型在正向任务上表现良好，但在反向推理任务中表现不佳，这表明模型可能只是在进行模式匹配，缺乏对概念的真正理解。这种“认知专业化”限制了模型的泛化能力和鲁棒性。

**核心思路**：论文的核心思路是利用对比学习的思想，通过引入正样本、负样本和正向混淆样本，迫使模型学习深层语义表示，而不是仅仅依赖于表面模式。正样本保持语义不变，负样本改变语义，正向混淆样本则模拟了需要进行反向推理的场景。通过这种方式，模型能够更好地理解概念的本质，从而提升双向推理能力。

**技术框架**：整体框架包括三个主要部分：数据构建、对比微调和评估。数据构建阶段，生成正样本、负样本和正向混淆样本。对比微调阶段，使用这些样本对大型语言模型进行微调，目标是使模型能够区分正样本和负样本，并能够从正向混淆样本中推断出原始语义。评估阶段，使用正向和反向推理任务来评估模型的性能。

**关键创新**：最重要的技术创新点是对比微调（CFT）方法，它通过引入负样本和正向混淆样本，有效地解决了模型在双向推理能力上的不足。与传统的微调方法相比，CFT方法能够更好地引导模型学习深层语义表示，从而提升模型的泛化能力和鲁棒性。

**关键设计**：CFT方法的关键设计包括：1) 正负样本的构建方式，需要保证正样本在语义上与原始样本一致，而负样本在语义上与原始样本不同；2) 正向混淆样本的生成方式，需要模拟需要进行反向推理的场景；3) 对比损失函数的选择，需要能够有效地区分正样本和负样本。论文中具体使用的损失函数和参数设置未明确说明，属于未知信息。

## 📊 实验亮点

实验结果表明，对比微调（CFT）方法能够显著提升模型在代码混淆任务中的双向推理能力。具体性能数据和对比基线未在摘要中明确给出，属于未知信息。但结论明确指出，CFT在保持正向任务能力的同时，实现了强大的反向性能。

## 🎯 应用场景

该研究成果可应用于代码理解、程序修复、自然语言处理等领域。例如，在代码理解中，可以帮助模型更好地理解代码的语义，从而进行代码分析、漏洞检测等任务。在程序修复中，可以帮助模型理解错误代码的意图，从而生成正确的代码。在自然语言处理中，可以提升模型在语义推理、问答系统等任务中的表现。

## 📄 摘要（原文）

> This research addresses a fundamental question in AI: whether large language models truly understand concepts or simply recognize patterns. The authors propose bidirectional reasoning,the ability to apply transformations in both directions without being explicitly trained on the reverse direction, as a test for genuine understanding. They argue that true comprehension should naturally allow reversibility. For example, a model that can change a variable name like userIndex to i should also be able to infer that i represents a user index without reverse training. The researchers tested current language models and discovered what they term cognitive specialization: when models are fine-tuned on forward tasks, their performance on those tasks improves, but their ability to reason bidirectionally becomes significantly worse. To address this issue, they developed Contrastive Fine-Tuning (CFT), which trains models using three types of examples: positive examples that maintain semantic meaning, negative examples with different semantics, and forward-direction obfuscation examples. This approach aims to develop deeper understanding rather than surface-level pattern recognition and allows reverse capabilities to develop naturally without explicit reverse training. Their experiments demonstrated that CFT successfully achieved bidirectional reasoning, enabling strong reverse performance while maintaining forward task capabilities. The authors conclude that bidirectional reasoning serves both as a theoretical framework for assessing genuine understanding and as a practical training approach for developing more capable AI systems.

