---
layout: default
title: "IN-RIL: Interleaved Reinforcement and Imitation Learning for Policy Fine-Tuning"
---

# IN-RIL: Interleaved Reinforcement and Imitation Learning for Policy Fine-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.10442" class="toolbar-btn" target="_blank">📄 arXiv: 2505.10442v1</a>
  <a href="https://arxiv.org/pdf/2505.10442.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.10442v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.10442v1', 'IN-RIL: Interleaved Reinforcement and Imitation Learning for Policy Fine-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dechen Gao, Hang Wang, Hanchu Zhou, Nejib Ammar, Shatadal Mishra, Ahmadreza Moradipari, Iman Soltani, Junshan Zhang

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-15

**🔗 代码/项目**: [GITHUB](https://github.com/ucd-dare/IN-RIL)

---

## 💡 一句话要点

**提出IN-RIL以解决强化学习微调中的不稳定性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模仿学习` `强化学习` `机器人学习` `策略微调` `样本效率` `梯度分离` `性能提升`

## 📋 核心要点

1. 现有的IL和RL结合方法在RL微调阶段常常面临不稳定性和样本效率低下的问题。
2. IN-RIL通过在多次RL更新后定期注入IL更新，结合了IL的稳定性和RL的探索性。
3. 在多个基准测试中，IN-RIL显著提高了样本效率，成功率提升幅度达到6.3倍。

## 📝 摘要（中文）

模仿学习（IL）和强化学习（RL）各自为机器人策略学习提供了独特的优势：IL通过示范提供稳定的学习，而RL通过探索促进泛化。现有的机器人学习方法通常采用IL预训练后进行RL微调，但这种两步学习范式在RL微调阶段常常面临不稳定性和样本效率低下的问题。为此，本文提出了IN-RIL（交错强化学习与模仿学习），该方法在多次RL更新后定期注入IL更新，从而在整个微调过程中利用IL的稳定性和专家数据的指导。我们还开发了梯度分离机制，以防止在微调过程中可能出现的干扰。通过在14个机器人操作和运动任务上的广泛实验，结果表明IN-RIL显著提高了样本效率，并减轻了在线微调中的性能崩溃。

## 🔬 方法详解

**问题定义**：本文旨在解决现有IL和RL结合方法在RL微调阶段的不稳定性和低样本效率问题。现有方法在RL微调时常常出现性能崩溃，导致学习效果不佳。

**核心思路**：IN-RIL的核心思路是交错使用IL和RL，通过在多次RL更新后定期注入IL更新，利用IL的稳定性和专家数据的指导来提高学习效率。

**技术框架**：IN-RIL的整体架构包括两个主要阶段：首先进行RL更新，然后在适当的时机插入IL更新。通过这种交错方式，IL和RL的优点得以结合。

**关键创新**：最重要的技术创新在于引入了梯度分离机制，以防止在微调过程中可能出现的干扰。这种机制通过在正交子空间中分离可能冲突的梯度更新，确保了学习过程的稳定性。

**关键设计**：在参数设置上，IL和RL的更新频率需要精心设计，以确保两者的有效结合。此外，损失函数的设计也考虑了IL和RL的不同优化目标，以实现更高效的学习。整体网络结构则需支持这种交错更新的策略。

## 📊 实验亮点

在14个机器人操作和运动任务的实验中，IN-RIL显著提高了样本效率，成功率在Robomimic Transport任务中从12%提升至88%，实现了6.3倍的提升，表明该方法在长短期任务中均表现出色。

## 🎯 应用场景

IN-RIL的研究成果在机器人操作和运动任务中具有广泛的应用潜力，能够有效提高机器人在复杂环境中的学习效率和适应能力。未来，该方法可扩展到更多的机器人学习场景，推动智能机器人技术的发展。

## 📄 摘要（原文）

> Imitation learning (IL) and reinforcement learning (RL) each offer distinct advantages for robotics policy learning: IL provides stable learning from demonstrations, and RL promotes generalization through exploration. While existing robot learning approaches using IL-based pre-training followed by RL-based fine-tuning are promising, this two-step learning paradigm often suffers from instability and poor sample efficiency during the RL fine-tuning phase. In this work, we introduce IN-RIL, INterleaved Reinforcement learning and Imitation Learning, for policy fine-tuning, which periodically injects IL updates after multiple RL updates and hence can benefit from the stability of IL and the guidance of expert data for more efficient exploration throughout the entire fine-tuning process. Since IL and RL involve different optimization objectives, we develop gradient separation mechanisms to prevent destructive interference during \ABBR fine-tuning, by separating possibly conflicting gradient updates in orthogonal subspaces. Furthermore, we conduct rigorous analysis, and our findings shed light on why interleaving IL with RL stabilizes learning and improves sample-efficiency. Extensive experiments on 14 robot manipulation and locomotion tasks across 3 benchmarks, including FurnitureBench, OpenAI Gym, and Robomimic, demonstrate that \ABBR can significantly improve sample efficiency and mitigate performance collapse during online finetuning in both long- and short-horizon tasks with either sparse or dense rewards. IN-RIL, as a general plug-in compatible with various state-of-the-art RL algorithms, can significantly improve RL fine-tuning, e.g., from 12\% to 88\% with 6.3x improvement in the success rate on Robomimic Transport. Project page: https://github.com/ucd-dare/IN-RIL.

