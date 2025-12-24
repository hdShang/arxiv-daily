---
layout: default
title: Active Intelligence in Video Avatars via Closed-loop World Modeling
---

# Active Intelligence in Video Avatars via Closed-loop World Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20615" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20615v1</a>
  <a href="https://arxiv.org/pdf/2512.20615.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20615v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20615v1', 'Active Intelligence in Video Avatars via Closed-loop World Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuanhua He, Tianyu Yang, Ke Cao, Ruiqi Wu, Cheng Meng, Yong Zhang, Zhuoliang Kang, Xiaoming Wei, Qifeng Chen

**分类**: cs.CV

**发布日期**: 2025-12-23

**备注**: Project Page: https://xuanhuahe.github.io/ORCA/

---

## 💡 一句话要点

**提出ORCA框架，通过闭环世界建模实现视频化身的主动智能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视频化身` `主动智能` `闭环控制` `世界模型` `POMDP`

## 📋 核心要点

1. 现有视频化身方法缺乏自主性，无法在复杂环境中完成长期目标，限制了其应用。
2. ORCA框架通过闭环OTAR循环和分层双系统架构，使视频化身具备内部世界模型和主动智能。
3. 实验表明，ORCA在任务成功率和行为连贯性方面显著优于现有方法，验证了其有效性。

## 📝 摘要（中文）

现有的视频化身生成方法擅长保持身份和对齐动作，但缺乏真正的自主性，无法通过自适应环境交互自主地追求长期目标。为了解决这个问题，我们提出了L-IVA（Long-horizon Interactive Visual Avatar），这是一个用于评估随机生成环境中目标导向规划的任务和基准。同时，我们提出了ORCA（Online Reasoning and Cognitive Architecture），这是第一个使视频化身具备主动智能的框架。ORCA通过两个关键创新体现了内部世界模型（IWM）的能力：（1）一个闭环的OTAR循环（观察-思考-行动-反思），通过持续验证预测结果与实际生成结果，在生成不确定性下保持鲁棒的状态跟踪；（2）一个分层的双系统架构，其中系统2利用状态预测执行战略推理，而系统1将抽象计划转化为精确的、特定于模型的动作描述。通过将化身控制建模为POMDP，并使用结果验证实现连续的信念更新，ORCA能够在开放域场景中实现自主的多步骤任务完成。大量的实验表明，ORCA在任务成功率和行为连贯性方面显著优于开放循环和非反思基线，验证了我们受IWM启发的、将视频化身智能从被动动画提升到主动的、目标导向行为的设计。

## 🔬 方法详解

**问题定义**：现有视频化身生成方法主要关注身份保持和动作对齐，缺乏自主性和与环境交互的能力。它们无法像智能体一样，根据环境变化调整行为，从而完成复杂的、长期的目标。现有方法通常是开环的，无法处理生成过程中的不确定性，导致行为不连贯和任务失败。

**核心思路**：ORCA的核心思路是赋予视频化身一个内部世界模型（IWM），使其能够像人类一样，通过观察、思考、行动和反思来理解环境并做出决策。通过闭环的反馈机制，ORCA可以不断修正对环境的理解，从而在不确定性中保持鲁棒性。分层双系统架构则模拟了人类的认知过程，将战略推理和具体动作执行分离，提高了效率和灵活性。

**技术框架**：ORCA框架包含以下几个主要模块：1) **观察模块**：接收环境的视觉输入；2) **思考模块（系统2）**：基于内部世界模型进行战略推理，生成抽象的行动计划；3) **行动模块（系统1）**：将抽象计划转化为具体的、特定于模型的动作描述；4) **生成模块**：根据动作描述生成视频化身的行为；5) **反思模块**：将生成的行为与预测结果进行比较，更新内部世界模型。整个流程构成一个闭环的OTAR循环。框架将化身控制建模为POMDP（部分可观测马尔可夫决策过程），并使用结果验证进行连续的信念更新。

**关键创新**：ORCA的关键创新在于其闭环的OTAR循环和分层双系统架构。OTAR循环通过持续验证预测结果，解决了生成过程中的不确定性问题，提高了状态跟踪的鲁棒性。分层双系统架构将战略推理和具体动作执行分离，提高了决策效率和灵活性。与现有方法的本质区别在于，ORCA赋予了视频化身主动智能，使其能够自主地与环境交互并完成长期目标。

**关键设计**：ORCA使用Transformer网络作为系统2的战略推理模块，预测未来的状态和奖励。系统1使用条件生成模型，将抽象的行动计划转化为具体的动作描述。损失函数包括状态预测损失、奖励预测损失和行为连贯性损失。OTAR循环中的验证机制采用阈值判断，当预测结果与实际生成结果的差异超过阈值时，触发内部世界模型的更新。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20615v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20615v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20615v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，ORCA在L-IVA基准测试中显著优于开放循环和非反思基线。在任务成功率方面，ORCA比最佳基线提高了约20%。在行为连贯性方面，ORCA生成的视频化身行为更加自然和流畅，减少了不必要的动作和停顿。

## 🎯 应用场景

ORCA框架具有广泛的应用前景，例如智能助手、虚拟社交、游戏AI和远程呈现等。它可以使虚拟化身更加智能、自然和具有互动性，从而提升用户体验。未来，ORCA可以应用于更复杂的场景，例如教育、医疗和工业等领域，实现更高级的人机协作。

## 📄 摘要（原文）

> Current video avatar generation methods excel at identity preservation and motion alignment but lack genuine agency, they cannot autonomously pursue long-term goals through adaptive environmental interaction. We address this by introducing L-IVA (Long-horizon Interactive Visual Avatar), a task and benchmark for evaluating goal-directed planning in stochastic generative environments, and ORCA (Online Reasoning and Cognitive Architecture), the first framework enabling active intelligence in video avatars. ORCA embodies Internal World Model (IWM) capabilities through two key innovations: (1) a closed-loop OTAR cycle (Observe-Think-Act-Reflect) that maintains robust state tracking under generative uncertainty by continuously verifying predicted outcomes against actual generations, and (2) a hierarchical dual-system architecture where System 2 performs strategic reasoning with state prediction while System 1 translates abstract plans into precise, model-specific action captions. By formulating avatar control as a POMDP and implementing continuous belief updating with outcome verification, ORCA enables autonomous multi-step task completion in open-domain scenarios. Extensive experiments demonstrate that ORCA significantly outperforms open-loop and non-reflective baselines in task success rate and behavioral coherence, validating our IWM-inspired design for advancing video avatar intelligence from passive animation to active, goal-oriented behavior.

