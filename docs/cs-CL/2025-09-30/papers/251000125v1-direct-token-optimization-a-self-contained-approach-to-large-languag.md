---
layout: default
title: "Direct Token Optimization: A Self-contained Approach to Large Language Model Unlearning"
---

# Direct Token Optimization: A Self-contained Approach to Large Language Model Unlearning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00125" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00125v1</a>
  <a href="https://arxiv.org/pdf/2510.00125.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00125v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00125v1', 'Direct Token Optimization: A Self-contained Approach to Large Language Model Unlearning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hong kyu Lee, Ruixuan Liu, Li Xiong

**分类**: cs.CL, cs.AI, cs.CR

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出直接Token优化（DTO）方法，实现大语言模型自包含式遗忘学习。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `遗忘学习` `隐私保护` `内容审核` `自包含` `Token优化` `模型校正`

## 📋 核心要点

1. 现有大语言模型遗忘学习方法依赖外部资源，如辅助模型或数据集，存在隐私风险且不实用。
2. DTO方法通过直接优化token级别目标，区分目标token和非目标token，实现高效的自包含式遗忘。
3. 实验表明，DTO在遗忘质量上显著优于现有方法，最高提升16.8倍，同时保持了模型效用。

## 📝 摘要（中文）

本文提出了一种针对大型语言模型（LLM）的自包含式遗忘学习方法——直接Token优化（DTO）。遗忘学习是一种新兴技术，旨在从模型中移除部分训练数据（遗忘集）的影响，而无需完全重新训练，其应用包括隐私保护、内容审核和模型校正。关键挑战在于确保模型完全忘记遗忘集的知识，同时不损害其整体效用。现有LLM遗忘学习方法通常依赖辅助语言模型、保留数据集，甚至商业AI服务，但这并不实用，并可能引入额外的隐私风险。DTO直接优化token级别的目标，无需外部资源。对于需要遗忘的序列，我们识别两种token：目标token（捕获遗忘的关键知识）和非目标token（维护模型效用）。前者用于优化遗忘目标，后者用于保持模型性能。实验结果表明，与最新的基线方法相比，DTO在多个基准数据集上实现了高达16.8倍的遗忘质量提升，同时保持了相当的模型效用。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）的遗忘学习问题，即如何从模型中移除特定训练数据（遗忘集）的影响，而无需完全重新训练。现有方法的痛点在于依赖外部资源（如辅助语言模型、保留数据集或商业AI服务），这不仅增加了计算成本，还可能引入额外的隐私风险。

**核心思路**：论文的核心思路是直接在token级别进行优化，区分需要遗忘的关键知识（目标token）和保持模型效用的非目标token。通过差异化处理这两类token，可以在实现有效遗忘的同时，尽可能地保留模型的原有能力。

**技术框架**：DTO方法的技术框架主要包含以下几个步骤：1) **序列识别**：确定需要遗忘的文本序列。2) **Token分类**：将序列中的token分为目标token和非目标token。目标token是包含需要遗忘知识的token，非目标token是用于保持模型通用能力的token。3) **目标优化**：针对目标token，优化遗忘目标，例如降低模型对这些token的预测概率。4) **效用保持**：针对非目标token，优化模型性能，例如提高模型对这些token的预测概率。

**关键创新**：DTO方法最重要的技术创新点在于其自包含性，即无需依赖任何外部资源即可实现遗忘学习。这与现有方法形成了本质区别，现有方法通常需要辅助模型或数据集来指导遗忘过程。此外，DTO方法通过区分目标token和非目标token，实现了更精细化的遗忘控制。

**关键设计**：DTO方法的关键设计包括：1) **目标token的选择策略**：如何准确识别包含需要遗忘知识的token。2) **遗忘损失函数**：如何设计损失函数来有效降低模型对目标token的预测概率。3) **效用保持损失函数**：如何设计损失函数来保持模型对非目标token的预测能力。具体的损失函数形式和参数设置需要在实验中进行调整和优化，以达到最佳的遗忘效果和模型效用。

## 📊 实验亮点

实验结果表明，DTO方法在多个基准数据集上显著优于现有方法。例如，在某些数据集上，DTO的遗忘质量比最新的基线方法提高了高达16.8倍，同时保持了与基线方法相当的模型效用。这些结果证明了DTO方法在实现高效且实用的遗忘学习方面的有效性。

## 🎯 应用场景

DTO方法可应用于多种场景，包括：1) 隐私保护：从模型中移除包含个人隐私的数据。2) 内容审核：删除模型中不当或有害的内容。3) 模型校正：修正模型中的错误知识或偏见。该方法具有自包含性，易于部署和使用，有望推动大语言模型在安全和可靠性方面的应用。

## 📄 摘要（原文）

> Machine unlearning is an emerging technique that removes the influence of a subset of training data (forget set) from a model without full retraining, with applications including privacy protection, content moderation, and model correction. The key challenge lies in ensuring that the model completely forgets the knowledge of the forget set without compromising its overall utility. Existing unlearning methods for large language models (LLMs) often utilize auxiliary language models, retain datasets, or even commercial AI services for effective unlearning and maintaining the model utility. However, dependence on these external resources is often impractical and could potentially introduce additional privacy risks. In this work, we propose direct token optimization (DTO), a novel self-contained unlearning approach for LLMs that directly optimizes the token level objectives and eliminates the need for external resources. Given a sequence to unlearn, we identify two categories of tokens: target tokens, which capture critical knowledge for unlearning, and the remaining non-target tokens, which are crucial for maintaining the model utility. The former are used to optimize the unlearning objective, while the latter serve to preserve the model's performance. The experimental results show that the proposed DTO achieves up to 16.8$\times$ improvement in forget quality on several benchmark datasets than the latest baselines while maintaining a comparable level of model utility.

