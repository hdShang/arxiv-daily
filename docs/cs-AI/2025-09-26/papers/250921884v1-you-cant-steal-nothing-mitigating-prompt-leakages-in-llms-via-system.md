---
layout: default
title: "You Can't Steal Nothing: Mitigating Prompt Leakages in LLMs via System Vectors"
---

# You Can't Steal Nothing: Mitigating Prompt Leakages in LLMs via System Vectors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21884" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21884v1</a>
  <a href="https://arxiv.org/pdf/2509.21884.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21884v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21884v1', 'You Can\'t Steal Nothing: Mitigating Prompt Leakages in LLMs via System Vectors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bochuan Cao, Changjiang Li, Yuanpu Cao, Yameng Ge, Ting Wang, Jinghui Chen

**分类**: cs.CR, cs.AI, cs.CL

**发布日期**: 2025-09-26

**备注**: 29 pages, 10 tables, 6figures, accepted by CCS 25

---

## 💡 一句话要点

**提出SysVec，通过系统向量编码缓解大语言模型中的提示词泄露问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `提示词泄露` `系统提示词` `向量编码` `安全` `指令遵循` `长文本遗忘`

## 📋 核心要点

1. 现有大语言模型容易遭受提示词泄露攻击，攻击者可以通过构造特定输入，从而获取模型的系统提示词，威胁模型安全。
2. 论文提出SysVec方法，将系统提示词编码为内部向量表示，而非直接使用文本，从而避免提示词直接暴露在上下文中。
3. 实验表明，SysVec有效缓解了提示词泄露攻击，同时保持了模型的功能完整性，并改善了长文本场景下的遗忘问题。

## 📝 摘要（中文）

大型语言模型（LLMs）已被广泛应用于各种应用中，利用定制的系统提示词来执行不同的任务。面对潜在的系统提示词泄露风险，模型开发者已经实施了一些策略来防止泄露，主要是通过禁止LLMs在遇到已知的攻击模式时重复其上下文。然而，这些方法仍然容易受到新的和未预见的提示词泄露技术的攻击。本文首先介绍了一种简单而有效的提示词泄露攻击，以揭示此类风险。我们的攻击能够从各种基于LLM的应用中提取系统提示词，甚至包括GPT-4o或Claude 3.5 Sonnet等SOTA LLM模型。我们的发现进一步启发我们通过在上下文中不包含系统提示词来寻找解决问题的根本方案。为此，我们提出SysVec，一种新颖的方法，将系统提示词编码为内部表示向量，而不是原始文本。通过这样做，SysVec最大限度地降低了未经授权的泄露风险，同时保留了LLM的核心语言能力。值得注意的是，这种方法不仅增强了安全性，还提高了模型的一般指令遵循能力。实验结果表明，SysVec有效地缓解了提示词泄露攻击，保持了LLM的功能完整性，并有助于缓解长上下文场景中的遗忘问题。

## 🔬 方法详解

**问题定义**：论文旨在解决大语言模型中系统提示词泄露的问题。现有方法主要通过检测已知的攻击模式来阻止泄露，但无法防御新型攻击，且依赖于对上下文的过滤，可能影响模型性能。直接将系统提示词以文本形式包含在上下文中，存在被恶意用户提取的风险。

**核心思路**：论文的核心思路是将系统提示词编码成一个向量表示（System Vector），并将其作为模型的内部状态。这样，系统提示词不再以文本形式存在于上下文中，从而避免了直接泄露的风险。同时，模型可以通过这个向量来理解和执行系统指令。

**技术框架**：SysVec方法主要包含以下几个阶段：1) **系统提示词编码**：使用一个编码器（例如，一个小型Transformer模型）将系统提示词编码成一个向量表示。2) **向量注入**：将编码后的向量注入到LLM的内部状态中。具体实现方式未知，可能通过修改LLM的注意力机制或直接修改隐藏层状态。3) **推理**：LLM在推理时，利用注入的系统向量来指导生成过程。

**关键创新**：最重要的创新点在于将系统提示词从文本形式转换为向量形式，从而从根本上避免了提示词泄露的风险。这种方法不需要依赖于对上下文的过滤或检测，因此更加安全和灵活。此外，SysVec还可以提高模型的指令遵循能力和缓解长文本遗忘问题。

**关键设计**：论文中关于编码器和向量注入的具体技术细节描述较少，例如：编码器的具体结构、训练方式，以及向量如何注入到LLM的内部状态。这些细节对于SysVec的实际应用至关重要，但目前未知。

## 📊 实验亮点

论文通过实验证明，SysVec能够有效缓解提示词泄露攻击，即使面对GPT-4o和Claude 3.5 Sonnet等先进模型也能成功防御。同时，SysVec在保持模型功能完整性的前提下，还提升了模型的指令遵循能力，并缓解了长文本场景下的遗忘问题。具体的性能数据和提升幅度未知。

## 🎯 应用场景

SysVec方法可以应用于各种需要定制系统提示词的大语言模型应用场景，例如智能助手、对话机器人、内容生成等。通过使用SysVec，可以有效保护系统提示词不被泄露，提高应用的安全性。此外，SysVec还有助于提高模型的指令遵循能力和缓解长文本遗忘问题，从而提升用户体验。该方法具有广泛的应用前景，尤其是在对安全性要求较高的场景下。

## 📄 摘要（原文）

> Large language models (LLMs) have been widely adopted across various applications, leveraging customized system prompts for diverse tasks. Facing potential system prompt leakage risks, model developers have implemented strategies to prevent leakage, primarily by disabling LLMs from repeating their context when encountering known attack patterns. However, it remains vulnerable to new and unforeseen prompt-leaking techniques. In this paper, we first introduce a simple yet effective prompt leaking attack to reveal such risks. Our attack is capable of extracting system prompts from various LLM-based application, even from SOTA LLM models such as GPT-4o or Claude 3.5 Sonnet. Our findings further inspire us to search for a fundamental solution to the problems by having no system prompt in the context. To this end, we propose SysVec, a novel method that encodes system prompts as internal representation vectors rather than raw text. By doing so, SysVec minimizes the risk of unauthorized disclosure while preserving the LLM's core language capabilities. Remarkably, this approach not only enhances security but also improves the model's general instruction-following abilities. Experimental results demonstrate that SysVec effectively mitigates prompt leakage attacks, preserves the LLM's functional integrity, and helps alleviate the forgetting issue in long-context scenarios.

