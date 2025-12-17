---
layout: default
title: Curiosity-Driven Development of Action and Language in Robots Through Self-Exploration
---

# Curiosity-Driven Development of Action and Language in Robots Through Self-Exploration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.05013" class="toolbar-btn" target="_blank">📄 arXiv: 2510.05013</a>
  <a href="https://arxiv.org/pdf/2510.05013.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.05013" onclick="toggleFavorite(this, '2510.05013', 'Curiosity-Driven Development of Action and Language in Robots Through Self-Exploration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Theodore Jerome Tinker, Kenji Doya, Jun Tani

**分类**: stat.ML, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出基于好奇心驱动的自探索方法，用于机器人动作与语言的自主发展**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `好奇心驱动学习` `主动推理` `强化学习` `机器人语言学习` `自主探索`

## 📋 核心要点

1. 现有语言模型需要大量数据，而人类婴儿仅需少量经验即可泛化学习语言，这其中的机制是核心问题。
2. 论文提出一种基于好奇心驱动的自探索方法，结合主动推理和强化学习，使机器人能够自主学习动作与语言。
3. 实验表明，该方法能够使机器人实现组合泛化和异常处理，并观察到与人类发展心理学相似的学习模式。

## 📝 摘要（中文）

本研究探讨了人类如何通过少量经验泛化学习语言，而大型语言模型却需要数十亿的训练token。我们通过机器人自主探索学习执行与命令句相关的动作（例如，推动红色立方体）的实验来研究这个问题。该方法结合了主动推理和强化学习，实现了内驱的自主学习。仿真结果揭示了与发展心理学观察结果相符的关键发现：i) 随着组合元素规模的增加，泛化能力显著提高；ii) 好奇心通过自我探索提高学习效果；iii) 句子和动作的机械配对先于组合泛化；iv) 简单的动作在依赖它们的复杂动作之前发展；v) 异常处理导致U型发展性能，类似于儿童语言学习中的表征重述。这些结果表明，好奇心驱动的主动推理可以解释内驱的感知运动-语言学习如何支持人类和人工智能体中可扩展的组合泛化和异常处理。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人如何像婴儿一样，通过少量经验自主学习语言和动作，并具备泛化能力的问题。现有方法通常依赖大量标注数据，缺乏自主探索和学习的能力，难以模拟人类的学习过程。

**核心思路**：论文的核心在于利用好奇心驱动的自探索机制，鼓励机器人主动探索环境，发现新的动作和语言组合。通过主动推理和强化学习的结合，机器人能够根据内在的好奇心信号选择行动，并从行动的结果中学习，从而实现自主学习和泛化。

**技术框架**：整体框架包含以下几个主要模块：1) 感知模块，用于接收环境信息（例如，视觉输入和语言指令）；2) 行动模块，用于执行机器人动作；3) 好奇心驱动模块，用于根据当前状态和预期状态之间的差异生成好奇心信号；4) 主动推理模块，用于根据好奇心信号选择行动；5) 强化学习模块，用于从行动的结果中学习，并更新策略。

**关键创新**：论文的关键创新在于将好奇心驱动的自探索机制与主动推理和强化学习相结合，实现了一种内驱的自主学习方法。这种方法能够使机器人主动探索环境，发现新的动作和语言组合，并从中学习，从而提高学习效率和泛化能力。与现有方法相比，该方法不需要大量标注数据，更接近人类的学习方式。

**关键设计**：在好奇心驱动模块中，论文使用预测误差作为好奇心信号，即当前状态和预期状态之间的差异越大，好奇心信号越强。在主动推理模块中，论文使用主动推理框架，根据好奇心信号选择行动，即选择能够最大程度地减少预测误差的行动。在强化学习模块中，论文使用Q-learning算法，从行动的结果中学习，并更新Q值函数。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.05013/images/new_architecture.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.05013/images/robot_and_objects.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.05013/images/evaluation.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，随着组合元素规模的增加，泛化能力显著提高。好奇心驱动的自探索能够有效提高学习效率。机器人首先学习句子和动作的机械配对，然后才能进行组合泛化。简单的动作在复杂的动作之前发展，异常处理会导致U型发展性能，这些都与人类发展心理学的观察结果相符。

## 🎯 应用场景

该研究成果可应用于开发更智能、更自主的机器人，使其能够在复杂环境中自主学习和适应。例如，可用于家庭服务机器人、工业机器人和医疗机器人等领域，提高机器人的智能化水平和服务能力。此外，该研究对于理解人类语言学习机制和开发更有效的语言学习算法也具有重要意义。

## 📄 摘要（原文）

> Infants acquire language with generalization from minimal experience, whereas large language models require billions of training tokens. What underlies efficient development in humans? We investigated this problem through experiments wherein robotic agents learn to perform actions associated with imperative sentences (e.g., push red cube) via curiosity-driven self-exploration. Our approach integrates active inference with reinforcement learning, enabling intrinsically motivated developmental learning. The simulations reveal key findings corresponding to observations in developmental psychology. i) Generalization improves drastically as the scale of compositional elements increases. ii) Curiosity improves learning through self-exploration. iii) Rote pairing of sentences and actions precedes compositional generalization. iv) Simpler actions develop before complex actions depending on them. v) Exception-handling induces U-shaped developmental performance, a pattern like representational redescription in child language learning. These results suggest that curiosity-driven active inference accounts for how intrinsically motivated sensorimotor-linguistic learning supports scalable compositional generalization and exception handling in humans and artificial agents.

