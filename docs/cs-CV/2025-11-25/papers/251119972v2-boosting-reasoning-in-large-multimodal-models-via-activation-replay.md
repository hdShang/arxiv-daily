---
layout: default
title: Boosting Reasoning in Large Multimodal Models via Activation Replay
---

# Boosting Reasoning in Large Multimodal Models via Activation Replay

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.19972" class="toolbar-btn" target="_blank">📄 arXiv: 2511.19972v2</a>
  <a href="https://arxiv.org/pdf/2511.19972.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.19972v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.19972v2', 'Boosting Reasoning in Large Multimodal Models via Activation Replay')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yun Xing, Xiaobin Hu, Qingdong He, Jiangning Zhang, Shuicheng Yan, Shijian Lu, Yu-Gang Jiang

**分类**: cs.CV

**发布日期**: 2025-11-25 (更新: 2025-11-27)

**备注**: 11 figures, 10 tables

---

## 💡 一句话要点

**提出Activation Replay，通过激活重放提升大型多模态模型推理能力，无需额外训练。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多模态推理` `大型语言模型` `强化学习` `激活重放` `低熵激活` `视觉智能体` `视频理解`

## 📋 核心要点

1. 现有方法对RLVR提升LMM推理能力的机制理解不足，缺乏有效利用激活信息的策略。
2. 提出Activation Replay，通过重放低熵激活来调节RLVR后的LMM，提升推理能力，无需额外训练。
3. 实验表明，Activation Replay在多种推理任务上有效，提升Pass@K指标，并扩大推理覆盖范围。

## 📝 摘要（中文）

本文旨在深入理解使用可验证奖励的强化学习(RLVR)提升大型多模态模型(LMMs)推理能力的内在机制。通过logit lens视角，研究发现RLVR主要影响低熵激活，而对高熵激活影响较小。受此启发，论文提出Activation Replay，一种无需训练的方法，通过在测试时操纵视觉tokens，重放来自基础LMM输入上下文的低熵激活，以调节RLVR后的模型，从而提升多模态推理能力。实验表明，Activation Replay在数学、视觉智能体和视频推理等场景中均能有效提升推理能力，提高Pass@K指标，并缓解RLVR带来的推理覆盖范围缩小问题。对比实验验证了重放低熵激活优于高熵激活，以及操纵输入tokens优于直接跨模型干预。

## 🔬 方法详解

**问题定义**：论文旨在解决大型多模态模型（LMMs）在经过基于可验证奖励的强化学习（RLVR）后，其推理能力提升的内在机制不明确的问题。现有方法缺乏对RLVR如何影响模型内部激活的深入理解，以及如何有效利用这些激活信息来进一步提升推理能力。RLVR虽然能提升推理能力，但也可能导致推理覆盖范围缩小。

**核心思路**：论文的核心思路是观察到RLVR主要影响低熵激活，而对高熵激活影响较小。基于此，论文提出通过在测试时重放低熵激活来调节RLVR后的模型，从而在不进行额外训练的情况下提升推理能力。这种思路的合理性在于，低熵激活可能包含模型推理过程中更关键的信息，通过重放这些激活可以引导模型进行更准确的推理。

**技术框架**：Activation Replay的技术框架主要包含以下几个步骤：1) 使用基础LMM处理输入上下文，获取低熵激活；2) 使用RLVR后的LMM处理相同的输入上下文；3) 在RLVR后的LMM中，通过操纵视觉tokens，重放来自基础LMM的低熵激活；4) 使用重放激活后的RLVR模型进行推理并输出结果。整个过程无需训练，仅在测试阶段进行。

**关键创新**：论文的关键创新在于提出Activation Replay这一简单而有效的训练-free方法，通过重放低熵激活来提升LMM的推理能力。与现有方法相比，Activation Replay不需要额外的训练，可以直接应用于已经经过RLVR训练的模型。此外，论文还通过实验验证了重放低熵激活优于重放高熵激活，以及操纵输入tokens优于直接跨模型干预。

**关键设计**：Activation Replay的关键设计在于如何选择和重放低熵激活。论文通过计算视觉tokens的熵值来选择低熵激活，具体实现细节未知。重放的方式是通过操纵视觉tokens，将基础LMM的低熵激活注入到RLVR后的LMM中。具体操纵方式和参数设置未知。

## 📊 实验亮点

实验结果表明，Activation Replay在数学、视觉智能体和视频推理等多种场景中均能有效提升推理能力。例如，在某些任务上，Pass@K指标得到了显著提升，并且缓解了RLVR带来的推理覆盖范围缩小问题。对比实验验证了重放低熵激活优于高熵激活，以及操纵输入tokens优于直接跨模型干预。

## 🎯 应用场景

Activation Replay具有广泛的应用前景，可以应用于各种需要多模态推理的场景，例如智能客服、自动驾驶、医疗诊断等。该方法无需额外训练，可以快速提升现有LMM的推理能力，具有很高的实际应用价值。未来可以探索如何更有效地选择和重放激活，以及如何将Activation Replay与其他推理增强技术相结合。

## 📄 摘要（原文）

> Recently, Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as an effective approach to incentivizing reasoning capability in Large Multimodal Models (LMMs), while the underlying mechanisms behind this post-training paradigm are poorly understood. We begin by exploring how input activations are affected by RLVR through the perspective of logit lens. Our systematic investigations across multiple post-trained LMMs suggest that RLVR shifts low-entropy activations unexpectedly, while high-entropy ones are less affected. We further demonstrate that such phenomena are associated with LMM reasoning by controlled experiments, suggesting a potentially beneficial role of modulating low-entropy activations. To this end, we propose Activation Replay, a novel simple yet effective training-free approach that boosts multimodal reasoning of post-trained LMMs without requiring expensive policy optimization. Our design involves manipulation of visual tokens at test time, replaying low-entropy activations from the input context of base LMMs to regulating the RLVR counterparts. Activation Replay triggers better reasoning across diverse scenarios, including mathematics, o3-like visual agents, and video reasoning. We further show that Activation Replay boosts Pass@K and mitigates narrower reasoning coverage of RLVR. Our design is compared against alternative choices, such as replaying high-entropy activations instead of low-entropy ones, or direct cross-model intervention instead of manipulating input tokens, demonstrating the superiority of our implementation. Codes will be made publicly available.

