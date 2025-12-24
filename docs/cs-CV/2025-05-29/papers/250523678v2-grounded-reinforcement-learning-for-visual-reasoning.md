---
layout: default
title: Grounded Reinforcement Learning for Visual Reasoning
---

# Grounded Reinforcement Learning for Visual Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23678" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23678v2</a>
  <a href="https://arxiv.org/pdf/2505.23678.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23678v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23678v2', 'Grounded Reinforcement Learning for Visual Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gabriel Sarch, Snigdha Saha, Naitik Khandelwal, Ayush Jain, Michael J. Tarr, Aviral Kumar, Katerina Fragkiadaki

**分类**: cs.CV

**发布日期**: 2025-05-29 (更新: 2025-10-20)

**备注**: Project website: https://visually-grounded-rl.github.io/

---

## 💡 一句话要点

**提出ViGoRL以解决视觉推理中的空间定位问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉推理` `强化学习` `多模态学习` `空间定位` `视觉注意力` `人机交互` `模型评估`

## 📋 核心要点

1. 现有方法在视觉推理中缺乏有效的空间定位能力，导致模型无法准确引导视觉注意力。
2. ViGoRL通过强化学习将推理步骤与视觉坐标相结合，模拟人类的视觉决策过程，提升推理的空间基础性。
3. 在多个视觉推理基准上，ViGoRL超越了传统的监督微调和缺乏明确基础机制的RL基线，显示出显著的性能提升。

## 📝 摘要（中文）

尽管强化学习（RL）在数学和编程等任务中显著提升了语言模型的能力，但视觉推理增加了复杂性，要求模型引导视觉注意力、解释感知输入，并将抽象推理与空间证据相结合。本文提出了ViGoRL（视觉基础强化学习），该模型通过RL训练，明确将每个推理步骤锚定到特定的视觉坐标。ViGoRL学习生成空间基础的推理轨迹，在每一步引导视觉注意力到任务相关区域。通过多轮RL框架，模型能够在推理过程中动态放大预测坐标。实验结果表明，ViGoRL在多个视觉推理基准上表现优异，尤其在小型GUI元素定位和视觉搜索任务中，达到了86.4%的V*Bench成绩。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉推理中模型无法有效引导视觉注意力和空间定位的问题。现有方法在处理复杂视觉信息时，往往缺乏将推理与视觉输入结合的能力，导致推理结果不够准确。

**核心思路**：ViGoRL的核心思想是通过强化学习将每个推理步骤与具体的视觉坐标锚定，从而实现空间基础的推理过程。这种设计灵感来源于人类的视觉决策过程，能够更好地引导模型关注任务相关的视觉区域。

**技术框架**：ViGoRL的整体架构包括多个模块：首先是视觉输入的处理模块，其次是推理过程中的动态坐标预测模块，最后是多轮RL框架，允许模型在推理过程中进行细致的视觉探索。

**关键创新**：ViGoRL的主要创新在于引入了多轮RL与放大视觉反馈的结合，使得模型能够在推理过程中动态调整视觉注意力。这一机制与传统RL方法的静态推理方式形成了鲜明对比。

**关键设计**：在模型设计中，采用了特定的损失函数来优化空间定位的准确性，并通过调整网络结构来增强模型对视觉输入的敏感性。具体的参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

ViGoRL在多个视觉推理基准上表现出色，尤其在V*Bench上达到了86.4%的准确率，显著超越了传统的监督微调和缺乏明确基础机制的RL基线。这表明视觉基础的强化学习在提升模型推理能力方面具有强大的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动驾驶、机器人视觉等，能够提升机器在复杂视觉环境中的推理能力和决策效率。未来，ViGoRL可能在更广泛的视觉推理任务中发挥重要作用，推动人机交互和自动化技术的发展。

## 📄 摘要（原文）

> While reinforcement learning (RL) over chains of thought has significantly advanced language models in tasks such as mathematics and coding, visual reasoning introduces added complexity by requiring models to direct visual attention, interpret perceptual inputs, and ground abstract reasoning in spatial evidence. We introduce ViGoRL (Visually Grounded Reinforcement Learning), a vision-language model trained with RL to explicitly anchor each reasoning step to specific visual coordinates. Inspired by human visual decision-making, ViGoRL learns to produce spatially grounded reasoning traces, guiding visual attention to task-relevant regions at each step. When fine-grained exploration is required, our novel multi-turn RL framework enables the model to dynamically zoom into predicted coordinates as reasoning unfolds. Across a diverse set of visual reasoning benchmarks--including SAT-2 and BLINK for spatial reasoning, V*bench for visual search, and ScreenSpot and VisualWebArena for web-based grounding--ViGoRL consistently outperforms both supervised fine-tuning and conventional RL baselines that lack explicit grounding mechanisms. Incorporating multi-turn RL with zoomed-in visual feedback significantly improves ViGoRL's performance on localizing small GUI elements and visual search, achieving 86.4% on V*Bench. Additionally, we find that grounding amplifies other visual behaviors such as region exploration, grounded subgoal setting, and visual verification. Finally, human evaluations show that the model's visual references are not only spatially accurate but also helpful for understanding model reasoning steps. Our results show that visually grounded RL is a strong paradigm for imbuing models with general-purpose visual reasoning.

