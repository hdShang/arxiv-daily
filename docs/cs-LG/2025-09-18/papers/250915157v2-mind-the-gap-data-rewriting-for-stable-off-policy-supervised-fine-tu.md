---
layout: default
title: "Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning"
---

# Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15157" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15157v2</a>
  <a href="https://arxiv.org/pdf/2509.15157.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15157v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15157v2', 'Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shiwan Zhao, Xuyang Zhao, Jiaming Zhou, Aobo Kong, Qicheng Li, Yong Qin

**分类**: cs.LG, cs.CL

**发布日期**: 2025-09-18 (更新: 2025-09-19)

**🔗 代码/项目**: [GITHUB](https://github.com/NKU-HLT/Off-Policy-SFT)

---

## 💡 一句话要点

**提出数据重写框架，解决SFT中Off-Policy学习的分布偏移问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `监督微调` `Off-Policy学习` `数据重写` `重要性采样` `策略对齐` `数学推理` `大语言模型`

## 📋 核心要点

1. SFT面临Off-Policy学习的挑战，即训练数据与目标策略存在分布差异，导致训练不稳定。
2. 论文提出数据重写框架，通过引导模型重新生成错误答案，主动缩小训练数据与目标策略的差距。
3. 实验表明，该方法在数学推理任务上显著优于传统SFT和动态微调方法，提升了模型性能。

## 📝 摘要（中文）

大型语言模型的监督微调(SFT)可以被视为一个Off-Policy学习问题，其中专家演示来自固定的行为策略，而训练旨在优化目标策略。重要性采样是校正这种分布不匹配的标准工具，但大的策略差距会导致权重倾斜、高方差和不稳定的优化。现有方法通过KL惩罚或裁剪来缓解这个问题，这些方法被动地限制更新，而不是主动地缩小差距。我们提出了一种简单而有效的数据重写框架，该框架在训练前主动缩小策略差距。对于每个问题，正确的模型生成解决方案被保留为On-Policy数据，而错误的解决方案通过引导重新解决来重写，仅在需要时才回退到专家演示。这使训练分布与目标策略对齐，从而降低方差并提高稳定性。为了处理重写后的残余不匹配，我们还在训练期间应用重要性采样，形成一个两阶段方法，将数据级对齐与轻量级优化级校正相结合。在五个数学推理基准上的实验表明，相对于vanilla SFT和最先进的动态微调(DFT)方法，该方法具有一致且显著的优势。数据和代码将在https://github.com/NKU-HLT/Off-Policy-SFT上发布。

## 🔬 方法详解

**问题定义**：监督微调（SFT）中，训练数据（专家演示）来自固定的行为策略，而目标是优化一个不同的目标策略。这构成了一个Off-Policy学习问题。现有方法如KL散度惩罚或梯度裁剪，试图缓解由此产生的分布偏移，但这些方法是被动的，无法有效缩小策略差距，导致训练不稳定和性能下降。

**核心思路**：核心思想是在训练前主动缩小策略差距。具体来说，对于每个训练样本，如果模型能够生成正确的答案，则保留该答案作为On-Policy数据。如果模型生成了错误的答案，则引导模型重新解决问题，生成正确的答案。只有在模型无法生成正确答案时，才使用专家演示。这样，训练数据更接近目标策略，从而减少了分布偏移。

**技术框架**：该方法是一个两阶段框架。第一阶段是数据重写阶段，如上所述，通过引导模型重新解决问题来生成更符合目标策略的训练数据。第二阶段是训练阶段，使用重写后的数据进行SFT。为了进一步处理残余的分布偏移，在训练阶段还使用了重要性采样。

**关键创新**：关键创新在于数据重写策略，它主动地将训练数据向目标策略靠拢，而不是被动地限制更新。这种方法能够更有效地缩小策略差距，从而提高训练的稳定性和性能。与现有方法相比，该方法在数据层面解决了Off-Policy学习的问题，而现有方法主要在优化层面进行调整。

**关键设计**：数据重写阶段的关键在于如何引导模型重新解决问题。论文中可能使用了特定的提示工程或约束解码方法来实现这一点。重要性采样在训练阶段用于校正数据重写后仍然存在的分布偏移。具体的损失函数和网络结构可能与标准的SFT方法相同，但训练数据是经过重写后的数据。

## 📊 实验亮点

实验结果表明，该方法在五个数学推理基准上均取得了显著的性能提升，超过了vanilla SFT和最先进的动态微调(DFT)方法。具体的数据提升幅度需要在论文中查找，但摘要中明确指出是“一致且显著的优势”。

## 🎯 应用场景

该研究成果可应用于各种需要使用Off-Policy数据进行模型微调的场景，例如机器人控制、对话系统、推荐系统等。通过数据重写，可以提高模型在这些场景下的泛化能力和鲁棒性，降低训练成本，并加速模型的部署。

## 📄 摘要（原文）

> Supervised fine-tuning (SFT) of large language models can be viewed as an off-policy learning problem, where expert demonstrations come from a fixed behavior policy while training aims to optimize a target policy. Importance sampling is the standard tool for correcting this distribution mismatch, but large policy gaps lead to skewed weights, high variance, and unstable optimization. Existing methods mitigate this issue with KL penalties or clipping, which passively restrict updates rather than actively reducing the gap. We propose a simple yet effective data rewriting framework that proactively shrinks the policy gap before training. For each problem, correct model-generated solutions are kept as on-policy data, while incorrect ones are rewritten through guided re-solving, falling back to expert demonstrations only when needed. This aligns the training distribution with the target policy, reducing variance and improving stability. To handle residual mismatch after rewriting, we additionally apply importance sampling during training, forming a two-stage approach that combines data-level alignment with lightweight optimization-level correction. Experiments on five mathematical reasoning benchmarks show consistent and significant gains over both vanilla SFT and the state-of-the-art Dynamic Fine-Tuning (DFT) approach. Data and code will be released at https://github.com/NKU-HLT/Off-Policy-SFT.

