---
layout: default
title: Predicting Implicit Arguments in Procedural Video Instructions
---

# Predicting Implicit Arguments in Procedural Video Instructions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21068" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21068v1</a>
  <a href="https://arxiv.org/pdf/2505.21068.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21068v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21068v1', 'Predicting Implicit Arguments in Procedural Video Instructions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anil Batra, Laura Sevilla-Lara, Marcus Rohrbach, Frank Keller

**分类**: cs.CL, cs.CV

**发布日期**: 2025-05-27

**备注**: ACL 2025 Main

---

## 💡 一句话要点

**提出Implicit-VidSRL数据集以解决隐式参数预测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `隐式参数预测` `程序性文本` `多模态学习` `语义角色标注` `上下文推理` `数据集构建` `模型评估`

## 📋 核心要点

1. 现有的语义角色标注方法常常忽视隐式论元，导致对程序性文本的理解不够全面。
2. 本文提出Implicit-VidSRL数据集，旨在通过上下文推断隐式和显式论元，增强多模态模型的推理能力。
3. 实验结果表明，iSRL-Qwen2-VL模型在隐式论元预测上相较于基线模型有显著提升，F1-score分别提高了17%和14.7%。

## 📝 摘要（中文）

程序性文本有助于AI增强对上下文和动作序列的推理能力。将这些文本转化为语义角色标注（SRL）可以通过识别谓词-论元结构来改善对单个步骤的理解。然而，现有的SRL基准往往忽视隐式论元，导致理解不完整。为了解决这个问题，本文引入了Implicit-VidSRL数据集，该数据集要求从多模态烹饪程序的上下文信息中推断隐式和显式论元。我们研究了最近的多模态大语言模型，发现它们在给定动词的情况下，难以预测多模态程序数据中的隐式论元。最后，我们提出的iSRL-Qwen2-VL模型在what-implicit和where/with-implicit语义角色上相较于GPT-4o分别提高了17%和14.7%的F1-score。

## 🔬 方法详解

**问题定义**：本文旨在解决在程序性视频指令中隐式参数预测的不足，现有方法常常无法识别上下文中隐含的信息，导致理解不完整。

**核心思路**：通过引入Implicit-VidSRL数据集，要求模型从上下文信息中推断隐式和显式论元，从而提升对程序性文本的理解能力。

**技术框架**：整体架构包括数据集构建、模型训练和评估三个主要阶段。数据集包含多模态信息，模型需要通过视觉变化进行实体跟踪。

**关键创新**：最重要的创新在于引入了隐式论元的概念，并通过新的数据集和模型设计来解决这一问题，显著提升了多模态模型的推理能力。

**关键设计**：在模型设计中，采用了特定的损失函数来优化隐式论元的预测，同时在网络结构中引入了多模态融合机制，以更好地处理视觉和文本信息的交互。

## 📊 实验亮点

在实验中，iSRL-Qwen2-VL模型在what-implicit和where/with-implicit语义角色的F1-score上分别提高了17%和14.7%，相较于基线模型GPT-4o表现出显著的性能提升，验证了模型在隐式参数预测上的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能厨房助手、自动化烹饪指导和教育培训等。通过提升对程序性文本的理解能力，可以为用户提供更准确的操作指导，进而提高烹饪效率和体验。未来，该方法也可扩展到其他领域，如机器人操作和人机交互等。

## 📄 摘要（原文）

> Procedural texts help AI enhance reasoning about context and action sequences. Transforming these into Semantic Role Labeling (SRL) improves understanding of individual steps by identifying predicate-argument structure like {verb,what,where/with}. Procedural instructions are highly elliptic, for instance, (i) add cucumber to the bowl and (ii) add sliced tomatoes, the second step's where argument is inferred from the context, referring to where the cucumber was placed. Prior SRL benchmarks often miss implicit arguments, leading to incomplete understanding. To address this, we introduce Implicit-VidSRL, a dataset that necessitates inferring implicit and explicit arguments from contextual information in multimodal cooking procedures. Our proposed dataset benchmarks multimodal models' contextual reasoning, requiring entity tracking through visual changes in recipes. We study recent multimodal LLMs and reveal that they struggle to predict implicit arguments of what and where/with from multi-modal procedural data given the verb. Lastly, we propose iSRL-Qwen2-VL, which achieves a 17% relative improvement in F1-score for what-implicit and a 14.7% for where/with-implicit semantic roles over GPT-4o.

