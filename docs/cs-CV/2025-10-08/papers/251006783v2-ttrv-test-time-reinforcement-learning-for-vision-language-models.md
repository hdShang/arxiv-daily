---
layout: default
title: "TTRV: Test-Time Reinforcement Learning for Vision Language Models"
---

# TTRV: Test-Time Reinforcement Learning for Vision Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.06783" class="toolbar-btn" target="_blank">📄 arXiv: 2510.06783v2</a>
  <a href="https://arxiv.org/pdf/2510.06783.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.06783v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.06783v2', 'TTRV: Test-Time Reinforcement Learning for Vision Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Akshit Singh, Shyam Marjit, Wei Lin, Paul Gavrikov, Serena Yeung-Levy, Hilde Kuehne, Rogerio Feris, Sivan Doveh, James Glass, M. Jehanzeb Mirza

**分类**: cs.CV

**发布日期**: 2025-10-08 (更新: 2025-12-04)

---

## 💡 一句话要点

**提出TTRV：一种用于视觉语言模型的测试时强化学习方法，无需标注数据。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `测试时强化学习` `视觉语言模型` `无监督学习` `模型自适应` `Group Relative Policy Optimization`

## 📋 核心要点

1. 现有强化学习方法依赖标注数据和专用训练集，与人类直接从环境中学习的方式不同，限制了模型的泛化能力。
2. TTRV通过在测试时动态调整模型，利用基础模型的输出频率设计奖励，并鼓励模型输出多样性，从而提升模型性能。
3. 实验表明，TTRV在图像识别和VQA任务上均取得了显著提升，甚至超越了GPT-4o等强大的专有模型。

## 📝 摘要（中文）

本文提出TTRV，一种在推理时动态调整视觉语言模型的方法，以增强其视觉语言理解能力，无需任何标注数据。TTRV通过改进Group Relative Policy Optimization (GRPO)框架实现，基于基础模型输出的频率设计奖励，并在每个测试样本上多次推理。此外，通过奖励模型以获得低熵的输出经验分布，来控制模型输出的多样性。在对象识别和视觉问答(VQA)任务中，该方法均取得了显著提升，分别高达52.4%和29.8%，在16个数据集上的平均提升分别为24.6%和10.0%。在图像识别方面，应用于InternVL 8B的TTRV超过了GPT-4o，在8个基准测试中平均提升了2.3%。在VQA任务中也保持了竞争力，证明了测试时强化学习可以匹敌甚至超越最强的专有模型。即使在数据极度受限的情况下，即仅在单个随机选择的未标记测试样本上进行调整，TTRV在识别任务中仍然可以产生高达5.5%的显著改进。

## 🔬 方法详解

**问题定义**：现有视觉语言模型在实际应用中，往往需要针对特定任务进行微调，而微调通常依赖大量的标注数据，成本高昂。此外，预训练模型在面对新的、未知的测试数据时，性能可能会下降。因此，如何在不依赖标注数据的情况下，提升模型在测试时的泛化能力是一个重要的挑战。

**核心思路**：TTRV的核心思路是在测试时利用强化学习动态调整模型的行为，使其更好地适应当前的测试样本。通过设计合适的奖励函数，引导模型探索不同的输出，并选择最优的策略。这种方法无需标注数据，可以在推理过程中持续改进模型性能。

**技术框架**：TTRV基于Group Relative Policy Optimization (GRPO)框架。整体流程如下：1) 对每个测试样本，模型进行多次推理，生成多个候选输出；2) 根据基础模型的输出频率和输出分布的熵，计算每个候选输出的奖励；3) 使用GRPO算法更新模型的策略，使其倾向于产生更高奖励的输出。这个过程在测试时循环进行，直到模型收敛或达到预定的迭代次数。

**关键创新**：TTRV的关键创新在于提出了基于模型自身输出频率和输出分布熵的奖励函数。传统的强化学习方法通常需要外部的奖励信号，而TTRV利用模型自身的输出作为奖励的来源，实现了无监督的测试时自适应。此外，通过引入输出分布熵的奖励，鼓励模型探索更多样化的输出，避免陷入局部最优。

**关键设计**：奖励函数的设计是TTRV的关键。具体来说，奖励函数包含两部分：一部分基于基础模型输出的频率，鼓励模型产生更常见的输出；另一部分基于输出分布的熵，鼓励模型探索更多样化的输出。这两个部分通过加权求和的方式结合在一起，权重系数需要根据具体任务进行调整。此外，GRPO算法的学习率和迭代次数也是重要的超参数，需要根据实验结果进行优化。

## 📊 实验亮点

TTRV在多个视觉语言任务上取得了显著的性能提升。在图像识别任务中，TTRV应用于InternVL 8B模型，在8个基准测试中平均超越GPT-4o 2.3%。在视觉问答任务中，TTRV在16个数据集上的平均提升为10.0%，最高提升达到29.8%。即使在数据极度受限的情况下，TTRV仍然可以产生显著的改进，证明了其强大的自适应能力。

## 🎯 应用场景

TTRV具有广泛的应用前景，可以应用于各种视觉语言任务，例如图像识别、视觉问答、图像描述等。该方法尤其适用于数据标注成本高昂或难以获取的场景。通过在测试时动态调整模型，可以显著提升模型的泛化能力和鲁棒性，使其更好地适应实际应用环境。未来，可以将TTRV与其他自监督学习方法相结合，进一步提升模型性能。

## 📄 摘要（原文）

> Existing methods for extracting reward signals in Reinforcement Learning typically rely on labeled data and dedicated training splits, a setup that contrasts with how humans learn directly from their environment. In this work, we propose TTRV to enhance vision language understanding by adapting the model on the fly at inference time, without the need for any labeled data. Concretely, we enhance the Group Relative Policy Optimization (GRPO) framework by designing rewards based on the frequency of the base model's output, while inferring on each test sample multiple times. Further, we also propose to control the diversity of the model's output by simultaneously rewarding the model for obtaining low entropy of the output empirical distribution. Our approach delivers consistent gains across both object recognition and visual question answering (VQA), with improvements of up to 52.4% and 29.8%, respectively, and average boosts of 24.6% and 10.0% across 16 datasets. Remarkably, on image recognition, TTRV applied to InternVL 8B surpasses GPT-4o by an average of 2.3% over 8 benchmarks, while remaining highly competitive on VQA, demonstrating that test-time reinforcement learning can match or exceed the strongest proprietary models. Finally, we find many interesting properties of test-time RL for VLMs: for example, even in extremely data-constrained scenarios, where adaptation is performed on a single randomly chosen unlabeled test example, TTRV still yields non-trivial improvements of up to 5.5% in recognition tasks.

