---
layout: default
title: "SightSound-R1: Cross-Modal Reasoning Distillation from Vision to Audio Language Models"
---

# SightSound-R1: Cross-Modal Reasoning Distillation from Vision to Audio Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15661" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15661v1</a>
  <a href="https://arxiv.org/pdf/2509.15661.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15661v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15661v1', 'SightSound-R1: Cross-Modal Reasoning Distillation from Vision to Audio Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qiaolin Wang, Xilin Jiang, Linyang He, Junkai Wu, Nima Mesgarani

**分类**: cs.SD, cs.AI, cs.CL, eess.AS

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**提出SightSound-R1，通过跨模态蒸馏提升听觉语言模型在复杂声景中的推理能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `跨模态学习` `知识蒸馏` `视听问答` `听觉语言模型` `思维链` `音频理解` `推理能力`

## 📋 核心要点

1. 现有听觉语言模型在复杂声景推理能力上存在不足，缺乏大规模思维链音频数据是主要瓶颈。
2. SightSound-R1通过跨模态蒸馏，将视觉语言模型的推理能力迁移到听觉语言模型，弥补数据和模态差距。
3. 实验表明，SightSound-R1显著提升了听觉语言模型在视听问答任务上的推理性能，优于现有基线方法。

## 📝 摘要（中文）

大型听觉语言模型(LALM)在音频理解方面表现出色，但在复杂声景中的推理能力仍落后于大型视觉语言模型(LVLM)。与视觉领域相比，缺乏大规模的思维链音频数据来教导LALM逐步推理是一个瓶颈。为了规避这种数据和模态差距，我们提出了SightSound-R1，这是一个跨模态蒸馏框架，它将更强的LVLM教师的先进推理能力转移到较弱的LALM学生身上，在同一个视听问答(AVQA)数据集上进行。SightSound-R1包括三个核心步骤：(i)测试时缩放，从LVLM教师生成以音频为中心的思维链(CoT)；(ii)音频引导验证，以过滤幻觉；(iii)一个蒸馏管道，包括监督微调(SFT)，然后是用于LALM学生的组相对策略优化(GRPO)。结果表明，SightSound-R1提高了LALM在领域内AVQA测试集以及未见过的听觉场景和问题中的推理性能，优于预训练和仅标签蒸馏的基线。因此，我们得出结论，视觉推理可以有效地转移到音频模型，并可以通过丰富的视听数据进行扩展。

## 🔬 方法详解

**问题定义**：论文旨在解决听觉语言模型(LALM)在复杂声景中推理能力不足的问题。现有方法缺乏大规模的思维链音频数据，难以训练LALM进行逐步推理，导致其性能落后于视觉语言模型(LVLM)。

**核心思路**：论文的核心思路是通过跨模态蒸馏，将更强大的LVLM的推理能力迁移到较弱的LALM。利用LVLM在视觉推理方面的优势，生成伪标签数据，并以此训练LALM，从而提升其在听觉场景下的推理能力。这种方法有效地利用了现有的视听数据，避免了直接收集大规模思维链音频数据的困难。

**技术框架**：SightSound-R1框架包含三个主要阶段：1) **测试时缩放(Test-time Scaling)**：利用LVLM生成以音频为中心的思维链(CoT)。通过调整LVLM的输入，使其更加关注音频信息，从而生成更适合LALM学习的推理过程。2) **音频引导验证(Audio-grounded Validation)**：过滤LVLM生成的思维链中的幻觉。通过音频信息验证推理步骤的合理性，去除与音频内容不符的推理路径，保证数据的质量。3) **蒸馏管道(Distillation Pipeline)**：使用监督微调(SFT)和组相对策略优化(GRPO)训练LALM。首先使用SFT对LALM进行初步训练，然后使用GRPO进一步优化其推理能力。

**关键创新**：SightSound-R1的关键创新在于提出了一种有效的跨模态蒸馏方法，将视觉推理能力迁移到听觉模型。通过测试时缩放和音频引导验证，保证了生成伪标签数据的质量，克服了直接收集大规模思维链音频数据的困难。此外，GRPO的使用进一步提升了LALM的推理性能。

**关键设计**：在测试时缩放阶段，论文可能使用了注意力机制或其他方法来调整LVLM的输入，使其更加关注音频信息。在音频引导验证阶段，可能使用了音频特征提取器和相似度度量方法来判断推理步骤的合理性。在蒸馏管道中，SFT使用了交叉熵损失函数，GRPO可能使用了强化学习中的策略梯度算法。具体的参数设置和网络结构细节可能在论文的实验部分有更详细的描述。

## 📊 实验亮点

SightSound-R1在AVQA测试集上显著提升了LALM的推理性能，并且在未见过的听觉场景和问题中也表现出良好的泛化能力。相较于预训练和仅标签蒸馏的基线方法，SightSound-R1取得了明显的性能提升，证明了视觉推理可以有效地转移到音频模型，并可以通过丰富的视听数据进行扩展。

## 🎯 应用场景

该研究成果可应用于智能安防、智能家居、自动驾驶等领域。例如，在智能安防中，可以利用该技术提升对异常声音事件的识别和推理能力；在自动驾驶中，可以帮助车辆更好地理解周围环境的声音信息，提高驾驶安全性。未来，该技术有望推动听觉智能的发展，实现更自然、更智能的人机交互。

## 📄 摘要（原文）

> While large audio-language models (LALMs) have demonstrated state-of-the-art audio understanding, their reasoning capability in complex soundscapes still falls behind large vision-language models (LVLMs). Compared to the visual domain, one bottleneck is the lack of large-scale chain-of-thought audio data to teach LALM stepwise reasoning. To circumvent this data and modality gap, we present SightSound-R1, a cross-modal distillation framework that transfers advanced reasoning from a stronger LVLM teacher to a weaker LALM student on the same audio-visual question answering (AVQA) dataset. SightSound-R1 consists of three core steps: (i) test-time scaling to generate audio-focused chains of thought (CoT) from an LVLM teacher, (ii) audio-grounded validation to filter hallucinations, and (iii) a distillation pipeline with supervised fine-tuning (SFT) followed by Group Relative Policy Optimization (GRPO) for the LALM student. Results show that SightSound-R1 improves LALM reasoning performance both in the in-domain AVQA test set as well as in unseen auditory scenes and questions, outperforming both pretrained and label-only distilled baselines. Thus, we conclude that vision reasoning can be effectively transferred to audio models and scaled with abundant audio-visual data.

