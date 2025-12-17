---
layout: default
title: CroSTAta: Cross-State Transition Attention Transformer for Robotic Manipulation
---

# CroSTAta: Cross-State Transition Attention Transformer for Robotic Manipulation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.00726" target="_blank" class="toolbar-btn">arXiv: 2510.00726v1</a>
    <a href="https://arxiv.org/pdf/2510.00726.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00726v1" 
            onclick="toggleFavorite(this, '2510.00726v1', 'CroSTAta: Cross-State Transition Attention Transformer for Robotic Manipulation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Giovanni Minelli, Giulio Turrisi, Victor Barasuol, Claudio Semini

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-10-01

**备注**: Code and data available at https://github.com/iit-DLSLab/croSTAta

---

## 💡 一句话要点

**提出Cross-State Transition Attention Transformer以解决机器人操作中的执行变异问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人操作` `注意力机制` `状态转移` `时间建模` `深度学习` `策略学习` `鲁棒性` `模拟实验`

## 📋 核心要点

1. 现有的机器人操作策略学习方法在面对未覆盖的执行变异时表现不佳，导致鲁棒性不足。
2. 本文提出的Cross-State Transition Attention Transformer通过状态转移注意力机制，基于历史状态演变模式调节注意力权重，从而增强策略的适应性。
3. 在模拟实验中，STA在所有任务上均优于传统的交叉注意力和时间建模方法，如TCN和LSTM，特别是在精度要求高的任务中实现了2倍以上的性能提升。

## 📝 摘要（中文）

通过从示范中学习机器人操作策略，仍然面临执行变异的挑战。尽管通过注意力机制引入历史上下文可以提高鲁棒性，但标准方法在处理所有过去状态时未能明确建模示范中的时间结构。本文提出了一种Cross-State Transition Attention Transformer，采用新颖的状态转移注意力机制（STA），根据学习到的状态演变模式调节标准注意力权重，从而使策略能够更好地根据执行历史调整行为。结合结构化注意力和训练中的时间掩蔽，实验结果表明，STA在所有任务中均优于标准的交叉注意力和时间建模方法，尤其在精度关键任务上实现了超过2倍的提升。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人操作策略在执行过程中遇到的变异问题，现有方法未能有效处理示范中的时间结构，导致策略鲁棒性不足。

**核心思路**：提出的Cross-State Transition Attention Transformer通过引入状态转移注意力机制，能够根据历史状态演变模式动态调整注意力权重，从而使策略更好地适应执行历史。

**技术框架**：该方法的整体架构包括状态转移注意力机制、时间掩蔽训练和标准注意力模块。通过对历史状态的建模，增强了策略的时间推理能力。

**关键创新**：最重要的技术创新在于状态转移注意力机制的引入，它与传统的交叉注意力方法相比，能够更有效地捕捉状态演变的模式，从而提升策略的适应性。

**关键设计**：在网络结构上，采用了多层Transformer架构，并在训练过程中引入时间掩蔽策略，以随机去除最近时间步的视觉信息，促进模型从历史上下文中进行推理。损失函数设计上，结合了标准的回归损失和基于注意力的损失，确保模型在学习过程中关注重要的历史信息。

## 📊 实验亮点

实验结果显示，Cross-State Transition Attention Transformer在所有任务中均优于传统的交叉注意力和时间建模方法，特别是在精度关键任务上，性能提升超过2倍，证明了该方法在实际应用中的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括工业机器人、服务机器人和自主系统等，能够显著提升机器人在复杂环境中的操作能力和适应性。未来，该方法可能推动更智能的机器人系统的发展，使其在动态和不确定的环境中表现更为出色。

## 📄 摘要（原文）

> Learning robotic manipulation policies through supervised learning from demonstrations remains challenging when policies encounter execution variations not explicitly covered during training. While incorporating historical context through attention mechanisms can improve robustness, standard approaches process all past states in a sequence without explicitly modeling the temporal structure that demonstrations may include, such as failure and recovery patterns. We propose a Cross-State Transition Attention Transformer that employs a novel State Transition Attention (STA) mechanism to modulate standard attention weights based on learned state evolution patterns, enabling policies to better adapt their behavior based on execution history. Our approach combines this structured attention with temporal masking during training, where visual information is randomly removed from recent timesteps to encourage temporal reasoning from historical context. Evaluation in simulation shows that STA consistently outperforms standard cross-attention and temporal modeling approaches like TCN and LSTM networks across all tasks, achieving more than 2x improvement over cross-attention on precision-critical tasks.

