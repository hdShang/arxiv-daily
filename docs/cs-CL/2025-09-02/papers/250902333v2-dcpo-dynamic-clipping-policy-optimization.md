---
layout: default
title: "DCPO: Dynamic Clipping Policy Optimization"
---

# DCPO: Dynamic Clipping Policy Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02333" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02333v2</a>
  <a href="https://arxiv.org/pdf/2509.02333.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02333v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02333v2', 'DCPO: Dynamic Clipping Policy Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shihui Yang, Chengfeng Dou, Peidong Guo, Kai Lu, Qiang Ju, Fei Deng, Rihui Xin

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-02 (更新: 2025-09-08)

---

## 💡 一句话要点

**DCPO：动态裁剪策略优化，提升LLM在可验证奖励下的推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `策略优化` `动态裁剪` `可验证奖励`

## 📋 核心要点

1. 现有RLVR方法（如GRPO）在训练LLM时存在梯度消失问题，限制了模型性能。
2. DCPO通过动态调整裁剪边界和使用平滑优势标准化，增强token级别探索和响应利用率。
3. 实验表明，DCPO在多个基准测试中超越现有方法，显著提升了LLM的推理能力和训练效率。

## 📝 摘要（中文）

本文提出动态裁剪策略优化（DCPO），旨在提升大型语言模型在可验证奖励下的强化学习（RLVR）框架中的推理能力。现有方法如GRPO常面临梯度消失问题，主要原因是token级别概率比率的固定裁剪边界以及相同奖励的标准化，导致梯度更新效率低下，生成响应的利用率不足。DCPO引入了一种动态裁剪策略，基于token特定的先验概率自适应地调整裁剪边界，以增强token级别的探索。同时，采用平滑优势标准化技术，在累积训练步骤中标准化奖励，以提高响应级别的生成响应有效利用率。在四个基准测试和四个不同模型上，DCPO均取得了最先进的性能。例如，在Qwen2.5-Math-7B模型上，AIME24基准测试中，贪婪解码下Avg@1达到46.7，32次采样下Avg@32达到38.8，超过了DAPO、GRPO和GSPO。

## 🔬 方法详解

**问题定义**：现有基于可验证奖励的强化学习方法，如GRPO，在训练大型语言模型时，由于token级别概率比率的固定裁剪边界和相同奖励的标准化，导致梯度消失，使得模型无法有效学习和利用生成的数据，最终限制了模型的推理能力。

**核心思路**：DCPO的核心思路是通过动态调整裁剪边界来增强token级别的探索，并使用平滑优势标准化来提高响应级别的生成响应利用率。动态裁剪边界允许模型在训练初期进行更广泛的探索，避免过早收敛到局部最优解。平滑优势标准化则确保奖励信号在训练过程中更加稳定和有效。

**技术框架**：DCPO的整体框架仍然是基于强化学习的策略优化，但其关键在于两个核心模块的改进：一是动态裁剪模块，用于自适应地调整token级别概率比率的裁剪边界；二是平滑优势标准化模块，用于在累积训练步骤中标准化奖励。整个流程包括：模型生成响应、计算奖励、动态裁剪概率比率、标准化优势函数、更新策略。

**关键创新**：DCPO最重要的创新点在于动态裁剪策略。与固定裁剪边界不同，DCPO根据token特定的先验概率自适应地调整裁剪边界。这意味着对于那些模型不太确定的token，裁剪边界会更宽松，允许模型进行更多的探索。这种动态调整机制能够有效地避免梯度消失问题，并提高模型的学习效率。

**关键设计**：动态裁剪边界的计算方式是基于token的先验概率。具体来说，裁剪边界可以设置为先验概率的函数，例如，裁剪范围可以与先验概率成反比。平滑优势标准化则通过在累积训练步骤中计算移动平均和标准差来实现。损失函数仍然是基于策略梯度的损失函数，但加入了动态裁剪和优势标准化后的梯度。

## 📊 实验亮点

DCPO在AIME24基准测试中，Qwen2.5-Math-7B模型上，贪婪解码下Avg@1达到46.7，32次采样下Avg@32达到38.8，显著超越DAPO (36.7/31.6)、GRPO (36.7/32.1)和GSPO (40.0/34.9)。在AIME25基准测试中，Qwen2.5-14B模型上，DCPO达到(23.3/19.0)，超过GRPO (13.3/10.5)、DAPO (20.0/15.3)和GSPO (16.7/9.9)。DCPO在四个模型上的非零优势平均提升了28%，训练效率是DAPO的两倍，token裁剪率也显著降低。

## 🎯 应用场景

DCPO具有广泛的应用前景，可用于提升大型语言模型在各种需要推理和决策的任务中的性能，例如数学问题求解、代码生成、知识问答等。通过更有效地利用生成数据进行强化学习，DCPO可以帮助模型更好地理解和掌握复杂任务的逻辑和规则，从而提高其解决问题的能力。此外，该方法还可以应用于其他序列生成任务，例如机器翻译和文本摘要。

## 📄 摘要（原文）

> Reinforcement Learning from Verifiable Rewards (RLVR) has emerged as a promising framework for enhancing the reasoning capabilities of large language models. However, existing approaches such as GRPO often suffer from zero gradients. This problem arises primarily due to fixed clipping bounds for token-level probability ratios and the standardization of identical rewards, which can lead to ineffective gradient updates and underutilization of generated responses. In this work, we propose Dynamic Clipping Policy Optimization(DCPO), which introduces a dynamic clipping strategy that adaptively adjusts clipping bounds based on token-specific prior probabilities to enhance token-level exploration, and a smooth advantage standardization technique that standardizes rewards across cumulative training steps to improve the response-level effective utilization of generated responses. DCPO achieved state-of-the-art performance on four benchmarks based on four different models. In particular, DCPO achieved an Avg@1 of 46.7 under greedy decoding and an Avg@32 of 38.8 under 32 times sampling on the AIME24 benchmark, surpassing DAPO (36.7/31.6), GRPO (36.7/32.1) and GSPO (40.0/34.9) on the Qwen2.5-Math-7B model. On the AIME25 benchmark based on Qwen2.5-14B, DCPO achieves a performance of (23.3/19.0), surpassing GRPO (13.3/10.5), DAPO (20.0/15.3) and GSPO (16.7/9.9). Furthermore, DCPO achieved an average 28% improvement in the nonzero advantage over GRPO in four models, doubled the training efficiency over DAPO, and significantly reduced the token clipping ratio by an order of magnitude compared to both GRPO and DAPO, while achieving superior performance. These results highlight DCPO's effectiveness in leveraging generated data more efficiently for reinforcement learning in large language models.

