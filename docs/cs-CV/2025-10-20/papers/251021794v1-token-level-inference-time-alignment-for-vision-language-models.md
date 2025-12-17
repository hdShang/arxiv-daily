---
layout: default
title: Token-Level Inference-Time Alignment for Vision-Language Models
---

# Token-Level Inference-Time Alignment for Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.21794" class="toolbar-btn" target="_blank">📄 arXiv: 2510.21794v1</a>
  <a href="https://arxiv.org/pdf/2510.21794.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21794v1" onclick="toggleFavorite(this, '2510.21794v1', 'Token-Level Inference-Time Alignment for Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kejia Chen, Jiawen Zhang, Jiacong Hu, Kewei Gao, Jian Lou, Zunlei Feng, Mingli Song

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-20

---

## 💡 一句话要点

**提出TITA：一种用于视觉-语言模型Token级推理时对齐的轻量级框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `推理时对齐` `幻觉减少` `奖励模型` `直接偏好优化`

## 📋 核心要点

1. 现有视觉-语言模型易产生幻觉，输出与视觉输入不符，且现有对齐方法成本高昂或反馈不足。
2. TITA框架通过训练奖励模型近似VLM分布，提取token级隐式偏好信号，实现推理时对齐。
3. 实验表明，TITA在多个基准测试中显著提升了模型性能，有效减少了幻觉，且推理开销极小。

## 📝 摘要（中文）

视觉-语言模型(VLMs)已成为现代多模态智能的关键骨干，但其输出仍然容易产生幻觉，即生成与视觉输入不一致的看似合理的文本。现有的对齐方法通常依赖于昂贵的、带有标注偏好数据的微调，或者仅提供粗略、延迟反馈的序列级推理策略。为了克服这些限制，我们提出了TITA(Token-level Inference-Time Alignment)，这是一个轻量级框架，它冻结了基础VLM，而是训练一个奖励模型来近似其分布。在推理过程中，隐式偏好信号被提取为奖励模型和目标VLM之间的对数概率比，从而产生密集的自回归反馈。这种公式可以被看作是直接偏好优化(DPO)的推理时变体，提供token级别的校正信号，而无需重新训练骨干网络。在LLaVA-1.5-7B和13B上的广泛评估表明，在12个基准测试中都获得了持续的收益，在MMVet上提高了8.6%，在POPE上提高了6.7%，表明更强的通用理解和减少的幻觉。在Qwen2.5-VL-7B和DeepSeek-VL2-27.5B上的额外实验显示了相当的收益，尤其是在减少幻觉和VQA准确性方面，同时产生的推理开销可以忽略不计。

## 🔬 方法详解

**问题定义**：视觉-语言模型（VLM）在生成文本时容易产生幻觉，即生成与图像内容不符但语法上合理的文本。现有的对齐方法，如微调或序列级推理，存在成本高、反馈延迟或不够精细的问题，难以有效解决幻觉问题。

**核心思路**：TITA的核心思路是在推理时进行token级别的对齐，通过奖励模型来评估每个token的生成质量，并利用奖励模型与原始VLM的概率比作为反馈信号，引导VLM生成更符合视觉内容的文本。这种方法无需重新训练VLM，降低了计算成本。

**技术框架**：TITA框架包含两个主要模块：冻结的基础VLM和一个训练好的奖励模型。在推理阶段，VLM自回归地生成token，同时奖励模型评估每个token的质量。然后，计算奖励模型和VLM的对数概率比，作为token级别的校正信号，用于调整VLM的生成概率分布。整个过程可以看作是DPO（Direct Preference Optimization）在推理时的一种变体。

**关键创新**：TITA的关键创新在于token级别的推理时对齐。与传统的序列级对齐方法相比，TITA能够提供更精细的反馈，从而更有效地减少幻觉。此外，TITA无需重新训练VLM，降低了计算成本，使其更易于部署和应用。

**关键设计**：奖励模型的设计至关重要，需要能够准确评估token的生成质量。损失函数通常采用对比学习或偏好学习的方式，例如DPO。在推理时，校正信号的强度需要仔细调整，以避免过度干预VLM的生成过程。具体参数设置和网络结构的选择可能需要根据具体任务进行调整。

## 📊 实验亮点

在LLaVA-1.5-7B和13B模型上，TITA在12个基准测试中取得了显著提升，MMVet上提升8.6%，POPE上提升6.7%，表明TITA能有效提升VLM的通用理解能力并减少幻觉。在Qwen2.5-VL-7B和DeepSeek-VL2-27.5B上的实验也显示了相似的增益，尤其是在幻觉减少和VQA准确性方面，且推理开销可以忽略不计。

## 🎯 应用场景

TITA框架可广泛应用于各种视觉-语言任务，例如图像描述、视觉问答、视觉推理等。通过减少幻觉，可以提高VLM在实际应用中的可靠性和准确性。该方法尤其适用于对安全性要求较高的场景，例如医疗影像分析、自动驾驶等。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have become essential backbones of modern multimodal intelligence, yet their outputs remain prone to hallucination-plausible text misaligned with visual inputs. Existing alignment approaches often rely on expensive fine-tuning with annotated preference data or sequence-level inference strategies that provide only coarse, delayed feedback. To overcome these limitations, we present TITA (Token-level Inference-Time Alignment), a lightweight framework that freezes the base VLM and instead trains a reward model to approximate its distribution. During inference, implicit preference signals are extracted as log-probability ratios between the reward model and the target VLM, yielding dense autoregressive feedback. This formulation can be viewed as an inference-time variant of Direct Preference Optimization (DPO), providing token-level corrective signals without retraining the backbone. Extensive evaluations on LLaVA-1.5-7B and 13B show consistent gains across 12 benchmarks, with improvements of 8.6% on MMVet and 6.7% on POPE, indicating stronger general understanding and reduced hallucinations. Additional experiments on Qwen2.5-VL-7B and DeepSeek-VL2-27.5B show comparable gains, especially in hallucination reduction and VQA accuracy, while incurring negligible inference overhead.

