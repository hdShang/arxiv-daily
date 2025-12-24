---
layout: default
title: "SeqVLA: Sequential Task Execution for Long-Horizon Manipulation with Completion-Aware Vision-Language-Action Model"
---

# SeqVLA: Sequential Task Execution for Long-Horizon Manipulation with Completion-Aware Vision-Language-Action Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14138" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14138v1</a>
  <a href="https://arxiv.org/pdf/2509.14138.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14138v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14138v1', 'SeqVLA: Sequential Task Execution for Long-Horizon Manipulation with Completion-Aware Vision-Language-Action Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ran Yang, Zijian An, Lifeng ZHou, Yiming Feng

**分类**: cs.RO

**发布日期**: 2025-09-17

**备注**: 8 pages, 9 figures, 1 table

---

## 💡 一句话要点

**SeqVLA：用于长时程操作的具有完成感知能力的视觉-语言-动作模型，解决序列任务执行问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `视觉语言动作模型` `序列任务执行` `完成感知` `长时程任务`

## 📋 核心要点

1. 现有VLA模型在长时程序列操作任务中，缺乏子任务完成状态的内部信号，导致任务失败。
2. SeqVLA通过增加一个轻量级的检测头来感知子任务完成状态，从而实现自主子任务切换。
3. 实验表明，SeqVLA在沙拉和糖果包装任务中显著优于基线模型，提升了整体成功率。

## 📝 摘要（中文）

长时程机器人操作任务需要在严格的序列中执行多个相互依赖的子任务，而检测子任务完成情况时出现的错误可能会导致下游任务失败。现有的视觉-语言-动作（VLA）模型，如$π_0$，擅长连续的低级控制，但缺乏识别子任务何时完成的内部信号，这使得它们在序列设置中显得脆弱。我们提出了SeqVLA，它是$π_0$的一个完成感知扩展，通过增加一个轻量级的检测头来感知当前子任务是否完成，从而增强了基础架构。这种双头设计使SeqVLA不仅能够生成操作动作，还能够自主地触发子任务之间的转换。我们研究了四种微调策略，这些策略在如何优化动作头和检测头（联合微调与顺序微调）以及如何保留预训练知识（完全微调与冻结骨干网络）方面有所不同。在两个多阶段任务（包含七个不同子任务的沙拉包装和包含四个不同子任务的糖果包装）上进行的实验表明，SeqVLA在总体成功率方面显著优于基线$π_0$和其他强大的基线。特别是，具有未冻结骨干网络的联合微调产生了最果断和统计上可靠的完成预测，消除了与序列相关的失败，并实现了稳健的长时程执行。我们的结果强调了将动作生成与子任务感知检测相结合对于可扩展的序列操作的重要性。

## 🔬 方法详解

**问题定义**：现有的视觉-语言-动作（VLA）模型，例如$π_0$，在连续的低级控制方面表现出色，但缺乏判断子任务何时完成的内部信号。这导致它们在需要按顺序执行多个子任务的长时程操作任务中表现脆弱，子任务完成状态判断错误会传递到后续任务，造成级联失败。

**核心思路**：SeqVLA的核心思路是在现有的VLA模型基础上，增加一个专门用于检测当前子任务是否完成的检测头。通过这个检测头，模型可以自主判断何时从一个子任务切换到下一个子任务，从而提高在序列任务中的鲁棒性。

**技术框架**：SeqVLA的整体架构是在原有VLA模型（如$π_0$）的基础上增加一个轻量级的检测头。该检测头接收与动作生成头相同的输入（视觉和语言信息），并输出一个表示当前子任务是否完成的信号。整个模型包含两个头：动作生成头和完成检测头。模型通过联合或顺序微调的方式进行训练。

**关键创新**：SeqVLA的关键创新在于将动作生成和子任务完成状态检测相结合。以往的VLA模型只关注动作生成，而忽略了对任务状态的感知。通过增加完成检测头，SeqVLA能够更好地理解任务的进展，从而更有效地执行序列任务。

**关键设计**：论文研究了四种微调策略：(1) 联合微调且骨干网络不冻结；(2) 联合微调且骨干网络冻结；(3) 顺序微调且骨干网络不冻结；(4) 顺序微调且骨干网络冻结。实验结果表明，联合微调且骨干网络不冻结的策略效果最佳。检测头的设计采用轻量级结构，以减少计算负担。损失函数的设计需要平衡动作生成和完成检测两个任务。

## 📊 实验亮点

SeqVLA在沙拉包装和糖果包装两个多阶段任务上进行了评估，结果表明，SeqVLA在总体成功率方面显著优于基线$π_0$和其他强大的基线。特别是，采用联合微调且骨干网络不冻结的策略时，SeqVLA能够产生最可靠的完成预测，从而消除了与序列相关的失败，并实现了稳健的长时程执行。具体性能数据在论文中有详细展示。

## 🎯 应用场景

SeqVLA具有广泛的应用前景，例如在智能制造、自动化装配、家庭服务机器人等领域。它可以应用于需要执行多个步骤才能完成的复杂任务，例如产品组装、食品制作、家居清洁等。通过提高机器人在序列任务中的鲁棒性和效率，SeqVLA可以降低人工成本，提高生产效率，并改善用户体验。

## 📄 摘要（原文）

> Long-horizon robotic manipulation tasks require executing multiple interdependent subtasks in strict sequence, where errors in detecting subtask completion can cascade into downstream failures. Existing Vision-Language-Action (VLA) models such as $π_0$ excel at continuous low-level control but lack an internal signal for identifying when a subtask has finished, making them brittle in sequential settings. We propose SeqVLA, a completion-aware extension of $π_0$ that augments the base architecture with a lightweight detection head perceiving whether the current subtask is complete. This dual-head design enables SeqVLA not only to generate manipulation actions but also to autonomously trigger transitions between subtasks. We investigate four finetuning strategies that vary in how the action and detection heads are optimized (joint vs. sequential finetuning) and how pretrained knowledge is preserved (full finetuning vs. frozen backbone). Experiments are performed on two multi-stage tasks: salad packing with seven distinct subtasks and candy packing with four distinct subtasks. Results show that SeqVLA significantly outperforms the baseline $π_0$ and other strong baselines in overall success rate. In particular, joint finetuning with an unfrozen backbone yields the most decisive and statistically reliable completion predictions, eliminating sequence-related failures and enabling robust long-horizon execution. Our results highlight the importance of coupling action generation with subtask-aware detection for scalable sequential manipulation.

