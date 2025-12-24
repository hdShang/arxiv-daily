---
layout: default
title: Interactive Post-Training for Vision-Language-Action Models
---

# Interactive Post-Training for Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.17016" class="toolbar-btn" target="_blank">📄 arXiv: 2505.17016v1</a>
  <a href="https://arxiv.org/pdf/2505.17016.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.17016v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.17016v1', 'Interactive Post-Training for Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuhan Tan, Kairan Dou, Yue Zhao, Philipp Krähenbühl

**分类**: cs.LG, cs.AI, cs.CV, cs.RO

**发布日期**: 2025-05-22

**备注**: Project page: https://ariostgx.github.io/ript_vla/

---

## 💡 一句话要点

**提出RIPT-VLA以解决VLA模型适应性不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `强化学习` `后训练` `稀疏奖励` `模型微调` `动态回滚采样` `优势估计` `适应性学习`

## 📋 核心要点

1. 现有的VLA训练方法过于依赖专家示范数据，导致在新任务和低数据环境下适应性不足。
2. RIPT-VLA通过强化学习的交互式后训练，利用稀疏的成功奖励进行模型微调，提升了适应性。
3. 实验结果显示，RIPT-VLA在多个模型上均取得显著提升，特别是7B OpenVLA-OFT模型成功率达到97.5%。

## 📝 摘要（中文）

我们介绍了RIPT-VLA，这是一种简单且可扩展的基于强化学习的交互式后训练范式，旨在通过稀疏的二元成功奖励对预训练的视觉-语言-动作（VLA）模型进行微调。现有的VLA训练流程严重依赖离线专家示范数据和监督模仿，限制了它们在低数据环境下适应新任务和新环境的能力。RIPT-VLA通过动态回滚采样和逐一优势估计的稳定策略优化算法，解决了这一问题。RIPT-VLA适用于多种VLA模型，显著提高了轻量级QueST模型的性能21.2%，并使7B OpenVLA-OFT模型的成功率达到了前所未有的97.5%。此外，RIPT-VLA在仅需一个示范的情况下，使得原本无法工作的SFT模型（4%）在15次迭代内成功率达到了97%。

## 🔬 方法详解

**问题定义**：论文旨在解决现有视觉-语言-动作（VLA）模型在新任务和低数据环境下适应性不足的问题。现有方法依赖大量的离线专家示范数据和监督模仿，限制了模型的灵活性和泛化能力。

**核心思路**：RIPT-VLA提出了一种基于强化学习的交互式后训练方法，通过稀疏的二元成功奖励进行微调，允许模型在少量示范下进行有效学习，从而增强其适应性和泛化能力。

**技术框架**：RIPT-VLA的整体架构包括动态回滚采样和逐一优势估计两个主要模块。动态回滚采样用于生成训练样本，而逐一优势估计则用于稳定策略优化，确保模型在训练过程中的收敛性。

**关键创新**：RIPT-VLA的核心创新在于其能够在仅有稀疏奖励的情况下进行有效的后训练，显著降低了对大量示范数据的依赖。这一方法与传统的监督学习方法有本质区别，后者通常需要大量的标注数据。

**关键设计**：在参数设置上，RIPT-VLA采用了动态回滚采样策略，以提高样本的多样性和代表性。同时，损失函数设计上注重于稀疏奖励的有效利用，确保模型能够在有限的信息下进行有效学习。

## 📊 实验亮点

RIPT-VLA在多个模型上取得了显著的实验结果，特别是轻量级QueST模型性能提升21.2%，而7B OpenVLA-OFT模型成功率达到了97.5%。此外，该方法在仅需一个示范的情况下，使得原本成功率仅为4%的SFT模型在15次迭代内成功率提升至97%。

## 🎯 应用场景

RIPT-VLA的研究成果具有广泛的潜在应用场景，尤其是在机器人控制、自动驾驶、智能助手等领域。通过减少对大量示范数据的依赖，该方法能够使得模型在新环境和新任务中快速适应，提升实际应用的灵活性和效率。未来，RIPT-VLA有望推动多模态学习和人机交互的进一步发展。

## 📄 摘要（原文）

> We introduce RIPT-VLA, a simple and scalable reinforcement-learning-based interactive post-training paradigm that fine-tunes pretrained Vision-Language-Action (VLA) models using only sparse binary success rewards. Existing VLA training pipelines rely heavily on offline expert demonstration data and supervised imitation, limiting their ability to adapt to new tasks and environments under low-data regimes. RIPT-VLA addresses this by enabling interactive post-training with a stable policy optimization algorithm based on dynamic rollout sampling and leave-one-out advantage estimation.
>   RIPT-VLA has the following characteristics. First, it applies to various VLA models, resulting in an improvement on the lightweight QueST model by 21.2%, and the 7B OpenVLA-OFT model to an unprecedented 97.5% success rate. Second, it is computationally efficient and data-efficient: with only one demonstration, RIPT-VLA enables an unworkable SFT model (4%) to succeed with a 97% success rate within 15 iterations. Furthermore, we demonstrate that the policy learned by RIPT-VLA generalizes across different tasks and scenarios and is robust to the initial state context. These results highlight RIPT-VLA as a practical and effective paradigm for post-training VLA models through minimal supervision.

