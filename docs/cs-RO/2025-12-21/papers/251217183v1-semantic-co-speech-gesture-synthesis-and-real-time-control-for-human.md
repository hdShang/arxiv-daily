---
layout: default
title: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots
---

# Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17183" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17183v1</a>
  <a href="https://arxiv.org/pdf/2512.17183.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17183v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17183v1', 'Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gang Zhang

**分类**: cs.RO

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**提出一种基于语义理解的共语姿势生成与人形机器人实时控制框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `共语姿势生成` `人形机器人` `实时控制` `大型语言模型` `模仿学习` `运动重定向` `人机交互`

## 📋 核心要点

1. 现有机器人共语姿势生成方法难以保证语义相关性，且难以在真实机器人上实时部署。
2. 该论文提出了一种端到端的框架，利用大型语言模型和Motion-GPT模型生成语义相关的姿势，并使用模仿学习控制策略进行实时控制。
3. 实验结果表明，该系统能够生成语义适当且节奏连贯的姿势，并由Unitree G1人形机器人准确跟踪和执行。

## 📝 摘要（中文）

本文提出了一种创新的端到端框架，用于合成具有语义意义的共语姿势，并将其在人形机器人上实时部署。该系统通过将先进的姿势生成技术与鲁棒的物理控制相结合，解决了为机器人创建自然、富有表现力的非语言交流的挑战。核心创新在于语义感知姿势合成模块的精心集成，该模块通过利用基于大型语言模型（LLMs）的生成检索机制和自回归Motion-GPT模型，从语音输入中导出富有表现力的参考动作。这与高保真模仿学习控制策略MotionTracker相结合，使Unitree G1人形机器人能够动态地执行这些复杂动作并保持平衡。为了确保可行性，我们采用了一种鲁棒的通用运动重定向（GMR）方法来弥合人体运动数据和机器人平台之间的具身差距。通过全面的评估，我们证明了我们的组合系统能够产生语义上适当且节奏上连贯的姿势，并且可以被物理机器人准确地跟踪和执行。据我们所知，这项工作代表了朝着通用现实世界使用迈出的重要一步，它提供了一个完整的管道，用于自动、语义感知的共语姿势生成以及在人形机器人上同步的实时物理部署。

## 🔬 方法详解

**问题定义**：现有方法在机器人共语姿势生成方面存在两个主要痛点。一是生成的姿势与语音的语义关联性较弱，缺乏自然性和表现力。二是难以将生成的姿势有效地部署到真实的机器人平台上，实现实时的同步控制，尤其是在保持机器人平衡的同时执行复杂动作。

**核心思路**：该论文的核心思路是将语义感知的姿势生成与高保真度的机器人控制相结合。通过利用大型语言模型理解语音的语义信息，并生成与之对应的姿势动作。然后，通过模仿学习训练控制策略，使机器人能够准确地复现这些姿势，并保持自身的平衡。

**技术框架**：该框架主要包含三个模块：1) 语义感知姿势合成模块：利用大型语言模型和Motion-GPT模型，从语音输入中生成参考动作。2) 通用运动重定向（GMR）模块：将人体运动数据映射到机器人平台上，解决具身差异。3) 模仿学习控制模块（MotionTracker）：训练控制策略，使机器人能够跟踪参考动作并保持平衡。

**关键创新**：该论文的关键创新在于将大型语言模型引入到共语姿势生成中，实现了语义感知的姿势合成。此外，通过模仿学习训练控制策略，实现了在真实机器人上的实时部署和控制。这种端到端的集成方法是现有方法所缺乏的。

**关键设计**：在姿势合成模块中，使用了基于大型语言模型的生成检索机制，以确保生成的姿势与语音的语义相关。Motion-GPT模型采用自回归结构，能够生成连贯的动作序列。在控制模块中，使用了模仿学习方法，通过学习人类的运动数据，训练机器人控制策略。GMR模块采用了一种鲁棒的映射方法，以减少人体和机器人之间的差异。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17183v1/paper.drawio.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17183v1/001_Neutral_0_mirror_x_1_0_retarget2mocap_comparison.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17183v1/joint_comparison.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该论文提出的系统在Unitree G1人形机器人上进行了实验验证，结果表明该系统能够生成语义适当且节奏连贯的姿势，并由机器人准确跟踪和执行。与传统的基于规则或运动捕捉的方法相比，该系统能够生成更自然、更富有表现力的姿势，并且能够更好地适应不同的语音输入。

## 🎯 应用场景

该研究成果可应用于多种人机交互场景，例如：智能客服机器人、教育机器人、康复机器人等。通过赋予机器人更自然、更富有表现力的非语言交流能力，可以显著提升人机交互的质量和效率，使机器人更好地理解人类意图并做出相应的反应。未来，该技术有望应用于更广泛的领域，例如：虚拟现实、游戏等。

## 📄 摘要（原文）

> We present an innovative end-to-end framework for synthesizing semantically meaningful co-speech gestures and deploying them in real-time on a humanoid robot. This system addresses the challenge of creating natural, expressive non-verbal communication for robots by integrating advanced gesture generation techniques with robust physical control. Our core innovation lies in the meticulous integration of a semantics-aware gesture synthesis module, which derives expressive reference motions from speech input by leveraging a generative retrieval mechanism based on large language models (LLMs) and an autoregressive Motion-GPT model. This is coupled with a high-fidelity imitation learning control policy, the MotionTracker, which enables the Unitree G1 humanoid robot to execute these complex motions dynamically and maintain balance. To ensure feasibility, we employ a robust General Motion Retargeting (GMR) method to bridge the embodiment gap between human motion data and the robot platform. Through comprehensive evaluation, we demonstrate that our combined system produces semantically appropriate and rhythmically coherent gestures that are accurately tracked and executed by the physical robot. To our knowledge, this work represents a significant step toward general real-world use by providing a complete pipeline for automatic, semantic-aware, co-speech gesture generation and synchronized real-time physical deployment on a humanoid robot.

